"""Bloodborne `GameParamBND`.

IMPORTANT: Param type `FACE_PARAM_ST` from older games has been renamed `FACE_GEN_PARAM_ST`, and there is a brand new
`FACE_PARAM_ST` type with different fields.
"""

from __future__ import annotations

__all__ = ["GameParamBND"]

import typing as tp
from dataclasses import field

from soulstruct.games import BLOODBORNE
from soulstruct.bloodborne.game_types import *
from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.base.params.gameparambnd import GameParamBND as _BaseGameParamBND, param_property
from soulstruct.base.params.param import Param
from soulstruct.utilities.misc import BiDict

from . import paramdef
from .paramdef import *

if tp.TYPE_CHECKING:
    from ..text.msg_directory import MSGDirectory


class GameParamBND(_BaseGameParamBND):

    PARAMDEF_MODULE: tp.ClassVar = paramdef

    PARAM_NICKNAMES: tp.ClassVar = BiDict(
        ("ActionButtonParam", "ActionButtons"),
        ("AiSoundParam", "AISounds"),
        ("AtkParam_Npc", "NonPlayerAttacks"),
        ("AtkParam_Pc", "PlayerAttacks"),
        ("BehaviorParam", "NonPlayerBehaviors"),
        ("BehaviorParam_PC", "PlayerBehaviors"),
        ("Bullet", "Bullets"),
        ("CalcCorrectGraph", "GrowthCurves"),
        ("CharMakeMenuListItemParam", "CharacterCreationMenuItems"),
        ("CharMakeMenuTopParam", "CharacterCreationMenuTop"),
        ("CharaInitParam", "Players"),
        ("DecalParam", "Decals"),
        ("DungeonFeatureParam", "DungeonFeatures"),
        ("DungeonSubFeatLotParam", "DungeonSubFeatureLots"),
        ("EquipParamProtector", "Armor"),
        ("EquipMtrlSetParam", "UpgradeMaterials"),
        ("EquipParamAccessory", "Rings"),
        ("EquipParamGoods", "Goods"),
        ("EquipParamWeapon", "Weapons"),
        ("FaceGenParam", "FaceGenerators"),
        ("FaceParam", "Faces"),
        ("FaceRangeParam", "FaceRanges"),
        ("GameAreaParam", "Bosses"),
        ("GameMapParam", "GameMaps"),
        ("GemCategoryParam", "GemCategories"),
        ("GemDropDopingParam", "GemDropDoping"),
        ("GemDropModifyParam", "GemDropModifications"),
        ("GemeffectParam", "GemEffects"),
        ("GemGenParam", "GemsAndRunes"),
        ("HitMtrlParam", "Terrains"),
        ("HolygrailExParam", "RitualChalices"),
        ("ItemLotLvdepParam", "ItemLotsWithScaling"),
        ("ItemLotParam", "ItemLots"),
        ("KnockBackParam", "Knockbacks"),
        ("LockCamParam", "Cameras"),
        ("Magic", "Spells"),
        ("MenuPropertyLayoutParam", "MenuPropertyLayouts"),
        ("MenuPropertySpecParam", "MenuPropertySpecs"),
        ("MenuValueTableSpecParam", "MenuValueTableSpecs"),
        ("MenuColorTableParam", "MenuColors"),
        ("MoveParam", "Movement"),
        ("NpcParam", "Characters"),
        ("NpcThinkParam", "AI"),
        ("ObjActParam", "ObjectActivations"),
        ("ObjectParam", "Objects"),
        ("ProtectorGenParam", "ArmorGenerators"),
        ("RagdollParam", "Ragdolls"),
        ("ReinforceParamProtector", "ArmorUpgrades"),
        ("ReinforceParamWeapon", "WeaponUpgrades"),
        ("ResidentVFXParam", "ResidentVFX"),
        ("ReturnPointParam", "ReturnPoints"),
        ("RitualRequiredMatParam", "RitualMaterials"),
        ("ShopLineupParam", "Shops"),
        ("SpEffectParam", "SpecialEffects"),
        ("SpEffectVfxParam", "SpecialEffectVisuals"),
        ("TalkParam", "Dialogue"),
        ("ThrowParam", "Throws"),
        ("WeaponGenParam", "WeaponGenerators"),
        ("WindParam", "Wind"),
    )

    # Maps attribute names to game types. Also defines display order.
    GAME_TYPES: tp.ClassVar = {
        "Players": PlayerParam,
        "Characters": CharacterParam,
        "PlayerBehaviors": BehaviorParam,
        "PlayerAttacks": AttackParam,
        "NonPlayerBehaviors": BehaviorParam,
        "NonPlayerAttacks": AttackParam,
        "AI": AIParam,
        "Bullets": BulletParam,
        "Throws": ThrowParam,
        "SpecialEffects": SpecialEffectParam,
        "Weapons": WeaponParam,
        "Armor": ArmorParam,
        "Accessories": AccessoryParam,
        "Goods": GoodParam,
        "WeaponUpgrades": WeaponUpgradeParam,
        "ArmorUpgrades": ArmorUpgradeParam,
        "UpgradeMaterials": UpgradeMaterialParam,
        "ItemLots": ItemLotParam,
        "Bosses": BossParam,
        "Shops": ShopParam,
        "Spells": SpellParam,
        "Objects": ObjectParam,
        "ObjectActivations": ObjActParam,
        "Movement": MovementParam,
        "Cameras": CameraParam,
        "Terrains": TerrainParam,
        "FaceGenerators": FaceGenParam,
        "Dialogue": DialogueParam,
        "MenuColors": MenuColorsParam,
        "SpecialEffectVisuals": SpecialEffectVisualParam,
        "GrowthCurves": GrowthCurveParam,

        # NEW IN BLOODBORNE
        # TODO: Mix order with above as desired.
        "AISounds": AISoundParam,
        "ActionButtonPrompts": ActionButtonParam,
        "Decals": DecalParam,
        "Faces": FaceParam,
        "CharacterCreationMenuItems": CharacterCreationMenuItemParam,
        "CharacterCreationMenuTop": CharacterCreationMenuTopParam,
        "DungeonFeatures": DungeonFeatureParam,
        "DungeonSubFeatureLots": DungeonSubFeatureLotParam,
        "FaceRanges": FaceRangeParam,
        "GameMaps": GameMapParam,
        "GemCategories": GemCategoryParam,
        "GemDropDoping": GemDropDopingParam,
        "GemDropModifications": GemDropModificationParam,
        "GemEffects": GemEffectParam,
        "GemsAndRunes": GemsAndRunesParam,
        "RitualChalices": RitualChaliceParam,
        "ItemLotsWithScaling": ItemLotWithScalingParam,
        "MenuPropertyLayouts": MenuPropertyLayoutParam,
        "MenuPropertySpecs": MenuPropertySpecParam,
        "MenuValueTableSpecs": MenuValueTableSpecParam,
        "ArmorGenerators": ArmorGeneratorParam,
        "ResidentVFX": ResidentVFXParam,
        "ReturnPoints": ReturnPointParam,
        "RitualMaterials": RitualMaterialsParam,
        "WeaponGenerators": WeaponGeneratorParam,
        "Wind": WindParam,
    }

    dcx_type = BLOODBORNE.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=lambda: BinderVersion4Info(False, False, True, 0))

    # TODO: Some of these may be Dark Souls junk (like EquipParamAccessory?).

    ActionButtons = param_property("ActionButtonParam")  # type: Param[ACTIONBUTTON_PARAM_ST]
    AI = param_property("NpcThinkParam")  # type: Param[NPC_THINK_PARAM_ST]
    AISounds = param_property("AISounds")  # type: Param[AI_SOUND_PARAM_ST]
    Armor = param_property("EquipParamProtector")  # type: Param[EQUIP_PARAM_PROTECTOR_ST]
    ArmorGenerators = param_property("ArmorGenerators")  # type: Param[PROTECTOR_GEN_PARAM_ST]
    ArmorUpgrades = param_property("ReinforceParamProtector")  # type: Param[REINFORCE_PARAM_PROTECTOR_ST]
    Bosses = param_property("GameAreaParam")  # type: Param[GAME_AREA_PARAM_ST]
    Bullets = param_property("Bullet")  # type: Param[BULLET_PARAM_ST]
    Cameras = param_property("LockCamParam")  # type: Param[LOCK_CAM_PARAM_ST]
    CharacterCreationMenuItems = param_property(
        "CharacterCreationMenuItems")  # type: Param[CHARMAKEMENU_LISTITEM_PARAM_ST]
    CharacterCreationMenuTop = param_property("CharacterCreationMenuTop")  # type: Param[CHARMAKEMENUTOP_PARAM_ST]
    Characters = param_property("NpcParam")  # type: Param[NPC_PARAM_ST]
    Decals = param_property("Decals")  # type: Param[DECAL_PARAM_ST]
    Dialogue = param_property("TalkParam")  # type: Param[TALK_PARAM_ST]
    DungeonFeatures = param_property("DungeonFeatures")  # type: Param[DUNGEON_FEATURE_PARAM_ST]
    DungeonSubFeatureLots = param_property("DungeonSubFeatureLots")  # type: Param[DUNGEON_SUB_FEAT_LOT_PARAM]
    FaceGenerators = param_property("FaceGenerators")  # type: Param[FACE_GEN_PARAM_ST]
    FaceRanges = param_property("FaceRanges")  # type: Param[FACE_RANGE_PARAM_ST]
    Faces = param_property("Faces")  # type: Param[FACE_PARAM_ST]
    GameMaps = param_property("GameMaps")  # type: Param[GAME_MAP_PARAM_ST]
    GemCategories = param_property("GemCategories")  # type: Param[GEM_CATEGORY_PARAM_ST]
    GemDropDoping = param_property("GemDropDoping")  # type: Param[GEM_DROP_DOPING_PARAM_ST]
    GemDropModifications = param_property("GemDropModifications")  # type: Param[GEM_DROP_MODIFY_PARAM_ST]
    GemEffects = param_property("GemEffects")  # type: Param[GEMEFFECT_PARAM_ST]
    GemsAndRunes = param_property("GemsAndRunes")  # type: Param[GEM_GEN_PARAM_ST]
    Goods = param_property("EquipParamGoods")  # type: Param[EQUIP_PARAM_GOODS_ST]
    GrowthCurves = param_property("CalcCorrectGraph")  # type: Param[CACL_CORRECT_GRAPH_ST]
    ItemLots = param_property("ItemLotParam")  # type: Param[ITEMLOT_PARAM_ST]
    ItemLotsWithScaling = param_property("ItemLotsWithScaling")  # type: Param[ITEMLOT_LVDEP_PARAM_ST]
    Knockbacks = param_property("KnockBackParam")  # type: Param[KNOCKBACK_PARAM_ST]
    MenuColors = param_property("MenuColorTableParam")  # type: Param[MENU_PARAM_COLOR_TABLE_ST]
    MenuPropertyLayouts = param_property("MenuPropertyLayouts")  # type: Param[MENUPROPERTY_LAYOUT]
    MenuPropertySpecs = param_property("MenuPropertySpecs")  # type: Param[MENUPROPERTY_SPEC]
    MenuValueTableSpecs = param_property("MenuValueTableSpecs")  # type: Param[MENU_VALUE_TABLE_SPEC]
    Movement = param_property("MoveParam")  # type: Param[MOVE_PARAM_ST]
    NonPlayerAttacks = param_property("AtkParam_Npc")  # type: Param[ATK_PARAM_ST]
    NonPlayerBehaviors = param_property("BehaviorParam")  # type: Param[BEHAVIOR_PARAM_ST]
    Objects = param_property("ObjectParam")  # type: Param[OBJECT_PARAM_ST]
    ObjectActivations = param_property("ObjActParam")  # type: Param[OBJ_ACT_PARAM_ST]
    Players = param_property("CharaInitParam")  # type: Param[CHARACTER_INIT_PARAM]
    PlayerAttacks = param_property("AtkParam_Pc")  # type: Param[ATK_PARAM_ST]
    PlayerBehaviors = param_property("BehaviorParam_PC")  # type: Param[BEHAVIOR_PARAM_ST]
    Ragdolls = param_property("RagdollParam")  # type: Param[RAGDOLL_PARAM_ST]
    ResidentVFX = param_property("ResidentVFX")  # type: Param[RESIDENT_FX_PARAM_ST]  # TODO: possibly `PlayerVFX`
    ReturnPoints = param_property("ReturnPoints")  # type: Param[RETURN_POINT_PARAM_ST]  # TODO: ?
    Rings = param_property("EquipParamAccessory")  # type: Param[EQUIP_PARAM_ACCESSORY_ST]
    RitualChalices = param_property("RitualChalices")  # type: Param[HOLYGRAIL_EX_PARAM_ST]
    RitualMaterials = param_property("RitualMaterials")  # type: Param[RITUAL_REQUIRED_MAT_PARAM]
    Shops = param_property("ShopLineupParam")  # type: Param[SHOP_LINEUP_PARAM]
    SpecialEffects = param_property("SpEffectParam")  # type: Param[SP_EFFECT_PARAM_ST]
    SpecialEffectVisuals = param_property("SpEffectVfxParam")  # type: Param[SP_EFFECT_VFX_PARAM_ST]
    Spells = param_property("Magic")  # type: Param[MAGIC_PARAM_ST]
    Terrains = param_property("HitMtrlParam")  # type: Param[HIT_MTRL_PARAM_ST]
    Throws = param_property("ThrowParam")  # type: Param[THROW_INFO_BANK]
    UpgradeMaterials = param_property("EquipMtrlSetParam")  # type: Param[EQUIP_MTRL_SET_PARAM_ST]
    Weapons = param_property("EquipParamWeapon")  # type: Param[EQUIP_PARAM_WEAPON_ST]
    WeaponGenerators = param_property("WeaponGenerators")  # type: Param[WEAPON_GEN_PARAM_ST]
    WeaponUpgrades = param_property("ReinforceParamWeapon")  # type: Param[REINFORCE_PARAM_WEAPON_ST]
    Wind = param_property("Wind")  # type: Param[WIND_PARAM_ST]

    def rename_entries_from_text(self, text: MSGDirectory, param_nickname: str = None):
        """Rename item param entries according to their (presumably more desirable) names in Bloodborne text data.

        Many Bloodborne names (mainly for cut stuff) use a single asterisk as a placeholder. Such names are ignored by
        this method.

        TODO: 'GemsAndRunes' uses some kind of text ID offset param field.

        Args:
            text (MSGDirectory): text data structure to pull names from.
            param_nickname (str or None): specific ParamTable name to rename, or None to rename all (default).
                Valid names are "Weapons", "Armor", "Goods", and "GemsAndRunes" (or None to do all).
        """
        if param_nickname:
            param_nickname = param_nickname.lower().rstrip("s")
            if param_nickname not in {"weapon", "armor", "good", "gemsandrune"}:
                raise ValueError(
                    f"Invalid `param_nickname`: {param_nickname}. "
                    f"Must be 'Weapons', 'Armor', 'Goods', or 'GemsAndRunes'."
                )
        for item_type_check, param, text_fmg in zip(
            ("weapon", "armor", "good", "gemsandrune"),
            (self.Weapons, self.Armor, self.Goods, self.GemsAndRunes),
            (text.WeaponNames, text.ArmorNames, text.GoodNames, text.BloodGemNames),
        ):
            if not param_nickname or param_nickname == item_type_check:
                for param_id, param_row in param.items():
                    if param_id in text_fmg and text_fmg[param_id].strip(" *"):
                        param_row.Name = text_fmg[param_id]
