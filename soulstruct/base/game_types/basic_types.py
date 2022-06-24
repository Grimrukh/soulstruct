from __future__ import annotations

__all__ = [
    "BaseGameObject",
    "GameObjectSequence",
    "BaseParam",
    "BaseGameParam",
    "Flag",
    "FlagInt",
    "MapFlagSuffix",
    "FlagRange",
    "FlagRangeTyping",
    "Texture",
    "VisualEffect",
    "TalkScript",
    "Text",
    "Animation",
    "PlayerAnimation",
    "BaseAIScript",
    "LogicAIScript",
    "BattleAIScript",
]

import typing as tp
from enum import IntEnum


class BaseGameObject:
    """Base class for all game types.

    Note that using `abc.ABC` for this, or any of its technically abstract intermediate subclasses, leads to problems.
    """

    @classmethod
    def get_event_arg_fmt(cls) -> tp.Optional[str]:
        """If not `None`, allows this type to be used as an EVS event arg type hint for this format."""
        return None


class GameObjectSequence(type):
    """Metaclass that generates types that represent sequences of `GameObject`s.

    `GameObjectSequence` takes one sequence of two: a `GameObject` subclass, and an integer indicating the length of the
    sequence. For example:

        `GameObjectSequence((Region, 8))`
    """
    game_object_type: tp.Type[BaseGameObject]
    count: int

    def __new__(mcs, game_object_and_count):
        if not game_object_and_count or len(game_object_and_count) != 2:
            raise TypeError("`GameObjectSequence` argument must be `(game_object_type, count)`.")
        if not issubclass(game_object_and_count[0], BaseGameObject):
            raise TypeError(
                f"`GameObjectSequence` takes one sequence of `GameObject` subclasses, with the last element "
                f"optionally being an integer. Invalid sequence element: {type(game_object_and_count[0])}."
            )
        cls = super().__new__(mcs, "GameObjectSequence", (GameObjectSequence,), {})
        cls.game_object_type, cls.count = game_object_and_count
        return cls


class BaseParam(BaseGameObject, IntEnum):
    """Base class for IDs of param entries."""

    @classmethod
    def get_param_nickname(cls):
        raise NotImplementedError


class BaseGameParam(BaseParam):
    """Base class for IDs of GameParam entries."""

    @classmethod
    def get_param_nickname(cls):
        raise NotImplementedError


class Flag(BaseGameObject, IntEnum):
    """Event flag."""

    @classmethod
    def get_event_arg_fmt(cls):
        return "i"


class MapFlagSuffix(IntEnum):
    """Flag up to four digits long, intended to be added to a map base flag (such as 11020000 for m10_02).

    `EVSParser` will compute the true flag ID automatically if it knows the map's base flag ID.
    """


class FlagRange(BaseGameObject):

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __iter__(self):
        """Allows easy conversion to sequence."""
        return iter((self.first, self.last))

    def __getitem__(self, index: int):
        if index == 0:
            return self.first
        elif index == 1:
            return self.last
        raise ValueError(f"`FlagRange` index must be 0 or 1, not {index}.")

    def __repr__(self) -> str:
        return f"({self.first}, {self.last})"


class Texture(BaseGameObject, IntEnum):
    """2D texture ID of something."""


class VisualEffect(BaseGameObject, IntEnum):
    """VFX ID of something."""


class TalkScript(BaseGameObject, IntEnum):
    """Talk ID of a Map Character."""


class Text(BaseGameObject, IntEnum):
    """Text ID for an entry in some FMG."""

    @classmethod
    def get_text_category(cls):
        raise NotImplementedError


class Animation(BaseGameObject, IntEnum):
    """Animation ID base class."""


class PlayerAnimation(Animation):
    """Animation IDs for player character and human NPCs."""


class BaseAIScript(BaseGameObject, IntEnum):
    """Base type for Logic and Battle scripts."""


class LogicAIScript(BaseAIScript):
    """Script that governs a character outside of battle."""


class BattleAIScript(BaseAIScript):
    """Script that governs a character in battle."""


FlagInt = tp.Union[Flag, int]
FlagRangeTyping = tp.Union[FlagRange, tuple, list]
