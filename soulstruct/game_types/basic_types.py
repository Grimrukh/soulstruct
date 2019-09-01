from enum import IntEnum
from typing import Union

from soulstruct.events.core import get_value_test
from soulstruct.events.shared import instructions as instr

__all__ = ['GameObject', 'Flag', 'FlagInt', 'FlagRange', 'Map', 'FlagRangeOrSequence', 'MapOrSequence']


class GameObject(object):
    """Base class for all game types."""
    pass


class Flag(GameObject, IntEnum):
    """ Condition upon a flag as a shortcut to condition upon it being enabled. """

    def __call__(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        value = self if isinstance(self, (int, float)) else self.value
        return get_value_test(
            value=value, negate=negate, condition=condition, skip_lines=skip_lines,
            end_event=end_event, restart_event=restart_event,
            skip_if_true_func=instr.SkipLinesIfFlagOn, skip_if_false_func=instr.SkipLinesIfFlagOff,
            if_true_func=instr.IfFlagOn, if_false_func=instr.IfFlagOff,
            end_if_true_func=instr.EndIfFlagOn, end_if_false_func=instr.EndIfFlagOff,
            restart_if_true_func=instr.RestartIfFlagOn, restart_if_false_func=instr.RestartIfFlagOff)


FlagInt = Union[Flag, int]


class FlagRange(GameObject):
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # TODO: use the methods below in EVS parser.

    def any(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        return get_value_test(
            value=self, negate=negate, condition=condition, skip_lines=skip_lines,
            end_event=end_event, restart_event=restart_event,
            skip_if_true_func=instr.SkipLinesIfFlagRangeAllOff, skip_if_false_func=instr.SkipLinesIfFlagRangeAnyOn,
            if_true_func=instr.IfFlagRangeAnyOn, if_false_func=instr.IfFlagRangeAllOff,
            end_if_true_func=instr.EndIfFlagRangeAnyOn, end_if_false_func=instr.EndIfFlagRangeAllOff,
            restart_if_true_func=instr.RestartIfFlagRangeAnyOn, restart_if_false_func=instr.RestartIfFlagRangeAllOff,
        )

    def all(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        return get_value_test(
            value=self, negate=negate, condition=condition, skip_lines=skip_lines,
            end_event=end_event, restart_event=restart_event,
            skip_if_true_func=instr.SkipLinesIfFlagRangeAnyOff, skip_if_false_func=instr.SkipLinesIfFlagRangeAllOn,
            if_true_func=instr.IfFlagRangeAllOn, if_false_func=instr.IfFlagRangeAnyOff,
            end_if_true_func=instr.EndIfFlagRangeAllOn, end_if_false_func=instr.EndIfFlagRangeAnyOff,
            restart_if_true_func=instr.RestartIfFlagRangeAllOn, restart_if_false_func=instr.RestartIfFlagRangeAnyOff,
        )

    def __iter__(self):
        """Allows easy conversion to sequence."""
        yield self.first
        yield self.last


class Map(GameObject):
    def __init__(self, area_id, block_id, msb_file_name=None):
        self.area_id = area_id
        self.block_id = block_id
        self.emevd_file_name = f'm{area_id:02d}_{block_id:02d}_00_00'
        self.msb_file_name = self.emevd_file_name if msb_file_name is None else msb_file_name

    def __eq__(self, other_map):
        return self.area_id == other_map.area_id and self.block_id == other_map.block_id

    def __iter__(self):
        yield self.area_id
        yield self.block_id

    def __repr__(self):
        return self.emevd_file_name


FlagRangeOrSequence = Union[FlagRange, tuple, list]
MapOrSequence = Union[Map, tuple, list]
