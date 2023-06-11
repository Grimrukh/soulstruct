from __future__ import annotations

__all__ = [
    "DSRMemoryHook",
    "MemoryDrawParam",
    "MemoryHookCallError",
    "UnhookedError",
]

import copy
import logging
import pickle
import struct
import typing as tp
from types import MappingProxyType

from soulstruct.darksouls1r.params import Param, GameParamBND, ParamRow
from soulstruct.utilities.binary import ByteOrder
from soulstruct.utilities.memory import *
from soulstruct.utilities.files import PACKAGE_PATH

if tp.TYPE_CHECKING:
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

    # NOTE: Still needed for `GameParam` for now.
    PARAM_MEM_SEARCH_REGIONS = (
        (0x31000000, 0x33000000),
        (0x35000000, 0x36000000),
        (0x24000000, 0x26000000),
        (0x10000000, 0x40000000),  # last resort
    )

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
    def get_event_flag_offset_mask(self, flag_id: int) -> tuple[int, int]:
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

    # region Params
    @memory_hook_validate
    def write_game_param_to_memory(self, game_param: Param):
        """Write the given `GameParam` Param (NOT the entire `GameParamBND`) to game memory.

        GameParams are loaded into memory only once, when the game is launched, and their addresses do not change after
        that.
        """
        if not game_param.path:
            raise ValueError("Param must have `path` set to write it to memory.")
        self._write_param(bytes(game_param.to_writer(sort=False)), game_param.path.name, game_param.param_type)

    @memory_hook_validate
    def write_gameparambnd_to_memory(self, gameparambnd: GameParamBND):
        """Write all `GameParam` params with `param_info` defined to game memory."""
        for game_param in gameparambnd.params.values():
            if isinstance(game_param, Param):  # NOT `ParamDict`
                self.write_game_param_to_memory(game_param)

    @memory_hook_validate
    def _write_param(self, packed_param: bytes, param_file_name: str, param_type: str):
        """Internal method shared by GameParam and DrawParam writes. Use public methods above."""
        data_address = self.get_param_address(param_file_name, param_type)
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
        """Find and cache addresses of given `Param` to avoid doing it lazily at write time."""
        if not param.path:
            raise ValueError("Param must have `path` set to cache its memory address.")
        if not force_recache and param.path.name in self._address_cache.get("ds1r", {}):
            return  # already cached; will not replace
        self.get_param_address(param.path.name, param.param_type)

    @memory_hook_validate
    def get_memory_draw_param(
        self, draw_param_row_type: tp.Type[ParamRow], draw_param_stem: str, area_id: int, is_extra_slot=False
    ) -> MemoryDrawParam:
        """Uses actual pointer table! No need to cache anymore, as no searching is required.

        Returns object can be modified, read from memory, and written to memory as long as this hook is valid.

        Does NOT read from memory automatically. Use `MemoryDrawParam.read_from_memory()` to do that.
        """
        return MemoryDrawParam(
            self,
            draw_param_row_type,
            draw_param_stem,
            area_id,
            is_extra_slot=is_extra_slot,
        )

    @memory_hook_validate
    @memory_hook_cache
    def get_param_address(self, param_file_name: str, param_type: str, force_recache=False):
        """Find memory address of given `param_file_name` (e.g. "NpcThinkParam" or "m15_1_LightScatteringBank").

        If an address is already cached, it is validated using `param_type` (e.g. "NPC_THINK_PARAM_ST" or
        "LIGHT_SCATTERING_BANK") first.
        """
        cached_address = self._address_cache.get("ds1r", {}).get(param_file_name, None)
        if cached_address is not None:
            if not force_recache:
                # Try cached address first.
                param_type_at_cached = self.read(cached_address + 12, 32).rstrip(b"\0")  # paramdef name string (32j)
                if param_type_at_cached == param_type.encode():
                    return cached_address  # address is still valid
            extra_memory_region_start = cached_address // 0x1000000 * 0x1000000
            extra_memory_regions = ((extra_memory_region_start, extra_memory_region_start + 0x1000000),)
        else:
            extra_memory_regions = ()

        # Search for address.
        print(f"Getting address of param {param_file_name}")
        encoded_name = param_file_name.encode("utf-16-le")
        param_string_address = self.single_param_scan(
            encoded_name, extra_memory_regions=extra_memory_regions
        )
        if param_string_address is None:
            raise MemoryError(f"Could not find memory address of Param '{param_file_name}' string in game memory.")
        # print(f"{param_file_name} string address: {hex(param_string_address)}")
        marker_search = self._PARAM_MARKER + struct.pack("Q", param_string_address)
        string_offset_address = self.single_param_scan(
            marker_search, extra_memory_regions=extra_memory_regions, ignore_repeats=True
        )
        if string_offset_address is None:
            raise MemoryError(f"Could not find memory address of Param '{param_file_name}' table in game memory.")
        # print(f"{param_file_name} string offset address: {hex(string_offset_address)}")
        data_address = self.read(string_offset_address + 56, 8, "q")
        self._address_cache.setdefault("ds1r", {})[param_file_name] = data_address
        return data_address

    @memory_hook_validate
    def get_param_addresses(self, param_file_names: list[str], param_types: list[str], force_recache=False):
        """Find memory address of all given `param_file_names` at once, which leads to more efficient scanning.

        If an address is already cached, it is validated using `param_type` (e.g. "NPC_THINK_PARAM_ST" or
        "LIGHT_SCATTERING_BANK") first.

        NOTE: For DrawParams, `param_file_names` should already include 'mAA' and slot prefix.
        """
        if len(param_file_names) != len(param_types):
            raise ValueError("Number of param file names and paramdef names to scan for must match.")

        try:
            with PACKAGE_PATH("__address_cache__").open("rb") as f:
                self._address_cache = pickle.load(f)
        except (FileNotFoundError, EOFError, ValueError):
            self._address_cache = {}

        params_to_find = list(param_file_names)
        param_addresses = {param_file_name: None for param_file_name in param_file_names}

        if not force_recache:
            for param_file_name, param_type in zip(param_addresses.keys(), param_types):
                cached_address = self._address_cache.get("ds1r", {}).get(param_file_name, None)
                if cached_address is not None:
                    # Try cached address first.
                    param_type_at_cached = self.read(cached_address + 12, 32).rstrip(b"\0")  # paramdef name string
                    if param_type_at_cached == param_type.encode():
                        param_addresses[param_file_name] = cached_address  # address is still valid
                        params_to_find.remove(param_file_name)

        # Use cached address as a clue to memory region.
        extra_memory_regions = []
        for param_file_name in param_addresses:
            cached_address = self._address_cache.get("ds1r", {}).get(param_file_name, None)
            if cached_address is not None:
                extra_memory_region_start = cached_address // 0x1000000 * 0x1000000  # e.g., `0x33000000`
                extra_memory_regions.append((extra_memory_region_start, extra_memory_region_start + 0x1000000))
        extra_memory_regions = sorted(set(extra_memory_regions))

        encoded_names = {param_file_name: param_file_name.encode("utf-16-le") for param_file_name in params_to_find}
        param_string_addresses = self.param_scan(
            encoded_names, extra_memory_regions=extra_memory_regions, ignore_repeats=True,
        )
        for param_file_name, string_address in param_string_addresses.items():
            if string_address is None:
                print(param_string_addresses)
                raise MemoryError(f"Could not find memory address of Param '{param_file_name}' string in game memory.")
        # print(f"{param_file_name} string address: {hex(param_string_address)}")
        marker_search = {
            param_file_name: self._PARAM_MARKER + struct.pack("Q", param_string_addresses[param_file_name])
            for param_file_name in params_to_find
        }
        string_offset_addresses = self.param_scan(
            marker_search, extra_memory_regions=extra_memory_regions, ignore_repeats=True
        )
        for param_file_name, offset_address in string_offset_addresses.items():
            if offset_address is None:
                raise MemoryError(f"Could not find memory address of Param '{param_file_name}' table in game memory.")
            else:
                param_addresses[param_file_name] = self.read(offset_address + 56, 8, "q")
                self._address_cache.setdefault("ds1r", {})[param_file_name] = param_addresses[param_file_name]

        with PACKAGE_PATH("__address_cache__").open("wb") as f:
            pickle.dump(self._address_cache, f)

        return param_addresses

    def param_scan(
        self,
        patterns: bytes | dict[str, bytes],
        extra_memory_regions=(),
        ignore_repeats=False,
    ) -> dict[str, int | None]:
        for address_range in tuple(extra_memory_regions) + self.PARAM_MEM_SEARCH_REGIONS:
            print(f"Searching mem region: {hex(address_range[0])} - {hex(address_range[1])}")
            result = self.scan(patterns, address_range=address_range, ignore_repeats=ignore_repeats)
            if all(v is not None for v in result.values()):
                return result  # all patterns found
        return {}

    def single_param_scan(self, pattern: bytes, extra_memory_regions=(), ignore_repeats=False) -> int | None:
        for address_range in tuple(extra_memory_regions) + self.PARAM_MEM_SEARCH_REGIONS:
            print(f"Searching mem region: {hex(address_range[0])} - {hex(address_range[1])}")
            result = self.single_scan(
                pattern, address_range=address_range, ignore_repeats=ignore_repeats
            )
            if result is not None:
                return result
        return None
    # endregion


PARAM_ROW_DATA_T = tp.TypeVar("PARAM_ROW_DATA_T", bound=ParamRow)


class MemoryDrawParam(tp.Generic[PARAM_ROW_DATA_T]):
    """Interface to reading/writing a single DrawParam table in memory."""

    # Base address of DrawParam manager struct (in DSR 1.03).
    DRAW_PARAM_BASE = 0x141D1C468
    # Bytes between slot 0 pointer and slot 1 pointer.
    DRAW_PARAM_SLOT_1_OFFSET = 0x138
    # Size of all draw param pointers combined per area, plus header.
    AREA_DRAW_PARAM_SIZE = 0x280
    # Offset in Param where row count (short) is stored.
    PARAM_ROW_COUNT_OFFSET = 0xA
    # Offset in Param where row pointer structs begin (i.e. header size).
    PARAM_ROW_POINTER_OFFSET = 0x30

    # Maps DrawParam types to their pointer offsets in the DrawParam manager struct.
    POINTER_OFFSETS = {
        "DofBank": 0x10,
        "EnvLightTexBank": 0x28,
        "FogBank": 0x40,
        "LensFlareBank": 0x58,
        "LensFlareExBank": 0x70,
        "LightBank": 0x88,
        "s_LightBank": 0xA0,
        "LightScatteringBank": 0xB8,
        # Unused: 0xD0
        "PointLightBank": 0xE8,
        "ShadowBank": 0x100,
        "ToneCorrectBank": 0x118,
        "ToneMapBank": 0x130,
    }

    hook: DSRMemoryHook
    draw_param_row_type: tp.Type[PARAM_ROW_DATA_T]
    area_id: int
    is_extra_slot: bool

    draw_param_stem: str  # e.g. 'FogBank'

    draw_param_file_stem: str  # e.g. 'm12_1_FogBank' for row type `FOG_BANK` in `area_id` 12 with `is_extra_slot=True`
    row_dict: MappingProxyType[int, PARAM_ROW_DATA_T]  # row ID -> row data (cannot change size)

    def __init__(
        self,
        hook: DSRMemoryHook,
        draw_param_row_type: tp.Type[PARAM_ROW_DATA_T],
        draw_param_stem: str,
        area_id: int,
        is_extra_slot=False,
    ):
        self.hook = hook
        self.draw_param_row_type = draw_param_row_type
        self.area_id = area_id
        self.is_extra_slot = is_extra_slot

        self.draw_param_stem = draw_param_stem

        if draw_param_stem.startswith("s_"):
            self.draw_param_file_stem = f"s{area_id:02d}{'_1' if is_extra_slot else ''}_{draw_param_stem[2:]}"
        else:
            self.draw_param_file_stem = f"m{area_id:02d}{'_1' if is_extra_slot else ''}_{draw_param_stem}"

        self.row_dict = MappingProxyType({})

    def read_from_memory(self):
        """Read all rows from memory into `row_dict`.

        NOTE: This will overwrite any changes you've made to `row_dict` since the last read!
        """
        if not self.hook.try_hooked():
            _LOGGER.warning(f"Cannot read DrawParam `{self.draw_param_file_stem}` from unhooked memory.")

        param_data_address = self._get_param_data_address()
        if param_data_address == 0:
            return  # cannot read

        self.row_dict = MappingProxyType(self._read_rows(param_data_address))

    def write_to_memory(self):
        """Write current `row_dict` to memory."""
        if not self.hook.try_hooked():
            _LOGGER.warning(f"Cannot write DrawParam `{self.draw_param_file_stem}` to unhooked memory.")

        if not self.row_dict:
            raise RuntimeError(
                f"Cannot write DrawParam `{self.draw_param_file_stem}` to memory before calling `read_from_memory()`."
            )

        param_data_address = self._get_param_data_address()
        if param_data_address == 0:
            return  # cannot write

        self._write_rows(param_data_address)

    def __getitem__(self, row_id: int) -> PARAM_ROW_DATA_T:
        return self.row_dict[row_id]

    def copy(self) -> MemoryDrawParam:
        """Return a deep copy of this `MemoryDrawParam`."""
        return copy.deepcopy(self)

    def set_from_draw_param(self, draw_param: DrawParam):
        if draw_param.ROW_TYPE != self.draw_param_row_type:
            raise ValueError(
                f"DrawParam of type `{draw_param.ROW_TYPE}` is not the correct type for "
                f"this MemoryDrawParam (`{self.draw_param_row_type}`)."
            )
        if len(draw_param.rows) != len(self.row_dict):
            raise ValueError(
                f"DrawParam of type `{draw_param.ROW_TYPE}` does not have the correct number of rows "
                f"({len(draw_param.rows)}) for this MemoryDrawParam ({len(self.row_dict)})."
            )
        # Copy all row data.
        self.row_dict = MappingProxyType({row_id: row for row_id, row in draw_param.rows.items()})

    def _read_rows(self, param_data_address: int) -> dict[int, PARAM_ROW_DATA_T]:
        row_count = self.hook.read_int16(param_data_address + self.PARAM_ROW_COUNT_OFFSET)
        _LOGGER.info(f"Reading {row_count} rows from memory for Param {self.draw_param_stem}.")

        row_dict = {}
        param_row_ptr_address = param_data_address + self.PARAM_ROW_POINTER_OFFSET  # first row pointer
        for i in range(row_count):
            row_id = self.hook.read_int32(param_row_ptr_address + i * 12 + 0)
            data_offset = self.hook.read_int32(param_row_ptr_address + i * 12 + 4)
            name_offset = self.hook.read_int32(param_row_ptr_address + i * 12 + 8)
            raw_name = self.hook.read_z_bytes(param_data_address + name_offset)
            if raw_name:
                _LOGGER.debug(f"Loaded {self.draw_param_stem} row {row_id} with RawName: {raw_name}")
            try:
                name = raw_name.decode("shift_jis_2004")
            except UnicodeDecodeError:
                name = ""  # cannot decode
            row_data = self.hook.read(param_data_address + data_offset, size=self.draw_param_row_type.get_size())
            row_dict[row_id] = self.draw_param_row_type.from_reader(row_data, raw_name=raw_name, name=name)
        return row_dict

    def _write_rows(self, param_data_address: int):
        """Write `row_dict`."""
        row_count = self.hook.read_int16(param_data_address + self.PARAM_ROW_COUNT_OFFSET)
        if row_count != len(self.row_dict):
            _LOGGER.error(
                f"DrawParam `{self.draw_param_file_stem}` has {row_count} rows in memory. Cannot write "
                f"{len(self.row_dict)} rows to it. (Did you reload the game with a new row count?)"
            )

        param_row_ptr_address = param_data_address + self.PARAM_ROW_POINTER_OFFSET  # first row pointer
        for i, (row_id, row_data) in enumerate(self.row_dict.items()):
            row_data: PARAM_ROW_DATA_T
            data_offset = self.hook.read_int32(param_row_ptr_address + i * 12 + 4)
            name_offset = self.hook.read_int32(param_row_ptr_address + i * 12 + 8)
            raw_name = self.hook.read_z_bytes(param_data_address + name_offset)
            if raw_name:
                _LOGGER.debug(f"Writing {self.draw_param_stem} row {row_id} with RawName: {raw_name}")
            self.hook.write(param_data_address + data_offset, row_data.to_bytes(byte_order=ByteOrder.LittleEndian))

    def _get_area_draw_param_list_address(self):
        draw_param_list_address = self.hook.read_int64(self.DRAW_PARAM_BASE)
        area_start = draw_param_list_address + 0x18 + (self.area_id - 10) * self.AREA_DRAW_PARAM_SIZE

        area_id_bytes = self.hook.read(area_start, 4)
        area_id = struct.unpack('>i', area_id_bytes)[0]  # area ID is big-endian for some reason
        if area_id == -1:
            _LOGGER.warning(f"Area {self.area_id} has not been loaded yet.", True)
            return 0
        if area_id != self.area_id:
            raise Exception(f"Area ID mismatch in memory: {area_id} != {self.area_id}")

        return area_start

    def _get_param_data_address(self) -> int:
        """Get the address where the loaded `DrawParam` starts."""
        area_start = self._get_area_draw_param_list_address()
        if area_start == 0:
            return 0

        pointer_offset = self.POINTER_OFFSETS[self.draw_param_stem]

        draw_param_header_address = self.hook.read_int64(
            area_start + pointer_offset + (self.DRAW_PARAM_SLOT_1_OFFSET if self.is_extra_slot else 0)
        )
        if draw_param_header_address == 0:
            if self.is_extra_slot:
                _LOGGER.warning(f"Slot 1 DrawParam '{self.draw_param_file_stem}' is empty.")
            else:
                raise MemoryHookCallError(
                    f"Slot 0 DrawParam '{self.draw_param_file_stem}' is empty. This should never happen!"
                )
            return 0

        file_stem_address = self.hook.read_int64(draw_param_header_address + 0x8)
        param_file_stem = self.hook.read_utf16_z_string(file_stem_address)
        if param_file_stem == self.draw_param_file_stem:
            return self.hook.read_int64(draw_param_header_address + 0x38)

        _LOGGER.error(
            f"Expected DrawParam file stem '{self.draw_param_file_stem}', but found '{param_file_stem}'. "
            f"Param not loaded."
        )
        return 0


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
