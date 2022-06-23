from __future__ import annotations

__all__ = [
    "BaseGameObject",
    "GameObjectSequence",
    "BaseParam",
    "Texture",
    "VisualEffect",
    "TalkScript",
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


class Texture(BaseGameObject, IntEnum):
    """2D texture ID of something."""


class VisualEffect(BaseGameObject, IntEnum):
    """VFX ID of something."""


class TalkScript(BaseGameObject, IntEnum):
    """Talk ID of a Map Character."""


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
