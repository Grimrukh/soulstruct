from enum import IntEnum
from typing import Union

from soulstruct.emevd.core import get_value_test
from soulstruct.emevd.shared import instructions as instr

__all__ = ['GameObject', 'Flag', 'FlagRange', 'EventInfo', 'Animation', 'PlayerAnimation', 'Map',
           'FlagInt', 'FlagRangeOrSequence', 'AnimationInt', 'MapOrSequence']


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


class FlagRange(GameObject):
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # TODO (minor): use the methods below in EVS parser.

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


class EventInfo(object):
    """Contains the ID and description of an event (not an enum). Name is to avoid clash with emevd.Event.

    The 'name' field is likely the key used to index instances of this, so is optional to pass in.
    """
    def __init__(self, event_id, description="None", name=""):
        self.id = event_id
        self.name = name
        self.description = description


class Animation(IntEnum):
    """Animation ID base class."""
    # TODO: playback methods.
    pass


class PlayerAnimation(IntEnum):
    """Animation IDs for player character and human NPCs."""
    # TODO: playback methods.
    pass


class Map(GameObject):
    def __init__(self, area_id, block_id):
        self.area_id = area_id
        self.block_id = block_id
        self.file_name = f'm{area_id:02d}_{block_id:02d}_00_00'

    def __eq__(self, other_map):
        return self.area_id == other_map.area_id and self.block_id == other_map.block_id

    def __iter__(self):
        yield self.area_id
        yield self.block_id

    def __repr__(self):
        return self.file_name


FlagInt = Union[Flag, int]
FlagRangeOrSequence = Union[FlagRange, tuple, list]
AnimationInt = Union[Animation, int]
MapOrSequence = Union[Map, tuple, list]
