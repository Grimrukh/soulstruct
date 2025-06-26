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
    "NavmeshFlag",
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


class NavmeshFlag(BaseEMEVDEnum):
    """Bit flags for Navmesh types. Shared by all games that use the NVM format (Demon's Souls to Bloodborne).

    NOTE: These EMEVD argument values are in reverse-bit-endian order to the actual NVM triangle flag. The NVM format
    stores the flags in this format and writes them back in reverse order, so the user never needs to worry about this.
    """
    Default = 0b0000_0000_0000_0000  # no special flags
    Disable = 0b0000_0000_0000_0001  # ignored completely during pathfinding
    Exit = 0b0000_0000_0000_0010  # location of an MCG gate node to connect to another navmesh in the same map
    Obstacle = 0b0000_0000_0000_0100  # will trigger enemies' 'destroy obstacle' animation; can stack with other flags
    Wall = 0b0000_0000_0000_1000  # wall that a character may drop off from a non-`FloorBeneathWall` face
    Degenerate = 0b0000_0000_0001_0000  # seen on triangles with co-linear vertices and potentially others
    FloorBeneathWall = 0b0000_0000_0010_0000  # adjacent `Wall` faces cannot be traversed from this side
    LandingPoint = 0b0000_0000_0100_0000
    Event = 0b0000_0000_1000_0000
    Edge = 0b0000_0001_0000_0000
    LargeSpace = 0b0000_0010_0000_0000
    Ladder = 0b0000_0100_0000_0000  # used at the bottom and top of ladders (but not on the vertical section itself)
    Hole = 0b0000_1000_0000_0000
    Door = 0b0001_0000_0000_0000
    ClosedDoor = 0b0010_0000_0000_0000
    BlockExit = 0b0100_0000_0000_0000  # used to generate dynamic gate nodes to connect to other map blocks
    InsideWall = 0b1000_0000_0000_0000  # unknown use


# Basic obvious booleans are omitted:
# ENUM_ON_OFF, ENUM_CONTAINED, ENUM_OWN_STATE, ENUM_BOOL, ENUM_CONDITION_STATE, ENUM_DEATH_STATUS, ENUM_ENABLE_STATE
