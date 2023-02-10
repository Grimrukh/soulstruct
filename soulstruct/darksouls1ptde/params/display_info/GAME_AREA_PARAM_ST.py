from __future__ import annotations

__all__ = ["GAME_AREA_PARAM_ST"]

from soulstruct.base.params.utils import ParamFieldInfo
from soulstruct.darksouls1ptde.game_types import *

GAME_AREA_PARAM_ST = {
    "param_type": "GAME_AREA_PARAM_ST",
    "file_name": "GameAreaParam",
    "nickname": "Bosses",
    "fields": [
        ParamFieldInfo(
            "bonusSoul_single",
            "SingleplayerSoulReward",
            True,
            int,
            "Souls awarded (after delay) when boss is defeated with no summons.",
        ),
        ParamFieldInfo(
            "bonusSoul_multi",
            "MultiplayerSoulReward",
            True,
            int,
            "Souls awarded to each player (after delay) when boss is defeated with summons.",
        ),
        ParamFieldInfo(
            "humanityPointCountFlagIdTop",
            "FirstHumanityFlag",
            True,
            Flag,
            "First flag for recording number of humanity drops awarded in boss's area.",
        ),
        ParamFieldInfo(
            "humanityDropPoint1",
            "HumanityDropPoint1",
            True,
            int,
            "Number of 'points' needed from killing enemies in the boss area for first Humanity.",
        ),
        ParamFieldInfo(
            "humanityDropPoint2",
            "HumanityDropPoint2",
            True,
            int,
            "Number of 'points' needed from killing enemies in the boss area for second Humanity.",
        ),
        ParamFieldInfo(
            "humanityDropPoint3",
            "HumanityDropPoint3",
            True,
            int,
            "Number of 'points' needed from killing enemies in the boss area for third Humanity.",
        ),
        ParamFieldInfo(
            "humanityDropPoint4",
            "HumanityDropPoint4",
            True,
            int,
            "Number of 'points' needed from killing enemies in the boss area for fourth Humanity.",
        ),
        ParamFieldInfo(
            "humanityDropPoint5",
            "HumanityDropPoint5",
            True,
            int,
            "Number of 'points' needed from killing enemies in the boss area for fifth Humanity.",
        ),
        ParamFieldInfo(
            "humanityDropPoint6",
            "HumanityDropPoint6",
            True,
            int,
            "Number of 'points' needed from killing enemies in the boss area for sixth Humanity.",
        ),
        ParamFieldInfo(
            "humanityDropPoint7",
            "HumanityDropPoint7",
            True,
            int,
            "Number of 'points' needed from killing enemies in the boss area for seventh Humanity.",
        ),
        ParamFieldInfo(
            "humanityDropPoint8",
            "HumanityDropPoint8",
            True,
            int,
            "Number of 'points' needed from killing enemies in the boss area for eighth Humanity.",
        ),
        ParamFieldInfo(
            "humanityDropPoint9",
            "HumanityDropPoint9",
            True,
            int,
            "Number of 'points' needed from killing enemies in the boss area for ninth Humanity.",
        ),
        ParamFieldInfo(
            "humanityDropPoint10",
            "HumanityDropPoint10",
            True,
            int,
            "Number of 'points' needed from killing enemies in the boss area for final Humanity.",
        ),
    ],
}
