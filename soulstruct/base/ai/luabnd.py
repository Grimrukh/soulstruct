"""AI Lua script management.

Currently works for Dark Souls 1 (either version) only, with decompilation for DSR thanks to Katalash.
"""
from __future__ import annotations

__all__ = ["LuaBND"]

import logging
import re
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.containers import Binder, BinderEntry
from soulstruct.utilities.binary import BinaryReader

from .lua import LuaError, LuaCompileError, LuaDecompileError
from .luainfo import LuaInfo
from .luagnl import LuaGNL
from .lua_scripts import LuaScriptBase, GoalType, LuaGoalScript, LuaUnknownScript

try:
    Self = tp.Self
except AttributeError:
    Self = "LuaBND"

_LOGGER = logging.getLogger(__name__)

_SNAKE_CASE_RE = re.compile(r"(?<!^)(?=[A-Z])")
_GOAL_SCRIPT_RE = re.compile(r"^(\d{6})_(battle|logic)\.lua$")
_LUA_SCRIPT_RE = re.compile(r"(.*)\.lua$")


@dataclass(slots=True)
class LuaBND(Binder):
    """Automatically loads all scripts, LuaInfo, and LuaGNL objects."""

    goals: list[LuaGoalScript] = field(default_factory=list)
    unknown_scripts: list[LuaUnknownScript] = field(default_factory=list)

    is_lua_32: bool = False  # as opposed to 64-bit (can't decompile 32-bit at present)

    @classmethod
    def from_reader(cls, reader: BinaryReader, bdt_reader: BinaryReader | None = None) -> Self:
        if bdt_reader is not None:
            raise TypeError("Cannot read `LuaBND` from a split `BXF` file.")

        luabnd = super(LuaBND, cls).from_reader(reader)  # type: Self

        # Load goals and unknown scripts.
        try:
            info_entry = luabnd.find_entry_id(1000001)
        except KeyError:
            # TODO: 'eventCommon.luabnd' has no '.luainfo' file. Not handling this yet.
            pass
        else:
            # Load initial goals from `LuaInfo`. We will still scan below for other 'loose' goals and files.
            luabnd.goals = info_entry.to_binary_file(LuaInfo).goals

        for entry in luabnd.entries:
            goal_match = _GOAL_SCRIPT_RE.match(entry.name)
            if goal_match:
                goal_id, goal_type = goal_match.group(1, 2)
                goal_id = int(goal_id)
                luabnd.load_goal_entry(entry, goal_id, GoalType(goal_type))
            elif entry.entry_id not in {1000000, 1000001}:
                lua_match = _LUA_SCRIPT_RE.match(entry.name)
                if not lua_match:
                    _LOGGER.warning(f"Found non-Lua file with BND path '{entry.path}'. File will be ignored.")
                    continue
                for goal in luabnd.goals:
                    # Try to find existing goal from `LuaInfo`.
                    snake_name = _SNAKE_CASE_RE.sub("_", goal.goal_name).lower()
                    if lua_match.group(1) == snake_name:
                        goal.bytecode = bytes(entry)
                        goal.script_name = entry.name
                        break
                else:
                    # Unknown Lua script file.
                    luabnd.unknown_scripts.append(LuaUnknownScript(bytecode=bytes(entry), name=entry.stem))

        # TODO: Not sorting goals by default, as their order in the LuaBND does appear to matter for loading.
        # self.sort_goals()
        return luabnd

    def sort_goals(self, key: tp.Callable[[LuaGoalScript], tp.Any] = None):
        if key is None:
            self.goals = sorted(self.goals, key=lambda g: (g.goal_id, g.goal_type))
        else:
            self.goals = sorted(self.goals, key=key)

    def load_goal_entry(self, entry: BinderEntry, goal_id: int, goal_type: GoalType):
        """Load a `LuaGoal` from `entry`, or just load its script and bytecode if already registered in `goals`."""
        entry_data = entry.get_uncompressed_data()
        try:
            script = entry_data.decode("shift_jis_2004")
            bytecode = b""
        except UnicodeDecodeError:
            script = ""
            bytecode = entry_data
        try:
            # See if goal is already loaded (e.g. from `LuaInfo`).
            goal = self.get_goal(goal_id, goal_type)
        except KeyError:
            if not script:
                bytes_re = self._get_goal_name_re(goal_type, goal_id, is_script=False)
                if (goal_name_match := bytes_re.search(bytecode)) is None:
                    _LOGGER.warning(
                        f"Lua file '{entry.name}' in `LuaBND` {self.path} has no corresponding `LuaInfo` entry and "
                        f"its goal name could not be auto-detected from its bytecode, so it will not be loaded."
                    )
                    return
                goal_name = goal_name_match.group(1).decode()
            else:
                string_re = self._get_goal_name_re(goal_type, goal_id, is_script=True)
                if (goal_name_match := string_re.search(script, re.MULTILINE)) is None:
                    _LOGGER.warning(
                        f"Lua file '{entry.name}' in `LuaBND` {self.path} has no corresponding `LuaInfo` entry and "
                        f"its goal name could not be auto-detected from its script, so it will not be loaded."
                    )
                    return
                goal_name = goal_name_match.group(1)

            goal = LuaGoalScript(
                goal_id=goal_id,
                goal_name=goal_name,
                goal_type=goal_type,
                script_name=entry.name,
                bytecode=bytecode,
                script=script,
            )
            self.goals.append(goal)
        else:
            # Assign script and bytecode to existing goal.
            goal.script = script
            goal.bytecode = bytecode

    @staticmethod
    def _get_goal_name_re(goal_type: GoalType, goal_id: int, is_script: bool) -> re.Pattern:
        if goal_type == GoalType.Battle:
            if is_script:
                return re.compile(rf"^function ([\w_]+{goal_id}Battle)_Activate\(")
            return re.compile(f"\0([\\w\\d_]+{goal_id}Battle)_Activate\0".encode())
        elif goal_type == GoalType.Logic:
            if is_script:
                return re.compile(rf"^function ([\w_]+{goal_id}_Logic)\(")
            return re.compile(f"\0([\\w\\d_]+{goal_id}_Logic)\0".encode())
        raise ValueError(f"Cannot detect goal name from goal {goal_id} of unknown goal type: {goal_type}")

    def get_gnl_names(self):
        try:
            # TODO: Search by `.luagnl` extension? Or confirm it.
            gnl_entry = self.find_entry_id(1000000)
        except KeyError:
            return []
        return gnl_entry.to_binary_file(LuaGNL).names

    def compile_all(self, output_directory=None, include_unknown_scripts=False):
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
        if include_unknown_scripts:
            for other in self.unknown_scripts:
                output_path = Path(output_directory) / other.script_name if output_directory else None
                try:
                    other.compile(output_path=output_path)
                except LuaError as e:
                    _LOGGER.error(f"Could not compile Lua non-goal script '{other.script_name}'. Error: {str(e)}")

    def add_bytecode_lua_file(self, lua_file: LuaScriptBase):
        """Add or replace compiled bytecode script in the `Binder`."""
        try:
            existing_entry = self.find_entry_name(lua_file.script_name)
            existing_entry.set_uncompressed_data(lua_file.bytecode)
            existing_entry.path = lua_file.script_name  # no nesting necessary
        except KeyError:
            new_entry_id = self.get_first_new_entry_id_in_range(1000, 1000000)
            new_entry = BinderEntry(data=lua_file.bytecode, entry_id=new_entry_id, path=lua_file.script_name)
            self.add_entry(new_entry)
            _LOGGER.debug(f"New compiled bytecode added to LuaBND[{new_entry_id}]: {lua_file.script_name}")

    def decompile_all(self, output_directory=None, include_unknown_scripts=False):
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
        if include_unknown_scripts:
            for other in self.unknown_scripts:
                output_path = Path(output_directory) / other.script_name if output_directory else None
                try:
                    other.decompile(output_path=output_path)
                except LuaError as e:
                    _LOGGER.error(f"Could not decompile Lua non-goal script '{other.script_name}'. Error: {str(e)}")

    def add_script_lua_file(self, lua_file: LuaScriptBase, compile_script=True, x64=None):
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

        encoded_script = lua_file.script.encode("shift_jis_2004")

        try:
            existing_entry = self.find_entry_name(lua_file.script_name)
            existing_entry.set_uncompressed_data(encoded_script)
            existing_entry.path = lua_file.script_name  # no nesting necessary
        except KeyError:
            new_entry_id = self.get_first_new_entry_id_in_range(1000, 1000000)
            new_entry = BinderEntry(data=encoded_script, entry_id=new_entry_id, path=lua_file.script_name)
            self.add_entry(new_entry)
            _LOGGER.debug(f"New decompiled script added to LuaBND[{new_entry_id}]: {lua_file.script_name}")

    def load_decompiled(self, directory: Path | str, include_unknown_scripts=False):
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
            elif include_unknown_scripts:
                lua_match = _LUA_SCRIPT_RE.match(lua_script.name)
                if not lua_match:
                    continue
                try:
                    with lua_script.open("r", encoding="shift_jis_2004") as f:
                        other_script = f.read()
                except UnicodeDecodeError:
                    raise LuaError(f"Could not read Lua script '{lua_script.name}'. Are you sure it's not compiled?")
                matching_scripts = [g for g in self.unknown_scripts if g.script_name == lua_script.name]
                if not matching_scripts:
                    # Create new LuaOther.
                    self.unknown_scripts.append(LuaUnknownScript(script=other_script, name=lua_script.stem))
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
            goal.write_bytecode(directory / goal.script_name)
        if including_other:
            for other in self.unknown_scripts:
                other.write_bytecode(directory / other.script_name)

    def write_all_decompiled_scripts(self, directory, including_other=True):
        directory = Path(directory)
        directory.mkdir(parents=True, exist_ok=True)
        for goal in self.goals:
            try:
                goal.write_script(directory / goal.script_name)
            except LuaError as ex:
                _LOGGER.error(ex)
                pass
        if including_other:
            for other in self.unknown_scripts:
                other.write_script(directory / other.script_name)

    def get_all_script_names(self, include_unknown_scripts=True) -> list[str]:
        names = [goal.script_name for goal in self.goals]
        if include_unknown_scripts:
            names += [unknown.script_name for unknown in self.unknown_scripts]
        return names

    def regenerate_entries(
        self,
        use_decompiled_goals=True,
        use_decompiled_unknown_scripts=False,
        compile_scripts=True,
        pack_luainfo=True,
        pack_luagnl=True,
    ):
        """Scan `goals` and `unknown_scripts` to rebuild Binder script entries and (if requested) `LuaInfo` and
        `LuaGNL` files."""

        # Remove BND script entries that aren't still present in this `LuaBND` instance.
        current_script_names = self.get_all_script_names(include_unknown_scripts=True)
        for entry_script_name in [entry.name for entry in self.entries if entry.entry_id < 1000000]:
            if entry_script_name not in current_script_names:
                self.remove_entry_name(entry_script_name)

        entries_by_id = self.get_entries_by_id()

        if pack_luagnl:
            if 1000000 not in entries_by_id:
                _LOGGER.warning(f"No existing `LuaGNL` file in {self.path.name}. Will not write a new one.")
            else:
                # TODO: This is pointlessly just repacking the same `LuaGNL`, since I have no function that collects
                #  global names on its own yet.
                gnl_names = self.get_gnl_names()
                luagnl = LuaGNL(names=gnl_names)
                entries_by_id[1000000].set_from_binary_file(luagnl)
        if pack_luainfo:
            if 1000001 not in entries_by_id:
                _LOGGER.warning(f"No existing `LuaInfo` file in {self.path.name}. Will not write a new one.")
            else:
                luainfo = LuaInfo(goals=self.goals)
                entries_by_id[1000001].set_from_binary_file(luainfo)
        for lua_list, use_decompiled in zip(
            (self.goals, self.unknown_scripts),
            (use_decompiled_goals, use_decompiled_unknown_scripts),
        ):
            for lua_entry in lua_list:
                if use_decompiled and lua_entry.script:
                    try:
                        self.add_script_lua_file(lua_entry, compile_scripts, x64=not self.is_lua_32)
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
                    self.add_bytecode_lua_file(lua_entry)
                elif (
                    not lua_entry.goal_name.endswith("Runaway")
                    and not lua_entry.goal_name.endswith("Hide")
                    and lua_entry.goal_name not in DS1_GOALS_WITH_NO_SCRIPT
                ):
                    _LOGGER.warning(f"Skipping unexpected goal that has no script or bytecode: {lua_entry.goal_name}")

    def write(
        self,
        file_path: None | str | Path = None,
        bdt_file_path: None | str | Path = None,
        make_dirs=True,
        check_hash=False,
        use_decompiled_goals=True,
        use_decompiled_unknown_scripts=False,
    ):
        if bdt_file_path is not None:
            raise TypeError(f"Cannot write `LuaBND` to a split `BXF` file. (Invalid `bdt_file_path`: {bdt_file_path})")
        self.regenerate_entries(
            use_decompiled_goals=use_decompiled_goals, use_decompiled_unknown_scripts=use_decompiled_unknown_scripts
        )
        super().write(file_path, make_dirs=make_dirs, check_hash=check_hash)

    def get_goal(self, goal_id, goal_type=GoalType.Battle) -> LuaGoalScript:
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
        return f"LuaBND:\n  " + "\n  ".join(str(g) for g in self.goals)


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
