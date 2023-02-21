from __future__ import annotations

__all__ = [
    "GameObject",
    "GAME_TYPE",
    "GameObjectSequence",
    "BaseParam",
    "BaseGameParam",
    "Flag",
    "FlagTyping",
    "MapFlagSuffix",
    "FlagRange",
    "FlagRangeTyping",
    "ModelDummy",
    "Texture",
    "Icon",
    "EquipmentModel",
    "VisualEffect",
    "TalkScript",
    "Cutscene",
    "Text",
    "Animation",
    "PlayerAnimation",
    "BaseAIScript",
    "LogicAIScript",
    "BattleAIScript",
]

import typing as tp
from enum import IntEnum


class GameObject:
    """Base class for all game types.

    Note that using `abc.ABC` for this, or any of its technically abstract intermediate subclasses, leads to problems.

    Also note that while most subclasses also inherit from `IntEnum`, not all of them do (e.g. `Map`), so this does not.
    """

    @classmethod
    def get_event_arg_fmt(cls) -> str:
        """If not `None`, allows this type to be used as an EVS event arg type hint for this format."""
        raise TypeError(f"Game type `{cls.__name__}` cannot be used as an EVS event argument type hint.")


# For type-hinting.
GAME_TYPE = tp.Type[GameObject]


class GameObjectSequence(type):
    """Metaclass that generates types that represent sequences of `GameObject`s.

    `GameObjectSequence` takes one sequence of two: a `GameObject` subclass, and an integer indicating the length of the
    sequence. For example:

        `GameObjectSequence((Region, 8))`
    """
    game_object_type: GAME_TYPE
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


class BaseParam(GameObject, IntEnum):
    """Base class for IDs of param entries."""

    @classmethod
    def get_param_nickname(cls):
        raise NotImplementedError


class BaseGameParam(BaseParam):
    """Base class for IDs of GameParam entries."""

    @classmethod
    def get_param_nickname(cls):
        raise NotImplementedError


class Flag(GameObject, IntEnum):
    """Event flag."""

    @classmethod
    def get_event_arg_fmt(cls):
        return "i"


class MapFlagSuffix(IntEnum):
    """Flag up to four digits long, intended to be added to a map base flag (such as 11020000 for m10_02).

    `EVSParser` will compute the true flag ID automatically if it knows the map's base flag ID.
    """


class FlagRange(GameObject):

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


class ModelDummy(GameObject, IntEnum):
    """`Dummy`, `dmy`, `damipoly`, etc. of a FLVER model."""


class Texture(GameObject, IntEnum):
    """2D texture ID of something."""


class Icon(GameObject, IntEnum):
    """Icon in some type-specific spritesheet."""


class EquipmentModel(GameObject, IntEnum):
    """FLVER model for c0000 appearance in the game `parts` folder."""


class VisualEffect(GameObject, IntEnum):
    """VFX ID of something."""


class TalkScript(GameObject, IntEnum):
    """Talk ID of a Map Character."""


class Cutscene(GameObject, IntEnum):
    """ID of a cutscene (`remo/scn...` file)."""


class Text(GameObject, IntEnum):
    """Text ID for an entry in some FMG."""

    @classmethod
    def get_text_category(cls):
        raise NotImplementedError


class Animation(GameObject, IntEnum):
    """Animation ID base class."""


class PlayerAnimation(Animation):
    """Animation IDs for player character and human NPCs."""


class BaseAIScript(GameObject, IntEnum):
    """Base type for Logic and Battle scripts."""


class LogicAIScript(BaseAIScript):
    """Script that governs a character outside of battle."""


class BattleAIScript(BaseAIScript):
    """Script that governs a character in battle."""


FlagTyping = tp.Union[Flag, int]
FlagRangeTyping = tp.Union[FlagRange, tuple, list]
