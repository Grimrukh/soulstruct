__all__ = [
    # Basic
    "RestartType",
    "uint",
    "short",
    "ushort",
    "char",
    "uchar",
    "PLAYER",
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


# Basic obvious booleans are omitted:
# ENUM_ON_OFF, ENUM_CONTAINED, ENUM_OWN_STATE, ENUM_BOOL, ENUM_CONDITION_STATE, ENUM_DEATH_STATUS, ENUM_ENABLE_STATE
