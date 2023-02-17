from __future__ import annotations

__all__ = ["LuaScriptBase", "GoalType", "LuaGoalScript", "LuaUnknownScript"]

import abc
import copy
import enum
import logging
import re
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.utilities.binary import *

from .lua import LuaError, LuaCompileError, LuaDecompileError, compile_lua, decompile_lua

_LOGGER = logging.getLogger(__name__)

_SNAKE_CASE_RE = re.compile(r"(?<!^)(?=[A-Z])")


class GoalType(enum.Enum):
    Battle = "battle"
    Logic = "logic"
    Unknown = "unknown"

    @classmethod
    def from_interrupt_info(cls, has_battle_interrupt: bool, has_logic_interrupt: bool, logic_interrupt_name: str):
        if has_battle_interrupt and not has_logic_interrupt and not logic_interrupt_name:
            return cls.Battle
        elif not has_battle_interrupt and has_logic_interrupt and logic_interrupt_name:
            return cls.Logic
        elif not has_battle_interrupt and not has_logic_interrupt and not logic_interrupt_name:
            return cls.Unknown
        raise LuaError(
            f"Could not determine goal type (battle={has_battle_interrupt}, logic={has_logic_interrupt}, "
            f"logic_name={repr(logic_interrupt_name)})."
        )


@dataclass(slots=True)
class LuaScriptBase(abc.ABC):

    bytecode: bytes = b""
    script: str = ""

    def compile(self, output_path=None, x64=True):
        """Generate `bytecode` from current `script`."""
        if not self.script:
            raise LuaCompileError(f"No Lua script to compile for {self.script_name}.")
        self.bytecode = compile_lua(self.script, script_name=self.script_name, output_path=output_path, x64=x64)

    def decompile(self, output_path=None):
        """Generate `script` from current `bytecode`."""
        if not self.bytecode:
            raise LuaDecompileError(f"No compiled Lua to decompile for {self.script_name}.")
        self.script = decompile_lua(self.bytecode, script_name=self.script_name, output_path=output_path)

    def write_bytecode(self, lua_path):
        if not self.bytecode:
            raise LuaError(f"No compiled Lua bytecode to write for {self.script_name}.")
        lua_path = Path(lua_path)
        lua_path.parent.mkdir(parents=True, exist_ok=True)
        with lua_path.open("wb") as f:
            f.write(self.bytecode)

    def write_script(self, lua_path):
        if not self.script:
            raise LuaError(f"No decompiled Lua script to write for {self.script_name}.")
        lua_path = Path(lua_path)
        lua_path.parent.mkdir(parents=True, exist_ok=True)
        with lua_path.open("w", encoding="shift_jis_2004") as f:
            f.write(self.script)

    def load_script(self, lua_path: Path | str):
        lua_path = Path(lua_path)
        with lua_path.open("r", encoding="shift_jis_2004") as f:
            self.script = f.read()

    def copy(self):
        return copy.deepcopy(self)

    @property
    @abc.abstractmethod
    def script_name(self) -> str:
        raise NotImplementedError


@dataclass(slots=True)
class LuaGoal32(BinaryStruct):
    goal_id: int
    name_offset: uint
    logic_interrupt_name_offset: uint
    has_battle_interrupt: bool
    has_logic_interrupt: bool
    _pad1: bytes = field(init=False, **BinaryPad(2))


@dataclass(slots=True)
class LuaGoal64(BinaryStruct):
    goal_id: int
    has_battle_interrupt: bool
    has_logic_interrupt: bool
    _pad1: bytes = field(init=False, **BinaryPad(2))
    name_offset: long
    logic_interrupt_name_offset: long


@dataclass(slots=True)
class LuaGoalScript(LuaScriptBase):
    """Goals can have type 'battle', 'logic', or 'neither'.

    All 'battle' goals have `has_battle_interrupt=True`, `has_logic_interrupt=False`, and `logic_interrupt_name=""`.
    Their names usually end in 'Battle' (no underscore), but this is not necessary (e.g. common battle functions).

    All 'logic' goals have `has_battle_interrupt=False`, `has_logic_interrupt=True`, and
    `logic_interrupt_name={goal_name_prefix}_Interupt` [sic]. The goal name always ends in '_Logic'.

    All 'neither' goals have `has_battle_interrupt=False`, `has_logic_interrupt=False`, and `logic_interrupt_name=""`.
    These goals are typically referenced in other files (e.g. 'CrystalLizard330000Runaway'). They can have any name.
    """

    goal_id: int = -1
    goal_name: str = ""
    goal_type: GoalType = GoalType.Unknown
    script_name: str = ""

    def __post_init__(self):
        if not self.script_name:
            self.script_name = self.get_auto_script_name()

    @classmethod
    def from_luainfo_reader(cls, reader: BinaryReader, long_varints: bool, encoding: str) -> LuaGoalScript:
        goal_struct = LuaGoal64.from_bytes(reader) if long_varints else LuaGoal32.from_bytes(reader)
        name = reader.unpack_string(offset=goal_struct.name_offset, encoding=encoding)
        if goal_struct.logic_interrupt_name_offset > 0:
            logic_interrupt_name = reader.unpack_string(
                offset=goal_struct.logic_interrupt_name_offset, encoding=encoding
            )
        else:
            logic_interrupt_name = ""

        goal_type = GoalType.from_interrupt_info(
            goal_struct.has_battle_interrupt, goal_struct.has_logic_interrupt, logic_interrupt_name
        )

        return LuaGoalScript(
            goal_id=goal_struct.goal_id,
            goal_name=name,
            goal_type=goal_type,
        )

    def to_luainfo_writer(self, writer: BinaryWriter, long_varints: bool):

        goal_kwargs = {
            "has_battle_interrupt": self.goal_type == GoalType.Battle,
            "has_logic_interrupt": self.goal_type == GoalType.Logic,
        }

        (LuaGoal64 if long_varints else LuaGoal32).object_to_writer(self, writer, **goal_kwargs)

    def pack_logic_interrupt_name(self, writer: BinaryWriter, encoding: str):
        if self.goal_type == GoalType.Logic:
            if not self.goal_name.endswith("_Logic"):
                raise LuaError(f"Lua logic goal name must end in '_Logic'. Invalid: {repr(self.goal_name)}")
            logic_interrupt_name = self.goal_name[:-6] + "_Interupt"
            writer.fill_with_position("logic_interrupt_name", obj=self)
            writer.pack_z_string(logic_interrupt_name, encoding=encoding)
        else:
            writer.fill("logic_interrupt_name", 0, obj=self)

    def validate_goal_name(self):
        if self.goal_type == GoalType.Logic and not self.goal_name.endswith("_Logic"):
            raise LuaError(f"Logic goal name must end in '_Logic'. Invalid: {repr(self.goal_name)}")
        elif self.goal_type == "battle" and not self.goal_name.endswith("Battle"):
            _LOGGER.warning(f"Battle goal name {repr(self.goal_name)} does not end in 'Battle', which is unusual.")

    def get_auto_script_name(self):
        if self.goal_type == GoalType.Battle:
            return f"{self.goal_id:06d}_battle.lua"
        elif self.goal_type == GoalType.Logic:
            return f"{self.goal_id:06d}_logic.lua"
        elif self.goal_type == GoalType.Unknown:
            # Shouldn't happen anymore.
            snake_case_name = _SNAKE_CASE_RE.sub("_", self.goal_name).lower()
            return f"{snake_case_name}.lua"
        raise ValueError(f"Invalid `LuaGoal.type`: {self.goal_type}")

    def get_interrupt_details(self):
        if self.goal_type == GoalType.Battle:
            return {"has_battle_interrupt": True, "has_logic_interrupt": False, "logic_interrupt_name": ""}
        elif self.goal_type == GoalType.Logic:
            if self.goal_name.endswith("_Logic"):
                name = self.goal_name[:-6] + "_Interupt"
            else:
                raise LuaError(f"Logic goal name must end in '_Logic'. Invalid: {repr(self.goal_name)}")
            return {"has_battle_interrupt": False, "has_logic_interrupt": True, "logic_interrupt_name": name}
        elif self.goal_type == GoalType.Unknown:
            return {"has_battle_interrupt": False, "has_logic_interrupt": False, "logic_interrupt_name": ""}

    def __repr__(self):
        return f"LuaGoal({self.goal_id:06d}, {repr(self.goal_name)}, {repr(self.goal_type)})"


@dataclass(slots=True)
class LuaUnknownScript(LuaScriptBase):

    name: str = ""

    @property
    def script_name(self):
        return f"{self.name}.lua"

    def __repr__(self):
        return f"LuaUnknownScript(name={repr(self.name)})"
