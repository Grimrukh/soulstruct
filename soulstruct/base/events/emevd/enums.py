from __future__ import annotations

__all__ = [
    # Basic
    "OnRestBehavior",
    "uint",
    "short",
    "ushort",
    "char",
    "uchar",
    "PLAYER",
    "BaseEMEVDEnum",
    "BaseNegatableEMEVDEnum",
    "BaseEMEVDFlags",
]

from enum import IntEnum


class OnRestBehavior(IntEnum):
    """Defines what happens to the event script when you rest at a checkpoint."""
    ContinueOnRest = 0
    RestartOnRest = 1
    EndOnRest = 2


uint = "I"
short = "h"
ushort = "H"
char = "b"
uchar = "B"

PLAYER = 10000


class BaseEMEVDEnum(IntEnum):
    """Base class for all EMEVD enums."""
    @classmethod
    def get_event_arg_fmt(cls):
        """All EMEVD enums that I'm aware of are `uchar`."""
        return "B"


class BaseNegatableEMEVDEnum(BaseEMEVDEnum):
    """EMEVD enum that supports `negate` for one or more members."""

    def negate(self):
        """Implemented by enums who support negation for one or more members."""
        raise ValueError(f"Cannot invert `{self.__class__.__name__}` value: {self}")


class BaseEMEVDFlags(BaseEMEVDEnum):
    """Base class for EMEVD enums that represent bit flags."""


# Basic obvious booleans are omitted:
# ENUM_ON_OFF, ENUM_CONTAINED, ENUM_OWN_STATE, ENUM_BOOL, ENUM_CONDITION_STATE, ENUM_DEATH_STATUS, ENUM_ENABLE_STATE
