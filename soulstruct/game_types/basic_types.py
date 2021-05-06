import typing as tp
from enum import IntEnum

__all__ = [
    "GameObject",
    "GameObjectSequence",
    "Flag",
    "FlagRange",
    "Texture",
    "VisualEffect",
    "TalkScript",
    "FlagInt",
    "FlagRangeTyping",
]


class GameObject:
    """Base class for all game types."""


class GameObjectSequence(type):
    """Metaclass that generates types that represent sequences of `GameObject`s.

    `GameObjectSequence` takes one sequence of two: a `GameObject` subclass, and an integer indicating the length of the
    sequence. For example:

        `GameObjectSequence((Region, 8))`
    """
    game_object_type: tp.Type[GameObject]
    count: int

    def __new__(mcs, game_object_and_count):
        if not game_object_and_count or len(game_object_and_count) != 2:
            raise TypeError("`GameObjectSequence` argument must be `(game_object_type, count)`.")
        if not issubclass(game_object_and_count[0], GameObject):
            raise TypeError(
                f"`GameObjectSequence` takes one sequence of `GameObject` subclasses, with the last element "
                f"optionally being an integer. Invalid sequence element: {type(game_object_and_count[0])}."
            )
        cls = super().__new__(mcs, "GameObjectSequence", (GameObjectSequence,), {})
        cls.game_object_type, cls.count = game_object_and_count
        return cls


class Flag(GameObject, IntEnum):
    """ Condition upon a flag as a shortcut to condition upon it being enabled. """

    def __call__(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        from soulstruct.base.events.emevd.utils import get_value_test
        from soulstruct.base.events.emevd import instructions as instr

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


class FlagRange(GameObject):
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # TODO: use the methods below in EVS parser.

    def any(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        from soulstruct.base.events.emevd.utils import get_value_test
        from soulstruct.base.events.emevd import instructions as instr

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
        from soulstruct.base.events.emevd.utils import get_value_test
        from soulstruct.base.events.emevd import instructions as instr

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


class Texture(GameObject, IntEnum):
    """2D texture ID of something."""


class VisualEffect(GameObject, IntEnum):
    """VFX ID of something."""


class TalkScript(GameObject):
    """Talk ID of a Map Character."""


FlagInt = tp.Union[Flag, int]
FlagRangeTyping = tp.Union[FlagRange, tuple, list]
