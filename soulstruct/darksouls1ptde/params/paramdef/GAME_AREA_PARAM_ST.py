from __future__ import annotations

__all__ = ["GAME_AREA_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.darksouls1ptde.game_types import *
from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class GAME_AREA_PARAM_ST(ParamRow):
    SingleplayerSoulReward: int = ParamField(
        uint, "bonusSoul_single", default=0,
        tooltip="Souls awarded (after delay) when boss is defeated with no summons.",
    )
    MultiplayerSoulReward: int = ParamField(
        uint, "bonusSoul_multi", default=0,
        tooltip="Souls awarded to each player (after delay) when boss is defeated with summons.",
    )
    FirstHumanityFlag: int = ParamField(
        int, "humanityPointCountFlagIdTop", game_type=Flag, default=-1,
        tooltip="First flag for recording number of humanity drops awarded in boss's area.",
    )
    HumanityDropPoint1: int = ParamField(
        ushort, "humanityDropPoint1", default=65535,
        tooltip="Number of 'points' needed from killing enemies in the boss area for first Humanity.",
    )
    HumanityDropPoint2: int = ParamField(
        ushort, "humanityDropPoint2", default=65535,
        tooltip="Number of 'points' needed from killing enemies in the boss area for second Humanity.",
    )
    HumanityDropPoint3: int = ParamField(
        ushort, "humanityDropPoint3", default=65535,
        tooltip="Number of 'points' needed from killing enemies in the boss area for third Humanity.",
    )
    HumanityDropPoint4: int = ParamField(
        ushort, "humanityDropPoint4", default=65535,
        tooltip="Number of 'points' needed from killing enemies in the boss area for fourth Humanity.",
    )
    HumanityDropPoint5: int = ParamField(
        ushort, "humanityDropPoint5", default=65535,
        tooltip="Number of 'points' needed from killing enemies in the boss area for fifth Humanity.",
    )
    HumanityDropPoint6: int = ParamField(
        ushort, "humanityDropPoint6", default=65535,
        tooltip="Number of 'points' needed from killing enemies in the boss area for sixth Humanity.",
    )
    HumanityDropPoint7: int = ParamField(
        ushort, "humanityDropPoint7", default=65535,
        tooltip="Number of 'points' needed from killing enemies in the boss area for seventh Humanity.",
    )
    HumanityDropPoint8: int = ParamField(
        ushort, "humanityDropPoint8", default=65535,
        tooltip="Number of 'points' needed from killing enemies in the boss area for eighth Humanity.",
    )
    HumanityDropPoint9: int = ParamField(
        ushort, "humanityDropPoint9", default=65535,
        tooltip="Number of 'points' needed from killing enemies in the boss area for ninth Humanity.",
    )
    HumanityDropPoint10: int = ParamField(
        ushort, "humanityDropPoint10", default=65535,
        tooltip="Number of 'points' needed from killing enemies in the boss area for final Humanity.",
    )
