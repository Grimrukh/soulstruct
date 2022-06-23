from __future__ import annotations

__all__ = [
    "Map",
    "MapEntry",
    "MapEntity",
    "MapTyping",
]

import typing as tp
from enum import IntEnum, unique

from .basic_types import BaseGameObject


class Map(BaseGameObject):
    def __init__(
        self,
        area_id: tp.Optional[int],
        block_id: tp.Optional[int],
        cc_id: tp.Optional[int] = 0,
        dd_id: tp.Optional[int] = 0,
        name=None,
        emevd_file_stem=None,
        msb_file_stem=None,
        ai_file_stem=None,
        esd_file_stem=None,
        ffxbnd_file_name=None,
        variable_name=None,
        verbose_name=None,
    ):
        """
        Create a game map instance with associated naming information. These instances can be used as arguments in EVS
        instructions.

        Soulstruct defines constants for existing game maps already, so you shouldn't need to use this class yourself.
        (You can theoretically use transient `Map(a, b)` calls as arguments in EVS instructions, but you may as well
        just use a tuple `(a, b)` in that case, which is also accepted.)

        Args:
            area_id: Area ID of map, which is the first number (of four) in the full map ID. Multiple maps can appear in
                the same area. Some game files (such as lighting parameters) are area-specific rather than map-specific.
            block_id: Block ID of map, which is the second number (of four) in the full map ID. Generally, the area ID
                and block ID fully specify the map. The third number in the map ID is essentially never used and the
                fourth number is only used for file revision purposes (e.g. the Dark Souls DLC version of Darkroot).
            cc_id: Third part of map ID, used only in later games with lots of maps.
            dd_id: Fourth and final part of map ID, used only in later games with lots of maps.

            name: Canonical name of map (e.g. "undeadburg"). Note that the map-finding utility `get_map` ignores case
                and underscores when looking for a specific name.

            emevd_file_stem: Name of `emevd` file for this map, without extension.
            msb_file_stem: Name of `msb` file for this map, without extension.
            ai_file_stem: Name of 'luabnd[.dcx]' for this map, without extension(s).
            esd_file_stem: Name of 'talkesdbnd[.dcx]' for this map, without extension(s).

            ffxbnd_file_name: Name of 'ffxbnd[.dcx]' file that Soulstruct should modify for this map. Map areas with
                multiple blocks may have an area-wide file and block-specific files that are both loaded. The block-
                specific files are preferred for ease/efficiency.

            variable_name: Name to use in EVS output (typically upper case with underscores).
            verbose_name: Full descriptive name of map for display in certain output-only fields.

        `name`, `emevd_file_stem`, `msb_file_stem`, `ai_file_stem`, and `esd_file_stem` all default to
        `m{area_id:02d}_{block_id:02d}_00_00` if not specified. `verbose_name` defaults to `name`. `variable_name`
        defaults to None (not a valid EVS instruction argument).
        """
        self.area_id = area_id
        self.block_id = block_id
        self.cc_id = cc_id
        self.dd_id = dd_id

        if area_id is not None and block_id is not None:
            base_id = f"m{area_id:02d}_{block_id:02d}_{cc_id:02d}_{dd_id:02d}"
        else:
            base_id = None
        self.name = base_id if name is None else name

        self.emevd_file_stem = base_id if emevd_file_stem is None else emevd_file_stem
        self.msb_file_stem = base_id if msb_file_stem is None else msb_file_stem
        self.ai_file_stem = base_id if ai_file_stem is None else ai_file_stem
        self.esd_file_stem = base_id if esd_file_stem is None else esd_file_stem
        self.map_load_tuple = (area_id, block_id, -1, -1)  # for `MSBMapConnection`
        self.ffxbnd_file_name = ffxbnd_file_name

        self.variable_name = variable_name
        self.verbose_name = self.name if verbose_name is None else verbose_name

        if self.area_id is not None:
            self.base_entity_id = 100000 * self.area_id + 10000 * self.block_id
            self.flag_prefix = 1000 + 10 * self.area_id + self.block_id

    def stem_set(self):
        return {
            stem
            for stem in (self.emevd_file_stem, self.msb_file_stem, self.ai_file_stem, self.esd_file_stem)
            if stem
        }

    def __eq__(self, other_map: Map):
        return self.area_id == other_map.area_id and self.block_id == other_map.block_id

    def __iter__(self):
        return iter((self.area_id, self.block_id, self.cc_id, self.dd_id))

    def __repr__(self):
        return self.emevd_file_stem

    def __getitem__(self, index: int):
        if index == 0:
            return self.area_id
        elif index == 1:
            return self.block_id
        elif index == 2:
            return self.cc_id
        elif index == 3:
            return self.dd_id
        else:
            raise ValueError(f"Index for `Map` must be 0, 1, 2, or 3, not {index}.")

    @classmethod
    def NO_MAP(cls):
        """Used as a default null map in MSB."""
        return cls(0, 0, 0, 0, name="NONE")


class MapEntry(BaseGameObject):
    """Anything that appears in an MSB."""
    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False) -> [str, str]:
        """Returns the pluralized name of the MSB type (e.g. "Parts") and the non-pluralized name of the subtype
        (e.g. "Character")."""
        raise NotImplementedError

    @classmethod
    def get_msb_class_name(cls) -> str:
        """Returns the name of the Soulstruct MSB class (e.g. "MSBRegionBox").

        By default, this is done by simply prefixing "MSB" to the class name."""
        if cls.__name__ == "MapEntry":
            raise NotImplementedError("MapEntry base class has no corresponding non-abstract MSB class.")
        return f"MSB{cls.__name__}"


@unique
class MapEntity(MapEntry, IntEnum):
    """Any MSB entry with an entity ID (enum values)."""

    @classmethod
    def get_msb_entry_type_subtype(cls, pluralized_subtype=False) -> [str, str]:
        raise NotImplementedError

    @classmethod
    def get_id_start_and_max(cls) -> tuple[int, int]:
        """Return first and last entity ID value for automatic generation of entity IDs for specific `game`.

        Not supported by default; supported subclasses will override this method.
        """
        raise TypeError(f"`{cls.__name__}` does not use entity IDs.")

    @classmethod
    def auto_generate(cls, count, map_range_start: int):
        """Get value for `auto()`.

        Raises `TypeError` if not valid for this class, and `NotImplementedError` if not implemented for given `game`.
        """
        start_value, max_value = cls.get_id_start_and_max()
        value = map_range_start + start_value + count
        if value > map_range_start + max_value:
            raise ValueError(f"Too many members in `{cls.__name__}` for `auto()` range `({start_value}, {max_value})`.")
        return value

    # noinspection PyMethodOverriding
    @staticmethod
    def _generate_next_value_(name, start, count, last_values):
        raise ValueError("Cannot use `auto()` for this `MapEntity` subclass.")


MapTyping = tp.Union[Map, tuple, list]
