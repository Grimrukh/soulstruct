from __future__ import annotations

__all__ = ["DOF_BANK"]

import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.params.utils import ParamFieldInfo, pad_field
from soulstruct.utilities.binary import *


DOF_BANK = {
    "param_type": "DOF_BANK",
    "file_name": "DofBank",
    "nickname": "DepthOfField",
    "fields": [
        ParamFieldInfo(
            "farDofBegin",
            "FarBlurStartDistance",
            True,
            float,
            "Distance (m) at which far depth of field blur begins.",
        ),
        ParamFieldInfo(
            "farDofEnd",
            "FarBlurEndDistance",
            True,
            float,
            "Distance (m) at which far depth of field blur ends (reaches maximum).",
        ),
        ParamFieldInfo(
            "farDofMul",
            "FarBlurMagnitude",
            True,
            int,
            "Amount of far depth of field blur applied between the start and end distances.",
        ),
        ParamFieldInfo("pad_0[3]", "Pad0", False, pad_field(3), "Null padding."),
        ParamFieldInfo(
            "nearDofBegin",
            "NearBlurStartDistance",
            True,
            float,
            "Distance (m) at which near depth of field blur begins (further away than end distance).",
        ),
        ParamFieldInfo(
            "nearDofEnd",
            "NearBlurEndDistance",
            True,
            float,
            "Distance (m) at which near depth of field blur ends (reaches maximum) (closer than start distance).",
        ),
        ParamFieldInfo(
            "nearDofMul",
            "NearBlurMagnitude",
            True,
            int,
            "Amount of near depth of field blur applied between start and end distances.",
        ),
        ParamFieldInfo("pad_1[3]", "Pad1", False, pad_field(3), "Null padding."),
        ParamFieldInfo(
            "dispersionSq",
            "BlurSquaredDispersion",
            True,
            float,
            "Squared dispersion of depth of field blur (greater value means more blur).",
        ),
    ],
}
