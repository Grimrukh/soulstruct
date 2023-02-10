"""Imports all names from all param categories (loosely sorted into scripts here)."""

from __future__ import annotations

import typing as tp

from .ai import *
from .attacks import *
from .behaviors import *
from .bullets import *
from .chalices import *
from .characters import *
from .effects import *
from .gems import *
from .items import *
from .lighting import *
from .misc import *
from .objects import *
from .shops import *
from .spells import *

if tp.TYPE_CHECKING:
    from soulstruct.base.params.utils import ParamFieldInfo


def get_param_info(param_name: str) -> dict:
    try:
        return globals()[param_name]
    except KeyError:
        raise KeyError(f"Could not find Param info for {param_name}.")


def get_param_info_field(param_name: str, field_name: str) -> ParamFieldInfo:
    param_info = globals()[param_name]
    field_hits = [field for field in param_info["fields"] if field.name == field_name]
    if not field_hits:
        raise ValueError(f"Could not find field {field_name} in param {param_name}.")
    return field_hits[0]
