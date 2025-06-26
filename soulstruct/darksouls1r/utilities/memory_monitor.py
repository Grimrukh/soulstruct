"""Utility that just prints out information about all characters in a given map when requested."""
from __future__ import annotations

__all__ = ["MapMonitor", "MapChrInfo"]

import logging
import typing as tp
from pathlib import Path

from soulstruct.darksouls1r.constants import CHARACTER_MODELS
from soulstruct.darksouls1r.maps import MSB, get_map
from soulstruct.darksouls1r.utilities.memory import DSRMemoryHook, MemoryHookCallError

_LOGGER = logging.getLogger(__name__)


class MapChrInfo(tp.NamedTuple):
    handle_id: int
    model_name: str
    current_hp: int
    max_hp: int
    facing_angle: float  # radians
    x: float
    y: float
    z: float
    # TODO: more


class MapMonitor(DSRMemoryHook):

    AREA_HEADER_SIZE = 0x20
    BLOCK_HEADER_SIZE = 0xE8
    CHR_HEADER_SIZE = 0x38

    def get_character_list_count_address(self, map_area: int, map_block: int) -> tuple[int, int]:
        if not 10 <= map_area <= 18:
            raise ValueError(f"Map area must be between 10 and 18, inclusive, not: {map_area}")

        world_chr_base = self.base_pointer_table["WORLD_CHR_BASE"]
        world_chr_man = self.read_int64(world_chr_base)
        if world_chr_man == 0:
            raise MemoryHookCallError(
                f"Pointer 'WORLD_CHR_BASE' is 0, which suggests it has not been loaded in-game (are you only in the "
                f"main menu?)."
            )

        world_area_count = self.read_int64(world_chr_man + 0x18)
        assert world_area_count == 9

        area_list_address = self.read_int64(world_chr_man + 0x20)
        area_address = area_list_address + (map_area - 10) * self.AREA_HEADER_SIZE
        block_count = self.read_int64(area_address + 0x10)
        if map_block >= block_count:
            raise ValueError(f"Map block {map_block} is larger than count of area {map_area} in memory: {block_count}")
        block_list_address = self.read_int64(area_address + 0x18)
        block_address = block_list_address + map_block * self.BLOCK_HEADER_SIZE

        chr_count = self.read_int64(block_address + 0x48)
        if chr_count == 0:
            print(f"Character count (address {block_address + 0x48}) is zero.")
            return 0, -1  # map is not loaded, or is empty

        return chr_count, self.read_int64(block_address + 0x50)

    def get_character_list(self, map_area: int, map_block: int) -> list[MapChrInfo]:
        chr_count, chr_list_address = self.get_character_list_count_address(map_area, map_block)

        print(f"Chr list address: {hex(chr_list_address)} (area {map_area}, block {map_block})")

        if chr_count == 0:
            return []  # map not loaded, or empty

        chr_list = []

        for i in range(chr_count):
            chr_address = self.read_int64(chr_list_address + i * self.CHR_HEADER_SIZE)  # first offset in each header

            handle_id = self.read_int32(chr_address + 0x8)
            model_name = self.read(chr_address + 0x88, 10).decode("utf-16-le")  # e.g. 'c0000'
            current_hp = self.read_int32(chr_address + 0x3E8)
            max_hp = self.read_int32(chr_address + 0x3EC)

            map_info_address = self.read_int64(chr_address + 0x68)
            transform_address = self.read_int64(map_info_address + 0x28)  # also offset at 0x28 in header
            facing_angle = self.read_float(transform_address + 0x4)
            x = self.read_float(transform_address + 0x10)
            y = self.read_float(transform_address + 0x14)
            z = self.read_float(transform_address + 0x18)

            chr_list.append(MapChrInfo(
                handle_id, model_name, current_hp, max_hp, facing_angle, x, y, z
            ))

        return chr_list

    @classmethod
    def print_chr_health(cls, game_path_or_msb: Path | MSB, map_area: int, map_block: int):
        """Quickly print current health of all game characters in given map.

        `game_path_or_msb` must be given to determine the MSB character names.
        """
        game_map = get_map((map_area, map_block))
        if isinstance(game_path_or_msb, MSB):
            if game_path_or_msb.path_minimal_stem != game_map.msb_file_stem:
                _LOGGER.warning(
                    f"Given MSB file stem does not match given map area/block (expected {game_map.msb_file_stem}, got "
                    f"{game_path_or_msb.path_minimal_stem})."
                )
            msb = game_path_or_msb
        else:
            msb = MSB.from_path(game_path_or_msb / f"map/MapStudio/{game_map.msb_file_stem}.msb")

        monitor = cls()
        memory_chr_list = monitor.get_character_list(map_area, map_block)

        if len(memory_chr_list) != len(msb.characters):
            raise ValueError(
                f"Number of loaded characters in memory ({len(memory_chr_list)}) does not match number of Character "
                f"entries in MSB ({len(msb.characters)}) for map {game_map.msb_file_stem}."
            )

        for msb_chr, memory_chr in zip(msb.characters, memory_chr_list):
            model_name = CHARACTER_MODELS.get(int(memory_chr.model_name[1:]), memory_chr.model_name)
            output = f"{msb_chr.name:>40}: {memory_chr.current_hp} / {memory_chr.max_hp} <{model_name}>"
            if memory_chr.current_hp == 0:
                monitor._console.print(f"[red]{output}")
            elif memory_chr.current_hp < memory_chr.max_hp:
                monitor._console.print(f"[yellow]{output}")
            else:
                monitor._console.print(output)
