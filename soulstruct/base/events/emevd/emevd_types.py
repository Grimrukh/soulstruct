
__all__ = [
    "BaseEMEVDObject",
    "Flag",
    "FlagRange",
    "MapFlagSuffix",
]

from enum import IntEnum, unique

from soulstruct.base.game_types import BaseGameObject
from .exceptions import NoNegateError, NoSkipOrReturnError


class BaseEMEVDObject(BaseGameObject):
    """Base class for game objects that can be referenced in EMEVD (a lot of them).

    Many of them implement `__call__` to use in EVS as an optional alternative to some instructions/tests.
    """

    @property
    def event_arg_fmt(self):
        """If not `None`, allows this type to be used as an EVS event arg type hint for this format."""
        return None

    @classmethod
    def get_enum(cls, enum_cls_name: str, enum_member_name: str):
        raise AttributeError("Cannot `get_enum` with base class `BaseEMEVDObject`.")

    @classmethod
    def compile_instruction(cls, instr_name: str, *args, **kwargs):
        raise AttributeError("Cannot `compile_instruction` with base class `BaseEMEVDObject`.")

    @classmethod
    def get_compile_func(cls, instr_name: str):
        raise AttributeError("Cannot `get_compile_func` with base class `BaseEMEVDObject`.")
    
    def get_value_test(
        self,
        value,
        negate=False,
        condition=None,
        skip_lines=0,
        end_event=False,
        restart_event=False,
        skip_if_true_func=None,
        skip_if_false_func=None,
        if_true_func=None,
        if_false_func=None,
        end_if_true_func=None,
        end_if_false_func=None,
        restart_if_true_func=None,
        restart_if_false_func=None,
    ):
        if skip_lines > 0:
            if condition is not None or end_event or restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if skip_if_true_func is None or skip_if_false_func is None:
                raise NoSkipOrReturnError  # Both of these functions must be defined.
            if negate:
                return skip_if_true_func(skip_lines, value)
            return skip_if_false_func(skip_lines, value)
        elif skip_lines < 0:
            raise ValueError("You cannot skip a negative number of lines.")

        if condition is not None:
            if end_event or restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if if_false_func is None:
                    raise NoNegateError  # Some game types only have a positive condition test (e.g. IfObjectActivated).
                return if_false_func(condition, value)
            return if_true_func(condition, value)

        if end_event:
            if restart_event:
                raise ValueError("Multiple condition outcomes specified (condition, skip, end, restart).")
            if negate:
                if end_if_false_func is None:
                    raise NoSkipOrReturnError
                return end_if_false_func(value)
            if end_if_true_func is None:
                raise NoSkipOrReturnError
            return end_if_true_func(value)

        if restart_event:
            if negate:
                if restart_if_false_func is None:
                    raise NoSkipOrReturnError
                return restart_if_false_func(value)
            if restart_if_true_func is None:
                raise NoSkipOrReturnError
            return restart_if_true_func(value)

        raise ValueError("Must specify one condition outcome (condition, skip, end, restart).")


@unique
class Flag(BaseEMEVDObject, IntEnum):
    """ Condition upon a flag as a shortcut to condition upon it being enabled. """

    def __call__(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):

        value = self if isinstance(self, (int, float, tuple)) else self.value
        return self.get_value_test(
            value=value,
            negate=negate,
            condition=condition,
            skip_lines=skip_lines,
            end_event=end_event,
            restart_event=restart_event,
            skip_if_true_func=self.get_compile_func("SkipLinesIfFlagEnabled"),
            skip_if_false_func=self.get_compile_func("SkipLinesIfFlagDisabled"),
            if_true_func=self.get_compile_func("IfFlagEnabled"),
            if_false_func=self.get_compile_func("IfFlagDisabled"),
            end_if_true_func=self.get_compile_func("EndIfFlagEnabled"),
            end_if_false_func=self.get_compile_func("EndIfFlagDisabled"),
            restart_if_true_func=self.get_compile_func("RestartIfFlagEnabled"),
            restart_if_false_func=self.get_compile_func("RestartIfFlagDisabled"),
        )


class FlagRange(BaseEMEVDObject):
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # TODO: use the methods below in EVS parser.

    def any(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        return self.get_value_test(
            value=self,
            negate=negate,
            condition=condition,
            skip_lines=skip_lines,
            end_event=end_event,
            restart_event=restart_event,
            skip_if_true_func=self.get_compile_func("SkipLinesIfFlagRangeAllDisabled"),
            skip_if_false_func=self.get_compile_func("SkipLinesIfFlagRangeAnyEnabled"),
            if_true_func=self.get_compile_func("IfFlagRangeAnyEnabled"),
            if_false_func=self.get_compile_func("IfFlagRangeAllDisabled"),
            end_if_true_func=self.get_compile_func("EndIfFlagRangeAnyEnabled"),
            end_if_false_func=self.get_compile_func("EndIfFlagRangeAllDisabled"),
            restart_if_true_func=self.get_compile_func("RestartIfFlagRangeAnyEnabled"),
            restart_if_false_func=self.get_compile_func("RestartIfFlagRangeAllDisabled"),
        )

    def all(self, negate=False, condition=None, skip_lines=0, end_event=False, restart_event=False):
        return self.get_value_test(
            value=self,
            negate=negate,
            condition=condition,
            skip_lines=skip_lines,
            end_event=end_event,
            restart_event=restart_event,
            skip_if_true_func=self.get_compile_func("SkipLinesIfFlagRangeAnyDisabled"),
            skip_if_false_func=self.get_compile_func("SkipLinesIfFlagRangeAllEnabled"),
            if_true_func=self.get_compile_func("IfFlagRangeAllEnabled"),
            if_false_func=self.get_compile_func("IfFlagRangeAnyDisabled"),
            end_if_true_func=self.get_compile_func("EndIfFlagRangeAllEnabled"),
            end_if_false_func=self.get_compile_func("EndIfFlagRangeAnyDisabled"),
            restart_if_true_func=self.get_compile_func("RestartIfFlagRangeAllEnabled"),
            restart_if_false_func=self.get_compile_func("RestartIfFlagRangeAnyDisabled"),
        )

    def __iter__(self):
        """Allows easy conversion to sequence."""
        return iter((self.first, self.last))

    def __getitem__(self, index: int):
        if index == 0:
            return self.first
        elif index == 1:
            return self.last
        raise ValueError(f"`FlagRange` index must be 0 or 1, not {index}.")

    def __repr__(self) -> str:
        return f"({self.first}, {self.last})"


class MapFlagSuffix(IntEnum):
    """Flag up to four digits long, intended to be added to a map base flag (such as 11020000 for m10_02).

    `EVSParser` will compute the true flag ID automatically if it knows the map's base flag ID.
    """
