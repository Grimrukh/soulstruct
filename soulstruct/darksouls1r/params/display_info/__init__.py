"""Imports all names from all param categories (loosely sorted into scripts here).

Identical to PTDE display info and just imports that, with the exception of Weapons.
"""
from __future__ import annotations

# noinspection PyUnresolvedReferences
from soulstruct.darksouls1ptde.params.display_info import *
from .items import EQUIP_PARAM_WEAPON_ST


def get_param_info(param_name: str) -> dict:
    try:
        return globals()[param_name]
    except KeyError:
        raise KeyError(f"Could not find Param info for {param_name}.")


def get_param_info_field(param_name: str, field_name: str) -> FieldDisplayInfo:
    param_info = get_param_info(param_name)
    field_hits = [field for field in param_info["fields"] if field.name == field_name]
    if not field_hits:
        raise ValueError(f"Could not find field {field_name} in param {param_name}.")
    return field_hits[0]
