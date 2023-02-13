from __future__ import annotations

__all__ = ["ATK_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ATK_PARAM_ST(ParamRow):
    Hit0Radius: float = ParamField(
        float, "hit0_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit1Radius: float = ParamField(
        float, "hit1_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit2Radius: float = ParamField(
        float, "hit2_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit3Radius: float = ParamField(
        float, "hit3_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    KnockbackDist: float = ParamField(
        float, "knockbackDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HitStopTime: float = ParamField(
        float, "hitStopTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId0: int = ParamField(
        int, "spEffectId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId1: int = ParamField(
        int, "spEffectId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId2: int = ParamField(
        int, "spEffectId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId3: int = ParamField(
        int, "spEffectId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectId4: int = ParamField(
        int, "spEffectId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Hit0DmyPoly1: int = ParamField(
        short, "hit0_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit1DmyPoly1: int = ParamField(
        short, "hit1_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit2DmyPoly1: int = ParamField(
        short, "hit2_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit3DmyPoly1: int = ParamField(
        short, "hit3_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit0DmyPoly2: int = ParamField(
        short, "hit0_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit1DmyPoly2: int = ParamField(
        short, "hit1_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit2DmyPoly2: int = ParamField(
        short, "hit2_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit3DmyPoly2: int = ParamField(
        short, "hit3_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlowingCorrection: int = ParamField(
        ushort, "blowingCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPhysCorrection: int = ParamField(
        ushort, "atkPhysCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkMagCorrection: int = ParamField(
        ushort, "atkMagCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkFireCorrection: int = ParamField(
        ushort, "atkFireCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkThunCorrection: int = ParamField(
        ushort, "atkThunCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkStamCorrection: int = ParamField(
        ushort, "atkStamCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardAtkRateCorrection: int = ParamField(
        ushort, "guardAtkRateCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardBreakCorrection: int = ParamField(
        ushort, "guardBreakCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkThrowEscapeCorrection: int = ParamField(
        ushort, "atkThrowEscapeCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubCategory1: int = ParamField(
        byte, "subCategory1", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubCategory2: int = ParamField(
        byte, "subCategory2", ATK_SUB_CATEGORY, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPhys: int = ParamField(
        ushort, "atkPhys", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkMag: int = ParamField(
        ushort, "atkMag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkFire: int = ParamField(
        ushort, "atkFire", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkThun: int = ParamField(
        ushort, "atkThun", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkStam: int = ParamField(
        ushort, "atkStam", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardAtkRate: int = ParamField(
        ushort, "guardAtkRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardBreakRate: int = ParamField(
        ushort, "guardBreakRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad6[1]")
    IsEnableCalcDamageForBushesObj: int = ParamField(
        byte, "isEnableCalcDamageForBushesObj", ATK_PARAM_BOOL, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkThrowEscape: int = ParamField(
        ushort, "atkThrowEscape", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkObj: int = ParamField(
        ushort, "atkObj", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardStaminaCutRate: int = ParamField(
        short, "guardStaminaCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardRate: int = ParamField(
        short, "guardRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowTypeId: int = ParamField(
        ushort, "throwTypeId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit0hitType: int = ParamField(
        byte, "hit0_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit1hitType: int = ParamField(
        byte, "hit1_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit2hitType: int = ParamField(
        byte, "hit2_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit3hitType: int = ParamField(
        byte, "hit3_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti0Priority: int = ParamField(
        byte, "hti0_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti1Priority: int = ParamField(
        byte, "hti1_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti2Priority: int = ParamField(
        byte, "hti2_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti3Priority: int = ParamField(
        byte, "hti3_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DmgLevel: int = ParamField(
        byte, "dmgLevel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MapHitType: int = ParamField(
        byte, "mapHitType", ATK_PARAM_MAP_HIT, default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardCutCancelRate: int = ParamField(
        sbyte, "guardCutCancelRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkAttribute: int = ParamField(
        byte, "atkAttribute", ATKPARAM_ATKATTR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    SpAttribute: int = ParamField(
        byte, "spAttribute", ATKPARAM_SPATTR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkType: int = ParamField(
        byte, "atkType", BEHAVIOR_ATK_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkMaterial: int = ParamField(
        byte, "atkMaterial", WEP_MATERIAL_ATK, default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardRangeType: int = ParamField(
        byte, "guardRangeType", ATKPARAM_GUARD_RANGE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSeMaterial1: int = ParamField(
        ushort, "defSeMaterial1", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitSourceType: int = ParamField(
        byte, "hitSourceType", ATK_PARAM_HIT_SOURCE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowFlag: int = ParamField(
        byte, "throwFlag", ATK_PATAM_THROWFLAG_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DisableGuard: bool = ParamField(
        byte, "disableGuard:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableStaminaAttack: bool = ParamField(
        byte, "disableStaminaAttack:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    DisableHitSpEffect: bool = ParamField(
        byte, "disableHitSpEffect:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreNotifyMissSwingForAI: bool = ParamField(
        byte, "IgnoreNotifyMissSwingForAI:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    RepeatHitSfx: bool = ParamField(
        byte, "repeatHitSfx:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsArrowAtk: bool = ParamField(
        byte, "isArrowAtk:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsGhostAtk: bool = ParamField(
        byte, "isGhostAtk:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableNoDamage: bool = ParamField(
        byte, "isDisableNoDamage:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    AtkPowforSfx: int = ParamField(
        sbyte, "atkPow_forSfx", ATKPARAM_SFX_ATK_POW, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkDirforSfx: int = ParamField(
        sbyte, "atkDir_forSfx", ATKPARAM_SFX_ATK_DIR, default=0,
        tooltip="TOOLTIP-TODO",
    )
    OpposeTarget: bool = ParamField(
        byte, "opposeTarget:1", ATK_PARAM_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    FriendlyTarget: bool = ParamField(
        byte, "friendlyTarget:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    SelfTarget: bool = ParamField(
        byte, "selfTarget:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsCheckDoorPenetration: bool = ParamField(
        byte, "isCheckDoorPenetration:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsVsRideAtk: bool = ParamField(
        byte, "isVsRideAtk:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAddBaseAtk: bool = ParamField(
        byte, "isAddBaseAtk:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeThreatLvNotify: bool = ParamField(
        byte, "excludeThreatLvNotify:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "pad1:1", bit_count=1)
    AtkBehaviorId: int = ParamField(
        byte, "atkBehaviorId", ATKPARAM_BEHAVIOR_ID, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPowforSe: int = ParamField(
        sbyte, "atkPow_forSe", ATKPARAM_SE_ATK_POW, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkSuperArmor: float = ParamField(
        float, "atkSuperArmor", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DecalId1: int = ParamField(
        int, "decalId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DecalId2: int = ParamField(
        int, "decalId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AppearAiSoundId: int = ParamField(
        int, "AppearAiSoundId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitAiSoundId: int = ParamField(
        int, "HitAiSoundId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitRumbleId: int = ParamField(
        int, "HitRumbleId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitRumbleIdByNormal: int = ParamField(
        int, "HitRumbleIdByNormal", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitRumbleIdByMiddle: int = ParamField(
        int, "HitRumbleIdByMiddle", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitRumbleIdByRoot: int = ParamField(
        int, "HitRumbleIdByRoot", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId0: int = ParamField(
        int, "traceSfxId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead0: int = ParamField(
        int, "traceDmyIdHead0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail0: int = ParamField(
        int, "traceDmyIdTail0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId1: int = ParamField(
        int, "traceSfxId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead1: int = ParamField(
        int, "traceDmyIdHead1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail1: int = ParamField(
        int, "traceDmyIdTail1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId2: int = ParamField(
        int, "traceSfxId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead2: int = ParamField(
        int, "traceDmyIdHead2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail2: int = ParamField(
        int, "traceDmyIdTail2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId3: int = ParamField(
        int, "traceSfxId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead3: int = ParamField(
        int, "traceDmyIdHead3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail3: int = ParamField(
        int, "traceDmyIdTail3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId4: int = ParamField(
        int, "traceSfxId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead4: int = ParamField(
        int, "traceDmyIdHead4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail4: int = ParamField(
        int, "traceDmyIdTail4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId5: int = ParamField(
        int, "traceSfxId5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead5: int = ParamField(
        int, "traceDmyIdHead5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail5: int = ParamField(
        int, "traceDmyIdTail5", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId6: int = ParamField(
        int, "traceSfxId6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead6: int = ParamField(
        int, "traceDmyIdHead6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail6: int = ParamField(
        int, "traceDmyIdTail6", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceSfxId7: int = ParamField(
        int, "traceSfxId7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdHead7: int = ParamField(
        int, "traceDmyIdHead7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    TraceDmyIdTail7: int = ParamField(
        int, "traceDmyIdTail7", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Hit4Radius: float = ParamField(
        float, "hit4_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit5Radius: float = ParamField(
        float, "hit5_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit6Radius: float = ParamField(
        float, "hit6_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit7Radius: float = ParamField(
        float, "hit7_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit8Radius: float = ParamField(
        float, "hit8_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit9Radius: float = ParamField(
        float, "hit9_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit10Radius: float = ParamField(
        float, "hit10_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit11Radius: float = ParamField(
        float, "hit11_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit12Radius: float = ParamField(
        float, "hit12_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit13Radius: float = ParamField(
        float, "hit13_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit14Radius: float = ParamField(
        float, "hit14_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit15Radius: float = ParamField(
        float, "hit15_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hit4DmyPoly1: int = ParamField(
        short, "hit4_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit5DmyPoly1: int = ParamField(
        short, "hit5_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit6DmyPoly1: int = ParamField(
        short, "hit6_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit7DmyPoly1: int = ParamField(
        short, "hit7_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit8DmyPoly1: int = ParamField(
        short, "hit8_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit9DmyPoly1: int = ParamField(
        short, "hit9_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit10DmyPoly1: int = ParamField(
        short, "hit10_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit11DmyPoly1: int = ParamField(
        short, "hit11_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit12DmyPoly1: int = ParamField(
        short, "hit12_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit13DmyPoly1: int = ParamField(
        short, "hit13_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit14DmyPoly1: int = ParamField(
        short, "hit14_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit15DmyPoly1: int = ParamField(
        short, "hit15_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit4DmyPoly2: int = ParamField(
        short, "hit4_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit5DmyPoly2: int = ParamField(
        short, "hit5_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit6DmyPoly2: int = ParamField(
        short, "hit6_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit7DmyPoly2: int = ParamField(
        short, "hit7_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit8DmyPoly2: int = ParamField(
        short, "hit8_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit9DmyPoly2: int = ParamField(
        short, "hit9_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit10DmyPoly2: int = ParamField(
        short, "hit10_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit11DmyPoly2: int = ParamField(
        short, "hit11_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit12DmyPoly2: int = ParamField(
        short, "hit12_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit13DmyPoly2: int = ParamField(
        short, "hit13_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit14DmyPoly2: int = ParamField(
        short, "hit14_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit15DmyPoly2: int = ParamField(
        short, "hit15_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit4hitType: int = ParamField(
        byte, "hit4_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit5hitType: int = ParamField(
        byte, "hit5_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit6hitType: int = ParamField(
        byte, "hit6_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit7hitType: int = ParamField(
        byte, "hit7_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit8hitType: int = ParamField(
        byte, "hit8_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit9hitType: int = ParamField(
        byte, "hit9_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit10hitType: int = ParamField(
        byte, "hit10_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit11hitType: int = ParamField(
        byte, "hit11_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit12hitType: int = ParamField(
        byte, "hit12_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit13hitType: int = ParamField(
        byte, "hit13_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit14hitType: int = ParamField(
        byte, "hit14_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit15hitType: int = ParamField(
        byte, "hit15_hitType", ATK_PARAM_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti4Priority: int = ParamField(
        byte, "hti4_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti5Priority: int = ParamField(
        byte, "hti5_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti6Priority: int = ParamField(
        byte, "hti6_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti7Priority: int = ParamField(
        byte, "hti7_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti8Priority: int = ParamField(
        byte, "hti8_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti9Priority: int = ParamField(
        byte, "hti9_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti10Priority: int = ParamField(
        byte, "hti10_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti11Priority: int = ParamField(
        byte, "hti11_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti12Priority: int = ParamField(
        byte, "hti12_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti13Priority: int = ParamField(
        byte, "hti13_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti14Priority: int = ParamField(
        byte, "hti14_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hti15Priority: int = ParamField(
        byte, "hti15_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSfxMaterial1: int = ParamField(
        ushort, "defSfxMaterial1", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSeMaterial2: int = ParamField(
        ushort, "defSeMaterial2", WEP_MATERIAL_DEF, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSfxMaterial2: int = ParamField(
        ushort, "defSfxMaterial2", WEP_MATERIAL_DEF_SFX, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkDarkCorrection: int = ParamField(
        ushort, "atkDarkCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkDark: int = ParamField(
        ushort, "atkDark", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "pad5:1", bit_count=1)
    IsDisableParry: bool = ParamField(
        byte, "isDisableParry:1", ATK_PARAM_BOOL, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableBothHandsAtkBonus: bool = ParamField(
        byte, "isDisableBothHandsAtkBonus:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsInvalidatedByNoDamageInAir: bool = ParamField(
        byte, "isInvalidatedByNoDamageInAir:1", ATK_PARAM_BOOL, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad2: int = ParamBitPad(byte, "pad2:4", bit_count=4)
    DmgLevelvsPlayer: int = ParamField(
        sbyte, "dmgLevel_vsPlayer", ATKPARAM_REP_DMGTYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    StatusAilmentAtkPowerCorrectRate: int = ParamField(
        ushort, "statusAilmentAtkPowerCorrectRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectAtkPowerCorrectRatebyPoint: int = ParamField(
        ushort, "spEffectAtkPowerCorrectRate_byPoint", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectAtkPowerCorrectRatebyRate: int = ParamField(
        ushort, "spEffectAtkPowerCorrectRate_byRate", default=100,
        tooltip="TOOLTIP-TODO",
    )
    SpEffectAtkPowerCorrectRatebyDmg: int = ParamField(
        ushort, "spEffectAtkPowerCorrectRate_byDmg", default=100,
        tooltip="TOOLTIP-TODO",
    )
    AtkBehaviorId2: int = ParamField(
        byte, "atkBehaviorId_2", ATKPARAM_BEHAVIOR_ID, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowDamageAttribute: int = ParamField(
        byte, "throwDamageAttribute", ATKPARAM_THROWATTR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    StatusAilmentAtkPowerCorrectRatebyPoint: int = ParamField(
        ushort, "statusAilmentAtkPowerCorrectRate_byPoint", default=100,
        tooltip="TOOLTIP-TODO",
    )
    OverwriteAttackElementCorrectId: int = ParamField(
        int, "overwriteAttackElementCorrectId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DecalBaseId1: int = ParamField(
        short, "decalBaseId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DecalBaseId2: int = ParamField(
        short, "decalBaseId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    WepRegainHpScale: int = ParamField(
        ushort, "wepRegainHpScale", default=100,
        tooltip="TOOLTIP-TODO",
    )
    AtkRegainHp: int = ParamField(
        ushort, "atkRegainHp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RegainableTimeScale: float = ParamField(
        float, "regainableTimeScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RegainableHpRateScale: float = ParamField(
        float, "regainableHpRateScale", default=1.0,
        tooltip="TOOLTIP-TODO",
    )
    RegainableSlotId: int = ParamField(
        sbyte, "regainableSlotId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpAttributeVariationValue: int = ParamField(
        byte, "spAttributeVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ParryForwardOffset: int = ParamField(
        short, "parryForwardOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkSuperArmorCorrection: float = ParamField(
        float, "atkSuperArmorCorrection", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DefSfxMaterialVariationValue: int = ParamField(
        byte, "defSfxMaterialVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(19, "pad4[19]")
    FinalDamageRateId: int = ParamField(
        int, "finalDamageRateId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(12, "pad7[12]")
