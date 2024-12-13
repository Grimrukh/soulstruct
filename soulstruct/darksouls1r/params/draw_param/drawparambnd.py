from __future__ import annotations

__all__ = ["DrawParamBND"]

import logging
import typing as tp
from types import ModuleType

from soulstruct.containers import BinderEntry
from soulstruct.games import DARK_SOULS_DSR

from soulstruct.darksouls1ptde.params.draw_param import DrawParam, DrawParamBND as DrawParamBND_PTDE, TypedDrawParam
from soulstruct.darksouls1ptde.params.paramdef import (
    TONE_MAP_BANK as PTDE_TONE_MAP_BANK,
    TONE_CORRECT_BANK as PTDE_TONE_CORRECT_BANK,
)
from .. import paramdef
from ..paramdef import *

_LOGGER = logging.getLogger("soulstruct")


class DrawParamBND(DrawParamBND_PTDE):
    """Structure that manages double-slots and DrawParam nicknames for one `DrawParamBND` file (i.e. one map "area").

    This DS1R override handles two known cases of vanilla Param corruption in `DrawParamBND` files.
    """

    DEFAULT_ENTRY_ROOT: tp.ClassVar[str] = f"{DARK_SOULS_DSR.interroot_prefix}\\param\\DrawParam"
    PARAMDEF_MODULE: tp.ClassVar[ModuleType] = paramdef

    dcx_type = DARK_SOULS_DSR.default_dcx_type

    def assign_param_from_entry(
        self, entry: BinderEntry, param_stem: str, slot: int, typed_draw_param_class: type[DrawParam]
    ):
        """Handles outdated `TONE_MAP_BANK` and `TONE_CORRECT_BANK` from `default` and `m99` DrawParams."""
        if slot not in {0, 1}:
            raise ValueError(f"DrawParamBND slot must be 0 or 1, not {slot}.")
        draw_params = self.draw_params_0 if slot == 0 else self.draw_params_1
        try:
            draw_params[param_stem] = entry.to_binary_file(typed_draw_param_class)
            return
        except Exception as ex:
            if param_stem not in {"ToneMapBank", "ToneCorrectBank"}:
                _LOGGER.error(
                    f"Could not load `DrawParam` from `DrawParamBND` entry '{entry.name}'.\n  Error: {ex}"
                )
                raise
            # Otherwise, handle known vanilla DS1R corruption by loading bundled PTDE versions.

        _LOGGER.info(
            f"Could not load `{param_stem}` Param from `DrawParamBND` entry '{entry.name}'. "
            f"This is expected for vanilla DS1R `DrawParamBND`, which is corrupt. Trying PTDE version...\n"
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
                f"Could not load PTDE `{param_stem}` Param from `DrawParamBND` entry '{entry.name}' while trying to "
                f"replace corrupted vanilla DS1R Param.\n  Error: {ex}"
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
            draw_params[param_stem] = dsr_draw_param
