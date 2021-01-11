from __future__ import annotations

__all__ = ["Param", "GameParamBND"]

from soulstruct.bnd import BND4
from soulstruct.games import BLOODBORNE
from soulstruct.game_types import *
from soulstruct.params.base.param import Param as _BaseParam
from soulstruct.params.base.game_param_bnd import GameParamBND as _BaseGameParamBND

from .paramdef import ParamDefBND, GET_BUNDLED_PARAMDEF


class Param(_BaseParam):
    GET_BUNDLED_PARAMDEF = staticmethod(GET_BUNDLED_PARAMDEF)


class GameParamBND(_BaseGameParamBND, BND4):
    Param = Param
    ParamDefBND = ParamDefBND

    PARAM_NICKNAMES = {
        "AtkParam_Npc": "NonPlayerAttacks",
        "AtkParam_Pc": "PlayerAttacks",
        "BehaviorParam": "NonPlayerBehaviors",
        "BehaviorParam_PC": "PlayerBehaviors",

        # TODO: Placing all undocumented new tables here for now.
        "ActionButtonParam": "ActionButtons",
        "AiSoundParam": "AISounds",
        "CharMakeMenuListItemParam": "CharacterCreationMenuItems",
        "CharMakeMenuTopParam": "CharacterCreationMenuTop",
        "DecalParam": "Decals",
        "DungeonFeatureParam": "DungeonFeatures",
        "DungeonSubFeatLotParam": "DungeonSubFeatureLots",
        "FaceGenParam": "FaceGenerators",
        "FaceParam": "Faces",
        "FaceRangeParam": "FaceRanges",
        "GameMapParam": "GameMaps",
        "GemCategoryParam": "GemCategories",
        "GemDropDopingParam": "GemDropDoping",
        "GemDropModifyParam": "GemDropModifications",
        "GemeffectParam": "GemEffects",
        "GemGenParam": "GemGenerators",
        "HolygrailExParam": "RitualChalices",
        "ItemLotLvdepParam": "ItemLotsWithScaling",
        "MenuPropertyLayoutParam": "MenuPropertyLayouts",
        "MenuPropertySpecParam": "MenuPropertySpecs",
        "MenuValueTableSpecParam": "MenuValueTableSpecs",
        "ProtectorGenParam": "ArmorGenerators",
        "ResidentVFXParam": "ResidentVFX",
        "ReturnPointParam": "ReturnPoints",
        "RitualRequiredMatParam": "RitualMaterials",
        "WeaponGenParam": "WeaponGenerators",
        "WindParam": "Wind",
    }

    # Maps attribute names to game types. Also defines display order.
    PARAM_TYPES = {
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
        "Rings": RingParam,
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
        "Faces": FaceParam,
        "Dialogue": DialogueParam,
        "MenuColors": MenuColorsParam,
        "SpecialEffectVisuals": SpecialEffectVisualParam,
        "GrowthCurves": GrowthCurveParam,
    }

    # TODO: Some of these may be Dark Souls junk (like Rings).
    ActionButtons: Param
    AI: Param
    AISounds: Param
    Armor: Param
    ArmorGenerators: Param
    ArmorUpgrades: Param
    Bosses: Param
    Bullets: Param
    Cameras: Param
    Characters: Param
    CharacterCreationMenuItems: Param
    CharacterCreationMenuTop: Param
    Decals: Param
    Dialogue: Param
    DungeonFeatures: Param
    DungeonSubFeatureLots: Param
    FaceGenerators: Param
    FaceRanges: Param
    Faces: Param
    GameMaps: Param
    GemCategories: Param
    GemDropDoping: Param
    GemDropModifications: Param
    GemEffects: Param
    GemGenerators: Param
    Goods: Param
    GrowthCurves: Param
    ItemLots: Param
    ItemLotsWithScaling: Param
    NonPlayerAttacks: Param
    NonPlayerBehaviors: Param
    MenuColors: Param
    MenuPropertyLayouts: Param
    MenuPropertySpecs: Param
    MenuValueTableSpecs: Param
    Movement: Param
    Objects: Param
    ObjectActivations: Param
    Players: Param
    PlayerAttacks: Param
    PlayerBehaviors: Param
    ResidentVFX: Param  # TODO: possibly `PlayerVFX`
    ReturnPoints: Param  # TODO: ?
    # Rings: Param
    RitualChalices: Param
    RitualMaterials: Param
    Shops: Param
    SpecialEffects: Param
    SpecialEffectVisuals: Param
    Spells: Param
    Terrains: Param
    Throws: Param
    UpgradeMaterials: Param
    Weapons: Param
    WeaponGenerators: Param
    WeaponUpgrades: Param
    Wind: Param

    def __init__(self, game_param_bnd_source=None, paramdef_bnd=None):
        super().__init__(game_param_bnd_source, paramdef_bnd=BLOODBORNE if paramdef_bnd is None else paramdef_bnd)
