from __future__ import annotations

__all__ = [
    "GoodReference",
]

import typing as tp

from soulstruct.darksouls1r.params.enums import *
from soulstruct.darksouls1r.game_types.param_types import *
from soulstruct.base.params.param_row import DynamicParamField


if tp.TYPE_CHECKING:
    from .EQUIP_PARAM_GOODS_ST import EQUIP_PARAM_GOODS_ST


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
