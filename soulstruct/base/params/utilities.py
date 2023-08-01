"""Miscellaneous utilities for manipulating Params."""
from __future__ import annotations

__all__ = ["ParamFieldComparisonType", "ParamFieldSearchCondition", "find_param_rows"]

import logging
import typing as tp
from enum import Enum

from .param import Param, ParamRow

_LOGGER = logging.getLogger(__name__)


class ParamFieldComparisonType(Enum):
    """Numerical comparator condition for a Param field search."""
    Equal = "=="
    NotEqual = "!="
    GreaterThan = ">"
    LessThan = "<"
    GreaterThanOrEqual = ">="
    LessThanOrEqual = "<="

    def compare(self, left, right) -> bool:
        match self:
            case ParamFieldComparisonType.Equal:
                return left == right
            case ParamFieldComparisonType.NotEqual:
                return left != right
            case ParamFieldComparisonType.GreaterThan:
                return left > right
            case ParamFieldComparisonType.LessThan:
                return left < right
            case ParamFieldComparisonType.GreaterThanOrEqual:
                return left >= right
            case ParamFieldComparisonType.LessThanOrEqual:
                return left <= right


class ParamFieldSearchCondition(tp.NamedTuple):
    field_name: str
    comparison_type: ParamFieldComparisonType
    value: tp.Any  # typically `int | float | bool`

    def __repr__(self):
        return f"{self.field_name} {self.comparison_type.value} {self.value}"


def find_param_rows(param: Param, conditions: tp.Iterable[ParamFieldSearchCondition]) -> dict[int, ParamRow]:
    """Return all rows in `param` that match all `conditions`."""
    return {
        row_id: row for row_id, row in param.items()
        if all(_check_condition(row, condition) for condition in conditions)
    }


def _check_condition(row: ParamRow, condition: ParamFieldSearchCondition) -> bool:
    """Return True if `row` matches `condition`.

    Currently always returns false, and logs a warning, for non-numeric fields.
    """
    value = row[condition.field_name]
    if not isinstance(value, (int, float)):
        # Only Equal/NotEqual supported.
        if condition.comparison_type not in (ParamFieldComparisonType.Equal, ParamFieldComparisonType.NotEqual):
            _LOGGER.warning(f"Non-numeric Param field '{condition.field_name}' can only be a condition with == or !=.")
            return False
    return condition.comparison_type.compare(value, condition.value)
