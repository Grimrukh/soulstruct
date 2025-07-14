from __future__ import annotations

__all__ = ["GAME_AREA_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.bloodborne.game_types import *
from soulstruct.utilities.binary import *


class GAME_AREA_PARAM_ST(ParamRow):
    SingleplayerSoulReward: int = ParamField(
        uint32, "bonusSoul_single", default=0,
        tooltip="Souls awarded (after delay) when boss is defeated with no summons.",
    )
    MultiplayerSoulReward: int = ParamField(
        uint32, "bonusSoul_multi", default=0,
        tooltip="Souls awarded to each player (after delay) when boss is defeated with summons.",
    )
    FirstHumanityFlag: int = ParamField(
        int32, "humanityPointCountFlagIdTop", game_type=Flag, default=-1,
        tooltip="First flag for recording number of humanity drops awarded in boss's area.",
    )
    HumanityDropPoint1: int = ParamField(
        uint16, "humanityDropPoint1", default=-1,
        tooltip="Number of 'points' needed from killing enemies in the boss area for first Humanity.",
    )
    HumanityDropPoint2: int = ParamField(
        uint16, "humanityDropPoint2", default=-1,
        tooltip="Number of 'points' needed from killing enemies in the boss area for second Humanity.",
    )
    HumanityDropPoint3: int = ParamField(
        uint16, "humanityDropPoint3", default=-1,
        tooltip="Number of 'points' needed from killing enemies in the boss area for third Humanity.",
    )
    HumanityDropPoint4: int = ParamField(
        uint16, "humanityDropPoint4", default=-1,
        tooltip="Number of 'points' needed from killing enemies in the boss area for fourth Humanity.",
    )
    HumanityDropPoint5: int = ParamField(
        uint16, "humanityDropPoint5", default=-1,
        tooltip="Number of 'points' needed from killing enemies in the boss area for fifth Humanity.",
    )
    HumanityDropPoint6: int = ParamField(
        uint16, "humanityDropPoint6", default=-1,
        tooltip="Number of 'points' needed from killing enemies in the boss area for sixth Humanity.",
    )
    HumanityDropPoint7: int = ParamField(
        uint16, "humanityDropPoint7", default=-1,
        tooltip="Number of 'points' needed from killing enemies in the boss area for seventh Humanity.",
    )
    HumanityDropPoint8: int = ParamField(
        uint16, "humanityDropPoint8", default=-1,
        tooltip="Number of 'points' needed from killing enemies in the boss area for eighth Humanity.",
    )
    HumanityDropPoint9: int = ParamField(
        uint16, "humanityDropPoint9", default=-1,
        tooltip="Number of 'points' needed from killing enemies in the boss area for ninth Humanity.",
    )
    HumanityDropPoint10: int = ParamField(
        uint16, "humanityDropPoint10", default=-1,
        tooltip="Number of 'points' needed from killing enemies in the boss area for final Humanity.",
    )
