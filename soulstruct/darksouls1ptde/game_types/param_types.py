"""GameParam types that refer to entry IDs in a certain game parameter table."""

__all__ = [
    "BaseParam",
    "BaseGameParam",
    "BaseItemParam",
    "BaseDrawParam",

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

    "FogParam",
    "BakedLightParam",
    "ScatteredLightParam",
    "PointLightParam",
    "LensFlareParam",
    "LensFlareSourceParam",
    "DepthOfFieldParam",
    "ToneMappingParam",
    "ToneCorrectionParam",
    "ShadowParam",

    "AITyping",
    "ArmorTyping",
    "ArmorUpgradeTyping",
    "AttackTyping",
    "BehaviorTyping",
    "BulletTyping",
    "CameraTyping",
    "DialogueTyping",
    "FaceTyping",
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


class BaseDrawParam(BaseParam):
    """Base class for DrawParam types."""
    @classmethod
    def get_param_nickname(cls):
        raise NotImplementedError


# region Game Params
class AIParam(BaseGameParam):
    """AI entry."""
    @classmethod
    def get_param_nickname(cls):
        return "AI"


class ArmorParam(BaseItemParam):
    """Armor entry."""

    @classmethod
    def get_item_enum(cls):
        from ..events.emevd.enums import ItemType
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


class DialogueParam(BaseGameParam):
    """Dialogue entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Dialogue"


class FaceGenParam(BaseGameParam):
    """Face entry."""
    @classmethod
    def get_param_nickname(cls):
        return "FaceGenerators"


class GoodParam(BaseItemParam):
    """Good entry."""

    @classmethod
    def get_item_enum(cls):
        from ..events.emevd.enums import ItemType
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
    def get_param_nickname(cls):
        return "ItemLots"


class KnockbackParam(BaseGameParam):
    """Knockback entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Knockback"


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
    """Ring entry."""

    @classmethod
    def get_item_enum(cls):
        from ..events.emevd.enums import ItemType
        return ItemType.Ring

    @classmethod
    def get_param_nickname(cls):
        return "Rings"


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
        from ..events.emevd.enums import ItemType
        return ItemType.Weapon

    @classmethod
    def get_param_nickname(cls):
        return "Weapons"


class WeaponUpgradeParam(BaseGameParam):
    """WeaponUpgrade entry."""
    @classmethod
    def get_param_nickname(cls):
        return "WeaponUpgrades"
# endregion


# region Draw Params
class FogParam(BaseDrawParam):
    @classmethod
    def get_param_nickname(cls):
        return "Fog"


class BakedLightParam(BaseDrawParam):
    @classmethod
    def get_param_nickname(cls):
        return "BakedLight"


class ScatteredLightParam(BaseDrawParam):
    @classmethod
    def get_param_nickname(cls):
        return "ScatteredLight"


class PointLightParam(BaseDrawParam):
    @classmethod
    def get_param_nickname(cls):
        return "PointLights"


class LensFlareParam(BaseDrawParam):
    @classmethod
    def get_param_nickname(cls):
        return "LensFlares"


class LensFlareSourceParam(BaseDrawParam):
    @classmethod
    def get_param_nickname(cls):
        return "LensFlareSources"


class DepthOfFieldParam(BaseDrawParam):
    @classmethod
    def get_param_nickname(cls):
        return "DepthOfField"


class ToneMappingParam(BaseDrawParam):
    @classmethod
    def get_param_nickname(cls):
        return "ToneMapping"


class ShadowParam(BaseDrawParam):
    @classmethod
    def get_param_nickname(cls):
        return "Shadows"


class ToneCorrectionParam(BaseDrawParam):
    @classmethod
    def get_param_nickname(cls):
        return "ToneCorrection"
# endregion


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
FaceTyping = tp.Union[FaceGenParam, int]
ItemLotTyping = tp.Union[ItemLotParam, int]
KnockbackTyping = tp.Union[KnockbackParam, int]
SpecialEffectTyping = tp.Union[SpecialEffectParam, int]
SpellTyping = tp.Union[SpellParam, int]
TerrainTyping = tp.Union[TerrainParam, int]
UpgradeMaterialTyping = tp.Union[UpgradeMaterialParam, int]
WeaponUpgradeTyping = tp.Union[WeaponUpgradeParam, int]
ArmorUpgradeTyping = tp.Union[ArmorUpgradeParam, int]
