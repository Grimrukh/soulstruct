from enum import IntEnum
from typing import Union

from soulstruct.events.internal import get_value_test
from soulstruct.events.shared import instructions as instr

__all__ = ["GameObject", "Flag", "FlagInt", "FlagRange", "Map", "FlagRangeOrSequence", "MapOrSequence"]


class GameObject:
    """Base class for all game types."""


class Flag(GameObject, IntEnum):
    """ Condition upon a flag as a shortcut to condition upon it being enabled. """

    def __call__(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        value = self if isinstance(self, (int, float, tuple)) else self.value
        return get_value_test(
            value=value,
            negate=negate,
            condition=condition,
            skip_lines=skip_lines,
            end_event=end_event,
            restart_event=restart_event,
            skip_if_true_func=instr.SkipLinesIfFlagOn,
            skip_if_false_func=instr.SkipLinesIfFlagOff,
            if_true_func=instr.IfFlagOn,
            if_false_func=instr.IfFlagOff,
            end_if_true_func=instr.EndIfFlagOn,
            end_if_false_func=instr.EndIfFlagOff,
            restart_if_true_func=instr.RestartIfFlagOn,
            restart_if_false_func=instr.RestartIfFlagOff,
        )


FlagInt = Union[Flag, int]


class FlagRange(GameObject):
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # TODO: use the methods below in EVS parser.

    def any(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        return get_value_test(
            value=self,
            negate=negate,
            condition=condition,
            skip_lines=skip_lines,
            end_event=end_event,
            restart_event=restart_event,
            skip_if_true_func=instr.SkipLinesIfFlagRangeAllOff,
            skip_if_false_func=instr.SkipLinesIfFlagRangeAnyOn,
            if_true_func=instr.IfFlagRangeAnyOn,
            if_false_func=instr.IfFlagRangeAllOff,
            end_if_true_func=instr.EndIfFlagRangeAnyOn,
            end_if_false_func=instr.EndIfFlagRangeAllOff,
            restart_if_true_func=instr.RestartIfFlagRangeAnyOn,
            restart_if_false_func=instr.RestartIfFlagRangeAllOff,
        )

    def all(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        return get_value_test(
            value=self,
            negate=negate,
            condition=condition,
            skip_lines=skip_lines,
            end_event=end_event,
            restart_event=restart_event,
            skip_if_true_func=instr.SkipLinesIfFlagRangeAnyOff,
            skip_if_false_func=instr.SkipLinesIfFlagRangeAllOn,
            if_true_func=instr.IfFlagRangeAllOn,
            if_false_func=instr.IfFlagRangeAnyOff,
            end_if_true_func=instr.EndIfFlagRangeAllOn,
            end_if_false_func=instr.EndIfFlagRangeAnyOff,
            restart_if_true_func=instr.RestartIfFlagRangeAllOn,
            restart_if_false_func=instr.RestartIfFlagRangeAnyOff,
        )

    def __iter__(self):
        """Allows easy conversion to sequence."""
        return iter((self.first, self.last))


class Map(GameObject):
    def __init__(
        self,
        area_id,
        block_id,
        name=None,
        emevd_file_stem=None,
        msb_file_stem=None,
        ai_file_stem=None,
        esd_file_stem=None,
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

            name: Canonical name of map (e.g. "undeadburg"). Note that the map-finding utility `get_map` ignores case
                and underscores when looking for a specific name.

            emevd_file_stem: Name of `emevd` file for this map, without extension.
            msb_file_stem: Name of `msb` file for this map, without extension.
            ai_file_stem: Name of 'luabnd[.dcx]' for this map, without extension(s).
            esd_file_stem: Name of 'talkesdbnd[.dcx]' for this map, without extension(s).

            variable_name: Name to use in EVS output (typically upper case with underscores).
            verbose_name: Full descriptive name of map for display in certain output-only fields.

        `name`, `emevd_file_stem`, `msb_file_stem`, `ai_file_stem`, and `esd_file_stem` all default to
        `m{area_id:02d}_{block_id:02d}_00_00` if not specified. `verbose_name` defaults to `name`. `variable_name`
        defaults to None (not a valid EVS instruction argument).
        """
        self.area_id = area_id
        self.block_id = block_id

        base_id = f"m{area_id:02d}_{block_id:02d}_00_00" if area_id is not None and block_id is not None else None
        self.name = base_id if name is None else name

        self.emevd_file_stem = base_id if emevd_file_stem is None else emevd_file_stem
        self.msb_file_stem = base_id if msb_file_stem is None else msb_file_stem
        self.ai_file_stem = base_id if ai_file_stem is None else ai_file_stem
        self.esd_file_stem = base_id if esd_file_stem is None else esd_file_stem
        self.map_load_tuple = (area_id, block_id, -1, -1)  # for `MSBMapLoadTrigger`

        self.variable_name = variable_name
        self.verbose_name = self.name if verbose_name is None else verbose_name

    def stem_set(self):
        return {self.emevd_file_stem, self.msb_file_stem, self.ai_file_stem, self.esd_file_stem}

    def __eq__(self, other_map):
        return self.area_id == other_map.area_id and self.block_id == other_map.block_id

    def __iter__(self):
        return iter((self.area_id, self.block_id))

    def __repr__(self):
        return self.emevd_file_stem


FlagRangeOrSequence = Union[FlagRange, tuple, list]
MapOrSequence = Union[Map, tuple, list]
