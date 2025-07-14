from __future__ import annotations

__all__ = ["ASSET_GEOMETORY_PARAM_ST"]

from soulstruct.base.params.param_row import *
from soulstruct.eldenring.params.enums import *
from soulstruct.utilities.binary import *


class ASSET_GEOMETORY_PARAM_ST(ParamRow):
    SoundBankId: int = ParamField(
        int32, "soundBankId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SoundBreakSEId: int = ParamField(
        int32, "soundBreakSEId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RefDrawParamId: int = ParamField(
        int32, "refDrawParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    HitCreateType: int = ParamField(
        int8, "hitCreateType", ASSET_HIT_CREATE_TYPE_ENUM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BehaviorType: int = ParamField(
        uint8, "behaviorType", ASSET_BEHAVIOR_TYPE, default=1,
        tooltip="TOOLTIP-TODO",
    )
    CollisionType: int = ParamField(
        uint8, "collisionType", ASSET_COLLISION_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    RainBlockingType: int = ParamField(
        uint8, "rainBlockingType", RAIN_BLOCKING_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    Hp: int = ParamField(
        int16, "hp", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    Defense: int = ParamField(
        uint16, "defense", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakStopTime: float = ParamField(
        float32, "breakStopTime", default=30.0,
        tooltip="TOOLTIP-TODO",
    )
    BreakSfxId: int = ParamField(
        int32, "breakSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakSfxCpId: int = ParamField(
        int32, "breakSfxCpId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakLandingSfxId: int = ParamField(
        int32, "breakLandingSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakBulletBehaviorId: int = ParamField(
        int32, "breakBulletBehaviorId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BreakBulletCpId: int = ParamField(
        int32, "breakBulletCpId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    FragmentInvisibleWaitTime: float = ParamField(
        float32, "FragmentInvisibleWaitTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    FragmentInvisibleTime: float = ParamField(
        float32, "FragmentInvisibleTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BreakAiSoundID: int = ParamField(
        int32, "BreakAiSoundID", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakItemLotType: int = ParamField(
        int8, "breakItemLotType", ASSET_BREAK_ITEM_LOT_TYPE_ENUM, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AnimBreakIdMax: int = ParamField(
        uint8, "animBreakIdMax", default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakBulletAttributeDamageType: int = ParamField(
        int8, "breakBulletAttributeDamageType", ASSET_BREAK_ATTRIBUTE_DAMAGE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByPlayerCollide: bool = ParamField(
        uint8, "isBreakByPlayerCollide:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByEnemyCollide: bool = ParamField(
        uint8, "isBreakByEnemyCollide:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByChrRide: bool = ParamField(
        uint8, "isBreak_ByChrRide:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableBreakForFirstAppear: bool = ParamField(
        uint8, "isDisableBreakForFirstAppear:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAnimBreak: bool = ParamField(
        uint8, "isAnimBreak:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDamageCover: bool = ParamField(
        uint8, "isDamageCover:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAttackBacklash: bool = ParamField(
        uint8, "isAttackBacklash:1", bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    _BitPad0: int = ParamBitPad(uint8, "Reserve_2:1", bit_count=1)
    Unknown0x3b7: bool = ParamField(
        uint8, "unknown_0x3b_7:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsLadder: bool = ParamField(
        uint8, "isLadder:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsMoveObj: bool = ParamField(
        uint8, "isMoveObj:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsSkydomeFlag: bool = ParamField(
        uint8, "isSkydomeFlag:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsAnimPauseOnRemoPlay: bool = ParamField(
        uint8, "isAnimPauseOnRemoPlay:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBurn: bool = ParamField(
        uint8, "isBurn:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableRepick: bool = ParamField(
        uint8, "isEnableRepick:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakOnPickUp: bool = ParamField(
        uint8, "isBreakOnPickUp:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsBreakByHugeenemyCollide: bool = ParamField(
        uint8, "isBreakByHugeenemyCollide:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    NavimeshFlag: int = ParamField(
        uint8, "navimeshFlag", ASSET_NAVIMESH_FLAG, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletInterval: int = ParamField(
        uint16, "burnBulletInterval", default=30,
        tooltip="TOOLTIP-TODO",
    )
    ClothUpdateDist: float = ParamField(
        float32, "clothUpdateDist", default=30.0,
        tooltip="TOOLTIP-TODO",
    )
    LifeTimeforRuntimeCreate: float = ParamField(
        float32, "lifeTime_forRuntimeCreate", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    ContactSeId: int = ParamField(
        int32, "contactSeId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RepickAnimIdOffset: int = ParamField(
        int32, "repickAnimIdOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectRate0: float = ParamField(
        float32, "windEffectRate_0", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectRate1: float = ParamField(
        float32, "windEffectRate_1", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectType0: int = ParamField(
        uint8, "windEffectType_0", ASSET_WIND_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    WindEffectType1: int = ParamField(
        uint8, "windEffectType_1", ASSET_WIND_EFFECT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    OverrideMaterialId: int = ParamField(
        int16, "overrideMaterialId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoCreateOffsetHeight: float = ParamField(
        float32, "autoCreateOffsetHeight", default=0.1,
        tooltip="TOOLTIP-TODO",
    )
    BurnTime: float = ParamField(
        float32, "burnTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnBraekRate: float = ParamField(
        float32, "burnBraekRate", default=0.5,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxId: int = ParamField(
        int32, "burnSfxId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxId1: int = ParamField(
        int32, "burnSfxId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxId2: int = ParamField(
        int32, "burnSfxId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxId3: int = ParamField(
        int32, "burnSfxId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMin: float = ParamField(
        float32, "burnSfxDelayTimeMin", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMin1: float = ParamField(
        float32, "burnSfxDelayTimeMin_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMin2: float = ParamField(
        float32, "burnSfxDelayTimeMin_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMin3: float = ParamField(
        float32, "burnSfxDelayTimeMin_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMax: float = ParamField(
        float32, "burnSfxDelayTimeMax", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMax1: float = ParamField(
        float32, "burnSfxDelayTimeMax_1", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMax2: float = ParamField(
        float32, "burnSfxDelayTimeMax_2", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnSfxDelayTimeMax3: float = ParamField(
        float32, "burnSfxDelayTimeMax_3", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletBehaviorId: int = ParamField(
        int32, "burnBulletBehaviorId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletBehaviorId1: int = ParamField(
        int32, "burnBulletBehaviorId_1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletBehaviorId2: int = ParamField(
        int32, "burnBulletBehaviorId_2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletBehaviorId3: int = ParamField(
        int32, "burnBulletBehaviorId_3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    BurnBulletDelayTime: float = ParamField(
        float32, "burnBulletDelayTime", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    PaintDecalTargetTextureSize: int = ParamField(
        uint16, "paintDecalTargetTextureSize", default=0,
        tooltip="TOOLTIP-TODO",
    )
    NavimeshFlagafter: int = ParamField(
        uint8, "navimeshFlag_after", ASSET_NAVIMESH_FLAG, default=0,
        tooltip="TOOLTIP-TODO",
    )
    CamNearBehaviorType: int = ParamField(
        int8, "camNearBehaviorType", ASSET_CAM_NEAR_BEHAVIOR_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    BreakItemLotParamId: int = ParamField(
        int32, "breakItemLotParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PickUpActionButtonParamId: int = ParamField(
        int32, "pickUpActionButtonParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PickUpItemLotParamId: int = ParamField(
        int32, "pickUpItemLotParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    AutoDrawGroupBackFaceCheck: int = ParamField(
        uint8, "autoDrawGroupBackFaceCheck", ASSET_AUTO_DRAW_GROUP_BACKFACE_CHECK_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoDrawGroupDepthWrite: int = ParamField(
        uint8, "autoDrawGroupDepthWrite", ASSET_AUTO_DRAW_GROUP_DEPTH_WRITE_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoDrawGroupShadowTest: int = ParamField(
        uint8, "autoDrawGroupShadowTest", ASSET_AUTO_DRAW_GROUP_SHADOW_TEST_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    DebugisHeightCheckEnable: int = ParamField(
        uint8, "debug_isHeightCheckEnable", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    HitCarverCancelAreaFlag: int = ParamField(
        uint8, "hitCarverCancelAreaFlag", HIT_CARVER_CANCEL_AREA_FLAG, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AssetNavimeshNoCombine: int = ParamField(
        uint8, "assetNavimeshNoCombine", ASSET_NAVIMESH_GENERATE_ATTRIBUTE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    NavimeshFlagApply: int = ParamField(
        uint8, "navimeshFlagApply", ASSET_NAVIMESH_FLAG_APPLY_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    NavimeshFlagApplyafter: int = ParamField(
        uint8, "navimeshFlagApply_after", ASSET_NAVIMESH_FLAG_APPLY_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    AutoDrawGroupPassPixelNum: float = ParamField(
        float32, "autoDrawGroupPassPixelNum", default=-1.0,
        tooltip="TOOLTIP-TODO",
    )
    PickUpReplacementEventFlag: int = ParamField(
        uint32, "pickUpReplacementEventFlag", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PickUpReplacementAnimIdOffset: int = ParamField(
        int32, "pickUpReplacementAnimIdOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    PickUpReplacementActionButtonParamId: int = ParamField(
        int32, "pickUpReplacementActionButtonParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    PickUpReplacementItemLotParamId: int = ParamField(
        int32, "pickUpReplacementItemLotParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    SlidingBulletHitType: int = ParamField(
        uint8, "slidingBulletHitType", ASSET_SLIDING_BULLET_HIT_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsBushesForDamage: int = ParamField(
        uint8, "isBushesForDamage", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    PenetrationBulletType: int = ParamField(
        uint8, "penetrationBulletType", ASSET_PENETRATION_BULLET_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkR3: int = ParamField(
        uint8, "unkR3", default=0,
        tooltip="TOOLTIP-TODO",
    )
    UnkR4: float = ParamField(
        float32, "unkR4", default=0.0,
        tooltip="TOOLTIP-TODO",
    )
    SoundBreakSECpId: int = ParamField(
        int32, "soundBreakSECpId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    DebugHeightCheckCapacityMin: float = ParamField(
        float32, "debug_HeightCheckCapacityMin", default=-99.0,
        tooltip="TOOLTIP-TODO",
    )
    DebugHeightCheckCapacityMax: float = ParamField(
        float32, "debug_HeightCheckCapacityMax", default=99.0,
        tooltip="TOOLTIP-TODO",
    )
    RepickActionButtonParamId: int = ParamField(
        int32, "repickActionButtonParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RepickItemLotParamId: int = ParamField(
        int32, "repickItemLotParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RepickReplacementAnimIdOffset: int = ParamField(
        int32, "repickReplacementAnimIdOffset", default=0,
        tooltip="TOOLTIP-TODO",
    )
    RepickReplacementActionButtonParamId: int = ParamField(
        int32, "repickReplacementActionButtonParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    RepickReplacementItemLotParamId: int = ParamField(
        int32, "repickReplacementItemLotParamId", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    NoGenerateCarver: int = ParamField(
        uint8, "noGenerateCarver", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    NoHitHugeAfterBreak: int = ParamField(
        uint8, "noHitHugeAfterBreak", BOOL_CIRCLECROSS_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    IsEnabledBreakSync: bool = ParamField(
        uint8, "isEnabledBreakSync:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsHiddenOnRepick: bool = ParamField(
        uint8, "isHiddenOnRepick:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsCreateMultiPlayOnly: bool = ParamField(
        uint8, "isCreateMultiPlayOnly:1", bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsDisableBulletHitSfx: bool = ParamField(
        uint8, "isDisableBulletHitSfx:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=False,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableSignPreBreak: bool = ParamField(
        uint8, "isEnableSignPreBreak:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    IsEnableSignPostBreak: bool = ParamField(
        uint8, "isEnableSignPostBreak:1", BOOL_CIRCLECROSS_TYPE, bit_count=1, default=True,
        tooltip="TOOLTIP-TODO",
    )
    UnkR1: int = ParamField(
        uint8, "unkR1:2", bit_count=2, default=0,
        tooltip="TOOLTIP-TODO",
    )
    GenerateMultiForbiddenRegion: int = ParamField(
        uint8, "generateMultiForbiddenRegion", MULTI_FORBIDDEN_REGION_GENERATE_ATTRIBUTE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeId0: int = ParamField(
        int32, "residentSeId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeId1: int = ParamField(
        int32, "residentSeId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeId2: int = ParamField(
        int32, "residentSeId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeId3: int = ParamField(
        int32, "residentSeId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeDmypolyId0: int = ParamField(
        int16, "residentSeDmypolyId0", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeDmypolyId1: int = ParamField(
        int16, "residentSeDmypolyId1", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeDmypolyId2: int = ParamField(
        int16, "residentSeDmypolyId2", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ResidentSeDmypolyId3: int = ParamField(
        int16, "residentSeDmypolyId3", default=-1,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeActivateRatioXboxoneGrid: int = ParamField(
        uint8, "excludeActivateRatio_Xboxone_Grid", ASSET_EXCLUDE_ACTIVATE_RATIO_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeActivateRatioXboxoneLegacy: int = ParamField(
        uint8, "excludeActivateRatio_Xboxone_Legacy", ASSET_EXCLUDE_ACTIVATE_RATIO_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeActivateRatioPS4Grid: int = ParamField(
        uint8, "excludeActivateRatio_PS4_Grid", ASSET_EXCLUDE_ACTIVATE_RATIO_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    ExcludeActivateRatioPS4Legacy: int = ParamField(
        uint8, "excludeActivateRatio_PS4_Legacy", ASSET_EXCLUDE_ACTIVATE_RATIO_TYPE, default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad0: bytes = ParamPad(32, "Reserve_0_old[32]")
    Unknown0x120: int = ParamField(
        uint8, "unknown_0x120", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x121: int = ParamField(
        uint8, "unknown_0x121", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x122: int = ParamField(
        uint8, "unknown_0x122", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x123: int = ParamField(
        uint8, "unknown_0x123", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x124: int = ParamField(
        uint8, "unknown_0x124", default=0,
        tooltip="TOOLTIP-TODO",
    )
    Unknown0x125: int = ParamField(
        uint8, "unknown_0x125", default=0,
        tooltip="TOOLTIP-TODO",
    )
    _Pad1: bytes = ParamPad(26, "Reserve_0[26]")
