from __future__ import annotations

__all__ = ["ATK_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ATK_PARAM_ST(ParamRowData):
    Hitbox0Radius: float = ParamField(
        float, "hit0_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox1Radius: float = ParamField(
        float, "hit1_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox2Radius: float = ParamField(
        float, "hit2_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox3Radius: float = ParamField(
        float, "hit3_Radius", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    KnockbackDistance: float = ParamField(
        float, "knockbackDist", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    HitStopTime: float = ParamField(
        float, "hitStopTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectOnHit0: int = ParamField(
        int, "spEffectId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectOnHit1: int = ParamField(
        int, "spEffectId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectOnHit2: int = ParamField(
        int, "spEffectId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectOnHit3: int = ParamField(
        int, "spEffectId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SpecialEffectOnHit4: int = ParamField(
        int, "spEffectId4", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox0StartModelPoint: int = ParamField(
        short, "hit0_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox1StartModelPoint: int = ParamField(
        short, "hit1_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox2StartModelPoint: int = ParamField(
        short, "hit2_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox3StartModelPoint: int = ParamField(
        short, "hit3_DmyPoly1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox0EndModelPoint: int = ParamField(
        short, "hit0_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox1EndModelPoint: int = ParamField(
        short, "hit1_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox2EndModelPoint: int = ParamField(
        short, "hit2_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox3EndModelPoint: int = ParamField(
        short, "hit3_DmyPoly2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BlowOffCorrection: int = ParamField(
        ushort, "blowingCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicalAttackPowerPercentage: int = ParamField(
        ushort, "atkPhysCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicAttackPowerPercentage: int = ParamField(
        ushort, "atkMagCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireAttackPowerPercentage: int = ParamField(
        ushort, "atkFireCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LightningAttackPowerPercentage: int = ParamField(
        ushort, "atkThunCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaAttackPowerPercentage: int = ParamField(
        ushort, "atkStamCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardAttackPercentage: int = ParamField(
        ushort, "guardAtkRateCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardBreakPercentage: int = ParamField(
        ushort, "guardBreakCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttackDuringThrowPercentage: int = ParamField(
        ushort, "atkThrowEscapeCorrection", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubCategory1: int = ParamField(
        byte, "subCategory1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    SubCategory2: int = ParamField(
        byte, "subCategory2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PhysicalAttackPower: int = ParamField(
        ushort, "atkPhys", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MagicAttackPower: int = ParamField(
        ushort, "atkMag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    FireAttackPower: int = ParamField(
        ushort, "atkFire", default=0,
        tooltip="TOOLTIP-TODO",
    )
    LightningAttackPower: int = ParamField(
        ushort, "atkThun", default=0,
        tooltip="TOOLTIP-TODO",
    )
    StaminaAttackPower: int = ParamField(
        ushort, "atkStam", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardAttackPower: int = ParamField(
        ushort, "guardAtkRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardBreakPower: int = ParamField(
        ushort, "guardBreakRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "pad6[1]")
    IsEnableCalcDamageForBushesObj: int = ParamField(
        byte, "isEnableCalcDamageForBushesObj", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttackPowerDuringThrows: int = ParamField(
        ushort, "atkThrowEscape", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ObjectDamage: int = ParamField(
        ushort, "atkObj", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardStaminaPercentage: int = ParamField(
        short, "guardStaminaCutRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardPercentage: int = ParamField(
        short, "guardRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowID: int = ParamField(
        ushort, "throwTypeId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox0HitType: int = ParamField(
        byte, "hit0_hitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox1HitType: int = ParamField(
        byte, "hit1_hitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox2HitType: int = ParamField(
        byte, "hit2_hitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox3HitType: int = ParamField(
        byte, "hit3_hitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox0Priority: int = ParamField(
        byte, "hti0_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox1Priority: int = ParamField(
        byte, "hti1_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox2Priority: int = ParamField(
        byte, "hti2_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hitbox3Priority: int = ParamField(
        byte, "hti3_Priority", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ImpactLevel: int = ParamField(
        byte, "dmgLevel", default=0,
        tooltip="TOOLTIP-TODO",
    )
    MapHitType: int = ParamField(
        byte, "mapHitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreGuardPercentage: int = ParamField(
        sbyte, "guardCutCancelRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AttackAttribute: int = ParamField(
        byte, "atkAttribute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ElementAttribute: int = ParamField(
        byte, "spAttribute", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VisualSoundEffectsOnAttack: int = ParamField(
        byte, "atkType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    VisualSoundEffectsOnHit: int = ParamField(
        byte, "atkMaterial", default=0,
        tooltip="TOOLTIP-TODO",
    )
    GuardRangeType: int = ParamField(
        byte, "guardRangeType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSeMaterial1: int = ParamField(
        ushort, "defSeMaterial1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ModelPointSource: int = ParamField(
        byte, "hitSourceType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowFlag: int = ParamField(
        byte, "throwFlag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreGuard: int = ParamField(
        byte, "disableGuard:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoStaminaDamage: int = ParamField(
        byte, "disableStaminaAttack:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoSpecialEffects: int = ParamField(
        byte, "disableHitSpEffect:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoMissNotificationForAI: int = ParamField(
        byte, "IgnoreNotifyMissSwingForAI:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RepeatHitSoundEffects: int = ParamField(
        byte, "repeatHitSfx:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsPhysicalProjectile: int = ParamField(
        byte, "isArrowAtk:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAttackByGhost: int = ParamField(
        byte, "isGhostAtk:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IgnoreInvincibilityFrames: int = ParamField(
        byte, "isDisableNoDamage:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPowforSfx: int = ParamField(
        sbyte, "atkPow_forSfx", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkDirforSfx: int = ParamField(
        sbyte, "atkDir_forSfx", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsEnemies: int = ParamField(
        byte, "opposeTarget:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    AffectsAllies: int = ParamField(
        byte, "friendlyTarget:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AffectsSelf: int = ParamField(
        byte, "selfTarget:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsCheckDoorPenetration: int = ParamField(
        byte, "isCheckDoorPenetration:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsVsRideAtk: int = ParamField(
        byte, "isVsRideAtk:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAddBaseAtk: int = ParamField(
        byte, "isAddBaseAtk:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeThreatLvNotify: int = ParamField(
        byte, "excludeThreatLvNotify:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "pad1:1")
    AtkBehaviorId: int = ParamField(
        byte, "atkBehaviorId", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AtkPowforSe: int = ParamField(
        sbyte, "atkPow_forSe", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PoiseAttackPower: float = ParamField(
        float, "atkSuperArmor", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DecalID1: int = ParamField(
        int, "decalId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DecalID2: int = ParamField(
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
        byte, "hit4_hitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit5hitType: int = ParamField(
        byte, "hit5_hitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit6hitType: int = ParamField(
        byte, "hit6_hitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit7hitType: int = ParamField(
        byte, "hit7_hitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit8hitType: int = ParamField(
        byte, "hit8_hitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit9hitType: int = ParamField(
        byte, "hit9_hitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit10hitType: int = ParamField(
        byte, "hit10_hitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit11hitType: int = ParamField(
        byte, "hit11_hitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit12hitType: int = ParamField(
        byte, "hit12_hitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit13hitType: int = ParamField(
        byte, "hit13_hitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit14hitType: int = ParamField(
        byte, "hit14_hitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hit15hitType: int = ParamField(
        byte, "hit15_hitType", default=0,
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
        ushort, "defSfxMaterial1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSeMaterial2: int = ParamField(
        ushort, "defSeMaterial2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DefSfxMaterial2: int = ParamField(
        ushort, "defSfxMaterial2", default=0,
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
    _Pad2: bytes = ParamPad(1, "pad5:1")
    IsDisableParry: int = ParamField(
        byte, "isDisableParry:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableBothHandsAtkBonus: int = ParamField(
        byte, "isDisableBothHandsAtkBonus:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsInvalidatedByNoDamageInAir: int = ParamField(
        byte, "isInvalidatedByNoDamageInAir:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(1, "pad2:4")
    DmgLevelvsPlayer: int = ParamField(
        sbyte, "dmgLevel_vsPlayer", default=0,
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
        byte, "atkBehaviorId_2", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ThrowDamageAttribute: int = ParamField(
        byte, "throwDamageAttribute", default=0,
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
    WeaponRegainHPScale: int = ParamField(
        ushort, "wepRegainHpScale", default=100,
        tooltip="TOOLTIP-TODO",
    )
    AttackRegainHP: int = ParamField(
        ushort, "atkRegainHp", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RegainTimeScale: float = ParamField(
        float, "regainableTimeScale", default=1,
        tooltip="TOOLTIP-TODO",
    )
    RegainHPRateScale: float = ParamField(
        float, "regainableHpRateScale", default=1,
        tooltip="TOOLTIP-TODO",
    )
    RegainableSlotID: int = ParamField(
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
    PoiseAttackPercentage: float = ParamField(
        float, "atkSuperArmorCorrection", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    DefSfxMaterialVariationValue: int = ParamField(
        byte, "defSfxMaterialVariationValue", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(19, "pad4[19]")
