"""Elden Ring Paramdefs can only be loaded from Paramdex XML files."""
from __future__ import annotations

__all__ = ["ParamDefBND", "GET_BUNDLED_PARAMDEFBND"]

import logging
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.base.params.paramdef import ParamDef, ParamDefBND as _BaseParamDefBND
from soulstruct.config import PARAMDEX_PATH
from soulstruct.utilities.files import PACKAGE_PATH

_LOGGER = logging.getLogger(__name__)
_BUNDLED = None


@dataclass(slots=True)
class ParamDefBND(_BaseParamDefBND):
    """Elden Ring does not come with `ParamDef` files, so this class instead holds a dictionary mapping `ParamDef` stems
    to `ParamDef` instances loaded from the XMl files generously provided in the `Paramdex` repository.

    Get Paramdex here and set its root path (the one containing the game subfolders) in `soulstruct_config.json`:
        https://github.com/soulsmods/Paramdex/

    You can also use the Paramdex fork extended for Yapped (Rune Bear), which contains better English descriptions.
    """
    PARAMDEF_CLASS: tp.ClassVar = ParamDef  # NOTE: Elden Ring has no `ParamDef` version info to override base with.
    
    paramdefs: dict[str, ParamDef] = field(default_factory=dict)

    # NOTE: If Elden Ring `paramdefbnd` files magically materialize some day, this class's base methods should still
    # work on them (if versions can be handled).

    @classmethod
    def from_paramdex(cls, paramdex_er_defs_path: Path | str = None):
        if paramdex_er_defs_path is None:
            # Default to Erd-Tools-Defs.
            paramdex_er_defs_path = PACKAGE_PATH("eldenring/params/paramdef/Erd-Tools-Defs")
        else:
            paramdex_er_defs_path = Path(paramdex_er_defs_path)
            if not paramdex_er_defs_path.is_dir():
                raise FileNotFoundError(f"Could not find '{paramdex_er_defs_path}' for loading Elden Ring XML paramdefs.")

        paramdefs = {}  # type: dict[str, ParamDef]

        # Iterate over all XML files.
        for xml_path in Path(paramdex_er_defs_path).glob("*.xml"):
            try:
                paramdef = ParamDef.from_paramdex_xml(xml_path)
            except Exception:
                _LOGGER.error(f"Could not parse Paramdex XML file '{xml_path}'.")
                raise
            if paramdef.param_type in paramdefs:
                raise KeyError(f"ParamDef type {paramdef.param_type} was loaded more than once from Paramdex.")
            paramdefs[paramdef.param_type] = paramdef

        return cls(path=paramdex_er_defs_path, paramdefs=paramdefs)


def GET_BUNDLED_PARAMDEFBND() -> ParamDefBND:
    global _BUNDLED
    if _BUNDLED is None:
        _LOGGER.info(f"Loading bundled `ParamDefBND` for {ParamDefBND.get_game().name}.")
        _BUNDLED = ParamDefBND.from_paramdex()
    return _BUNDLED
