"""AI Lua script management.

Currently works for Dark Souls 1 (either version) only, with decompilation for DSR thanks to Katalash.
"""
from __future__ import annotations

import abc
import logging
import os
import re
import struct
import subprocess
from contextlib import contextmanager
from copy import deepcopy
from io import BufferedIOBase, BytesIO
from pathlib import Path
from typing import List

from soulstruct.core import SoulstructError
from soulstruct.bnd import BND, BNDEntry
from soulstruct.utilities.core import read_chars_from_buffer, create_bak, PACKAGE_PATH, get_startupinfo, \
    unpack_from_buffer
from soulstruct.utilities.binary_struct import BinaryStruct

__all__ = [
    "LuaBND",
    "LuaGoal",
    "LuaInfo",
    "LuaError",
    "LuaDecompileError",
    "LuaCompileError",
    "decompile_lua",
    "compile_lua",
]


_LOGGER = logging.getLogger(__name__)

COMPILER_x64 = str(PACKAGE_PATH("ai/lua/x64/LuaC.exe"))
COMPILER_x86 = str(PACKAGE_PATH("ai/lua/x86/luac50.exe"))
DECOMPILER_x64 = str(PACKAGE_PATH("ai/lua/x64/DSLuaDecompiler.exe"))
# No x86 decompiler.


_SNAKE_CASE_RE = re.compile(r"(?<!^)(?=[A-Z])")
_GOAL_SCRIPT_RE = re.compile(r"^(\d{6})_(battle|logic)\.lua$")
_LUA_SCRIPT_RE = re.compile(r"(.*)\.lua$")


class LuaError(SoulstructError):
    pass


class LuaCompileError(LuaError):
    pass


class LuaDecompileError(LuaError):
    pass


class LuaBND:
    """Automatically loads all scripts, LuaInfo, and LuaGNL objects."""

    def __init__(self, luabnd_path, sort_goals=True, require_luainfo=False, require_luagnl=False):
        self.bnd = BND(luabnd_path)  # path is remembered in BND

        self.goals = []  # type: List[LuaGoal]
        self.other = []  # type: List[LuaOther]

        self.global_names = []
        self.gnl = LuaGNL()
        self.bnd_name = ""
        self._bnd_path_parent = None
        self.is_lua_32 = False  # as opposed to 64-bit (can't decompile 32-bit at present)

        try:
            gnl_entry = self.bnd.entries_by_id[1000000]
        except KeyError:
            if require_luagnl:
                raise LuaError(f"Could not find `.luagnl` file in LuaBND: {str(luabnd_path)}")
        else:
            self.global_names = LuaGNL(gnl_entry.data).names

        try:
            info_entry = self.bnd.entries_by_id[1000001]
        except KeyError:
            if require_luainfo:
                # TODO: 'eventCommon.luabnd' has no '.luainfo' file. Not handling this yet.
                raise LuaError(f"Could not find `.luainfo` file in LuaBND: {str(luabnd_path)}")
        else:
            self.goals = LuaInfo(info_entry.data).goals
            self.bnd_name = Path(info_entry.path).stem

        _slow_warning_done = False
        for entry in self.bnd:
            entry_path = Path(entry.path)
            goal_match = _GOAL_SCRIPT_RE.match(entry_path.name)
            if goal_match:
                goal_id, goal_type = goal_match.group(1, 2)
                goal_id = int(goal_id)
                try:
                    script = entry.data.decode("shift_jis_2004")
                    bytecode = b""
                except UnicodeDecodeError:
                    script = ""
                    bytecode = entry.data
                try:
                    goal = self.get_goal(goal_id, goal_type)
                except KeyError:
                    if not _slow_warning_done:
                        _LOGGER.warning(
                            f"One or more goals are missing from `LuaInfo` in {luabnd_path.name} and will be "
                            "automatically decompiled to detect the goal name from the script directly. "
                            "Initialization may take longer."
                        )
                        _slow_warning_done = True
                    if not script:
                        script = decompile_lua(bytecode, script_name=entry_path.name)
                    # Scan file for goal name.
                    if goal_type == LuaGoal.BATTLE_TYPE:
                        search_string = rf"^function ([\w\d_]+{goal_id}Battle)_Activate\("
                    elif goal_type == LuaGoal.LOGIC_TYPE:
                        search_string = rf"^function ([\w\d_]+{goal_id}_Logic)\("
                    else:
                        continue  # ignore 'neither'

                    if (goal_name_match := re.search(search_string, script, re.MULTILINE)) is None:
                        _LOGGER.warning(
                            f"Lua file {entry_path.name} in {luabnd_path} has no corresponding `LuaInfo` entry and its "
                            f"goal name could not be auto-detected from its script, so it will not be loaded."
                        )
                        continue
                    goal = LuaGoal(
                        goal_id=goal_id,
                        goal_name=goal_name_match.group(1),
                        goal_type=goal_type,
                        script_name=entry_path.name,
                        bytecode=bytecode,
                        script=script,
                    )
                    self.goals.append(goal)
                else:
                    goal.script = script
                    goal.bytecode = bytecode

                if self._bnd_path_parent is None:
                    self._bnd_path_parent = str(Path(entry.path).parent)
                    self.is_lua_32 = "INTERROOT_x32" in self._bnd_path_parent
            elif entry.id not in {1000000, 1000001}:
                lua_match = _LUA_SCRIPT_RE.match(entry_path.name)
                if not lua_match:
                    _LOGGER.warning(f"Found non-Lua file with BND path: '{entry.path}'. File will be ignored.")
                    continue
                for goal in self.goals:
                    snake_name = _SNAKE_CASE_RE.sub("_", goal.goal_name).lower()
                    if lua_match.group(1) == snake_name:
                        goal.bytecode = entry.data
                        goal.script_name = entry_path.name
                        break
                else:
                    self.other.append(LuaOther(entry_path.stem, bytecode=entry.data))

        if sort_goals:
            self.goals = sorted(self.goals, key=lambda g: (g.goal_id, g.goal_type))

    def compile_all(self, output_directory=None, including_other=False):
        """Compile all goals (and optionally, other Lua scripts) to Lua bytecode.

        Not necessary for writing game files, but useful to test for script syntax errors.

        Any files that produce errors will be reported, but will not halt the function.
        """
        for goal in self.goals:
            output_path = Path(output_directory) / goal.script_name if output_directory else None
            try:
                goal.compile(output_path=output_path)
            except LuaDecompileError as e:
                _LOGGER.error(f"Could not compile Lua goal script '{goal.script_name}'. Error: {str(e)}")
        if including_other:
            for other in self.other:
                output_path = Path(output_directory) / other.script_name if output_directory else None
                try:
                    other.compile(output_path=output_path)
                except LuaError as e:
                    _LOGGER.error(f"Could not compile Lua non-goal script '{other.script_name}'. Error: {str(e)}")

    def update_bnd_from_compiled(self, lua_entry: LuaScriptBase):
        """Insert compiled script into the BND."""
        bnd_path = self._bnd_path_parent + f"\\{lua_entry.script_name}"
        if bnd_path in self.bnd.entries_by_path:
            self.bnd.entries_by_path[bnd_path].data = lua_entry.bytecode
        else:
            try:
                # Get next ID below 1000000 (GNL).
                bnd_id = max([entry.id for entry in self.bnd.entries if entry.id < 1000000]) + 1
            except ValueError:
                bnd_id = 1000  # first ID
            new_entry = BNDEntry(data=lua_entry.bytecode, entry_id=bnd_id, path=bnd_path)
            self.bnd.add_entry(new_entry)
            _LOGGER.debug(f"New compiled bytecode added to LuaBND[{bnd_id}]: {lua_entry.script_name}")

    def decompile_all(self, output_directory=None, including_other=False):
        """Decompile all goals (and optionally, other Lua scripts).

        Any files that produce errors will be reported, but will not halt the function.
        """
        if self.is_lua_32:
            raise ValueError(
                "Cannot decompile PTDE Lua scripts. Decompile the DSR scripts, then copy those "
                "into your PTDE Soulstruct project's 'ai' folder or call `.load_decompiled()`."
            )
        for goal in self.goals:
            output_path = Path(output_directory) / goal.script_name if output_directory else None
            try:
                goal.decompile(output_path=output_path)
            except LuaDecompileError as e:
                _LOGGER.error(f"Could not decompile Lua goal script '{goal.script_name}'. Error: {str(e)}")
        if including_other:
            for other in self.other:
                output_path = Path(output_directory) / other.script_name if output_directory else None
                try:
                    other.decompile(output_path=output_path)
                except LuaError as e:
                    _LOGGER.error(f"Could not decompile Lua non-goal script '{other.script_name}'. Error: {str(e)}")

    def update_bnd_from_decompiled(self, lua_file: LuaScriptBase, compile_script=True, x64=None):
        """Insert decompiled script into the BND.

        This will overwrite any existing scripts (compiled or decompiled) and create a new one if the BND entry is
        absent.
        """
        if not lua_file.script:
            raise LuaError(f"No decompiled Lua script exists for '{lua_file.script_name}'.")
        if compile_script:
            if x64 is None:
                raise ValueError("`x64` must be specified to test if script compiles.")
            lua_file.compile(x64=x64)
        bnd_path = self._bnd_path_parent + f"\\{lua_file.script_name}"
        if bnd_path in self.bnd.entries_by_path:
            self.bnd.entries_by_path[bnd_path].data = lua_file.script.encode("shift_jis_2004")
        else:
            try:
                # Get next ID below 1000000 (GNL).
                bnd_id = max([entry.id for entry in self.bnd.entries if entry.id < 1000000]) + 1
            except ValueError:
                bnd_id = 1000  # first ID
            new_entry = BNDEntry(data=lua_file.script.encode("shift_jis_2004"), entry_id=bnd_id, path=bnd_path)
            self.bnd.add_entry(new_entry)
            _LOGGER.debug(f"New decompiled script added to LuaBND[{bnd_id}]: {lua_file.script_name}")

    def load_decompiled(self, directory, including_other=False):
        """Load decompiled scripts from an arbitrary directory (e.g. to get DSR scripts into PTDE)."""
        directory = Path(directory)
        for lua_script in directory.glob("*.lua"):
            goal_match = _GOAL_SCRIPT_RE.match(lua_script.name)
            if goal_match:
                goal_id, goal_type = goal_match.group(1, 2)
                goal_id = int(goal_id)
                try:
                    goal = self.get_goal(goal_id, goal_type)
                except KeyError:
                    # TODO: parse script to guess what goal name should be (from Activate function name).
                    _LOGGER.warning(
                        f"# WARNING: No goal found for script {lua_script.name}. Ignoring file.\n"
                        f"# (Future versions of Soulstruct may automatically create the goal.)"
                    )
                    continue
                try:
                    with lua_script.open("r", encoding="shift_jis_2004") as f:
                        goal.script = f.read()
                except UnicodeDecodeError:
                    raise LuaError(f"Could not read Lua script '{lua_script.name}'. Are you sure it's not compiled?")
            elif including_other:
                lua_match = _LUA_SCRIPT_RE.match(lua_script.name)
                if not lua_match:
                    continue
                try:
                    with lua_script.open("r", encoding="shift_jis_2004") as f:
                        other_script = f.read()
                except UnicodeDecodeError:
                    raise LuaError(f"Could not read Lua script '{lua_script.name}'. Are you sure it's not compiled?")
                matching_scripts = [g for g in self.other if g.script_name == lua_script.name]
                if not matching_scripts:
                    # Create new LuaOther.
                    self.other.append(LuaOther(lua_script.stem, script=other_script))
                elif len(matching_scripts) >= 2:
                    raise LuaError(
                        f"Lua script {lua_script.name} has been loaded from LuaBND multiple times. You must "
                        f"have done this intentionally, but it's not valid; you should delete one of them."
                    )
                else:
                    other = matching_scripts[0]
                    other.script = other_script

    def write_all_compiled_scripts(self, directory, including_other=True):
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        for goal in self.goals:
            goal.write_compiled(directory / goal.script_name)
        if including_other:
            for other in self.other:
                other.write_compiled(directory / other.script_name)

    def write_all_decompiled_scripts(self, directory, including_other=True):
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        for goal in self.goals:
            try:
                goal.write_decompiled(directory / goal.script_name)
            except LuaError as ex:
                _LOGGER.error(ex)
                pass
        if including_other:
            for other in self.other:
                other.write_decompiled(directory / other.script_name)

    def update_bnd(
        self,
        use_decompiled_goals=True,
        use_decompiled_other=False,
        compile_scripts=True,
        pack_luainfo=True,
        pack_luagnl=True,
    ):
        for script_entry_id in [entry.id for entry in self.bnd.entries if entry.id < 1000000]:
            self.bnd.remove_entry(script_entry_id)

        if pack_luagnl:
            self.bnd.entries_by_id[1000000].data = LuaGNL(self.global_names).pack()
        if pack_luainfo:
            self.bnd.entries_by_id[1000001].data = LuaInfo(self.goals).pack()
        for lua_list, use_decompiled in zip((self.goals, self.other), (use_decompiled_goals, use_decompiled_other)):
            for lua_entry in lua_list:
                if use_decompiled and lua_entry.script:
                    try:
                        self.update_bnd_from_decompiled(lua_entry, compile_scripts, x64=not self.is_lua_32)
                    except LuaCompileError:
                        if lua_entry.bytecode:
                            _LOGGER.error(f"Could not compile script {lua_entry.script_name}. Using existing bytecode.")
                        else:
                            raise LuaError(
                                f"Could not compile script {lua_entry.script_name} and no bytecode exists "
                                f"to use instead. BND update aborted (it may have been partially updated)."
                            )
                    else:
                        continue
                if lua_entry.bytecode:
                    # Fall back to compiled bytecode if it exists; otherwise, skip (e.g. 'Runaway' and 'Hide' goals).
                    self.update_bnd_from_compiled(lua_entry)
                elif (
                    not lua_entry.goal_name.endswith("Runaway")
                    and not lua_entry.goal_name.endswith("Hide")
                    and lua_entry.goal_name not in DS1_GOALS_WITH_NO_SCRIPT
                ):
                    _LOGGER.warning(f"Skipping unexpected goal that has no script or bytecode: {lua_entry.goal_name}")

    def write(self, luabnd_path=None, use_decompiled_goals=True, use_decompiled_other=False):
        self.update_bnd(use_decompiled_goals=use_decompiled_goals, use_decompiled_other=use_decompiled_other)
        self.bnd.write(luabnd_path)

    def get_goal(self, goal_id, goal_type) -> LuaGoal:
        if goal_type not in {LuaGoal.BATTLE_TYPE, LuaGoal.LOGIC_TYPE, LuaGoal.NEITHER_TYPE}:
            raise ValueError("goal_type must be 'battle', 'logic', or 'neither'.")
        goals = [g for g in self.goals if g.goal_id == goal_id and g.goal_type == goal_type]
        if not goals:
            raise KeyError(f"No goal in LuaBND with ID {goal_id} and type {repr(goal_type)}.")
        elif len(goals) >= 2:
            raise LuaError(f"Multiple {repr(goal_type)} goals with ID {goal_id}. This shouldn't happen.")
        return goals[0]

    def get_goal_index(self, goal_id, goal_type) -> int:
        goal = self.get_goal(goal_id, goal_type)
        return self.goals.index(goal)

    def get_goal_dict(self):
        return {(g.goal_id, g.goal_type): g for g in self.goals}

    def __repr__(self):
        return f"{self.bnd_name}:\n  " + "\n  ".join(str(g) for g in self.goals)


@contextmanager
def _temp_lua_path(content, as_bytes=False, encoding=None, set_cwd=False):
    temp = PACKAGE_PATH("ai/lua/temp")
    if set_cwd:
        previous_cwd = os.getcwd()
        os.chdir(str(temp.parent))
    else:
        previous_cwd = None
    with temp.open(mode="wb" if as_bytes else "w", encoding=encoding) as f:
        f.write(content)
    yield temp
    try:
        os.remove(str(PACKAGE_PATH("ai/lua/temp")))
    except FileNotFoundError:
        pass
    if previous_cwd:
        os.chdir(previous_cwd)


def compile_lua(script: str, script_name="<unknown script>", output_path=None, x64=True):
    with _temp_lua_path(script, as_bytes=False, set_cwd=True, encoding="shift_jis_2004") as temp:
        compiler_path = COMPILER_x64 if x64 else COMPILER_x86
        result = subprocess.run(
            [compiler_path, "-o", "temp.lua", temp],
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            startupinfo=get_startupinfo(),
        )
        if result.stdout.strip():
            _LOGGER.warning(f"Lua Compiler Warning for script {script_name}: {result.stdout.strip()}")
        if result.returncode != 0:
            raise LuaCompileError(f"Script {script_name}: {result.stderr.strip()}")
        with Path("temp.lua").open("rb") as f:
            bytecode = f.read()
        os.remove("temp.lua")
        if output_path:
            with Path(output_path).open("wb") as o:
                o.write(f.read())
        return bytecode


def decompile_lua(bytecode: bytes, script_name="<unknown script>", output_path=None):
    if output_path:
        output_path = Path(output_path).resolve()  # resolve before changing to temp working dir
    with _temp_lua_path(bytecode, as_bytes=True, set_cwd=True) as temp:
        result = subprocess.run(
            [DECOMPILER_x64, temp],
            text=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            startupinfo=get_startupinfo(),
        )
        if result.stdout.strip():
            _LOGGER.warning(f"Lua Decompiler Warning for script {script_name}: {result.stdout.strip()}")
        if result.returncode != 0:
            raise LuaDecompileError(f"Script {script_name}: {result.stderr.strip()}")
        with Path("temp.dec.lua").open("r", encoding="shift_jis_2004") as f:
            script_string = f.read()
        os.remove("temp.dec.lua")
        if output_path:
            output_path = Path(output_path)
            output_path.parent.mkdir(exist_ok=True, parents=True)
            with Path(output_path).open("w", encoding="shift_jis_2004") as o:
                o.write(script_string)
                _LOGGER.info(f"Decompiled Lua file written: {str(output_path)}")
        return script_string


class LuaScriptBase(abc.ABC):
    def __init__(self, bytecode=b"", script=""):
        self.bytecode = bytecode
        self.script = script

    def compile(self, output_path=None, x64=True):
        if not self.script:
            raise LuaCompileError(f"No Lua script to compile for {self.script_name}.")
        self.bytecode = compile_lua(self.script, script_name=self.script_name, output_path=output_path, x64=x64)

    def decompile(self, output_path=None):
        if not self.bytecode:
            raise LuaDecompileError(f"No compiled Lua to decompile for {self.script_name}.")
        self.script = decompile_lua(self.bytecode, script_name=self.script_name, output_path=output_path)

    def write_compiled(self, lua_path):
        if not self.bytecode:
            raise LuaError(f"No compiled Lua bytecode to write for {self.script_name}.")
        lua_path = Path(lua_path)
        lua_path.parent.mkdir(parents=True, exist_ok=True)
        with lua_path.open("wb") as f:
            f.write(self.bytecode)

    def write_decompiled(self, lua_path):
        if not self.script:
            raise LuaError(f"No decompiled Lua script to write for {self.script_name}.")
        lua_path = Path(lua_path)
        lua_path.parent.mkdir(parents=True, exist_ok=True)
        with lua_path.open("w", encoding="shift_jis_2004") as f:
            f.write(self.script)

    def load_decompiled(self, lua_path):
        lua_path = Path(lua_path)
        with lua_path.open("r", encoding="shift_jis_2004") as f:
            self.script = f.read()

    @property
    @abc.abstractmethod
    def script_name(self) -> str:
        raise NotImplementedError


class LuaGoal(LuaScriptBase):
    """Goals can have type 'battle', 'logic', or 'neither'.

    All 'battle' goals have `has_battle_interrupt=True`, `has_logic_interrupt=False`, and `logic_interrupt_name=""`.
    Their names usually end in 'Battle' (no underscore), but this is not necessary (e.g. common battle functions).

    All 'logic' goals have `has_battle_interrupt=False`, `has_logic_interrupt=True`, and
    `logic_interrupt_name={goal_name_prefix}_Interupt` [sic]. The goal name always ends in '_Logic'.

    All 'neither' goals have `has_battle_interrupt=False`, `has_logic_interrupt=False`, and `logic_interrupt_name=""`.
    These goals are typically referenced in other files (e.g. 'CrystalLizard330000Runaway'). They can have any name.
    """

    BATTLE_TYPE = "battle"
    LOGIC_TYPE = "logic"
    NEITHER_TYPE = "neither"

    def __init__(
        self,
        goal_id: int,
        goal_name: str,
        goal_type: str = None,
        has_battle_interrupt: bool = None,
        has_logic_interrupt: bool = None,
        logic_interrupt_name="",
        bytecode=b"",
        script="",
        script_name=None,
    ):
        super().__init__(bytecode=bytecode, script=script)
        self.goal_id = goal_id
        self._goal_name = goal_name
        self._goal_type = (
            goal_type
            if goal_type is not None
            else self._detect_goal_type(has_battle_interrupt, has_logic_interrupt, logic_interrupt_name)
        )
        self._script_name = script_name

    def _detect_goal_type(self, has_battle_interrupt, has_logic_interrupt, logic_interrupt_name):
        if has_battle_interrupt and not has_logic_interrupt and not logic_interrupt_name:
            return self.BATTLE_TYPE
        elif not has_battle_interrupt and has_logic_interrupt and logic_interrupt_name:
            return self.LOGIC_TYPE
        elif not has_battle_interrupt and not has_logic_interrupt and not logic_interrupt_name:
            return self.NEITHER_TYPE
        raise LuaError(
            f"Could not determine goal type (battle={has_battle_interrupt}, logic={has_logic_interrupt}, "
            f"logic_name={repr(logic_interrupt_name)})."
        )

    @property
    def goal_name(self):
        return self._goal_name

    @goal_name.setter
    def goal_name(self, name):
        if self._goal_type == "logic" and not name.endswith("_Logic"):
            raise LuaError(f"Logic goal name must end in '_Logic'. Invalid: {repr(name)}")
        elif self._goal_type == "battle" and not name.endswith("Battle"):
            _LOGGER.warning(f"Battle goal name {repr(name)} does not end in 'Battle', which is unusual.")
        self._goal_name = name

    @property
    def goal_type(self):
        return self._goal_type

    @goal_type.setter
    def goal_type(self, new_type):
        new_type = new_type.lower()
        if not self._goal_name.endswith("_Logic") and new_type == "logic":
            raise LuaError(f"Logic goal name must end in '_Logic'. Invalid: {repr(self._goal_name)}")
        elif not self._goal_name.endswith("Battle") and new_type == "battle":
            _LOGGER.warning(f"Battle goal name {repr(self._goal_name)} does not end in 'Battle', which is unusual.")
        self._goal_type = new_type

    def set_name_and_type(self, goal_name, goal_type):
        self._goal_name = goal_name  # no type checking
        self.goal_type = goal_type  # yes type checking

    @property
    def script_name(self):
        if self._script_name is not None:
            return self._script_name
        elif self.goal_type == self.BATTLE_TYPE:
            return f"{self.goal_id:06d}_battle.lua"
        elif self.goal_type == self.LOGIC_TYPE:
            return f"{self.goal_id:06d}_logic.lua"
        elif self.goal_type == self.NEITHER_TYPE:
            # Shouldn't happen anymore.
            snake_case_name = _SNAKE_CASE_RE.sub("_", self.goal_name).lower()
            return f"{snake_case_name}.lua"

    @script_name.setter
    def script_name(self, name):
        self._script_name = name

    def __repr__(self):
        return f"LuaGoal({self.goal_id:06d}, {repr(self.goal_name)}, {repr(self.goal_type)})"

    def copy(self):
        return deepcopy(self)

    def get_interrupt_details(self):
        if self.goal_type == self.BATTLE_TYPE:
            return {"has_battle_interrupt": True, "has_logic_interrupt": False, "logic_interrupt_name": ""}
        elif self.goal_type == self.LOGIC_TYPE:
            if self.goal_name.endswith("_Logic"):
                name = self.goal_name[:-6] + "_Interupt"
            else:
                raise LuaError(f"Logic goal name must end in '_Logic'. Invalid: {repr(self._goal_name)}")
            return {"has_battle_interrupt": False, "has_logic_interrupt": True, "logic_interrupt_name": name}
        elif self.goal_type == self.NEITHER_TYPE:
            return {"has_battle_interrupt": False, "has_logic_interrupt": False, "logic_interrupt_name": ""}


class LuaOther(LuaScriptBase):
    def __init__(self, name, bytecode=b"", script=""):
        super().__init__(bytecode=bytecode, script=script)
        self.name = name

    @property
    def script_name(self):
        return f"{self.name}.lua"

    def __repr__(self):
        return f"LuaOther(name={repr(self.name)})"


class LuaInfo:
    """Describes the lua scripts contained inside this `luabnd` archive.

    Registration in this file is necessary for the scripts to be loaded with the corresponding map. Individual Lua
    function names should also be registered in `luagnl`, though it's unclear exactly when this is necessary. If a
    script doesn't appear to be working (the enemy isn't moving at all), adding the function names to `luagnl` should
    be the first solution you try. Another reason for non-functional scripts that I've experienced is a clash between
    maps (the same script is being loaded by multiple maps at the same time). If your script is used in multiple maps,
    it's better to put it in `aiCommon.luabnd`.
    """

    HEADER_STRUCT = (
        ("lua_version", "4s", b"LUAI"),
        ("endian_one", "i", 1),  # checked manually to guess endianness
        ("goal_count", "i"),
        "4x",
    )

    GOAL_STRUCT_32 = (
        ("goal_id", "i"),
        ("name_offset", "I"),
        ("logic_interrupt_name_offset", "I"),
        ("has_battle_interrupt", "?"),
        ("has_logic_interrupt", "?"),
        "2x",
    )

    GOAL_STRUCT_64 = (
        ("goal_id", "i"),
        ("has_battle_interrupt", "?"),
        ("has_logic_interrupt", "?"),
        "2x",
        ("name_offset", "q"),
        ("logic_interrupt_name_offset", "q"),
    )

    def __init__(self, luainfo_source=None, big_endian=False, use_struct_64=False):
        self.big_endian = big_endian
        self.use_struct_64 = use_struct_64
        self.luainfo_path = None
        self.header_struct = BinaryStruct(*self.HEADER_STRUCT, byte_order=">" if self.big_endian else "<")

        self.goals = []  # type: List[LuaGoal]

        if luainfo_source is None:
            return
        if isinstance(luainfo_source, (list, tuple)):
            self.goals = luainfo_source  # type: List[LuaGoal]
            return
        if isinstance(luainfo_source, (str, Path)):
            self.luainfo_path = Path(luainfo_source)
            with self.luainfo_path.open("rb") as f:
                self.unpack(f)
            return
        if hasattr(luainfo_source, "data"):
            luainfo_source = luainfo_source.data
        if isinstance(luainfo_source, bytes):
            luainfo_source = BytesIO(luainfo_source)
        if isinstance(luainfo_source, BufferedIOBase):
            self.unpack(luainfo_source)

    def unpack(self, info_buffer):
        self.big_endian = self._check_big_endian(info_buffer)
        self.header_struct = BinaryStruct(*self.HEADER_STRUCT, byte_order=">" if self.big_endian else "<")
        header = self.header_struct.unpack(info_buffer)
        self.use_struct_64 = self._check_use_struct_64(info_buffer, header["goal_count"])
        goal_struct = BinaryStruct(
            *(self.GOAL_STRUCT_64 if self.use_struct_64 else self.GOAL_STRUCT_32),
            byte_order=">" if self.big_endian else "<",
        )
        self.goals = []
        for _ in range(header["goal_count"]):
            goal = self.unpack_goal(info_buffer, goal_struct)
            if goal.script_name in [g.script_name for g in self.goals]:
                _LOGGER.warning(
                    f"Goal '{goal.goal_id}' is referenced multiple times in LuaInfo (same ID and type). Each goal ID "
                    f"should have (at most) one 'battle' goal and one 'logic' goal. All goal entries after the first "
                    f"will be ignored."
                )
            else:
                self.goals.append(goal)

    def pack(self):
        header = self.header_struct.pack(goal_count=len(self.goals))
        packed_goals = b""
        packed_strings = b""
        goal_struct = BinaryStruct(
            *(self.GOAL_STRUCT_64 if self.use_struct_64 else self.GOAL_STRUCT_32),
            byte_order=">" if self.big_endian else "<",
        )
        packed_strings_offset = len(header) + len(self.goals) * goal_struct.size
        encoding = self.encoding
        z_term = b"\0\0" if self.use_struct_64 else b"\0"
        for goal in self.goals:
            name_offset = packed_strings_offset + len(packed_strings)
            packed_strings += goal.goal_name.encode(encoding=encoding) + z_term
            goal_kwargs = goal.get_interrupt_details()
            logic_interrupt_name = goal_kwargs.pop("logic_interrupt_name")
            if logic_interrupt_name:
                logic_interrupt_name_offset = packed_strings_offset + len(packed_strings)
                packed_strings += logic_interrupt_name.encode(encoding=encoding) + z_term
            else:
                logic_interrupt_name_offset = 0
            packed_goals += goal_struct.pack(
                goal_id=goal.goal_id,
                name_offset=name_offset,
                logic_interrupt_name_offset=logic_interrupt_name_offset,
                **goal_kwargs,
            )

        return header + packed_goals + packed_strings

    def write(self, luainfo_path=None):
        if luainfo_path is None:
            luainfo_path = self.luainfo_path
        else:
            luainfo_path = Path(luainfo_path)
        create_bak(luainfo_path)
        with luainfo_path.open("wb") as f:
            f.write(self.pack())

    def unpack_goal(self, info_buffer, goal_struct) -> LuaGoal:
        goal = goal_struct.unpack(info_buffer)
        name = read_chars_from_buffer(info_buffer, offset=goal.name_offset, encoding=self.encoding)
        if goal.logic_interrupt_name_offset > 0:
            logic_interrupt_name = read_chars_from_buffer(
                info_buffer, offset=goal.logic_interrupt_name_offset, encoding=self.encoding
            )
        else:
            logic_interrupt_name = ""
        return LuaGoal(
            goal_id=goal.goal_id,
            goal_name=name,
            has_battle_interrupt=goal.has_battle_interrupt,
            has_logic_interrupt=goal.has_logic_interrupt,
            logic_interrupt_name=logic_interrupt_name,
        )

    @property
    def encoding(self):
        if self.use_struct_64:
            return f"utf-16-{'be' if self.big_endian else 'le'}"
        return "shift_jis_2004"

    @staticmethod
    def _check_big_endian(info_buffer):
        info_buffer.seek(4)
        (endian,) = struct.unpack("i", info_buffer.read(4))
        info_buffer.seek(0)
        if endian == 0x1000000:
            return True
        elif endian == 0x1:
            return False
        raise ValueError(f"Invalid marker for LuaInfo byte order: {hex(endian)}")

    @staticmethod
    def _check_use_struct_64(info_buffer, goal_count):
        if goal_count == 0:
            raise LuaError(f"Cannot detect `LuaInfo` version if no goals are present.")
        elif goal_count >= 2:
            return unpack_from_buffer(info_buffer, "i", offset=0x24)[0] == 0
        else:
            # Hacky check if there's only one goal.
            if unpack_from_buffer(info_buffer, "i", offset=0x18)[0] == 0x28:
                return True
            if unpack_from_buffer(info_buffer, "i", offset=0x14)[0] == 0x20:
                return False
            raise ValueError(f"Found unexpected data while trying to detect `LuaInfo` version from single goal.")


class LuaGNL:
    def __init__(self, luagnl_source=None, big_endian=False, use_struct_64=False):
        self.big_endian = big_endian
        self.use_struct_64 = use_struct_64
        self.luagnl_path = None

        self.names = []  # type: List[str]

        if luagnl_source is None:
            return
        if isinstance(luagnl_source, (list, tuple)):
            self.names = luagnl_source
            return
        if isinstance(luagnl_source, (str, Path)):
            self.luagnl_path = Path(luagnl_source)
            with self.luagnl_path.open("rb") as f:
                self.unpack(f)
            return
        if hasattr(luagnl_source, "data"):
            luagnl_source = luagnl_source.data
        if isinstance(luagnl_source, bytes):
            luagnl_source = BytesIO(luagnl_source)
        if isinstance(luagnl_source, BufferedIOBase):
            self.unpack(luagnl_source)

    def unpack(self, gnl_buffer):
        self.big_endian, self.use_struct_64 = self._check_big_endian_and_struct_64(gnl_buffer)
        fmt = f"{'>' if self.big_endian else '<'}{'q' if self.use_struct_64 else 'i'}"
        read_size = struct.calcsize(fmt)
        self.names = []
        offset = None
        while offset != 0:
            (offset,) = struct.unpack(fmt, gnl_buffer.read(read_size))
            if offset != 0:
                self.names.append(read_chars_from_buffer(gnl_buffer, offset=offset, encoding=self.encoding))

    def pack(self):
        packed_offsets = b""
        packed_names = b""
        fmt = f"{'>' if self.big_endian else '<'}{'q' if self.use_struct_64 else 'i'}"
        packed_names_offset = (len(self.names) + 1) * struct.calcsize(fmt)
        encoding = self.encoding
        z_term = b"\0\0" if self.use_struct_64 else b"\0"
        for name in self.names:
            name_offset = packed_names_offset + len(packed_names)
            packed_offsets += struct.pack(fmt, name_offset)
            packed_names += name.encode(encoding=encoding) + z_term
        packed_offsets += struct.pack(fmt, 0)
        packed_names += b"\0" * 16
        return packed_offsets + packed_names

    def write(self, luagnl_path=None):
        if luagnl_path is None:
            luagnl_path = self.luagnl_path
        luagnl_path = Path(luagnl_path)
        create_bak(luagnl_path)
        with luagnl_path.open("wb") as f:
            f.write(self.pack())

    @property
    def encoding(self):
        if self.use_struct_64:
            return f"utf-16-{'be' if self.big_endian else 'le'}"
        return "shift_jis_2004"

    @staticmethod
    def _check_big_endian_and_struct_64(gnl_buffer):
        """Guessed based on the number and position of zero bytes the first offset."""
        gnl_buffer.seek(0)
        # First two bytes of first offset should be zeroes if big-endian.
        big_endian = struct.unpack("h", gnl_buffer.read(2))[0] == 0
        if big_endian:
            # Remainder of first half of first offset should be zeroes if 64-bit.
            use_struct_64 = struct.unpack("h", gnl_buffer.read(2))[0] == 0
        else:
            # Second half of first offset should be zeroes if 64-bit.
            gnl_buffer.seek(4)
            use_struct_64 = struct.unpack("i", gnl_buffer.read(4))[0] == 0
        gnl_buffer.seek(0)
        return big_endian, use_struct_64


DS1_GOALS_WITH_NO_SCRIPT = (
    "Default_Logic",
    "Stay",
    "BackToHome",
    "Wait",
    "TurnAround",
    "LeaveTarget",
    "SidewayMove",
    "KeepDist",
    "MoveToSomewhere",
    "SpinStep",
    "LiftOff",
    "Landing_Move",
    "Landing_Landing",
    "KeepDistYAxis",
    "Guard",
    "GuardBreakAttack",
    "ApproachStep",
    "DashAttack",
    "DashAttack_Attack",
    "Parry",
    "SpecialTurn",
    "ObjActTest",
    "ComboAttack180",
    "ComboRepeat_SuccessAngle180",
    "GuardBreakTunable",
    # "*Runaway",
    # "*Hide",
)
