from __future__ import annotations

__all__ = ["LuaInfo"]

import logging
from dataclasses import dataclass, field

from soulstruct.base.game_file import GameFile
from soulstruct.utilities.binary import *

from .lua import LuaError
from .lua_scripts import LuaGoalScript

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class LuaInfoStruct(NewBinaryStruct):
    lua_version: bytes = field(**Binary(length=4, asserted=b"LUAI"))
    endian_one: int = field(**Binary(asserted=1))  # confirms byte order is correcet
    goal_count: int
    _pad1: bytes = field(init=False, **BinaryPad(4))


@dataclass(slots=True)
class LuaInfo(GameFile):
    """Lists the goals defined in the Lua scripts contained inside the same `LuaBND` binder.

    Registration in this file is necessary for goal function names (e.g. `{goal}_Activate`) to be called by the AI
    system. However, `REGISTER_GOAL(goal_id, goal_name)` can also be called at the top of each Lua script to do this
    automatically, making this file unnecessary. (Dark Souls Remastered uses this call, even though the `LuaInfo` files
    are still present from PTDE.)

    Individual Lua function names may also be registered in the adjacent `LuaGNL` file but this is generally not needed.
    """

    byte_order: ByteOrder = ByteOrder.LittleEndian
    varint_size: int = 4
    goals: list[LuaGoalScript] = field(default_factory=list)

    @classmethod
    def from_reader(cls, reader: BinaryReader) -> LuaInfo:
        byte_order = BinaryCondition(
            (4, 4), [(ByteOrder.BigEndian, b"\00\00\00\01"), (ByteOrder.LittleEndian, b"\01\00\00\00")]
        )(reader)
        luainfo_struct = LuaInfoStruct.from_bytes(reader, byte_order=byte_order)
        varint_size = cls.get_varint_size(reader, luainfo_struct.goal_count)
        encoding = cls.get_encoding(byte_order, varint_size)

        goals = []
        goal_script_names = []
        for _ in range(luainfo_struct.goal_count):
            goal = LuaGoalScript.from_luainfo_reader(reader, varint_size, encoding)
            if goal.script_name in goal_script_names:
                _LOGGER.warning(
                    f"Goal '{goal.goal_id}' is referenced multiple times in LuaInfo (same ID and type). Each goal ID "
                    f"should have (at most) one 'battle' goal and one 'logic' goal. All goal entries after the first "
                    f"will be ignored, including: '{goal.script_name}'"
                )
            else:
                goals.append(goal)
                goal_script_names.append(goal.script_name)

        return cls(byte_order, varint_size, goals)

    def to_writer(self) -> BinaryWriter:
        writer = LuaInfoStruct.object_to_writer(self, byte_order=self.byte_order, goal_count=len(self.goals))
        encoding = self.get_encoding(self.byte_order, self.varint_size)

        for goal in self.goals:
            goal.to_luainfo_writer(writer, self.varint_size)
        for goal in self.goals:
            goal.pack_logic_interrupt_name(writer, encoding)

        return writer

    @staticmethod
    def get_encoding(byte_order: ByteOrder, varint_size: int):
        if varint_size == 8:
            return f"utf-16-{'be' if byte_order == ByteOrder.BigEndian else 'le'}"
        return "shift_jis_2004"

    @staticmethod
    def get_varint_size(reader: BinaryReader, goal_count: int) -> int:
        if goal_count == 0:
            raise LuaError("Cannot detect `LuaInfo` version if no goals are present.")
        elif goal_count >= 2:
            return reader.unpack_value("i", offset=0x24) == 0
        else:
            # Hacky check if there's only one goal.
            if reader.unpack_value("i", offset=0x18) == 0x28:
                return 8
            if reader.unpack_value("i", offset=0x14) == 0x20:
                return 4
            raise ValueError("Found unexpected data while trying to detect `LuaInfo` version from single goal.")
