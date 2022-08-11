from __future__ import annotations

import logging
import struct
import typing as tp

from soulstruct.utilities.memory import *

if tp.TYPE_CHECKING:
    from soulstruct.darksouls1r.params import Param, GameParamBND
    from soulstruct.darksouls1r.params.draw_param import DrawParam

_LOGGER = logging.getLogger(__name__)


_PLAYER_TRANSFORM_PTRS = (0x68, 0x68, 0x28)  # WORLD_CHR_BASE
_DISPLAY_GROUP_PTRS = (0x20, 0x58, 0x498, 0x58, 0x2C0, 0x4E8)  # WORLD_CHR_BASE
_DISP_GROUP_DEBUG_PTRS = (0x4C0, 0x68, 0xA8)


class DSRMemoryHook(MemoryHook):

    # B8 DF 36 41 01 00 00 00
    _PARAM_MARKER = b"\xB8\xDF\x36\x41\x01\x00\x00\x00"  # appears at the start of every in-memory Param header struct

    PROCESS_NAME = "DarkSoulsRemastered.exe"
    BASE_ADDRESS = 0x140000000
    EVENT_FLAG_OFFSETS = (0x141D19950, 0, 0)

    PARAM_MEM_SEARCH_REGIONS = [
        (0x31000000, 0x33000000),
        (0x35000000, 0x36000000),
        (0x24000000, 0x26000000),
        (0x10000000, 0x40000000),  # last resort
    ]

    EVENT_FLAG_GROUPS = {
        "0": 0x00000,
        "1": 0x00500,
        "5": 0x05F00,
        "6": 0x0B900,
        "7": 0x11300,
    }

    EVENT_FLAG_AREAS = {
        "000": 0,
        "100": 1,
        "101": 2,
        "102": 3,
        "110": 4,
        "120": 5,
        "121": 6,
        "130": 7,
        "131": 8,
        "132": 9,
        "140": 10,
        "141": 11,
        "150": 12,
        "151": 13,
        "160": 14,
        "170": 15,
        "180": 16,
        "181": 17,
    }

    BASE_POINTER_TABLE = {
        # "WORLD_CHR_BASE": BasePointerSearch(
        #     br"\x48\x8B\x05....\x48\x8B\x48\x68\x48\x85\xC9\x0F\x84....\x48\x39\x5e\x10\x0F\x84....\x48",
        #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
        "WORLD_CHR_BASE": 0x141D151B0,
        "CURRENT_MAP": 0x141D27D60,
        # "CHR_CLASS_BASE": BasePointerSearch(
        #     br"\x48\x8B\x05....\x48\x85\xC0..\xF3\x0F\x58\x80\xAC\x00\x00\x00",
        #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
        # "CHR_CLASS_WARP": BasePointerSearch(
        #     br"\x48\x8B\x05....\x66\x0F\x7F\x80\xA0\x0B\x00\x00\x0F\x28\x02\x66\x0F\x7F\x80\xB0\x0B\x00\x00\xC6\x80",
        #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
        # "CAM_MAN_BASE": BasePointerSearch(
        #     br"\x48\x8B\x05....\x48\x63\xD1\x48\x8B\x44\xD0\x08\xC3",
        #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
        # "CHR_FOLLOW_CAM": BasePointerSearch(
        #     br"\x48\x8B\x0D....\xE8....\x48\x8B\x4E\x68",
        #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
        # "LOCK_TGT_BASE": BasePointerSearch(
        #     br"\x48\x8B\x0D....\x89\x99....\x4C\x89\x6D\x58",
        #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
        # "MENU_MAN_BASE": BasePointerSearch(
        #     br"\x48\x8B\x05....\x89\x88\x28\x08\x00\x00\x85\xC9",
        #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
        # "WORLD_CHR_DBG_BASE": BasePointerSearch(
        #     br"\x48\x8B\x05....\x48\x8B\x80\xF0\x00\x00\x00\x48\x85\xC0",
        #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
        # "PARAM": BasePointerSearch(
        #     br"\x4C\x8B\x05....\x48\x63\xC9\x48\x8D\x04\xC9\x41\x3B\x54\xC0\x10",
        #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
        # "THROW_PARAM": BasePointerSearch(
        #     br"\x48\x8B\x05....\x48\x8B\x40\x08\x48\x8B\x40\x38\x0F\xB7\x50\x0A\x3B\xCA..\x8B\xC9\x48\x83\xC1\x04\x48\x8D"
        #     br"\x0C\x49\x8B\x04\x88",
        #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
        # "DBG_EVENT_BASE": BasePointerSearch(
        #     br"\x48\x8B\x05....\x44\x38\x80......\x44\x38\x41\x49\x0F\x84....\x66\x0F\x6E\x41\x38\x48\x8B\x41\x10\x0F\x28"
        #     br"\x0D....\x48\x89\xBC\x24....\x0F\x5B\xC0\x4C\x89\xA4\x24",
        #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
        # "FRPG_NET_BASE": BasePointerSearch(
        #     br"\x48\x8B\x1D....\x48\x8D\x94\x24....\x4C\x8B\xF1\x0F\x29\x7C\x24\x40",
        #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
        # "NETWORK_PROP": BasePointerSearch(
        #     br"\x48\x89\x05....\x48\x83\x3D....\x00..\x4C\x8B\x05....\x4C\x89\x44\x24\x48\xBA\x08\x00\x00\x00\xB9\x58\x60"
        #     br"\x00\x00",
        #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
        # "WORLD_CHR_BASE_P": BasePointerSearch(
        #     br"\x48\x89\x05....\x48\x89\x5C\x24\x38\x48\x85\xDB..\x48\x8B\x03",
        #     lambda hook, addr: addr + hook.read_int32(addr + 3) + 7),
        # "WORLD_CHR_BASE_P": 0x141acd758,
    }

    VALUE_TABLE = {
        "player_angle": MemoryValue("WORLD_CHR_BASE", _PLAYER_TRANSFORM_PTRS + (0x4,), 4, "<f"),
        "player_x": MemoryValue("WORLD_CHR_BASE", _PLAYER_TRANSFORM_PTRS + (0x10,), 4, "<f"),
        "player_y": MemoryValue("WORLD_CHR_BASE", _PLAYER_TRANSFORM_PTRS + (0x14,), 4, "<f"),
        "player_z": MemoryValue("WORLD_CHR_BASE", _PLAYER_TRANSFORM_PTRS + (0x18,), 4, "<f"),
        "m10_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x850,), 16, "<IIII"),
        "m10_01_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0xAC0,), 16, "<IIII"),
        "m10_02_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0xD30,), 16, "<IIII"),
        "m11_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0xFA0,), 16, "<IIII"),
        "m12_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x1210,), 16, "<IIII"),
        "m12_01_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x1480,), 16, "<IIII"),
        "m13_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x16F0,), 16, "<IIII"),
        "m13_01_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x1960,), 16, "<IIII"),
        "m13_02_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x1BD0,), 16, "<IIII"),
        "m14_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x1E40,), 16, "<IIII"),
        "m14_01_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x20B0,), 16, "<IIII"),
        "m15_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x2320,), 16, "<IIII"),
        "m15_01_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x2590,), 16, "<IIII"),
        "m16_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x2800,), 16, "<IIII"),
        "m17_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x2A70,), 16, "<IIII"),
        "m18_00_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x2CE0,), 16, "<IIII"),
        "m18_01_display_groups": MemoryValue("WORLD_CHR_BASE", _DISPLAY_GROUP_PTRS + (0x2F50,), 16, "<IIII"),
        # "stable_angle": MemoryValue("CHR_CLASS_WARP", (0xBB4,), 4, "<f"),
        # "stable_x": MemoryValue("CHR_CLASS_WARP", (0xBA0,), 4, "<f"),
        # "stable_y": MemoryValue("CHR_CLASS_WARP", (0xBA4,), 4, "<f"),
        # "stable_z": MemoryValue("CHR_CLASS_WARP", (0xBA8,), 4, "<f"),
        "current_map": MemoryValue("CURRENT_MAP", (0xA20,), 4, "<BBBB"),  # (dd, cc, bb, aa)
    }

    @memory_hook_validate
    def get_event_flag_offset_mask(self, flag_id: int) -> (int, int):
        """Returns offset and bit mask of given flag ID.

        Raises a ValueError if the flag ID is not valid.
        """
        id_string = f"{flag_id:0>8}"
        if len(id_string) > 8:
            raise ValueError(f"Invalid flag ID (too large): {id_string}")
        group = id_string[:1]  # first digit
        area = id_string[1:4]  # second, third, fourth digits
        section = int(id_string[4:5])  # fifth digit
        number = int(id_string[5:8])  # sixth, seventh, eighth digits

        if group not in self.EVENT_FLAG_GROUPS:
            raise ValueError(f"Invalid flag ID (invalid group): {id_string}")
        if area not in self.EVENT_FLAG_AREAS:
            raise ValueError(f"Invalid flag ID (invalid area): {id_string}")

        offset = self.EVENT_FLAG_GROUPS[group]
        offset += self.EVENT_FLAG_AREAS[area] * 0x500
        offset += section * 128
        offset += (number - (number % 32)) // 8

        mask = 0x80000000 >> (number % 32)
        return offset, mask

    @memory_hook_validate
    def write_draw_param_to_memory(self, draw_param: DrawParam, area_id: int, slot=0):
        """Write the given `draw_param` for area `area_id` and slot `slot` to game memory.

        You MUST NOT change the number of rows in the `DrawParam` since the last time the game was loaded, as the size
        of the binary `DrawParam` data must stay the same. This method will check the DrawParam header to try to
        prevent this, as otherwise the game will definitely crash from invalid memory.

        Unlike GameParams, DrawParams are reloaded every time the game is *loaded*, not every time the game is started.
        This is fortunate for in-game testing, but it means the DrawParam memory addresses need to be reloaded (and
        re-cached) every time the game is reloaded.
        """
        if not draw_param.param_info:
            raise ValueError(f"Cannot write to game memory for Param type '{draw_param.param_type}'.")
        if slot not in {0, 1}:
            raise ValueError(f"Slot must be 0 or 1, not {slot}.")
        param_file_name = f"m{area_id}_{'1_' if slot == 1 else ''}{draw_param.param_info['file_name']}"
        paramdef_name = draw_param.param_info["paramdef_name"]
        self._write_param(draw_param.pack(sort=False), param_file_name, paramdef_name)

    @memory_hook_validate
    def write_game_param_to_memory(self, game_param: Param):
        """Write the given `GameParam` Param (NOT the entire `GameParamBND`) to game memory.

        GameParams are loaded into memory only once, when the game is launched, and their addresses do not change after
        that. Use `write_draw_param_to_memory` for DrawParams, which are reloaded every time the game loads (and require
        the area ID and slot to find the right param).
        """
        if not game_param.param_info:
            raise ValueError(f"Cannot write to game memory for Param type '{game_param.param_type}'.")
        param_file_name = game_param.param_info["file_name"]
        try:
            paramdef_name = game_param.param_info["paramdef_name"]
        except KeyError:
            print(game_param.param_info)
            raise
        self._write_param(game_param.pack(sort=False), param_file_name, paramdef_name)

    @memory_hook_validate
    def write_game_param_bnd_to_memory(self, game_param_bnd: GameParamBND):
        """Write all `GameParam` params with `param_info` defined to game memory."""
        for game_param in game_param_bnd.params.values():
            if game_param.param_info:
                self.write_game_param_to_memory(game_param)

    @memory_hook_validate
    def _write_param(self, packed_param: bytes, param_file_name: str, paramdef_name: str):
        """Internal method shared by GameParam and DrawParam writes. Use public methods above."""
        data_address = self.get_param_address(param_file_name, paramdef_name)
        existing_header = self.read(data_address, 44)  # up to end of param name (32j)
        if existing_header != packed_param[:44]:
            raise ValueError(
                f"Start of new Param header does not match start of existing Param header:\n"
                f"  New: {packed_param[:44]}\n"
                f"  Old: {existing_header}\n"
                f"This could be because the number of rows has changed or (less likely) the address is wrong."
            )
        self.write(data_address, packed_param)

    @memory_hook_validate
    def pre_cache_gameparam(self, param: Param, force_recache=False):
        """Find and cache addresses of all given `Params` to avoid doing it one-by-one later."""
        if not param.param_info:
            raise ValueError(f"Cannot write to game memory for Param type '{param.param_type}'.")
        param_file_name = param.param_info["file_name"]
        if not force_recache and param_file_name in self._address_cache.get("ds1r", {}):
            return
        try:
            paramdef_name = param.param_info["paramdef_name"]
        except KeyError:
            print(param.param_info)
            raise
        self.get_param_address(param_file_name, paramdef_name)

    @memory_hook_validate
    def pre_cache_drawparam(self, draw_param: DrawParam, area_id: int, slot: int, force_recache=False):
        """Find and cache addresses of all given `DrawParams` to avoid doing it one-by-one later."""
        if not draw_param.param_info:
            raise ValueError(f"Cannot write to game memory for Param type '{draw_param.param_type}'.")
        if slot not in {0, 1}:
            raise ValueError(f"Slot must be 0 or 1, not {slot}.")
        param_file_name = f"m{area_id}_{'1_' if slot == 1 else ''}{draw_param.param_info['file_name']}"
        paramdef_name = draw_param.param_info["paramdef_name"]
        self.get_param_address(param_file_name, paramdef_name, force_recache)

    @memory_hook_validate
    @memory_hook_cache
    def get_param_address(self, param_file_name: str, paramdef_name: str, force_recache=False):
        """Find memory address of given `param_file_name` (e.g. "NpcThinkParam" or "m15_1_LightScatteringBank").

        If an address is already cached, it is validated using `paramdef_name` (e.g. "NPC_THINK_PARAM_ST" or
        "LIGHT_SCATTERING_BANK") first.
        """
        if not force_recache:
            cached_address = self._address_cache.get("ds1r", {}).get(param_file_name, None)
            if cached_address is not None:
                # Try cached address first.
                paramdef_name_at_cached = self.read(cached_address + 12, 32).rstrip(b"\0")  # paramdef name string (32j)
                if paramdef_name_at_cached == paramdef_name.encode():
                    return cached_address  # address is still valid

        # Search for address.
        encoded_name = param_file_name.encode("utf-16-le")
        param_string_address = self.param_scan(encoded_name)
        if param_string_address is None:
            raise MemoryError(f"Could not find memory address of Param '{param_file_name}' in game memory.")
        # print(f"{param_file_name} string address: {hex(param_string_address)}")
        marker_search = self._PARAM_MARKER + struct.pack("Q", param_string_address)
        string_offset_address = self.param_scan(marker_search)
        if string_offset_address is None:
            raise MemoryError(f"Could not find memory address of Param '{param_file_name}' in game memory.")
        # print(f"{param_file_name} string offset address: {hex(string_offset_address)}")
        data_address = self.read(string_offset_address + 56, 8, "q")
        self._address_cache.setdefault("ds1r", {})[param_file_name] = data_address
        return data_address

    def param_scan(self, pattern: bytes) -> int | None:
        for start, end in self.PARAM_MEM_SEARCH_REGIONS:
            result = self.scan(pattern, search_from_address=start, max_address=end)
            if result is not None:
                return result
        return None


def test_dsr_hook():
    import time
    hook = DSRMemoryHook()
    print("Base pointers:")
    for pointer_base, pointer_value in hook.base_pointer_table.items():
        print(f"  {pointer_base}: {hex(pointer_value)}")
    print("Current values:")
    while True:
        time.sleep(2)
        try:
            print(f"  current_map = {hook.get('current_map')}")
        except MemoryHookCallError as ex:
            _LOGGER.exception(ex)
        except UnhookedError:
            print(f"UNHOOKED")


if __name__ == '__main__':
    test_dsr_hook()
