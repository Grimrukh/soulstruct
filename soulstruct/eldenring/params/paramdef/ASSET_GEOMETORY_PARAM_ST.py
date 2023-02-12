from __future__ import annotations

__all__ = ["ASSET_GEOMETORY_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.utils import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ASSET_GEOMETORY_PARAM_ST(ParamRowData):
    SoundBankId: int = ParamField(
        int, "soundBankId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBreakSEId: int = ParamField(
        int, "soundBreakSEId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefDrawParamId: int = ParamField(
        int, "refDrawParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitCreateType: int = ParamField(
        sbyte, "hitCreateType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BehaviorType: int = ParamField(
        byte, "behaviorType", default=1,
        tooltip="TOOLTIP-TODO",
    )
    CollisionType: int = ParamField(
        byte, "collisionType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RainBlockingType: int = ParamField(
        byte, "rainBlockingType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hp: int = ParamField(
        short, "hp", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Defense: int = ParamField(
        ushort, "defense", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakStopTime: float = ParamField(
        float, "breakStopTime", default=30,
        tooltip="TOOLTIP-TODO",
    )
    BreakSfxId: int = ParamField(
        int, "breakSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakSfxCpId: int = ParamField(
        int, "breakSfxCpId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakLandingSfxId: int = ParamField(
        int, "breakLandingSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakBulletBehaviorId: int = ParamField(
        int, "breakBulletBehaviorId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakBulletCpId: int = ParamField(
        int, "breakBulletCpId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FragmentInvisibleWaitTime: float = ParamField(
        float, "FragmentInvisibleWaitTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FragmentInvisibleTime: float = ParamField(
        float, "FragmentInvisibleTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BreakAiSoundID: int = ParamField(
        int, "BreakAiSoundID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakItemLotType: int = ParamField(
        sbyte, "breakItemLotType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AnimBreakIdMax: int = ParamField(
        byte, "animBreakIdMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakBulletAttributeDamageType: int = ParamField(
        sbyte, "breakBulletAttributeDamageType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByPlayerCollide: int = ParamField(
        byte, "isBreakByPlayerCollide:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByEnemyCollide: int = ParamField(
        byte, "isBreakByEnemyCollide:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByChrRide: int = ParamField(
        byte, "isBreak_ByChrRide:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableBreakForFirstAppear: int = ParamField(
        byte, "isDisableBreakForFirstAppear:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnimBreak: int = ParamField(
        byte, "isAnimBreak:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDamageCover: int = ParamField(
        byte, "isDamageCover:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAttackBacklash: int = ParamField(
        byte, "isAttackBacklash:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "Reserve_2:1")
    IsLadder: int = ParamField(
        byte, "isLadder:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsMoveObj: int = ParamField(
        byte, "isMoveObj:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsSkydomeFlag: int = ParamField(
        byte, "isSkydomeFlag:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsAnimPauseOnRemoPlay: int = ParamField(
        byte, "isAnimPauseOnRemoPlay:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBurn: int = ParamField(
        byte, "isBurn:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableRepick: int = ParamField(
        byte, "isEnableRepick:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakOnPickUp: int = ParamField(
        byte, "isBreakOnPickUp:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByHugeenemyCollide: int = ParamField(
        byte, "isBreakByHugeenemyCollide:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NavimeshFlag: int = ParamField(
        byte, "navimeshFlag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletInterval: int = ParamField(
        ushort, "burnBulletInterval", default=30,
        tooltip="TOOLTIP-TODO",
    )
    ClothUpdateDist: float = ParamField(
        float, "clothUpdateDist", default=30,
        tooltip="TOOLTIP-TODO",
    )
    LifeTimeforRuntimeCreate: float = ParamField(
        float, "lifeTime_forRuntimeCreate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ContactSeId: int = ParamField(
        int, "contactSeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RepickAnimIdOffset: int = ParamField(
        int, "repickAnimIdOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectRate0: float = ParamField(
        float, "windEffectRate_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectRate1: float = ParamField(
        float, "windEffectRate_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectType0: int = ParamField(
        byte, "windEffectType_0", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectType1: int = ParamField(
        byte, "windEffectType_1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverrideMaterialId: int = ParamField(
        short, "overrideMaterialId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoCreateOffsetHeight: float = ParamField(
        float, "autoCreateOffsetHeight", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BurnTime: float = ParamField(
        float, "burnTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnBraekRate: float = ParamField(
        float, "burnBraekRate", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxId: int = ParamField(
        int, "burnSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxId1: int = ParamField(
        int, "burnSfxId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxId2: int = ParamField(
        int, "burnSfxId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxId3: int = ParamField(
        int, "burnSfxId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMin: float = ParamField(
        float, "burnSfxDelayTimeMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMin1: float = ParamField(
        float, "burnSfxDelayTimeMin_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMin2: float = ParamField(
        float, "burnSfxDelayTimeMin_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMin3: float = ParamField(
        float, "burnSfxDelayTimeMin_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMax: float = ParamField(
        float, "burnSfxDelayTimeMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMax1: float = ParamField(
        float, "burnSfxDelayTimeMax_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMax2: float = ParamField(
        float, "burnSfxDelayTimeMax_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMax3: float = ParamField(
        float, "burnSfxDelayTimeMax_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletBehaviorId: int = ParamField(
        int, "burnBulletBehaviorId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletBehaviorId1: int = ParamField(
        int, "burnBulletBehaviorId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletBehaviorId2: int = ParamField(
        int, "burnBulletBehaviorId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletBehaviorId3: int = ParamField(
        int, "burnBulletBehaviorId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletDelayTime: float = ParamField(
        float, "burnBulletDelayTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PaintDecalTargetTextureSize: int = ParamField(
        ushort, "paintDecalTargetTextureSize", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NavimeshFlagafter: int = ParamField(
        byte, "navimeshFlag_after", default=0,
        tooltip="TOOLTIP-TODO",
    )
    CamNearBehaviorType: int = ParamField(
        sbyte, "camNearBehaviorType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakItemLotParamId: int = ParamField(
        int, "breakItemLotParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PickUpActionButtonParamId: int = ParamField(
        int, "pickUpActionButtonParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PickUpItemLotParamId: int = ParamField(
        int, "pickUpItemLotParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoDrawGroupBackFaceCheck: int = ParamField(
        byte, "autoDrawGroupBackFaceCheck", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoDrawGroupDepthWrite: int = ParamField(
        byte, "autoDrawGroupDepthWrite", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoDrawGroupShadowTest: int = ParamField(
        byte, "autoDrawGroupShadowTest", default=0,
        tooltip="TOOLTIP-TODO",
    )
    DebugisHeightCheckEnable: int = ParamField(
        byte, "debug_isHeightCheckEnable", default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitCarverCancelAreaFlag: int = ParamField(
        byte, "hitCarverCancelAreaFlag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AssetNavimeshNoCombine: int = ParamField(
        byte, "assetNavimeshNoCombine", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NavimeshFlagApply: int = ParamField(
        byte, "navimeshFlagApply", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NavimeshFlagApplyafter: int = ParamField(
        byte, "navimeshFlagApply_after", default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoDrawGroupPassPixelNum: float = ParamField(
        float, "autoDrawGroupPassPixelNum", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PickUpReplacementEventFlag: int = ParamField(
        uint, "pickUpReplacementEventFlag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PickUpReplacementAnimIdOffset: int = ParamField(
        int, "pickUpReplacementAnimIdOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PickUpReplacementActionButtonParamId: int = ParamField(
        int, "pickUpReplacementActionButtonParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PickUpReplacementItemLotParamId: int = ParamField(
        int, "pickUpReplacementItemLotParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SlidingBulletHitType: int = ParamField(
        byte, "slidingBulletHitType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBushesForDamage: int = ParamField(
        byte, "isBushesForDamage", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PenetrationBulletType: int = ParamField(
        byte, "penetrationBulletType", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(1, "Reserve_3[1]")
    _Pad2: bytes = ParamPad(4, "Reserve_4[4]")
    SoundBreakSECpId: int = ParamField(
        int, "soundBreakSECpId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DebugHeightCheckCapacityMin: float = ParamField(
        float, "debug_HeightCheckCapacityMin", default=-99,
        tooltip="TOOLTIP-TODO",
    )
    DebugHeightCheckCapacityMax: float = ParamField(
        float, "debug_HeightCheckCapacityMax", default=99,
        tooltip="TOOLTIP-TODO",
    )
    RepickActionButtonParamId: int = ParamField(
        int, "repickActionButtonParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RepickItemLotParamId: int = ParamField(
        int, "repickItemLotParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RepickReplacementAnimIdOffset: int = ParamField(
        int, "repickReplacementAnimIdOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RepickReplacementActionButtonParamId: int = ParamField(
        int, "repickReplacementActionButtonParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RepickReplacementItemLotParamId: int = ParamField(
        int, "repickReplacementItemLotParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NoGenerateCarver: int = ParamField(
        byte, "noGenerateCarver", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoHitHugeAfterBreak: int = ParamField(
        byte, "noHitHugeAfterBreak", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnabledBreakSync: int = ParamField(
        byte, "isEnabledBreakSync:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsHiddenOnRepick: int = ParamField(
        byte, "isHiddenOnRepick:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsCreateMultiPlayOnly: int = ParamField(
        byte, "isCreateMultiPlayOnly:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableBulletHitSfx: int = ParamField(
        byte, "isDisableBulletHitSfx:1", default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableSignPreBreak: int = ParamField(
        byte, "isEnableSignPreBreak:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableSignPostBreak: int = ParamField(
        byte, "isEnableSignPostBreak:1", default=1,
        tooltip="TOOLTIP-TODO",
    )
    _Pad3: bytes = ParamPad(1, "Reserve_1:2")
    GenerateMultiForbiddenRegion: int = ParamField(
        byte, "generateMultiForbiddenRegion", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeId0: int = ParamField(
        int, "residentSeId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeId1: int = ParamField(
        int, "residentSeId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeId2: int = ParamField(
        int, "residentSeId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeId3: int = ParamField(
        int, "residentSeId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeDmypolyId0: int = ParamField(
        short, "residentSeDmypolyId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeDmypolyId1: int = ParamField(
        short, "residentSeDmypolyId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeDmypolyId2: int = ParamField(
        short, "residentSeDmypolyId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeDmypolyId3: int = ParamField(
        short, "residentSeDmypolyId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeActivateRatioXboxoneGrid: int = ParamField(
        byte, "excludeActivateRatio_Xboxone_Grid", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeActivateRatioXboxoneLegacy: int = ParamField(
        byte, "excludeActivateRatio_Xboxone_Legacy", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeActivateRatioPS4Grid: int = ParamField(
        byte, "excludeActivateRatio_PS4_Grid", default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeActivateRatioPS4Legacy: int = ParamField(
        byte, "excludeActivateRatio_PS4_Legacy", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad4: bytes = ParamPad(32, "Reserve_0[32]")
