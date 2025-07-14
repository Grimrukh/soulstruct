from __future__ import annotations

__all__ = ["GameParamBND"]

import logging
import typing as tp
from dataclasses import field
from pathlib import Path

from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.dcx import DCXType
from soulstruct.base.params.gameparambnd import GameParamBND as _BaseGameParamBND, param_property
from soulstruct.utilities.files import SOULSTRUCT_PATH
from soulstruct.utilities.ParamCrypt import ParamCrypt

from . import paramdef

_LOGGER = logging.getLogger(__name__)


class GameParamBND(_BaseGameParamBND):

    DEFAULT_ENTRY_ROOT: tp.ClassVar[str] = "N:\\GR\\data\\Param\\param\\GameParam"
    PARAMDEF_MODULE: tp.ClassVar = paramdef

    signature: str = "10811000"
    dcx_type: DCXType = DCXType.DCX_ZSTD  # NOTE: As of Elden Ring DLC.
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=lambda: BinderVersion4Info(hash_table_type=4))

    # TODO: Currently no nicknames, even for classic Params that have nicknames in earlier games in Soulstruct.
    #  Planning on removing nicknames across the board, more than likely.
    ActionButtonParam = param_property("ActionButtonParam")  # type: Param[ACTIONBUTTON_PARAM_ST]
    AiSoundParam = param_property("AiSoundParam")  # type: Param[AI_SOUND_PARAM_ST]
    AssetEnvironmentGeometryParam = param_property("AssetEnvironmentGeometryParam")  # type: Param[ASSET_GEOMETORY_PARAM_ST]
    AssetMaterialSfxParam = param_property("AssetMaterialSfxParam")  # type: Param[ASSET_MATERIAL_SFX_PARAM_ST]
    AssetModelSfxParam = param_property("AssetModelSfxParam")  # type: Param[ASSET_MODEL_SFX_PARAM_ST]
    AtkParam_Npc = param_property("AtkParam_Npc")  # type: Param[ATK_PARAM_ST]
    AtkParam_Pc = param_property("AtkParam_Pc")  # type: Param[ATK_PARAM_ST]
    AttackElementCorrectParam = param_property("AttackElementCorrectParam")  # type: Param[ATTACK_ELEMENT_CORRECT_PARAM_ST]
    AutoCreateEnvSoundParam = param_property("AutoCreateEnvSoundParam")  # type: Param[AUTO_CREATE_ENV_SOUND_PARAM_ST]
    BaseChrSelectMenuParam = param_property("BaseChrSelectMenuParam")  # type: Param[BASECHR_SELECT_MENU_PARAM_ST]
    BehaviorParam = param_property("BehaviorParam")  # type: Param[BEHAVIOR_PARAM_ST]
    BehaviorParam_PC = param_property("BehaviorParam_PC")  # type: Param[BEHAVIOR_PARAM_ST]
    BonfireWarpParam = param_property("BonfireWarpParam")  # type: Param[BONFIRE_WARP_PARAM_ST]
    BonfireWarpSubCategoryParam = param_property("BonfireWarpSubCategoryParam")  # type: Param[BONFIRE_WARP_SUB_CATEGORY_PARAM_ST]
    BonfireWarpTabParam = param_property("BonfireWarpTabParam")  # type: Param[BONFIRE_WARP_TAB_PARAM_ST]
    BuddyParam = param_property("BuddyParam")  # type: Param[BUDDY_PARAM_ST]
    BuddyStoneParam = param_property("BuddyStoneParam")  # type: Param[BUDDY_STONE_PARAM_ST]
    BudgetParam = param_property("BudgetParam")  # type: Param[BUDGET_PARAM_ST]
    Bullet = param_property("Bullet")  # type: Param[BULLET_PARAM_ST]
    BulletCreateLimitParam = param_property("BulletCreateLimitParam")  # type: Param[BULLET_CREATE_LIMIT_PARAM_ST]
    CalcCorrectGraph = param_property("CalcCorrectGraph")  # type: Param[CACL_CORRECT_GRAPH_ST]
    Ceremony = param_property("Ceremony")  # type: Param[CEREMONY_PARAM_ST]
    CharaInitParam = param_property("CharaInitParam")  # type: Param[CHARACTER_INIT_PARAM]
    CharMakeMenuListItemParam = param_property("CharMakeMenuListItemParam")  # type: Param[CHARMAKEMENU_LISTITEM_PARAM_ST]
    CharMakeMenuTopParam = param_property("CharMakeMenuTopParam")  # type: Param[CHARMAKEMENUTOP_PARAM_ST]
    ChrActivateConditionParam = param_property("ChrActivateConditionParam")  # type: Param[CHR_ACTIVATE_CONDITION_PARAM_ST]
    ChrEquipModelParam = param_property("ChrEquipModelParam")  # type: Param[CHR_EQUIP_MODEL_PARAM_ST]
    ChrModelParam = param_property("ChrModelParam")  # type: Param[CHR_MODEL_PARAM_ST]
    ClearCountCorrectParam = param_property("ClearCountCorrectParam")  # type: Param[CLEAR_COUNT_CORRECT_PARAM_ST]
    CoolTimeParam = param_property("CoolTimeParam")  # type: Param[COOL_TIME_PARAM_ST]
    CutsceneGparamTimeParam = param_property("CutsceneGparamTimeParam")  # type: Param[CUTSCENE_GPARAM_TIME_PARAM_ST]
    CutsceneGparamWeatherParam = param_property("CutsceneGparamWeatherParam")  # type: Param[CUTSCENE_GPARAM_WEATHER_PARAM_ST]
    CutsceneMapIdParam = param_property("CutsceneMapIdParam")  # type: Param[CUTSCENE_MAP_ID_PARAM_ST]
    CutSceneTextureLoadParam = param_property("CutSceneTextureLoadParam")  # type: Param[CUTSCENE_TEXTURE_LOAD_PARAM_ST]
    CutsceneTimezoneConvertParam = param_property("CutsceneTimezoneConvertParam")  # type: Param[CUTSCENE_TIMEZONE_CONVERT_PARAM_ST]
    CutsceneWeatherOverrideGparamConvertParam = param_property("CutsceneWeatherOverrideGparamConvertParam")  # type: Param[CUTSCENE_WEATHER_OVERRIDE_GPARAM_ID_CONVERT_PARAM_ST]
    DecalParam = param_property("DecalParam")  # type: Param[DECAL_PARAM_ST]
    DirectionCameraParam = param_property("DirectionCameraParam")  # type: Param[DIRECTION_CAMERA_PARAM_ST]
    EnemyCommonParam = param_property("EnemyCommonParam")  # type: Param[ENEMY_COMMON_PARAM_ST]
    EnvObjLotParam = param_property("EnvObjLotParam")  # type: Param[ENV_OBJ_LOT_PARAM_ST]
    EquipMtrlSetParam = param_property("EquipMtrlSetParam")  # type: Param[EQUIP_MTRL_SET_PARAM_ST]
    EquipParamAccessory = param_property("EquipParamAccessory")  # type: Param[EQUIP_PARAM_ACCESSORY_ST]
    EquipParamCustomWeapon = param_property("EquipParamCustomWeapon")  # type: Param[EQUIP_PARAM_CUSTOM_WEAPON_ST]
    EquipParamGem = param_property("EquipParamGem")  # type: Param[EQUIP_PARAM_GEM_ST]
    EquipParamGoods = param_property("EquipParamGoods")  # type: Param[EQUIP_PARAM_GOODS_ST]
    EquipParamProtector = param_property("EquipParamProtector")  # type: Param[EQUIP_PARAM_PROTECTOR_ST]
    EquipParamWeapon = param_property("EquipParamWeapon")  # type: Param[EQUIP_PARAM_WEAPON_ST]
    FaceParam = param_property("FaceParam")  # type: Param[FACE_PARAM_ST]
    FaceRangeParam = param_property("FaceRangeParam")  # type: Param[FACE_RANGE_PARAM_ST]
    FeTextEffectParam = param_property("FeTextEffectParam")  # type: Param[FE_TEXT_EFFECT_PARAM_ST]
    FinalDamageRateParam = param_property("FinalDamageRateParam")  # type: Param[FINAL_DAMAGE_RATE_PARAM_ST]
    FootSfxParam = param_property("FootSfxParam")  # type: Param[FOOT_SFX_PARAM_ST]
    GameAreaParam = param_property("GameAreaParam")  # type: Param[GAME_AREA_PARAM_ST]
    GameSystemCommonParam = param_property("GameSystemCommonParam")  # type: Param[GAME_SYSTEM_COMMON_PARAM_ST]
    GestureParam = param_property("GestureParam")  # type: Param[GESTURE_PARAM_ST]
    GparamRefSettings = param_property("GparamRefSettings")  # type: Param[GPARAM_REF_SETTINGS_PARAM_ST]
    GraphicsCommonParam = param_property("GraphicsCommonParam")  # type: Param[GRAPHICS_COMMON_PARAM_ST]
    GraphicsConfig = param_property("GraphicsConfig")  # type: Param[CS_GRAPHICS_CONFIG_PARAM_ST]
    GrassLodRangeParam = param_property("GrassLodRangeParam")  # type: Param[GRASS_LOD_RANGE_PARAM_ST]
    GrassTypeParam = param_property("GrassTypeParam")  # type: Param[GRASS_TYPE_PARAM_ST]
    GrassTypeParam_Lv1 = param_property("GrassTypeParam_Lv1")  # type: Param[GRASS_TYPE_PARAM_ST]
    GrassTypeParam_Lv2 = param_property("GrassTypeParam_Lv2")  # type: Param[GRASS_TYPE_PARAM_ST]
    HitEffectSeParam = param_property("HitEffectSeParam")  # type: Param[HIT_EFFECT_SE_PARAM_ST]
    HitEffectSfxConceptParam = param_property("HitEffectSfxConceptParam")  # type: Param[HIT_EFFECT_SFX_CONCEPT_PARAM_ST]
    HitEffectSfxParam = param_property("HitEffectSfxParam")  # type: Param[HIT_EFFECT_SFX_PARAM_ST]
    HitMtrlParam = param_property("HitMtrlParam")  # type: Param[HIT_MTRL_PARAM_ST]
    HPEstusFlaskRecoveryParam = param_property("HPEstusFlaskRecoveryParam")  # type: Param[ESTUS_FLASK_RECOVERY_PARAM_ST]
    ItemLotParam_enemy = param_property("ItemLotParam_enemy")  # type: Param[ITEMLOT_PARAM_ST]
    ItemLotParam_map = param_property("ItemLotParam_map")  # type: Param[ITEMLOT_PARAM_ST]
    KeyAssignMenuItemParam = param_property("KeyAssignMenuItemParam")  # type: Param[CS_KEY_ASSIGN_MENUITEM_PARAM]
    KeyAssignParam_TypeA = param_property("KeyAssignParam_TypeA")  # type: Param[KEY_ASSIGN_PARAM_ST]
    KeyAssignParam_TypeB = param_property("KeyAssignParam_TypeB")  # type: Param[KEY_ASSIGN_PARAM_ST]
    KeyAssignParam_TypeC = param_property("KeyAssignParam_TypeC")  # type: Param[KEY_ASSIGN_PARAM_ST]
    KnockBackParam = param_property("KnockBackParam")  # type: Param[KNOCKBACK_PARAM_ST]
    KnowledgeLoadScreenItemParam = param_property("KnowledgeLoadScreenItemParam")  # type: Param[KNOWLEDGE_LOADSCREEN_ITEM_PARAM_ST]
    LegacyDistantViewPartsReplaceParam = param_property("LegacyDistantViewPartsReplaceParam")  # type: Param[LEGACY_DISTANT_VIEW_PARTS_REPLACE_PARAM]
    LoadBalancerDrawDistScaleParam = param_property("LoadBalancerDrawDistScaleParam")  # type: Param[LOAD_BALANCER_DRAW_DIST_SCALE_PARAM_ST]
    LoadBalancerDrawDistScaleParam_ps4 = param_property("LoadBalancerDrawDistScaleParam_ps4")  # type: Param[LOAD_BALANCER_DRAW_DIST_SCALE_PARAM_ST]
    LoadBalancerDrawDistScaleParam_ps5 = param_property("LoadBalancerDrawDistScaleParam_ps5")  # type: Param[LOAD_BALANCER_DRAW_DIST_SCALE_PARAM_ST]
    LoadBalancerDrawDistScaleParam_xb1 = param_property("LoadBalancerDrawDistScaleParam_xb1")  # type: Param[LOAD_BALANCER_DRAW_DIST_SCALE_PARAM_ST]
    LoadBalancerDrawDistScaleParam_xb1x = param_property("LoadBalancerDrawDistScaleParam_xb1x")  # type: Param[LOAD_BALANCER_DRAW_DIST_SCALE_PARAM_ST]
    LoadBalancerDrawDistScaleParam_xss = param_property("LoadBalancerDrawDistScaleParam_xss")  # type: Param[LOAD_BALANCER_DRAW_DIST_SCALE_PARAM_ST]
    LoadBalancerDrawDistScaleParam_xsx = param_property("LoadBalancerDrawDistScaleParam_xsx")  # type: Param[LOAD_BALANCER_DRAW_DIST_SCALE_PARAM_ST]
    LoadBalancerNewDrawDistScaleParam_ps4 = param_property("LoadBalancerNewDrawDistScaleParam_ps4")  # type: Param[LOAD_BALANCER_NEW_DRAW_DIST_SCALE_PARAM_ST]
    LoadBalancerNewDrawDistScaleParam_ps5 = param_property("LoadBalancerNewDrawDistScaleParam_ps5")  # type: Param[LOAD_BALANCER_NEW_DRAW_DIST_SCALE_PARAM_ST]
    LoadBalancerNewDrawDistScaleParam_win64 = param_property("LoadBalancerNewDrawDistScaleParam_win64")  # type: Param[LOAD_BALANCER_NEW_DRAW_DIST_SCALE_PARAM_ST]
    LoadBalancerNewDrawDistScaleParam_xb1 = param_property("LoadBalancerNewDrawDistScaleParam_xb1")  # type: Param[LOAD_BALANCER_NEW_DRAW_DIST_SCALE_PARAM_ST]
    LoadBalancerNewDrawDistScaleParam_xb1x = param_property("LoadBalancerNewDrawDistScaleParam_xb1x")  # type: Param[LOAD_BALANCER_NEW_DRAW_DIST_SCALE_PARAM_ST]
    LoadBalancerNewDrawDistScaleParam_xss = param_property("LoadBalancerNewDrawDistScaleParam_xss")  # type: Param[LOAD_BALANCER_NEW_DRAW_DIST_SCALE_PARAM_ST]
    LoadBalancerNewDrawDistScaleParam_xsx = param_property("LoadBalancerNewDrawDistScaleParam_xsx")  # type: Param[LOAD_BALANCER_NEW_DRAW_DIST_SCALE_PARAM_ST]
    LoadBalancerParam = param_property("LoadBalancerParam")  # type: Param[LOAD_BALANCER_PARAM_ST]
    LockCamParam = param_property("LockCamParam")  # type: Param[LOCK_CAM_PARAM_ST]
    Magic = param_property("Magic")  # type: Param[MAGIC_PARAM_ST]
    MapDefaultInfoParam = param_property("MapDefaultInfoParam")  # type: Param[MAP_DEFAULT_INFO_PARAM_ST]
    MapGdRegionDrawParam = param_property("MapGdRegionDrawParam")  # type: Param[MAP_GD_REGION_DRAW_PARAM]
    MapGdRegionInfoParam = param_property("MapGdRegionInfoParam")  # type: Param[MAP_GD_REGION_ID_PARAM_ST]
    MapGridCreateHeightDetailLimitInfo = param_property("MapGridCreateHeightDetailLimitInfo")  # type: Param[MAP_GRID_CREATE_HEIGHT_LIMIT_DETAIL_INFO_PARAM_ST]
    MapGridCreateHeightLimitInfoParam = param_property("MapGridCreateHeightLimitInfoParam")  # type: Param[MAP_GRID_CREATE_HEIGHT_LIMIT_INFO_PARAM_ST]
    MapMimicryEstablishmentParam = param_property("MapMimicryEstablishmentParam")  # type: Param[MAP_MIMICRY_ESTABLISHMENT_PARAM_ST]
    MapNameTexParam = param_property("MapNameTexParam")  # type: Param[MAP_NAME_TEX_PARAM_ST]
    MapNameTexParam_m61 = param_property("MapNameTexParam_m61")  # type: Param[MAP_NAME_TEX_PARAM_ST_DLC02]
    MapPieceTexParam = param_property("MapPieceTexParam")  # type: Param[MAP_PIECE_TEX_PARAM_ST]
    MapPieceTexParam_m61 = param_property("MapPieceTexParam_m61")  # type: Param[MAP_PIECE_TEX_PARAM_ST_DLC02]
    MaterialExParam = param_property("MaterialExParam")  # type: Param[MATERIAL_EX_PARAM_ST]
    MenuColorTableParam = param_property("MenuColorTableParam")  # type: Param[MENU_PARAM_COLOR_TABLE_ST]
    MenuCommonParam = param_property("MenuCommonParam")  # type: Param[MENU_COMMON_PARAM_ST]
    MenuOffscrRendParam = param_property("MenuOffscrRendParam")  # type: Param[MENU_OFFSCR_REND_PARAM_ST]
    MenuPropertyLayoutParam = param_property("MenuPropertyLayoutParam")  # type: Param[MENUPROPERTY_LAYOUT]
    MenuPropertySpecParam = param_property("MenuPropertySpecParam")  # type: Param[MENUPROPERTY_SPEC]
    MenuValueTableParam = param_property("MenuValueTableParam")  # type: Param[MENU_VALUE_TABLE_SPEC]
    MimicryEstablishmentTexParam = param_property("MimicryEstablishmentTexParam")  # type: Param[MIMICRY_ESTABLISHMENT_TEX_PARAM_ST]
    MimicryEstablishmentTexParam_m61 = param_property("MimicryEstablishmentTexParam_m61")  # type: Param[MIMICRY_ESTABLISHMENT_TEX_PARAM_ST_DLC02]
    MoveParam = param_property("MoveParam")  # type: Param[MOVE_PARAM_ST]
    MPEstusFlaskRecoveryParam = param_property("MPEstusFlaskRecoveryParam")  # type: Param[ESTUS_FLASK_RECOVERY_PARAM_ST]
    MultiHPEstusFlaskBonusParam = param_property("MultiHPEstusFlaskBonusParam")  # type: Param[MULTI_ESTUS_FLASK_BONUS_PARAM_ST]
    MultiMPEstusFlaskBonusParam = param_property("MultiMPEstusFlaskBonusParam")  # type: Param[MULTI_ESTUS_FLASK_BONUS_PARAM_ST]
    MultiPlayCorrectionParam = param_property("MultiPlayCorrectionParam")  # type: Param[MULTI_PLAY_CORRECTION_PARAM_ST]
    MultiSoulBonusRateParam = param_property("MultiSoulBonusRateParam")  # type: Param[MULTI_SOUL_BONUS_RATE_PARAM_ST]
    NetworkAreaParam = param_property("NetworkAreaParam")  # type: Param[NETWORK_AREA_PARAM_ST]
    NetworkMsgParam = param_property("NetworkMsgParam")  # type: Param[NETWORK_MSG_PARAM_ST]
    NetworkParam = param_property("NetworkParam")  # type: Param[NETWORK_PARAM_ST]
    NpcAiActionParam = param_property("NpcAiActionParam")  # type: Param[NPC_AI_ACTION_PARAM_ST]
    NpcAiBehaviorProbability = param_property("NpcAiBehaviorProbability")  # type: Param[NPC_AI_BEHAVIOR_PROBABILITY_PARAM_ST]
    NpcParam = param_property("NpcParam")  # type: Param[NPC_PARAM_ST]
    NpcThinkParam = param_property("NpcThinkParam")  # type: Param[NPC_THINK_PARAM_ST]
    ObjActParam = param_property("ObjActParam")  # type: Param[OBJ_ACT_PARAM_ST]
    PartsDrawParam = param_property("PartsDrawParam")  # type: Param[PARTS_DRAW_PARAM_ST]
    PhantomParam = param_property("PhantomParam")  # type: Param[PHANTOM_PARAM_ST]
    PlayerCommonParam = param_property("PlayerCommonParam")  # type: Param[PLAYER_COMMON_PARAM_ST]
    PlayRegionParam = param_property("PlayRegionParam")  # type: Param[PLAY_REGION_PARAM_ST]
    PostureControlParam_Gender = param_property("PostureControlParam_Gender")  # type: Param[POSTURE_CONTROL_PARAM_GENDER_ST]
    PostureControlParam_Pro = param_property("PostureControlParam_Pro")  # type: Param[POSTURE_CONTROL_PARAM_PRO_ST]
    PostureControlParam_WepLeft = param_property("PostureControlParam_WepLeft")  # type: Param[POSTURE_CONTROL_PARAM_WEP_LEFT_ST]
    PostureControlParam_WepRight = param_property("PostureControlParam_WepRight")  # type: Param[POSTURE_CONTROL_PARAM_WEP_RIGHT_ST]
    RandomAppearParam = param_property("RandomAppearParam")  # type: Param[RANDOM_APPEAR_PARAM_ST]
    ReinforceParamProtector = param_property("ReinforceParamProtector")  # type: Param[REINFORCE_PARAM_PROTECTOR_ST]
    ReinforceParamWeapon = param_property("ReinforceParamWeapon")  # type: Param[REINFORCE_PARAM_WEAPON_ST]
    ResistCorrectParam = param_property("ResistCorrectParam")  # type: Param[RESIST_CORRECT_PARAM_ST]
    RideParam = param_property("RideParam")  # type: Param[RIDE_PARAM_ST]
    RoleParam = param_property("RoleParam")  # type: Param[ROLE_PARAM_ST]
    RollingObjLotParam = param_property("RollingObjLotParam")  # type: Param[ROLLING_OBJ_LOT_PARAM_ST]
    RuntimeBoneControlParam = param_property("RuntimeBoneControlParam")  # type: Param[RUNTIME_BONE_CONTROL_PARAM_ST]
    SeActivationRangeParam = param_property("SeActivationRangeParam")  # type: Param[SE_ACTIVATION_RANGE_PARAM_ST]
    SeMaterialConvertParam = param_property("SeMaterialConvertParam")  # type: Param[SE_MATERIAL_CONVERT_PARAM_ST]
    SfxBlockResShareParam = param_property("SfxBlockResShareParam")  # type: Param[SFX_BLOCK_RES_SHARE_PARAM]
    ShopLineupParam = param_property("ShopLineupParam")  # type: Param[SHOP_LINEUP_PARAM]
    ShopLineupParam_Recipe = param_property("ShopLineupParam_Recipe")  # type: Param[SHOP_LINEUP_PARAM]
    SignPuddleParam = param_property("SignPuddleParam")  # type: Param[SIGN_PUDDLE_PARAM_ST]
    SignPuddleSubCategoryParam = param_property("SignPuddleSubCategoryParam")  # type: Param[SIGN_PUDDLE_SUB_CATEGORY_PARAM_ST]
    SignPuddleTabParam = param_property("SignPuddleTabParam")  # type: Param[SIGN_PUDDLE_TAB_PARAM_ST]
    SoundAssetSoundObjEnableDistParam = param_property("SoundAssetSoundObjEnableDistParam")  # type: Param[SOUND_ASSET_SOUND_OBJ_ENABLE_DIST_PARAM_ST]
    SoundAutoEnvSoundGroupParam = param_property("SoundAutoEnvSoundGroupParam")  # type: Param[SOUND_AUTO_ENV_SOUND_GROUP_PARAM_ST]
    SoundAutoReverbEvaluationDistParam = param_property("SoundAutoReverbEvaluationDistParam")  # type: Param[SOUND_AUTO_REVERB_EVALUATION_DIST_PARAM_ST]
    SoundAutoReverbSelectParam = param_property("SoundAutoReverbSelectParam")  # type: Param[SOUND_AUTO_REVERB_SELECT_PARAM_ST]
    SoundChrPhysicsSeParam = param_property("SoundChrPhysicsSeParam")  # type: Param[SOUND_CHR_PHYSICS_SE_PARAM_ST]
    SoundCommonIngameParam = param_property("SoundCommonIngameParam")  # type: Param[SOUND_COMMON_INGAME_PARAM_ST]
    SoundCutsceneParam = param_property("SoundCutsceneParam")  # type: Param[SOUND_CUTSCENE_PARAM_ST]
    SpeedtreeParam = param_property("SpeedtreeParam")  # type: Param[SPEEDTREE_MODEL_PARAM_ST]
    SpEffectParam = param_property("SpEffectParam")  # type: Param[SP_EFFECT_PARAM_ST]
    SpEffectSetParam = param_property("SpEffectSetParam")  # type: Param[SP_EFFECT_SET_PARAM_ST]
    SpEffectVfxParam = param_property("SpEffectVfxParam")  # type: Param[SP_EFFECT_VFX_PARAM_ST]
    SwordArtsParam = param_property("SwordArtsParam")  # type: Param[SWORD_ARTS_PARAM_ST]
    TalkParam = param_property("TalkParam")  # type: Param[TALK_PARAM_ST]
    ThrowDirectionSfxParam = param_property("ThrowDirectionSfxParam")  # type: Param[THROW_DIRECTION_SFX_PARAM_ST]
    ThrowParam = param_property("ThrowParam")  # type: Param[THROW_PARAM_ST]
    ToughnessParam = param_property("ToughnessParam")  # type: Param[TOUGHNESS_PARAM_ST]
    TutorialParam = param_property("TutorialParam")  # type: Param[TUTORIAL_PARAM_ST]
    WaypointParam = param_property("WaypointParam")  # type: Param[WAYPOINT_PARAM_ST]
    WeatherAssetCreateParam = param_property("WeatherAssetCreateParam")  # type: Param[WEATHER_ASSET_CREATE_PARAM_ST]
    WeatherAssetReplaceParam = param_property("WeatherAssetReplaceParam")  # type: Param[WEATHER_ASSET_REPLACE_PARAM_ST]
    WeatherLotParam = param_property("WeatherLotParam")  # type: Param[WEATHER_LOT_PARAM_ST]
    WeatherLotTexParam = param_property("WeatherLotTexParam")  # type: Param[WEATHER_LOT_TEX_PARAM_ST]
    WeatherLotTexParam_m61 = param_property("WeatherLotTexParam_m61")  # type: Param[WEATHER_LOT_TEX_PARAM_ST_DLC02]
    WeatherParam = param_property("WeatherParam")  # type: Param[WEATHER_PARAM_ST]
    WepAbsorpPosParam = param_property("WepAbsorpPosParam")  # type: Param[WEP_ABSORP_POS_PARAM_ST]
    WetAspectParam = param_property("WetAspectParam")  # type: Param[WET_ASPECT_PARAM_ST]
    WhiteSignCoolTimeParam = param_property("WhiteSignCoolTimeParam")  # type: Param[WHITE_SIGN_COOL_TIME_PARAM_ST]
    WorldMapLegacyConvParam = param_property("WorldMapLegacyConvParam")  # type: Param[WORLD_MAP_LEGACY_CONV_PARAM_ST]
    WorldMapPieceParam = param_property("WorldMapPieceParam")  # type: Param[WORLD_MAP_PIECE_PARAM_ST]
    WorldMapPlaceNameParam = param_property("WorldMapPlaceNameParam")  # type: Param[WORLD_MAP_PLACE_NAME_PARAM_ST]
    WorldMapPointParam = param_property("WorldMapPointParam")  # type: Param[WORLD_MAP_POINT_PARAM_ST]
    WwiseValueToStrParam_BgmBossChrIdConv = param_property("WwiseValueToStrParam_BgmBossChrIdConv")  # type: Param[WWISE_VALUE_TO_STR_CONVERT_PARAM_ST]
    WwiseValueToStrParam_EnvPlaceType = param_property("WwiseValueToStrParam_EnvPlaceType")  # type: Param[WWISE_VALUE_TO_STR_CONVERT_PARAM_ST]
    WwiseValueToStrParam_Switch_AttackStrength = param_property("WwiseValueToStrParam_Switch_AttackStrength")  # type: Param[WWISE_VALUE_TO_STR_CONVERT_PARAM_ST]
    WwiseValueToStrParam_Switch_AttackType = param_property("WwiseValueToStrParam_Switch_AttackType")  # type: Param[WWISE_VALUE_TO_STR_CONVERT_PARAM_ST]
    WwiseValueToStrParam_Switch_DamageAmount = param_property("WwiseValueToStrParam_Switch_DamageAmount")  # type: Param[WWISE_VALUE_TO_STR_CONVERT_PARAM_ST]
    WwiseValueToStrParam_Switch_DeffensiveMaterial = param_property("WwiseValueToStrParam_Switch_DeffensiveMaterial")  # type: Param[WWISE_VALUE_TO_STR_CONVERT_PARAM_ST]
    WwiseValueToStrParam_Switch_GrassHitType = param_property("WwiseValueToStrParam_Switch_GrassHitType")  # type: Param[WWISE_VALUE_TO_STR_CONVERT_PARAM_ST]
    WwiseValueToStrParam_Switch_HitStop = param_property("WwiseValueToStrParam_Switch_HitStop")  # type: Param[WWISE_VALUE_TO_STR_CONVERT_PARAM_ST]
    WwiseValueToStrParam_Switch_OffensiveMaterial = param_property("WwiseValueToStrParam_Switch_OffensiveMaterial")  # type: Param[WWISE_VALUE_TO_STR_CONVERT_PARAM_ST]
    WwiseValueToStrParam_Switch_PlayerEquipmentBottoms = param_property("WwiseValueToStrParam_Switch_PlayerEquipmentBottoms")  # type: Param[WWISE_VALUE_TO_STR_CONVERT_PARAM_ST]
    WwiseValueToStrParam_Switch_PlayerEquipmentTops = param_property("WwiseValueToStrParam_Switch_PlayerEquipmentTops")  # type: Param[WWISE_VALUE_TO_STR_CONVERT_PARAM_ST]
    WwiseValueToStrParam_Switch_PlayerShoes = param_property("WwiseValueToStrParam_Switch_PlayerShoes")  # type: Param[WWISE_VALUE_TO_STR_CONVERT_PARAM_ST]
    WwiseValueToStrParam_Switch_PlayerVoiceType = param_property("WwiseValueToStrParam_Switch_PlayerVoiceType")  # type: Param[WWISE_VALUE_TO_STR_CONVERT_PARAM_ST]

    @classmethod
    def from_encrypted_path(cls, encrypted_path: Path | str) -> tp.Self:
        """Load `GameParamBND` from encrypted DCX-compressed Binder, generally `regulation.bin`."""
        encrypted_path = Path(encrypted_path)
        temp_decrypted = SOULSTRUCT_PATH("__ParamCrypt__.parambnd.dcx")
        _LOGGER.info(f"Decrypting Elden Ring `GameParamBND` from regulation: {encrypted_path}")
        ParamCrypt(encrypted_path, "decrypt", "er", temp_decrypted)
        data = Path(temp_decrypted).read_bytes()  # DCX-compressed `Binder` (BND4)
        temp_decrypted.unlink()
        gameparambnd = cls.from_bytes(data)
        gameparambnd.path = encrypted_path
        return gameparambnd

    def write_encrypted(self, file_path: None | str | Path = None, make_dirs=True):
        """Write back to encrypted, game-ready encrypted file, generally `regulation.bin`."""
        if file_path is None:
            if self.path is None:
                raise ValueError("You must specify `file_path` because file default `path` has not been set.")
            file_path = self.path.parent / "regulation.bin"
        else:
            file_path = Path(file_path)

        if make_dirs:
            file_path.parent.mkdir(parents=True, exist_ok=True)

        temp_decrypted = SOULSTRUCT_PATH("__ParamCrypt__.parambnd.dcx")
        self.write(temp_decrypted, make_dirs=False, check_hash=False)
        ParamCrypt(temp_decrypted, "encrypt", "er", file_path)
        # temp_decrypted.unlink()

    # TODO: `rename_entries_from_text` and other utilities


def examine_er_params():

    from soulstruct.base.params.param import Param, TypedParam
    from soulstruct.base.params.param_dict import ParamDict
    from soulstruct.config import ELDEN_RING_PATH
    from soulstruct.eldenring.params import paramdef

    reg = GameParamBND.from_encrypted_path(ELDEN_RING_PATH / "regulation.bin")
    for entry in reg.entries:
        param_type = Param.detect_param_type(entry.data)
        try:
            data_type = getattr(paramdef, param_type)
        except AttributeError:
            # Fall back to `ParamDict` (with no `ParamDef`).
            param = entry.to_binary_file(ParamDict)
            print(f"{entry.name} read as a ParamDict.")
        else:
            param = entry.to_binary_file(TypedParam(data_type))
            print(f"{entry.name} read successfully.")


if __name__ == '__main__':
    examine_er_params()
