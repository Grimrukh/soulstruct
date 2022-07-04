__all__ = [
    # Basic
    "RestartType",
    "uint",
    "short",
    "ushort",
    "char",
    "uchar",
    "PLAYER",
    "BaseEMEVDEnum",
    "BaseEMEVDFlags",
]

from enum import IntEnum


class RestartType(IntEnum):
    NeverRestart = 0
    RestartOnRest = 1
    UnknownRestart = 2


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
        # All EMEVD enums that I'm aware of are `uchar`.
        return "B"


class BaseEMEVDFlags(BaseEMEVDEnum):
    """Base class for EMEVD enums that represent bit flags."""


# Basic obvious booleans are omitted:
# ENUM_ON_OFF, ENUM_CONTAINED, ENUM_OWN_STATE, ENUM_BOOL, ENUM_CONDITION_STATE, ENUM_DEATH_STATUS, ENUM_ENABLE_STATE
