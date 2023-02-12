from __future__ import annotations

__all__ = ["NETWORK_MSG_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class NETWORK_MSG_PARAM_ST(ParamRow):
    Priority: int = ParamField(
        ushort, "priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ForcePlay: int = ParamField(
        byte, "forcePlay", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad1[1]")
    NormalWhite: int = ParamField(
        int, "normalWhite", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UmbasaWhite: int = ParamField(
        int, "umbasaWhite", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BerserkerWhite: int = ParamField(
        int, "berserkerWhite", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SinnerHeroWhite: int = ParamField(
        int, "sinnerHeroWhite", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NormalBlack: int = ParamField(
        int, "normalBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    UmbasaBlack: int = ParamField(
        int, "umbasaBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BerserkerBlack: int = ParamField(
        int, "berserkerBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinBlack: int = ParamField(
        int, "forceJoinBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinUmbasaBlack: int = ParamField(
        int, "forceJoinUmbasaBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinBerserkerBlack: int = ParamField(
        int, "forceJoinBerserkerBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SinnerHunterVisitor: int = ParamField(
        int, "sinnerHunterVisitor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RedHunterVisitor: int = ParamField(
        int, "redHunterVisitor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GuardianOfBossVisitor: int = ParamField(
        int, "guardianOfBossVisitor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GuardianOfForestMapVisitor: int = ParamField(
        int, "guardianOfForestMapVisitor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    GuardianOfAnolisVisitor: int = ParamField(
        int, "guardianOfAnolisVisitor", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RosaliaBlack: int = ParamField(
        int, "rosaliaBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinRosaliaBlack: int = ParamField(
        int, "forceJoinRosaliaBlack", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RedHunterVisitor2: int = ParamField(
        int, "redHunterVisitor2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc1: int = ParamField(
        int, "npc1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc2: int = ParamField(
        int, "npc2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc3: int = ParamField(
        int, "npc3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc4: int = ParamField(
        int, "npc4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BattleRoyal: int = ParamField(
        int, "battleRoyal", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc5: int = ParamField(
        int, "npc5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc6: int = ParamField(
        int, "npc6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc7: int = ParamField(
        int, "npc7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc8: int = ParamField(
        int, "npc8", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc9: int = ParamField(
        int, "npc9", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc10: int = ParamField(
        int, "npc10", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc11: int = ParamField(
        int, "npc11", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc12: int = ParamField(
        int, "npc12", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc13: int = ParamField(
        int, "npc13", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc14: int = ParamField(
        int, "npc14", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc15: int = ParamField(
        int, "npc15", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Npc16: int = ParamField(
        int, "npc16", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinBlackB: int = ParamField(
        int, "forceJoinBlack_B", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NormalWhiteNpc: int = ParamField(
        int, "normalWhite_Npc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinBlackNpc: int = ParamField(
        int, "forceJoinBlack_Npc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinBlackBNpc: int = ParamField(
        int, "forceJoinBlack_B_Npc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ForceJoinBlackCNpc: int = ParamField(
        int, "forceJoinBlack_C_Npc", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(28, "pad2[28]")
