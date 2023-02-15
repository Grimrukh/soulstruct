from __future__ import annotations

__all__ = ["HIT_EFFECT_SE_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class HIT_EFFECT_SE_PARAM_ST(ParamRow):
    IronSlashS: int = ParamField(
        int, "Iron_Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IronSlashL: int = ParamField(
        int, "Iron_Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IronSlashLL: int = ParamField(
        int, "Iron_Slash_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IronThrustS: int = ParamField(
        int, "Iron_Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IronThrustL: int = ParamField(
        int, "Iron_Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IronThrustLL: int = ParamField(
        int, "Iron_Thrust_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IronBlowS: int = ParamField(
        int, "Iron_Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IronBlowL: int = ParamField(
        int, "Iron_Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IronBlowLL: int = ParamField(
        int, "Iron_Blow_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireSlashS: int = ParamField(
        int, "Fire_Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireSlashL: int = ParamField(
        int, "Fire_Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireSlashLL: int = ParamField(
        int, "Fire_Slash_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireThrustS: int = ParamField(
        int, "Fire_Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireThrustL: int = ParamField(
        int, "Fire_Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireThrustLL: int = ParamField(
        int, "Fire_Thrust_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireBlowS: int = ParamField(
        int, "Fire_Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireBlowL: int = ParamField(
        int, "Fire_Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireBlowLL: int = ParamField(
        int, "Fire_Blow_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WoodSlashS: int = ParamField(
        int, "Wood_Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WoodSlashL: int = ParamField(
        int, "Wood_Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WoodSlashLL: int = ParamField(
        int, "Wood_Slash_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WoodThrustS: int = ParamField(
        int, "Wood_Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WoodThrustL: int = ParamField(
        int, "Wood_Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WoodThrustLL: int = ParamField(
        int, "Wood_Thrust_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WoodBlowS: int = ParamField(
        int, "Wood_Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WoodBlowL: int = ParamField(
        int, "Wood_Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WoodBlowLL: int = ParamField(
        int, "Wood_Blow_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BodySlashS: int = ParamField(
        int, "Body_Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BodySlashL: int = ParamField(
        int, "Body_Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BodySlashLL: int = ParamField(
        int, "Body_Slash_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BodyThrustS: int = ParamField(
        int, "Body_Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BodyThrustL: int = ParamField(
        int, "Body_Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BodyThrustLL: int = ParamField(
        int, "Body_Thrust_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BodyBlowS: int = ParamField(
        int, "Body_Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BodyBlowL: int = ParamField(
        int, "Body_Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BodyBlowLL: int = ParamField(
        int, "Body_Blow_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseSlashS: int = ParamField(
        int, "Eclipse_Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseSlashL: int = ParamField(
        int, "Eclipse_Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseSlashLL: int = ParamField(
        int, "Eclipse_Slash_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseThrustS: int = ParamField(
        int, "Eclipse_Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseThrustL: int = ParamField(
        int, "Eclipse_Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseThrustLL: int = ParamField(
        int, "Eclipse_Thrust_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseBlowS: int = ParamField(
        int, "Eclipse_Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseBlowL: int = ParamField(
        int, "Eclipse_Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseBlowLL: int = ParamField(
        int, "Eclipse_Blow_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergySlashS: int = ParamField(
        int, "Energy_Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergySlashL: int = ParamField(
        int, "Energy_Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergySlashLL: int = ParamField(
        int, "Energy_Slash_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergyThrustS: int = ParamField(
        int, "Energy_Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergyThrustL: int = ParamField(
        int, "Energy_Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergyThrustLL: int = ParamField(
        int, "Energy_Thrust_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergyBlowS: int = ParamField(
        int, "Energy_Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergyBlowL: int = ParamField(
        int, "Energy_Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergyBlowLL: int = ParamField(
        int, "Energy_Blow_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoneSlashS: int = ParamField(
        int, "None_Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoneSlashL: int = ParamField(
        int, "None_Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoneSlashLL: int = ParamField(
        int, "None_Slash_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoneThrustS: int = ParamField(
        int, "None_Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoneThrustL: int = ParamField(
        int, "None_Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoneThrustLL: int = ParamField(
        int, "None_Thrust_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoneBlowS: int = ParamField(
        int, "None_Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoneBlowL: int = ParamField(
        int, "None_Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoneBlowLL: int = ParamField(
        int, "None_Blow_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy1SlashS: int = ParamField(
        int, "Dmy1_Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy1SlashL: int = ParamField(
        int, "Dmy1_Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy1SlashLL: int = ParamField(
        int, "Dmy1_Slash_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy1ThrustS: int = ParamField(
        int, "Dmy1_Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy1ThrustL: int = ParamField(
        int, "Dmy1_Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy1ThrustLL: int = ParamField(
        int, "Dmy1_Thrust_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy1BlowS: int = ParamField(
        int, "Dmy1_Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy1BlowL: int = ParamField(
        int, "Dmy1_Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy1BlowLL: int = ParamField(
        int, "Dmy1_Blow_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy2SlashS: int = ParamField(
        int, "Dmy2_Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy2SlashL: int = ParamField(
        int, "Dmy2_Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy2SlashLL: int = ParamField(
        int, "Dmy2_Slash_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy2ThrustS: int = ParamField(
        int, "Dmy2_Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy2ThrustL: int = ParamField(
        int, "Dmy2_Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy2ThrustLL: int = ParamField(
        int, "Dmy2_Thrust_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy2BlowS: int = ParamField(
        int, "Dmy2_Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy2BlowL: int = ParamField(
        int, "Dmy2_Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy2BlowLL: int = ParamField(
        int, "Dmy2_Blow_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy3SlashS: int = ParamField(
        int, "Dmy3_Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy3SlashL: int = ParamField(
        int, "Dmy3_Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy3SlashLL: int = ParamField(
        int, "Dmy3_Slash_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy3ThrustS: int = ParamField(
        int, "Dmy3_Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy3ThrustL: int = ParamField(
        int, "Dmy3_Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy3ThrustLL: int = ParamField(
        int, "Dmy3_Thrust_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy3BlowS: int = ParamField(
        int, "Dmy3_Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy3BlowL: int = ParamField(
        int, "Dmy3_Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Dmy3BlowLL: int = ParamField(
        int, "Dmy3_Blow_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaggotSlashS: int = ParamField(
        int, "Maggot_Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaggotSlashL: int = ParamField(
        int, "Maggot_Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaggotSlashLL: int = ParamField(
        int, "Maggot_Slash_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaggotThrustS: int = ParamField(
        int, "Maggot_Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaggotThrustL: int = ParamField(
        int, "Maggot_Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaggotThrustLL: int = ParamField(
        int, "Maggot_Thrust_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaggotBlowS: int = ParamField(
        int, "Maggot_Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaggotBlowL: int = ParamField(
        int, "Maggot_Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MaggotBlowLL: int = ParamField(
        int, "Maggot_Blow_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WaxSlashS: int = ParamField(
        int, "Wax_Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WaxSlashL: int = ParamField(
        int, "Wax_Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WaxSlashLL: int = ParamField(
        int, "Wax_Slash_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WaxThrustS: int = ParamField(
        int, "Wax_Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WaxThrustL: int = ParamField(
        int, "Wax_Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WaxThrustLL: int = ParamField(
        int, "Wax_Thrust_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WaxBlowS: int = ParamField(
        int, "Wax_Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WaxBlowL: int = ParamField(
        int, "Wax_Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WaxBlowLL: int = ParamField(
        int, "Wax_Blow_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireFlameSlashS: int = ParamField(
        int, "FireFlame_Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireFlameSlashL: int = ParamField(
        int, "FireFlame_Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireFlameSlashLL: int = ParamField(
        int, "FireFlame_Slash_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireFlameThrustS: int = ParamField(
        int, "FireFlame_Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireFlameThrustL: int = ParamField(
        int, "FireFlame_Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireFlameThrustLL: int = ParamField(
        int, "FireFlame_Thrust_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireFlameBlowS: int = ParamField(
        int, "FireFlame_Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireFlameBlowL: int = ParamField(
        int, "FireFlame_Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireFlameBlowLL: int = ParamField(
        int, "FireFlame_Blow_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseGasSlashS: int = ParamField(
        int, "EclipseGas_Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseGasSlashL: int = ParamField(
        int, "EclipseGas_Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseGasSlashLL: int = ParamField(
        int, "EclipseGas_Slash_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseGasThrustS: int = ParamField(
        int, "EclipseGas_Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseGasThrustL: int = ParamField(
        int, "EclipseGas_Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseGasThrustLL: int = ParamField(
        int, "EclipseGas_Thrust_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseGasBlowS: int = ParamField(
        int, "EclipseGas_Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseGasBlowL: int = ParamField(
        int, "EclipseGas_Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EclipseGasBlowLL: int = ParamField(
        int, "EclipseGas_Blow_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergyStrongSlashS: int = ParamField(
        int, "EnergyStrong_Slash_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergyStrongSlashL: int = ParamField(
        int, "EnergyStrong_Slash_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergyStrongSlashLL: int = ParamField(
        int, "EnergyStrong_Slash_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergyStrongThrustS: int = ParamField(
        int, "EnergyStrong_Thrust_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergyStrongThrustL: int = ParamField(
        int, "EnergyStrong_Thrust_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergyStrongThrustLL: int = ParamField(
        int, "EnergyStrong_Thrust_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergyStrongBlowS: int = ParamField(
        int, "EnergyStrong_Blow_S", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergyStrongBlowL: int = ParamField(
        int, "EnergyStrong_Blow_L", default=0,
        tooltip="TOOLTIP-TODO",
    )
    EnergyStrongBlowLL: int = ParamField(
        int, "EnergyStrong_Blow_LL", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(100, "reserve[100]")
