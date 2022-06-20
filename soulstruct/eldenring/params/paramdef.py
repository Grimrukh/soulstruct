"""Elden Ring Paramdefs can only be loaded from Paramdex XML files."""
from __future__ import annotations

__all__ = ["ParamDefField", "ParamDef", "ParamDefBND", "GET_BUNDLED_PARAMDEF"]

import logging
import typing as tp
from pathlib import Path

from soulstruct.base.params.paramdef import (
    ParamDefField as _BaseParamDefField,
    ParamDef as _BaseParamDef,
    ParamDefBND as _BaseParamDefBND,
)
from soulstruct.config import PARAMDEX_PATH
from soulstruct.games import EldenRingType
from soulstruct.utilities.files import PACKAGE_PATH

from .defaults import DEFAULTS

if tp.TYPE_CHECKING:
    from soulstruct.base.params.param import ParamRow

_LOGGER = logging.getLogger(__name__)
_BUNDLED = None


class ParamDefField(_BaseParamDefField):
    STRUCT = None

    def get_display_info(self, row: ParamRow):
        try:
            field_info = get_param_info_field(self.param_name, self.name)
        except ValueError:
            raise ValueError(f"No display information given for field '{self.name}'.")
        return field_info(row)

    def get_default_value(self):
        v = DEFAULTS.get(self.param_name, {}).get(self.name, self.default)
        if self.bit_count == 1 and self.internal_type != "dummy8":
            return bool(v)
        elif self.internal_type == "":
            if self.display_name == "sfxMultiplier":  # malformed in ParamDef
                return v  # float
            raise ValueError(f"No internal type for {self.param_name} field {self.display_name}")
        elif self.internal_type in {"fixstr", "fixstrW"}:
            return v  # string
        elif self.internal_type not in {"f32", "f64"}:
            return int(v)
        return v


class ParamDef(_BaseParamDef):
    HEADER_STRUCT = None  # Paramdex only
    FIELD_CLASS = ParamDefField

    @property
    def param_info(self):
        try:
            return get_param_info(self.param_type)
        except KeyError:
            # This param has no extra information.
            return None


class ParamDefBND(_BaseParamDefBND, EldenRingType):
    PARAMDEF_CLASS = ParamDef

    def __init__(self, paramdef_bnd_source=None):
        """Elden Ring does not come with ParamDef files, so this "BND" is actually a dictionary of `ParamDef`s loaded
        from the XMl files generously provided in Paramdex.

        Get Paramdex here and set its root path (the one containing the game subfolders) in `soulstruct_config.json`:
            https://github.com/soulsmods/Paramdex/

        You can also use the Paramdex fork extended for Yapped (Rune Bear), which contains better English descriptions.
        """
        if paramdef_bnd_source is None:
            # Default to PARAMDEX_PATH.
            if not PARAMDEX_PATH:
                paramdef_bnd_source = PACKAGE_PATH("Paramdex/ER/Defs")
            else:
                paramdef_bnd_source = Path(PARAMDEX_PATH, "ER/Defs")
            if not paramdef_bnd_source.is_dir():
                raise FileNotFoundError(
                    f"Could not find path '{paramdef_bnd_source}' for loading Elden Ring XML paramdefs.\n"
                    f"This path defaults to the Soulstruct root. Change it in `soulstruct_config.json` if needed."
                )
        elif not isinstance(paramdef_bnd_source, (str, Path)):
            raise TypeError(
                f"`paramdef_bnd_source` for Elden Ring `ParamDefBND` must be the path to a folder of Paramdex files."
            )
        elif not Path(paramdef_bnd_source).is_dir():
            raise FileNotFoundError(f"Could not find '{paramdef_bnd_source}' for loading Elden Ring XML paramdefs.")

        paramdef_bnd_source = Path(paramdef_bnd_source)
        self.paramdefs = {}  # type: dict[str, ParamDef]

        # Iterate over all XML files.
        for xml_path in Path(paramdef_bnd_source).glob("*.xml"):
            try:
                paramdef = self.PARAMDEF_CLASS(xml_path)
            except Exception:
                _LOGGER.error(f"Could not parse Paramdex XML file '{xml_path}'.")
                raise
            if paramdef.param_type in self.paramdefs:
                raise KeyError(f"ParamDef type {paramdef.param_type} was loaded more than once from Paramdex.")
            self.paramdefs[paramdef.param_type] = paramdef


def GET_BUNDLED_PARAMDEF() -> ParamDefBND:
    global _BUNDLED
    if _BUNDLED is None:
        _LOGGER.info(f"Loading bundled `ParamDefBND` for {ParamDefBND.GAME.name}.")
        _BUNDLED = ParamDefBND()
    return _BUNDLED
