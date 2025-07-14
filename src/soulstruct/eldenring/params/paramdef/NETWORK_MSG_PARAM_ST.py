from __future__ import annotations

__all__ = ["NETWORK_MSG_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class NETWORK_MSG_PARAM_ST(ParamRow):
    Priority: int = ParamField(
        uint16, "priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ForcePlay: int = ParamField(
        uint8, "forcePlay", BOOL_YESNO_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad1[1]")
    NormalWhite: int = ParamField(
        int32, "normalWhite", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UmbasaWhite: int = ParamField(
        int32, "umbasaWhite", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BerserkerWhite: int = ParamField(
        int32, "berserkerWhite", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SinnerHeroWhite: int = ParamField(
        int32, "sinnerHeroWhite", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NormalBlack: int = ParamField(
        int32, "normalBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UmbasaBlack: int = ParamField(
        int32, "umbasaBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BerserkerBlack: int = ParamField(
        int32, "berserkerBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinBlack: int = ParamField(
        int32, "forceJoinBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinUmbasaBlack: int = ParamField(
        int32, "forceJoinUmbasaBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinBerserkerBlack: int = ParamField(
        int32, "forceJoinBerserkerBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SinnerHunterVisitor: int = ParamField(
        int32, "sinnerHunterVisitor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RedHunterVisitor: int = ParamField(
        int32, "redHunterVisitor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GuardianOfBossVisitor: int = ParamField(
        int32, "guardianOfBossVisitor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GuardianOfForestMapVisitor: int = ParamField(
        int32, "guardianOfForestMapVisitor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GuardianOfAnolisVisitor: int = ParamField(
        int32, "guardianOfAnolisVisitor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RosaliaBlack: int = ParamField(
        int32, "rosaliaBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinRosaliaBlack: int = ParamField(
        int32, "forceJoinRosaliaBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RedHunterVisitor2: int = ParamField(
        int32, "redHunterVisitor2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc1: int = ParamField(
        int32, "npc1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc2: int = ParamField(
        int32, "npc2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc3: int = ParamField(
        int32, "npc3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc4: int = ParamField(
        int32, "npc4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BattleRoyal: int = ParamField(
        int32, "battleRoyal", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc5: int = ParamField(
        int32, "npc5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc6: int = ParamField(
        int32, "npc6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc7: int = ParamField(
        int32, "npc7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc8: int = ParamField(
        int32, "npc8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc9: int = ParamField(
        int32, "npc9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc10: int = ParamField(
        int32, "npc10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc11: int = ParamField(
        int32, "npc11", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc12: int = ParamField(
        int32, "npc12", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc13: int = ParamField(
        int32, "npc13", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc14: int = ParamField(
        int32, "npc14", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc15: int = ParamField(
        int32, "npc15", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc16: int = ParamField(
        int32, "npc16", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinBlackB: int = ParamField(
        int32, "forceJoinBlack_B", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NormalWhiteNpc: int = ParamField(
        int32, "normalWhite_Npc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinBlackNpc: int = ParamField(
        int32, "forceJoinBlack_Npc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinBlackBNpc: int = ParamField(
        int32, "forceJoinBlack_B_Npc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinBlackCNpc: int = ParamField(
        int32, "forceJoinBlack_C_Npc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xa4: int = ParamField(
        int32, "unknown_0xa4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xa8: int = ParamField(
        int32, "unknown_0xa8", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xac: int = ParamField(
        int32, "unknown_0xac", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xb0: int = ParamField(
        int32, "unknown_0xb0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0xb4: int = ParamField(
        int32, "unknown_0xb4", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(8, "pad2_new[8]")
