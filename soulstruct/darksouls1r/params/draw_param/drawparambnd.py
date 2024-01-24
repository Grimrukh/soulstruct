from __future__ import annotations

__all__ = ["DrawParamBND"]

import logging
import typing as tp
from dataclasses import dataclass
from types import ModuleType

from soulstruct.containers import BinderEntry
from soulstruct.games import DARK_SOULS_DSR

from soulstruct.darksouls1ptde.params.draw_param import DrawParam, DrawParamBND, TypedDrawParam
from soulstruct.darksouls1ptde.params.paramdef import (
    TONE_MAP_BANK as PTDE_TONE_MAP_BANK,
    TONE_CORRECT_BANK as PTDE_TONE_CORRECT_BANK,
)
from .. import paramdef
from ..paramdef import *

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class DrawParamBND(DrawParamBND):
    """Structure that manages double-slots and DrawParam nicknames for one `DrawParamBND` file (i.e. one map "area")."""

    PARAMDEF_MODULE: tp.ClassVar[ModuleType] = paramdef
    GET_BUNDLED_PARAMDEFBND: tp.ClassVar[tp.Callable] = staticmethod(GET_BUNDLED_PARAMDEFBND)

    dcx_type = DARK_SOULS_DSR.default_dcx_type

    @classmethod
    def get_default_new_entry_path(cls, entry_name: str) -> str:
        return f"N:\\FRPG\\data\\INTERROOT_x64\\param\\DrawParam\\{entry_name}"

    def assign_param_from_entry(
        self, entry: BinderEntry, param_stem: str, slot: int, typed_draw_param_class: type[DrawParam]
    ):
        """Handles outdated `TONE_MAP_BANK` and `TONE_CORRECT_BANK` from `default` and `m99` DrawParams."""
        try:
            self.draw_params[param_stem][slot] = entry.to_binary_file(typed_draw_param_class)
        except Exception as ex:
            if param_stem in {"ToneMapBank", "ToneCorrectBank"}:
                _LOGGER.warning(
                    f"Could not load `{param_stem}` Param from `DrawParamBND` entry '{entry.name}'. "
                    f"Trying PTDE version...\n"
                )
                if param_stem == "ToneMapBank":
                    dsr_draw_param_row_type = TONE_MAP_BANK
                    ptde_draw_param_type = TypedDrawParam(PTDE_TONE_MAP_BANK)
                else:
                    dsr_draw_param_row_type = TONE_CORRECT_BANK
                    ptde_draw_param_type = TypedDrawParam(PTDE_TONE_CORRECT_BANK)
                try:
                    ptde_draw_param = entry.to_binary_file(ptde_draw_param_type)  # type: DrawParam
                except Exception as ex:
                    _LOGGER.error(
                        f"Could not load DSR or PTDE `{param_stem}` Param from `DrawParamBND` entry "
                        f"'{entry.name}'.\n  Error: {ex}"
                    )
                    raise
                else:
                    # Convert PTDE Param to DSR Param for future writes/re-reads.
                    # noinspection PyArgumentList
                    dsr_draw_param = typed_draw_param_class(
                        param_type=ptde_draw_param.param_type,
                        big_endian=ptde_draw_param.big_endian,
                        unknown=ptde_draw_param.unknown,
                        flags1=ptde_draw_param.flags1,
                        flags2=ptde_draw_param.flags2,
                        paramdef_data_version=ptde_draw_param.paramdef_data_version,
                        paramdef_format_version=ptde_draw_param.paramdef_format_version,
                        rows={
                            i: dsr_draw_param_row_type(
                                RawName=ptde_row.RawName,
                                Name=ptde_row.Name,
                                **ptde_row.to_dict(ignore_defaults=False, binary_fields_only=True),
                            )
                            for i, ptde_row in ptde_draw_param.rows.items()
                        }
                    )
                    self.draw_params[param_stem][slot] = dsr_draw_param
            else:
                _LOGGER.error(
                    f"Could not load `DrawParam` from `DrawParamBND` entry '{entry.name}'.\n  Error: {ex}"
                )
                raise
