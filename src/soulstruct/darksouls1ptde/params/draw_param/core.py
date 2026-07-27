from __future__ import annotations

__all__ = ["DrawParam", "TypedDrawParam"]

import typing as tp
from functools import lru_cache

from soulstruct.base.params.param import Param
from soulstruct.base.params.param_row import ParamRow
from soulstruct.dcx import DCXType


class DrawParam[PARAM_ROW_DATA_T: ParamRow](Param[PARAM_ROW_DATA_T]):
    """`Param` with some extra methods that are specific to DrawParam tables."""

    # No DCX.
    dcx_type = DCXType.Null

    def get_nonzero_entries(self, ignore_polyg=True):
        """Filters table entries and returns only those with a non-empty name that does not start with '0' (or,
        by default, 'PolyG', which I assume is cutscene-specific lighting). """
        if ignore_polyg:
            return {
                index: row
                for index, row in self.rows.items()
                if row.Name and not row.Name.lower().startswith(("0", "polyg"))
            }
        return {
            index: row for index, row
            in self.rows.items()
            if row.Name and not row.Name.startswith("0")
        }

DRAW_PARAM_ROW_T = tp.TypeVar("DRAW_PARAM_ROW_T", bound=ParamRow)

@lru_cache(maxsize=None)
def _typed_param(row_type: type[DRAW_PARAM_ROW_T]) -> type:
    new_cls = type(f"DrawParam_{row_type.__name__}", (DrawParam,), {"ROW_TYPE": row_type})
    new_cls.__module__ = row_type.__module__
    new_cls.__qualname__ = new_cls.__name__
    return new_cls


def TypedDrawParam(row_type: type[DRAW_PARAM_ROW_T]) -> type[DrawParam[DRAW_PARAM_ROW_T]]:
    return tp.cast(type[DrawParam[DRAW_PARAM_ROW_T]], _typed_param(row_type))
