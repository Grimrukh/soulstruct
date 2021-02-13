"""GameParam types that refer to entry IDs in a certain game parameter table."""

__all__ = [
    "BaseParam",
    "BaseGameParam",
    "BaseItemParam",
    "BaseLightingParam",

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
    "FaceParam",
    "GoodParam",
    "GrowthCurveParam",
    "ItemLotParam",
    "KnockbackParam",
    "MenuColorsParam",
    "MovementParam",
    "ObjActParam",
    "ObjectParam",
    "PlayerParam",
    "RingParam",
    "RuneParam",
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
    "AmbientLightParam",
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
    "RingTyping",
    "RuneTyping",
    "SpecialEffectTyping",
    "SpellTyping",
    "TerrainTyping",
    "UpgradeMaterialTyping",
    "WeaponTyping",
    "WeaponUpgradeTyping",
]

from enum import IntEnum
from typing import Union

from soulstruct.base.events.emevd import instructions as instr
from soulstruct.base.events.emevd.enums import ItemType
from soulstruct.base.events.emevd.utils import get_value_test
from soulstruct.game_types.basic_types import GameObject


class BaseParam(GameObject, IntEnum):
    """Base class for IDs of param entries."""

    @classmethod
    def get_param_nickname(cls):
        raise NotImplementedError


class BaseGameParam(BaseParam):
    """Base class for IDs of GameParam entries."""

    @classmethod
    def get_param_nickname(cls):
        raise NotImplementedError


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

    You can call an instance of any Item to test if the player currently has that item (not in Bottomless Box).
    """

    def __call__(self, negate=False, condition=None):
        value = self if isinstance(self, (int, float, tuple)) else self.value
        return get_value_test(
            value=value,
            negate=negate,
            condition=condition,
            if_true_func=lambda c, i: getattr(instr, f"IfPlayerHas{self.item_enum.name}")(c, i, False),
            if_false_func=lambda c, i: getattr(instr, f"IfPlayerDoesNotHave{self.item_enum.name}")(c, i, False),
        )

    @property
    def item_enum(self) -> ItemType:
        raise NotImplementedError("You must use a subclass of `Item`.")

    @classmethod
    def get_param_nickname(cls):
        raise NotImplementedError


class BaseLightingParam(BaseParam):
    """Base class for DrawParam types."""
    @classmethod
    def get_param_nickname(cls):
        raise NotImplementedError


class AIParam(BaseGameParam):
    """AI entry."""
    @classmethod
    def get_param_nickname(cls):
        return "AI"


class ArmorParam(BaseItemParam):
    """Armor entry."""
    @property
    def item_enum(self):
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


class FaceParam(BaseGameParam):
    """Face entry."""
    @classmethod
    def get_param_nickname(cls):
        return "Faces"


class GoodParam(BaseItemParam):
    """Good entry."""
    @property
    def item_enum(self):
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


class RingParam(BaseItemParam):
    """Ring entry."""
    @property
    def item_enum(self):
        return ItemType.Ring

    @classmethod
    def get_param_nickname(cls):
        return "Rings"


RuneParam = RingParam


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
    @property
    def item_enum(self):
        return ItemType.Weapon

    @classmethod
    def get_param_nickname(cls):
        return "Weapons"


class WeaponUpgradeParam(BaseGameParam):
    """WeaponUpgrade entry."""
    @classmethod
    def get_param_nickname(cls):
        return "WeaponUpgrades"


class FogParam(BaseLightingParam):
    @classmethod
    def get_param_nickname(cls):
        return "Fog"


class AmbientLightParam(BaseLightingParam):
    @classmethod
    def get_param_nickname(cls):
        return "AmbientLight"


class ScatteredLightParam(BaseLightingParam):
    @classmethod
    def get_param_nickname(cls):
        return "ScatteredLight"


class PointLightParam(BaseLightingParam):
    @classmethod
    def get_param_nickname(cls):
        return "PointLights"


class LensFlareParam(BaseLightingParam):
    @classmethod
    def get_param_nickname(cls):
        return "LensFlares"


class LensFlareSourceParam(BaseLightingParam):
    @classmethod
    def get_param_nickname(cls):
        return "LensFlareSources"


class DepthOfFieldParam(BaseLightingParam):
    @classmethod
    def get_param_nickname(cls):
        return "DepthOfField"


class ToneMappingParam(BaseLightingParam):
    @classmethod
    def get_param_nickname(cls):
        return "ToneMapping"


class ShadowParam(BaseLightingParam):
    @classmethod
    def get_param_nickname(cls):
        return "Shadows"


class ToneCorrectionParam(BaseLightingParam):
    @classmethod
    def get_param_nickname(cls):
        return "ToneCorrection"


AITyping = Union[AIParam, int]
AttackTyping = Union[AttackParam, int]
BehaviorTyping = Union[BehaviorParam, int]
BulletTyping = Union[BulletParam, int]
DialogueTyping = Union[DialogueParam, int]
ItemTyping = Union[BaseItemParam, int]
WeaponTyping = Union[WeaponParam, int]
ArmorTyping = Union[ArmorParam, int]
RingTyping = Union[RingParam, int]
RuneTyping = Union[RuneParam, int]
GoodTyping = Union[GoodParam, int]
CameraTyping = Union[CameraParam, int]
FaceTyping = Union[FaceParam, int]
ItemLotTyping = Union[ItemLotParam, int]
KnockbackTyping = Union[KnockbackParam, int]
SpecialEffectTyping = Union[SpecialEffectParam, int]
SpellTyping = Union[SpellParam, int]
TerrainTyping = Union[TerrainParam, int]
UpgradeMaterialTyping = Union[UpgradeMaterialParam, int]
WeaponUpgradeTyping = Union[WeaponUpgradeParam, int]
ArmorUpgradeTyping = Union[ArmorUpgradeParam, int]
