from __future__ import annotations

__all__ = ["DrawParam", "TypedDrawParam"]

import types
from dataclasses import field

from soulstruct.base.params.param import Param
from soulstruct.base.params.param_row import ParamRow
from soulstruct.dcx import DCXType


class DrawParam(Param):
    """`Param` with some extra methods that are specific to DrawParam tables."""

    # No DCX.
    dcx_type = DCXType.Null

    def get_nonzero_entries(self, ignore_polyg=True):
        """Filters table entries and returns only those with a non-empty name that does not start with '0' (or,
        by default, 'PolyG', which I assume is cutscene-specific lighting). """
        if ignore_polyg:
            return {
                index: row for index, row in self.rows.items() if row.Name and not row.Name.startswith("0")
            }
        return {
            index: row
            for index, row in self.rows.items()
            if row.Name and not row.Name.startswith("0") and not row.Name.lower().startswith("polyg")
        }


def TypedDrawParam(data_type: type[ParamRow]):
    """Generate a `Param` subclass dynamically with the given row type (or retrieve correct existing subclass).

    TODO: Add game-appropriate DCX (probably `Null`).
    TODO: Cache classes so they aren't generated more than once.
    """
    for draw_param_subclass in DrawParam.__subclasses__():
        if draw_param_subclass.__name__ == "ParamDict":
            continue
        if draw_param_subclass.ROW_TYPE is data_type:
            return draw_param_subclass
    # noinspection PyTypeChecker
    new_draw_param_subclass = types.new_class(
        name=f"DrawParam_{data_type.__name__}",
        bases=(DrawParam,),
    )  # type: type[DrawParam]
    new_draw_param_subclass.ROW_TYPE = data_type
    new_draw_param_subclass.__module__ = DrawParam.__module__
    return new_draw_param_subclass
