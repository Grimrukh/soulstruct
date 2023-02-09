from __future__ import annotations

__all__ = ["Param", "GameParamBND"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.games import BLOODBORNE
from soulstruct.bloodborne.game_types import *
from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.base.params.game_param_bnd import GameParamBND as _BaseGameParamBND, param_property
from soulstruct.base.params.param import Param as _BaseParam
from soulstruct.utilities.misc import BiDict

from .paramdef import GET_BUNDLED_PARAMDEF

if tp.TYPE_CHECKING:
    from ..text.msg_directory import MSGDirectory


@dataclass(slots=True)
class Param(_BaseParam):
    GET_BUNDLED_PARAMDEF: tp.ClassVar = staticmethod(GET_BUNDLED_PARAMDEF)


@dataclass(slots=True)
class GameParamBND(_BaseGameParamBND):
    PARAM_CLASS: tp.ClassVar = Param

    PARAM_NICKNAMES: tp.ClassVar = BiDict(
        ("AtkParam_Npc", "NonPlayerAttacks"),
        ("AtkParam_Pc", "PlayerAttacks"),
        ("BehaviorParam", "NonPlayerBehaviors"),
        ("BehaviorParam_PC", "PlayerBehaviors"),

        # TODO: Placing all undocumented new tables here for now.
        ("ActionButtonParam", "ActionButtons"),
        ("AiSoundParam", "AISounds"),
        ("CharMakeMenuListItemParam", "CharacterCreationMenuItems"),
        ("CharMakeMenuTopParam", "CharacterCreationMenuTop"),
        ("DecalParam", "Decals"),
        ("DungeonFeatureParam", "DungeonFeatures"),
        ("DungeonSubFeatLotParam", "DungeonSubFeatureLots"),
        ("FaceGenParam", "FaceGenerators"),
        ("FaceParam", "Faces"),
        ("FaceRangeParam", "FaceRanges"),
        ("GameMapParam", "GameMaps"),
        ("GemCategoryParam", "GemCategories"),
        ("GemDropDopingParam", "GemDropDoping"),
        ("GemDropModifyParam", "GemDropModifications"),
        ("GemeffectParam", "GemEffects"),
        ("GemGenParam", "GemsAndRunes"),
        ("HolygrailExParam", "RitualChalices"),
        ("ItemLotLvdepParam", "ItemLotsWithScaling"),
        ("MenuPropertyLayoutParam", "MenuPropertyLayouts"),
        ("MenuPropertySpecParam", "MenuPropertySpecs"),
        ("MenuValueTableSpecParam", "MenuValueTableSpecs"),
        ("ProtectorGenParam", "ArmorGenerators"),
        ("ResidentVFXParam", "ResidentVFX"),
        ("ReturnPointParam", "ReturnPoints"),
        ("RitualRequiredMatParam", "RitualMaterials"),
        ("WeaponGenParam", "WeaponGenerators"),
        ("WindParam", "Wind"),
    )

    # Maps attribute names to game types. Also defines display order.
    PARAM_TYPES: tp.ClassVar = {
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
        "Faces": FaceParam,  # TODO: different for BB? FaceGenerators?
        "Dialogue": DialogueParam,
        "MenuColors": MenuColorsParam,
        "SpecialEffectVisuals": SpecialEffectVisualParam,
        "GrowthCurves": GrowthCurveParam,

        # TODO: Create param types for these new BB params. Some are currently disabled.
        "ActionButtons": None,
        "AISounds": None,
        # "CharacterCreationMenuItems": None,
        # "CharacterCreationMenuTop": None,
        "Decals": None,
        "DungeonFeatures": None,
        # "DungeonSubFeatureLots": None,
        "FaceGenerators": None,
        "FaceRanges": None,
        "GameMaps": None,
        "GemCategories": None,
        "GemDropDoping": None,
        "GemDropModifications": None,
        "GemEffects": None,
        "GemsAndRunes": None,
        "RitualChalices": None,
        # "ItemLotsWithScaling": None,
        # "MenuPropertyLayouts": None,
        # "MenuPropertySpecs": None,
        # "MenuValueTableSpecs": None,
        # "ArmorGenerators": None,
        "ResidentVFX": None,
        "ReturnPoints": None,
        "RitualMaterials": None,
        "WeaponGenerators": None,
        "Wind": None,
    }

    dcx_type = BLOODBORNE.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=lambda: BinderVersion4Info(False, False, True, 0))

    # TODO: Some of these may be Dark Souls junk (like Rings).
    ActionButtons = param_property("ActionButtons")  # type: Param
    AI = param_property("AI")  # type: Param
    AISounds = param_property("AISounds")  # type: Param
    Armor = param_property("Armor")  # type: Param
    ArmorGenerators = param_property("ArmorGenerators")  # type: Param
    ArmorUpgrades = param_property("ArmorUpgrades")  # type: Param
    Bosses = param_property("Bosses")  # type: Param
    Bullets = param_property("Bullets")  # type: Param
    Cameras = param_property("Cameras")  # type: Param
    Characters = param_property("Characters")  # type: Param
    CharacterCreationMenuItems = param_property("CharacterCreationMenuItems")  # type: Param
    CharacterCreationMenuTop = param_property("CharacterCreationMenuTop")  # type: Param
    Decals = param_property("Decals")  # type: Param
    Dialogue = param_property("Dialogue")  # type: Param
    DungeonFeatures = param_property("DungeonFeatures")  # type: Param
    DungeonSubFeatureLots = param_property("DungeonSubFeatureLots")  # type: Param
    FaceGenerators = param_property("FaceGenerators")  # type: Param
    FaceRanges = param_property("FaceRanges")  # type: Param
    Faces = param_property("Faces")  # type: Param
    GameMaps = param_property("GameMaps")  # type: Param
    GemCategories = param_property("GemCategories")  # type: Param
    GemDropDoping = param_property("GemDropDoping")  # type: Param
    GemDropModifications = param_property("GemDropModifications")  # type: Param
    GemEffects = param_property("GemEffects")  # type: Param
    GemsAndRunes = param_property("GemsAndRunes")  # type: Param
    Goods = param_property("Goods")  # type: Param
    GrowthCurves = param_property("GrowthCurves")  # type: Param
    ItemLots = param_property("ItemLots")  # type: Param
    ItemLotsWithScaling = param_property("ItemLotsWithScaling")  # type: Param
    NonPlayerAttacks = param_property("NonPlayerAttacks")  # type: Param
    NonPlayerBehaviors = param_property("NonPlayerBehaviors")  # type: Param
    MenuColors = param_property("MenuColors")  # type: Param
    MenuPropertyLayouts = param_property("MenuPropertyLayouts")  # type: Param
    MenuPropertySpecs = param_property("MenuPropertySpecs")  # type: Param
    MenuValueTableSpecs = param_property("MenuValueTableSpecs")  # type: Param
    Movement = param_property("Movement")  # type: Param
    Objects = param_property("Objects")  # type: Param
    ObjectActivations = param_property("ObjectActivations")  # type: Param
    Players = param_property("Players")  # type: Param
    PlayerAttacks = param_property("PlayerAttacks")  # type: Param
    PlayerBehaviors = param_property("PlayerBehaviors")  # type: Param
    ResidentVFX = param_property("ResidentVFX")  # type: Param  # TODO: possibly `PlayerVFX`
    ReturnPoints = param_property("ReturnPoints")  # type: Param  # TODO: ?
    # Accessories: Param
    RitualChalices = param_property("RitualChalices")  # type: Param
    RitualMaterials = param_property("RitualMaterials")  # type: Param
    Shops = param_property("Shops")  # type: Param
    SpecialEffects = param_property("SpecialEffects")  # type: Param
    SpecialEffectVisuals = param_property("SpecialEffectVisuals")  # type: Param
    Spells = param_property("Spells")  # type: Param
    Terrains = param_property("Terrains")  # type: Param
    Throws = param_property("Throws")  # type: Param
    UpgradeMaterials = param_property("UpgradeMaterials")  # type: Param
    Weapons = param_property("Weapons")  # type: Param
    WeaponGenerators = param_property("WeaponGenerators")  # type: Param
    WeaponUpgrades = param_property("WeaponUpgrades")  # type: Param
    Wind = param_property("Wind")  # type: Param

    def rename_entries_from_text(self, text: MSGDirectory, param_nickname=None):
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
                    f"Invalid item type: {param_nickname}. Must be 'Weapons', 'Armor', 'Goods', or 'GemsAndRunes'."
                )
        for item_type_check, param, text_dict in zip(
            ("weapon", "armor", "good", "gemsandrune"),
            (self.Weapons, self.Armor, self.Goods, self.GemsAndRunes),
            (text.WeaponNames, text.ArmorNames, text.GoodNames, text.BloodGemNames),
        ):
            if not param_nickname or param_nickname == item_type_check:
                for param_id, param_row in param.items():
                    if param_id in text_dict and text_dict[param_id].strip(" *"):
                        param_row.name = text_dict[param_id]
