"""GameParam types that refer to entry IDs in a certain game parameter table."""

__all__ = [
    "BaseParam",
    "BaseGameParam",
    "BaseItemParam",

    # OLD TYPES
    "AIParam",
    "ArmorParam",
    "ArmorUpgradeParam",
    "AttackParam",
    "BehaviorParam",
    "BossParam",
    "BulletParam",
    "CameraParam",
    "CharacterParam",
    "DialogueParam",
    "FaceGenParam",
    "GoodParam",
    "GrowthCurveParam",
    "ItemLotParam",
    "KnockbackParam",
    "MenuColorsParam",
    "MovementParam",
    "ObjActParam",
    "ObjectParam",
    "PlayerParam",
    "AccessoryParam",
    "ShopParam",
    "SpecialEffectParam",
    "SpecialEffectVisualParam",
    "SpellParam",
    "TerrainParam",
    "ThrowParam",
    "UpgradeMaterialParam",
    "WeaponParam",
    "WeaponUpgradeParam",

    # NEW IN BLOODBORNE
    "ActionButtonParam",
    "AISoundParam",
    "CharacterCreationMenuItemParam",
    "CharacterCreationMenuTopParam",
    "DecalParam",
    "DungeonFeatureParam",
    "DungeonSubFeatureLotParam",
    "FaceParam",
    "FaceRangeParam",
    "GameMapParam",
    "GemCategoryParam",
    "GemDropDopingParam",
    "GemDropModificationParam",
    "GemEffectParam",
    "GemsAndRunesParam",
    "RitualChaliceParam",
    "ItemLotWithScalingParam",
    "MenuPropertyLayoutParam",
    "MenuPropertySpecParam",
    "MenuValueTableSpecParam",
    "ArmorGeneratorParam",
    "ResidentVFXParam",
    "ReturnPointParam",
    "RitualMaterialsParam",
    "WeaponGeneratorParam",
    "WindParam",

    "AITyping",
    "ArmorTyping",
    "ArmorUpgradeTyping",
    "AttackTyping",
    "BehaviorTyping",
    "BulletTyping",
    "CameraTyping",
    "DialogueTyping",
    "FaceGenTyping",
    "GoodTyping",
    "ItemTyping",
    "ItemLotTyping",
    "KnockbackTyping",
    "AccessoryTyping",
    "SpecialEffectTyping",
    "SpellTyping",
    "TerrainTyping",
    "UpgradeMaterialTyping",
    "WeaponTyping",
    "WeaponUpgradeTyping",

    "ActionButtonTyping",
    "AISoundTyping",
    "CharacterCreationMenuItemTyping",
    "CharacterCreationMenuTopTyping",
    "DecalTyping",
    "DungeonFeatureTyping",
    "DungeonSubFeatureLotTyping",
    "FaceTyping",
    "FaceRangeTyping",
    "GameMapTyping",
    "GemCategoryTyping",
    "GemDropDopingTyping",
    "GemDropModificationTyping",
    "GemEffectTyping",
    "GemsAndRunesTyping",
    "RitualChaliceTyping",
    "ItemLotWithScalingTyping",
    "MenuPropertyLayoutTyping",
    "MenuPropertySpecTyping",
    "MenuValueTableSpecTyping",
    "ArmorGeneratorTyping",
    "ResidentVFXTyping",
    "ReturnPointTyping",
    "RitualMaterialsTyping",
    "WeaponGeneratorTyping",
    "WindTyping",
]

import typing as tp

from soulstruct.base.game_types import BaseParam, BaseGameParam


class BaseItemParam(BaseGameParam):
    """Base class for items.

    Unfortunately, the naming of item types is inconsistent. There are four types of items, which are internally called
    'Weapon', 'Protector', 'Accessory', and 'Good'. (Note that the 'Accessory' type is used for Runes in Bloodborne.)

    The name 'Equipment' is sometimes used to describe this general item type, and in the internal text of Dark Souls
    Remastered, the name 'Item' is used to refer to the type 'Good' (which is probably what most people think of when
    they read the name 'Item').

    In Soulstruct, the name 'Item' exclusively refers to this base type (i.e. anything that can appear in your in-game
    inventory) and the name 'Good' is used for the main item type (i.e. things you do not wear). This is consistent with
    terms such as ItemLot. The name 'Equipment' is not used. I have also renamed 'Protector' to 'Armor', and 'Accessory'
    to 'Ring' (with an alias 'Rune').

    You can call an instance of any Item to test if the player currently has that item (excluding storage).
    """

    @classmethod
    def get_event_arg_fmt(cls):
        return "I"

    @classmethod
    def get_item_enum(cls):
        raise NotImplementedError("You must use a subclass of `BaseItemParam`.")

    @classmethod
    def get_param_nickname(cls):
        raise NotImplementedError


# region Game Params


class ActionButtonParam(BaseGameParam):
    """Entry collecting information about a button prompt."""
    @classmethod
    def get_param_nickname(cls):
        return "ActionButtonPrompts"


class AIParam(BaseGameParam):
    """AI entry."""
    @classmethod
    def get_param_nickname(cls):
        return "AI"


class AISoundParam(BaseGameParam):
    """AI 'sound' entry."""
    @classmethod
    def get_param_nickname(cls):
        return "AISounds"


class ArmorParam(BaseItemParam):
    """Armor entry."""

    @classmethod
    def get_item_enum(cls):
        from ..events.enums import ItemType
        return ItemType.Armor

    @classmethod
    def get_param_nickname(cls):
        return "Armor"


class ArmorUpgradeParam(BaseGameParam):
    """ArmorUpgrade entry."""
    @classmethod
    def get_param_nickname(cls):
        return "ArmorUpgrades"


class AttackParam(BaseGameParam):
    """Attack entry."""
    @classmethod
    def get_param_nickname(cls):
        raise ValueError("Param nickname for `Attack` could be 'PlayerAttacks' or 'NonPlayerAttacks'.")


class BehaviorParam(BaseGameParam):
    """Behavior entry."""
    @classmethod
    def get_param_nickname(cls):
        raise ValueError("Param nickname for `Behavior` could be 'PlayerBehaviors' or 'NonPlayerBehaviors'.")


class BossParam(BaseGameParam):
    """Boss (or 'GameArea') param entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Bosses"


class BulletParam(BaseGameParam):
    """Bullet entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Bullets"


class CameraParam(BaseGameParam):
    """Camera entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Cameras"


class CharacterParam(BaseGameParam):
    """Character entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Characters"


class DecalParam(BaseGameParam):
    """Decal (e.g. blood spatter on player) entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Decals"


class DialogueParam(BaseGameParam):
    """Dialogue entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Dialogue"


class FaceParam(BaseGameParam):
    """Face entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Faces"


class FaceGenParam(BaseGameParam):
    """Face generator entry."""
    @classmethod
    def get_param_nickname(cls):
        return "FaceGenerators"


class GoodParam(BaseItemParam):
    """Good entry."""

    @classmethod
    def get_item_enum(cls):
        from ..events.enums import ItemType
        return ItemType.Good

    @classmethod
    def get_param_nickname(cls):
        return "Goods"


class GrowthCurveParam(BaseGameParam):
    """Growth curve entry."""
    @classmethod
    def get_param_nickname(cls):
        return "GrowthCurves"


class ItemLotParam(BaseGameParam):
    """ItemLot entry."""
    @classmethod
    def get_event_arg_fmt(cls) -> str:
        return "i"

    @classmethod
    def get_param_nickname(cls):
        return "ItemLots"


class KnockbackParam(BaseGameParam):
    """Knockback entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Knockbacks"


class MenuColorsParam(BaseGameParam):
    """MenuColors entry."""
    @classmethod
    def get_param_nickname(cls):
        return "MenuColors"


class MovementParam(BaseGameParam):
    """Movement entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Movement"


class ObjActParam(BaseGameParam):
    """ObjAct entry."""
    @classmethod
    def get_param_nickname(cls):
        return "ObjectActivations"


class ObjectParam(BaseGameParam):
    """Object param. Not to be confused with `ObjActParam`."""
    @classmethod
    def get_param_nickname(cls):
        return "Objects"


class PlayerParam(BaseGameParam):
    """Player entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Players"


class AccessoryParam(BaseItemParam):
    """Accessory entry."""

    @classmethod
    def get_item_enum(cls):
        from ..events.enums import ItemType
        return ItemType.GemOrRune

    @classmethod
    def get_param_nickname(cls):
        return "GemsAndRunes"


class ShopParam(BaseGameParam):
    """Shop entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Shops"


class SpecialEffectParam(BaseGameParam):
    """SpecialEffect entry."""
    @classmethod
    def get_param_nickname(cls):
        return "SpecialEffects"


class SpecialEffectVisualParam(BaseGameParam):
    """SpecialEffectVisuals entry."""
    @classmethod
    def get_param_nickname(cls):
        return "SpecialEffectVisuals"


class SpellParam(BaseGameParam):
    """Spell entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Spells"


class TerrainParam(BaseGameParam):
    """Terrain entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Terrains"


class ThrowParam(BaseGameParam):
    """Throw entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Throws"


class UpgradeMaterialParam(BaseGameParam):
    """UpgradeMaterial entry."""
    @classmethod
    def get_param_nickname(cls):
        return "UpgradeMaterials"


class WeaponParam(BaseItemParam):
    """Weapon entry."""

    @classmethod
    def get_item_enum(cls):
        from ..events.enums import ItemType
        return ItemType.Weapon

    @classmethod
    def get_param_nickname(cls):
        return "Weapons"


class WeaponUpgradeParam(BaseGameParam):
    """WeaponUpgrade entry."""
    @classmethod
    def get_param_nickname(cls):
        return "WeaponUpgrades"


# TODO: Sort these new BB params. alphabetically into the above.


class CharacterCreationMenuItemParam(BaseGameParam):
    """CharacterCreationMenuItems entry."""
    @classmethod
    def get_param_nickname(cls):
        return "CharacterCreationMenuItems"


class CharacterCreationMenuTopParam(BaseGameParam):
    """CharacterCreationMenuTop entry."""
    @classmethod
    def get_param_nickname(cls):
        return "CharacterCreationMenuTop"


class DungeonFeatureParam(BaseGameParam):
    """DungeonFeatures entry."""
    @classmethod
    def get_param_nickname(cls):
        return "DungeonFeatures"


class DungeonSubFeatureLotParam(BaseGameParam):
    """DungeonSubFeatureLots entry."""
    @classmethod
    def get_param_nickname(cls):
        return "DungeonSubFeatureLots"


class FaceRangeParam(BaseGameParam):
    """FaceRanges entry."""
    @classmethod
    def get_param_nickname(cls):
        return "FaceRanges"


class GameMapParam(BaseGameParam):
    """GameMaps entry."""
    @classmethod
    def get_param_nickname(cls):
        return "GameMaps"


class GemCategoryParam(BaseGameParam):
    """GemCategories entry."""
    @classmethod
    def get_param_nickname(cls):
        return "GemCategories"


class GemDropDopingParam(BaseGameParam):
    """GemDropDoping entry."""
    @classmethod
    def get_param_nickname(cls):
        return "GemDropDoping",


class GemDropModificationParam(BaseGameParam):
    """GemDropModifications entry."""
    @classmethod
    def get_param_nickname(cls):
        return "GemDropModifications"


class GemEffectParam(BaseGameParam):
    """GemEffects entry."""
    @classmethod
    def get_param_nickname(cls):
        return "GemEffects"


class GemsAndRunesParam(BaseGameParam):
    """GemsAndRunes entry."""
    @classmethod
    def get_param_nickname(cls):
        return "GemsAndRunes"


class RitualChaliceParam(BaseGameParam):
    """RitualChalices entry."""
    @classmethod
    def get_param_nickname(cls):
        return "RitualChalices"


class ItemLotWithScalingParam(BaseGameParam):
    """ItemLotsWithScaling entry."""
    @classmethod
    def get_param_nickname(cls):
        return "ItemLotsWithScaling"


class MenuPropertyLayoutParam(BaseGameParam):
    """MenuPropertyLayouts entry."""
    @classmethod
    def get_param_nickname(cls):
        return "MenuPropertyLayouts"


class MenuPropertySpecParam(BaseGameParam):
    """MenuPropertySpecs entry."""
    @classmethod
    def get_param_nickname(cls):
        return "MenuPropertySpecs"


class MenuValueTableSpecParam(BaseGameParam):
    """MenuValueTableSpecs entry."""
    @classmethod
    def get_param_nickname(cls):
        return "MenuValueTableSpecs"


class ArmorGeneratorParam(BaseGameParam):
    """ArmorGenerators entry."""
    @classmethod
    def get_param_nickname(cls):
        return "ArmorGenerators"


class ResidentVFXParam(BaseGameParam):
    """ResidentVFX entry."""
    @classmethod
    def get_param_nickname(cls):
        return "ResidentVFX"


class ReturnPointParam(BaseGameParam):
    """ReturnPoints entry."""
    @classmethod
    def get_param_nickname(cls):
        return "ReturnPoints"


class RitualMaterialsParam(BaseGameParam):
    """RitualMaterials entry."""
    @classmethod
    def get_param_nickname(cls):
        return "RitualMaterials"


class WeaponGeneratorParam(BaseGameParam):
    """WeaponGenerators entry."""
    @classmethod
    def get_param_nickname(cls):
        return "WeaponGenerators"


class WindParam(BaseGameParam):
    """Wind entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Wind",
# endregion


# OLD TYPES
AITyping = tp.Union[AIParam, int]
AttackTyping = tp.Union[AttackParam, int]
BehaviorTyping = tp.Union[BehaviorParam, int]
BulletTyping = tp.Union[BulletParam, int]
DialogueTyping = tp.Union[DialogueParam, int]
ItemTyping = tp.Union[BaseItemParam, int]
WeaponTyping = tp.Union[WeaponParam, int]
ArmorTyping = tp.Union[ArmorParam, int]
AccessoryTyping = tp.Union[AccessoryParam, int]
GoodTyping = tp.Union[GoodParam, int]
CameraTyping = tp.Union[CameraParam, int]
FaceGenTyping = tp.Union[FaceGenParam, int]
ItemLotTyping = tp.Union[ItemLotParam, int]
KnockbackTyping = tp.Union[KnockbackParam, int]
SpecialEffectTyping = tp.Union[SpecialEffectParam, int]
SpellTyping = tp.Union[SpellParam, int]
TerrainTyping = tp.Union[TerrainParam, int]
UpgradeMaterialTyping = tp.Union[UpgradeMaterialParam, int]
WeaponUpgradeTyping = tp.Union[WeaponUpgradeParam, int]
ArmorUpgradeTyping = tp.Union[ArmorUpgradeParam, int]

# NEW IN BLOODBORNE
ActionButtonTyping = tp.Union[ActionButtonParam, int]
AISoundTyping = tp.Union[AISoundParam, int]
CharacterCreationMenuItemTyping = tp.Union[CharacterCreationMenuItemParam, int]
CharacterCreationMenuTopTyping = tp.Union[CharacterCreationMenuTopParam, int]
DecalTyping = tp.Union[DecalParam, int]
DungeonFeatureTyping = tp.Union[DungeonFeatureParam, int]
DungeonSubFeatureLotTyping = tp.Union[DungeonSubFeatureLotParam, int]
FaceTyping = tp.Union[FaceParam, int]
FaceRangeTyping = tp.Union[FaceRangeParam, int]
GameMapTyping = tp.Union[GameMapParam, int]
GemCategoryTyping = tp.Union[GemCategoryParam, int]
GemDropDopingTyping = tp.Union[GemDropDopingParam, int]
GemDropModificationTyping = tp.Union[GemDropModificationParam, int]
GemEffectTyping = tp.Union[GemEffectParam, int]
GemsAndRunesTyping = tp.Union[GemsAndRunesParam, int]
RitualChaliceTyping = tp.Union[RitualChaliceParam, int]
ItemLotWithScalingTyping = tp.Union[ItemLotWithScalingParam, int]
MenuPropertyLayoutTyping = tp.Union[MenuPropertyLayoutParam, int]
MenuPropertySpecTyping = tp.Union[MenuPropertySpecParam, int]
MenuValueTableSpecTyping = tp.Union[MenuValueTableSpecParam, int]
ArmorGeneratorTyping = tp.Union[ArmorGeneratorParam, int]
ResidentVFXTyping = tp.Union[ResidentVFXParam, int]
ReturnPointTyping = tp.Union[ReturnPointParam, int]
RitualMaterialsTyping = tp.Union[RitualMaterialsParam, int]
WeaponGeneratorTyping = tp.Union[WeaponGeneratorParam, int]
WindTyping = tp.Union[WindParam, int]
