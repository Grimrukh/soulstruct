from __future__ import annotations

__all__ = [
    "GameObject",
    "GAME_TYPE",
    "GameObjectIntMeta",
    "GameObjectInt",
    "GAME_INT_TYPE",
    "GameObjectIntSequence",
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
from enum import IntEnum, EnumMeta


class GameObject:
    """Base class for ANY object that appears in a game file and is referenced or called by other game file/code.

    Note that there are used for typing, and not for actual Python deserialization. For example, every entry type that
    appears in an MSB map file has a data class like `MSBCharacter` that points to a game type here like `MapCharacter`.

    Almost all game objects inherit from `GameObjectInt` below as they have integer IDs, but a few do not, e.g.:
        `Map`, `MapEntry`, `FlagRange`.
    """

    @classmethod
    def get_event_arg_fmt(cls) -> str:
        """If not `None`, allows this type to be used as an EVS event arg type hint for this format."""
        raise TypeError(f"Game type `{cls.__name__}` cannot be used as an EVS event argument type hint.")


# For type-hinting.
GAME_TYPE = tp.Type[GameObject]


class GameObjectIntMeta(EnumMeta):
    """Allows easy specification of `auto()` behavior for `IntEnum`-mixed subclasses."""

    @classmethod
    def __prepare__(
        metacls,
        cls,
        bases,
        first_value: int = None,
        last_value: int = None,
        max_count: int = None,
        **kwds,  # NOTE: None are actually acceptable.
    ):
        if kwds:
            raise TypeError(f"Unexpected keyword arguments for `GameObjectIntMeta`: {kwds}")

        enum_dict = super().__prepare__(cls, bases, **kwds)

        # We also need an `__init_subclass__` method that ignores `first_value` and `max_count` arguments.
        # noinspection PyUnusedLocal
        def __init_subclass__(cls_, **kwargs):
            super().__init_subclass__()

        enum_dict["__init_subclass__"] = __init_subclass__

        if first_value is None and max_count is None and last_value is None:
            # Standard behavior. May inherit `_generate_next_value_` from closest enum parent class, as usual.
            return enum_dict

        if first_value is None:
            first_value = 0

        if last_value is not None and max_count is not None:
            raise ValueError("Cannot specify both `last_value` and `max_count` for `GameObjectInt` subclass.")
        elif last_value is not None:
            max_count = last_value - first_value

        # noinspection PyUnusedLocal
        def _generate_next_value_(name, start, count, last_values):
            if max_count is not None and count >= max_count:
                raise ValueError(f"Max count {max_count} exceeded for `auto()` values in `{cls.__name__}`.")
            return first_value + count

        enum_dict["_generate_next_value_"] = _generate_next_value_
        return enum_dict


class GameObjectInt(GameObject, IntEnum, metaclass=GameObjectIntMeta):
    """Base class for all game objects that correspond to integer (`IntEnume`) IDs.

    Uses a metaclass that allows easy specification of `enum.auto()` value behavior with class arguments, e.g.:
        ```
        class SomeGameObject(GameObjectInt, first_value=1000, max_count=100):
            Object0 = enum.auto()  # 1000
            Object1 = enum.auto()  # 1001
            ...
            Object99 = enum.auto()  # 1099
            Object100 = enum.auto()  # ERROR!
        ```

    NOTE: This is an ABC in practice, but I can't actually (easily) mix `abc.ABC` with `IntEnum`.
    """


# For type-hinting.
GAME_INT_TYPE = tp.Type[GameObjectInt]


class GameObjectIntSequence(type):
    """Metaclass that generates types that represent sequences of `GameObjectInt`s.

    `GameObjectIntSequence` takes one sequence of two: a `GameObjectInt` subclass, and an integer indicating the length
    of the sequence. For example:

        `GameObjectIntSequence((Region, 8))`
    """
    game_object_type: GAME_INT_TYPE
    count: int

    def __new__(mcs, game_object_and_count):
        if not game_object_and_count or len(game_object_and_count) != 2:
            raise TypeError("`GameObjectIntSequence` argument must be `(game_object_type, count)`.")
        if not issubclass(game_object_and_count[0], GameObjectInt):
            raise TypeError(
                f"`GameObjectIntSequence` takes one sequence of `GameObjectInt` subclasses, with the last element "
                f"optionally being an integer. Invalid sequence element: {type(game_object_and_count[0])}."
            )
        cls = super().__new__(mcs, "GameObjectIntSequence", (GameObjectIntSequence,), {})
        cls.game_object_type, cls.count = game_object_and_count
        return cls


class BaseParam(GameObjectInt):
    """Base class for IDs of param entries."""

    @classmethod
    def get_param_nickname(cls):
        raise NotImplementedError


class BaseGameParam(BaseParam):
    """Base class for IDs of GameParam entries."""

    @classmethod
    def get_param_nickname(cls):
        raise NotImplementedError


class Flag(GameObjectInt):
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


class ModelDummy(GameObjectInt):
    """`Dummy`, `dmy`, `damipoly`, etc. of a FLVER model."""


class Texture(GameObjectInt):
    """2D texture ID of something."""


class Icon(GameObjectInt):
    """Icon in some type-specific spritesheet."""


class EquipmentModel(GameObjectInt):
    """FLVER model for c0000 appearance in the game `parts` folder."""


class VisualEffect(GameObjectInt):
    """VFX ID of something."""


class TalkScript(GameObjectInt):
    """Talk ID of a Map Character."""


class Cutscene(GameObjectInt):
    """ID of a cutscene (`remo/scn...` file)."""


class Text(GameObjectInt):
    """Text ID for an entry in some FMG."""

    @classmethod
    def get_text_category(cls):
        raise NotImplementedError


class Animation(GameObjectInt):
    """Animation ID base class."""


class PlayerAnimation(Animation):
    """Animation IDs for player character and human NPCs."""


class BaseAIScript(GameObjectInt):
    """Base type for Logic and Battle scripts."""


class LogicAIScript(BaseAIScript):
    """Script that governs a character outside of battle."""


class BattleAIScript(BaseAIScript):
    """Script that governs a character in battle."""


FlagTyping = tp.Union[Flag, int]
FlagRangeTyping = tp.Union[FlagRange, tuple, list]
