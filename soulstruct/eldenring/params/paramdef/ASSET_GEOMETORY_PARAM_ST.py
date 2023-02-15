from __future__ import annotations

__all__ = ["ASSET_GEOMETORY_PARAM_ST"]

from dataclasses import dataclass

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.game_types import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


# noinspection PyDataclass
@dataclass(slots=True)
class ASSET_GEOMETORY_PARAM_ST(ParamRow):
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
        sbyte, "hitCreateType", ASSET_HIT_CREATE_TYPE_ENUM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BehaviorType: int = ParamField(
        byte, "behaviorType", ASSET_BEHAVIOR_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    CollisionType: int = ParamField(
        byte, "collisionType", ASSET_COLLISION_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RainBlockingType: int = ParamField(
        byte, "rainBlockingType", RAIN_BLOCKING_TYPE, default=0,
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
        float, "breakStopTime", default=30.0,
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
        sbyte, "breakItemLotType", ASSET_BREAK_ITEM_LOT_TYPE_ENUM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AnimBreakIdMax: int = ParamField(
        byte, "animBreakIdMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakBulletAttributeDamageType: int = ParamField(
        sbyte, "breakBulletAttributeDamageType", ASSET_BREAK_ATTRIBUTE_DAMAGE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByPlayerCollide: bool = ParamField(
        byte, "isBreakByPlayerCollide:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByEnemyCollide: bool = ParamField(
        byte, "isBreakByEnemyCollide:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByChrRide: bool = ParamField(
        byte, "isBreak_ByChrRide:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableBreakForFirstAppear: bool = ParamField(
        byte, "isDisableBreakForFirstAppear:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAnimBreak: bool = ParamField(
        byte, "isAnimBreak:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDamageCover: bool = ParamField(
        byte, "isDamageCover:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAttackBacklash: bool = ParamField(
        byte, "isAttackBacklash:1", bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(byte, "Reserve_2:1", bit_count=1)
    IsLadder: bool = ParamField(
        byte, "isLadder:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsMoveObj: bool = ParamField(
        byte, "isMoveObj:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSkydomeFlag: bool = ParamField(
        byte, "isSkydomeFlag:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAnimPauseOnRemoPlay: bool = ParamField(
        byte, "isAnimPauseOnRemoPlay:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBurn: bool = ParamField(
        byte, "isBurn:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableRepick: bool = ParamField(
        byte, "isEnableRepick:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakOnPickUp: bool = ParamField(
        byte, "isBreakOnPickUp:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByHugeenemyCollide: bool = ParamField(
        byte, "isBreakByHugeenemyCollide:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    NavimeshFlag: int = ParamField(
        byte, "navimeshFlag", ASSET_NAVIMESH_FLAG, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletInterval: int = ParamField(
        ushort, "burnBulletInterval", default=30,
        tooltip="TOOLTIP-TODO",
    )
    ClothUpdateDist: float = ParamField(
        float, "clothUpdateDist", default=30.0,
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
        float, "windEffectRate_0", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectRate1: float = ParamField(
        float, "windEffectRate_1", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectType0: int = ParamField(
        byte, "windEffectType_0", ASSET_WIND_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectType1: int = ParamField(
        byte, "windEffectType_1", ASSET_WIND_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverrideMaterialId: int = ParamField(
        short, "overrideMaterialId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoCreateOffsetHeight: float = ParamField(
        float, "autoCreateOffsetHeight", default=0.1,
        tooltip="TOOLTIP-TODO",
    )
    BurnTime: float = ParamField(
        float, "burnTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnBraekRate: float = ParamField(
        float, "burnBraekRate", default=0.5,
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
        byte, "navimeshFlag_after", ASSET_NAVIMESH_FLAG, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CamNearBehaviorType: int = ParamField(
        sbyte, "camNearBehaviorType", ASSET_CAM_NEAR_BEHAVIOR_TYPE, default=0,
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
        byte, "autoDrawGroupBackFaceCheck", ASSET_AUTO_DRAW_GROUP_BACKFACE_CHECK_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoDrawGroupDepthWrite: int = ParamField(
        byte, "autoDrawGroupDepthWrite", ASSET_AUTO_DRAW_GROUP_DEPTH_WRITE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoDrawGroupShadowTest: int = ParamField(
        byte, "autoDrawGroupShadowTest", ASSET_AUTO_DRAW_GROUP_SHADOW_TEST_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DebugisHeightCheckEnable: int = ParamField(
        byte, "debug_isHeightCheckEnable", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitCarverCancelAreaFlag: int = ParamField(
        byte, "hitCarverCancelAreaFlag", HIT_CARVER_CANCEL_AREA_FLAG, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AssetNavimeshNoCombine: int = ParamField(
        byte, "assetNavimeshNoCombine", ASSET_NAVIMESH_GENERATE_ATTRIBUTE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    NavimeshFlagApply: int = ParamField(
        byte, "navimeshFlagApply", ASSET_NAVIMESH_FLAG_APPLY_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    NavimeshFlagApplyafter: int = ParamField(
        byte, "navimeshFlagApply_after", ASSET_NAVIMESH_FLAG_APPLY_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoDrawGroupPassPixelNum: float = ParamField(
        float, "autoDrawGroupPassPixelNum", default=-1.0,
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
        byte, "slidingBulletHitType", ASSET_SLIDING_BULLET_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBushesForDamage: int = ParamField(
        byte, "isBushesForDamage", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PenetrationBulletType: int = ParamField(
        byte, "penetrationBulletType", ASSET_PENETRATION_BULLET_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(1, "Reserve_3[1]")
    _Pad1: bytes = ParamPad(4, "Reserve_4[4]")
    SoundBreakSECpId: int = ParamField(
        int, "soundBreakSECpId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DebugHeightCheckCapacityMin: float = ParamField(
        float, "debug_HeightCheckCapacityMin", default=-99.0,
        tooltip="TOOLTIP-TODO",
    )
    DebugHeightCheckCapacityMax: float = ParamField(
        float, "debug_HeightCheckCapacityMax", default=99.0,
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
        byte, "noGenerateCarver", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoHitHugeAfterBreak: int = ParamField(
        byte, "noHitHugeAfterBreak", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnabledBreakSync: bool = ParamField(
        byte, "isEnabledBreakSync:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsHiddenOnRepick: bool = ParamField(
        byte, "isHiddenOnRepick:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsCreateMultiPlayOnly: bool = ParamField(
        byte, "isCreateMultiPlayOnly:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableBulletHitSfx: bool = ParamField(
        byte, "isDisableBulletHitSfx:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableSignPreBreak: bool = ParamField(
        byte, "isEnableSignPreBreak:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableSignPostBreak: bool = ParamField(
        byte, "isEnableSignPostBreak:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad1: int = ParamBitPad(byte, "Reserve_1:2", bit_count=2)
    GenerateMultiForbiddenRegion: int = ParamField(
        byte, "generateMultiForbiddenRegion", MULTI_FORBIDDEN_REGION_GENERATE_ATTRIBUTE, default=0,
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
        byte, "excludeActivateRatio_Xboxone_Grid", ASSET_EXCLUDE_ACTIVATE_RATIO_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeActivateRatioXboxoneLegacy: int = ParamField(
        byte, "excludeActivateRatio_Xboxone_Legacy", ASSET_EXCLUDE_ACTIVATE_RATIO_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeActivateRatioPS4Grid: int = ParamField(
        byte, "excludeActivateRatio_PS4_Grid", ASSET_EXCLUDE_ACTIVATE_RATIO_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeActivateRatioPS4Legacy: int = ParamField(
        byte, "excludeActivateRatio_PS4_Legacy", ASSET_EXCLUDE_ACTIVATE_RATIO_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad2: bytes = ParamPad(32, "Reserve_0[32]")
