from __future__ import annotations

__all__ = ["ROLE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ROLE_PARAM_ST(ParamRow):
    TeamType: int = ParamField(
        byte, "teamType", TEAM_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(3, "pad10[3]")
    PhantomParamId: int = ParamField(
        int, "phantomParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID0: int = ParamField(
        int, "spEffectID0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID1: int = ParamField(
        int, "spEffectID1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID2: int = ParamField(
        int, "spEffectID2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID3: int = ParamField(
        int, "spEffectID3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID4: int = ParamField(
        int, "spEffectID4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID5: int = ParamField(
        int, "spEffectID5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID6: int = ParamField(
        int, "spEffectID6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID7: int = ParamField(
        int, "spEffectID7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID8: int = ParamField(
        int, "spEffectID8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectID9: int = ParamField(
        int, "spEffectID9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SosSignSfxId: int = ParamField(
        int, "sosSignSfxId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MySosSignSfxId: int = ParamField(
        int, "mySosSignSfxId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SummonStartAnimId: int = ParamField(
        int, "summonStartAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ItemlotParamId: int = ParamField(
        int, "itemlotParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    VoiceChatGroup: int = ParamField(
        byte, "voiceChatGroup", VOICE_CHAT_GROUP_Type, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RoleNameColor: int = ParamField(
        byte, "roleNameColor", ROLE_NAME_COLOR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(2, "pad1[2]")
    RoleNameId: int = ParamField(
        int, "roleNameId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThreatLv: int = ParamField(
        uint, "threatLv", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhantomParamIdvowRank1: int = ParamField(
        int, "phantomParamId_vowRank1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PhantomParamIdvowRank2: int = ParamField(
        int, "phantomParamId_vowRank2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PhantomParamIdvowRank3: int = ParamField(
        int, "phantomParamId_vowRank3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIDvowRank0: int = ParamField(
        int, "spEffectID_vowRank0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIDvowRank1: int = ParamField(
        int, "spEffectID_vowRank1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIDvowRank2: int = ParamField(
        int, "spEffectID_vowRank2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectIDvowRank3: int = ParamField(
        int, "spEffectID_vowRank3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SignPhantomId: int = ParamField(
        int, "signPhantomId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NonPlayerSummonStartAnimId: int = ParamField(
        int, "nonPlayerSummonStartAnimId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(16, "pad2[16]")
