from __future__ import annotations

__all__ = [
    "ShopReference",
    "MagicReference",
    "ItemLotReference",
    "GoodReference",
    "BehaviorReference",
    "ObjActSuccessCondition",
]

import typing as tp

from soulstruct.darksouls1ptde.params.enums import *
from soulstruct.darksouls1ptde.game_types.param_types import *
from soulstruct.base.params.utils import DynamicParamField


if tp.TYPE_CHECKING:
    from .BEHAVIOR_PARAM_ST import BEHAVIOR_PARAM_ST
    from .EQUIP_PARAM_GOODS_ST import EQUIP_PARAM_GOODS_ST
    from .ITEMLOT_PARAM_ST import ITEMLOT_PARAM_ST
    from .MAGIC_PARAM_ST import MAGIC_PARAM_ST
    from .OBJ_ACT_PARAM_ST import OBJ_ACT_PARAM_ST
    from .SHOP_LINEUP_PARAM import SHOP_LINEUP_PARAM


class ShopReference(DynamicParamField):

    POSSIBLE_TYPES = {WeaponParam, ArmorParam, AccessoryParam, GoodParam, SpellParam}

    def __call__(self, data: SHOP_LINEUP_PARAM):
        item_type = data.ItemType
        if item_type == SHOP_LINEUP_EQUIPTYPE.Weapon:
            return WeaponParam, "Weapon", "Weapon to be listed in shop menu."
        if item_type == SHOP_LINEUP_EQUIPTYPE.Armor:
            return ArmorParam, "Armor", "Armor to be listed in shop menu."
        if item_type == SHOP_LINEUP_EQUIPTYPE.Ring:
            return AccessoryParam, "Ring", "Ring to be listed in shop menu."
        if item_type == SHOP_LINEUP_EQUIPTYPE.Good:
            return GoodParam, "Good", "Good to be listed in shop menu."
        if item_type == SHOP_LINEUP_EQUIPTYPE.Spell:
            return SpellParam, "Spell", "Spell to be listed in shop menu."
        else:
            return (
                int,
                "Unknown",
                f"Item to be listed in shop/attunement menu (unknown item type {item_type}).",
            )


class MagicReference(DynamicParamField):

    POSSIBLE_TYPES = {BulletParam, SpecialEffectParam}

    def __call__(self, data: MAGIC_PARAM_ST):
        if data.ReferenceType == BEHAVIOR_REF_TYPE.Default:
            return (
                int,
                "Null",
                "This value should be -1 when 'Default' reference type is selected.",
            )
        elif data.ReferenceType == BEHAVIOR_REF_TYPE.Bullet:
            return (
                BulletParam,
                "Bullet",
                "Bullet triggered by casting spell (which may simply be targeted at self).",
            )
        elif data.ReferenceType == BEHAVIOR_REF_TYPE.SpecialEffect:
            return (
                SpecialEffectParam,
                "SpecialEffect",
                "Special effect triggered (on self) by casting spell.",
            )
        else:
            return (
                int,
                "Unknown",
                "Could not determine spell reference type (usually Bullet or SpecialEffect).",
            )


class ItemLotReference(DynamicParamField):
    
    POSSIBLE_TYPES = {WeaponParam, ArmorParam, AccessoryParam, GoodParam}
    
    index: int
    
    def __init__(self, index: int):
        self.index = index
    
    def __call__(self, data: ITEMLOT_PARAM_ST):
        try:
            item_type = getattr(data, f"Item{self.index}Category")
        except AttributeError:
            raise ValueError(f"Invalid `ItemLotReference` index: {self.index}")
        
        if item_type == ITEMLOT_ITEMCATEGORY.Weapon:
            return (
                WeaponParam,
                "Weapon",
                f"Item slot {self.index} (Weapon).",
            )
        elif item_type == ITEMLOT_ITEMCATEGORY.Armor:
            return (
                ArmorParam,
                "Armor",
                f"Item slot {self.index} (Armor).",
            )
        elif item_type == ITEMLOT_ITEMCATEGORY.Good:
            return (
                GoodParam,
                "Good",
                f"Item slot {self.index} (Good).",
            )
        elif item_type == ITEMLOT_ITEMCATEGORY.Ring:
            return (
                AccessoryParam,
                "Ring",
                f"Item slot {self.index} (Ring).",
            )
        else:
            return (
                int,
                "Unknown",
                f"Item slot {self.index} (unknown item type {item_type}).",
            )


class GoodReference(DynamicParamField):

    POSSIBLE_TYPES = {BulletParam, SpecialEffectParam}

    def __call__(self, data: EQUIP_PARAM_GOODS_ST):
        if data.ReferenceType == BEHAVIOR_REF_TYPE.Default:
            return (
                int,
                "Null",
                "This value should be -1 when 'Default' reference type is selected.",
            )
        elif data.ReferenceType == BEHAVIOR_REF_TYPE.Bullet:
            return (
                BulletParam,
                "Bullet",
                "Bullet triggered by using good (which may simply be targeted at self).",
            )
        elif data.ReferenceType == BEHAVIOR_REF_TYPE.SpecialEffect:
            return (
                SpecialEffectParam,
                "SpecialEffect",
                "Special effect triggered (on self) by using good.",
            )
        else:
            return (
                int,
                "Unknown",
                "Could not determine reference ID type (usually Bullet or SpecialEffect).",
            )


class BehaviorReference(DynamicParamField):

    POSSIBLE_TYPES = {AttackParam, BulletParam, SpecialEffectParam}

    def __call__(self, data: BEHAVIOR_PARAM_ST):
        if data.ReferenceType == BEHAVIOR_REF_TYPE.Default:
            return (
                AttackParam,
                "Attack",
                "Attack ID triggered by behavior.",
            )
        elif data.ReferenceType == BEHAVIOR_REF_TYPE.Bullet:
            return (
                BulletParam,
                "Bullet",
                "Bullet ID triggered by behavior.",
            )
        elif data.ReferenceType == BEHAVIOR_REF_TYPE.SpecialEffect:
            return (
                SpecialEffectParam,
                "SpecialEffect",
                "Special Effect ID triggered by behavior. (Never used; may not work.)",
            )
        else:
            return (
                int,
                "Unknown",
                "Could not determine behavior reference ID type (usually Attack or Bullet).",
            )


class ObjActSuccessCondition(DynamicParamField):

    POSSIBLE_TYPES = {GoodParam, SpecialEffectParam}

    index: int

    def __init__(self, index: int):
        self.index = index

    def __call__(self, data: OBJ_ACT_PARAM_ST):
        if self.index == 1:
            condition_type = data.SuccessCondition1Type
        elif self.index == 2:
            condition_type = data.SuccessCondition2Type
        else:
            raise ValueError(f"Invalid `ObjActSuccessCondition` index: {self.index}")

        if condition_type == OBJACT_SP_QUALIFIED_TYPE.NoCondition:
            return int, "Null", "No condition type selected.",
        elif condition_type == OBJACT_SP_QUALIFIED_TYPE.HasGood:
            return (
                GoodParam,
                "Good",
                "Condition: ObjAct will succeed if user has this good in their inventory.",
            )
        elif condition_type == OBJACT_SP_QUALIFIED_TYPE.HasSpecialEffect:
            return (
                SpecialEffectParam,
                "SpecialEffect",
                "Condition: ObjAct will succeed if user has this special effect.",
            )
        else:
            return (
                int,
                "Unknown",
                "Could not determine success condition ID type (usually Good or SpecialEffect).",
            )
