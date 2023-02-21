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
    "CLIENT_PLAYER_1",
    "CLIENT_PLAYER_2",
    "CLIENT_PLAYER_3",
    "CLIENT_PLAYER_4",
    "CLIENT_PLAYER_5",
    "CLIENT_PLAYER_6",
    "CLIENT_PLAYER_7",
    "CLIENT_PLAYER_8",
    "CLIENT_PLAYER_9",
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

# NOTE: Not sure exactly how many clients are supported, but being safe.
# MSB entries should not use any five-digit entity IDs anyway.
PLAYER = 10000
CLIENT_PLAYER_1 = 10001
CLIENT_PLAYER_2 = 10002
CLIENT_PLAYER_3 = 10003
CLIENT_PLAYER_4 = 10004
CLIENT_PLAYER_5 = 10005
CLIENT_PLAYER_6 = 10006
CLIENT_PLAYER_7 = 10007
CLIENT_PLAYER_8 = 10008
CLIENT_PLAYER_9 = 10009


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
