from __future__ import annotations

__all__ = ["Param", "GameParamBND"]

import typing as tp

from soulstruct.containers.bnd import BND4
from soulstruct.games import BLOODBORNE
from soulstruct.game_types import *
from soulstruct.base.params.game_param_bnd import GameParamBND as _BaseGameParamBND
from soulstruct.base.params.param import Param as _BaseParam

from .paramdef import ParamDefBND, GET_BUNDLED_PARAMDEF

if tp.TYPE_CHECKING:
    from ..text.msg_directory import MSGDirectory


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
        "GemGenParam": "GemsAndRunes",
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
    GemsAndRunes: Param
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
        for item_type_check, param_table, text_dict in zip(
            ("weapon", "armor", "good", "gemsandrune"),
            (self.Weapons, self.Armor, self.Goods, self.GemsAndRunes),
            (text.WeaponNames, text.ArmorNames, text.GoodNames, text.BloodGemNames),
        ):
            if not param_nickname or param_nickname == item_type_check:
                for param_id, param_entry in param_table.items():
                    if param_id in text_dict and text_dict[param_id].strip(" *"):
                        param_entry.name = text_dict[param_id]
