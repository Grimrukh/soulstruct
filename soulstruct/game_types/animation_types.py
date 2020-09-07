from enum import IntEnum
from typing import Union

__all__ = ["Animation", "PlayerAnimation"]


class Animation(IntEnum):
    """Animation ID base class."""

    # TODO: playback methods.


class PlayerAnimation(Animation):
    """Animation IDs for player character and human NPCs."""

    # TODO: playback methods.


AnimationTyping = Union[Animation, int]
