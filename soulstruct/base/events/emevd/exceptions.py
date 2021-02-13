__all__ = [
    "EMEVDError",
    "InstructionNotFoundError",
    "NoNegateError",
    "NoSkipOrReturnError",
    "NumericEmevdError",
]

from soulstruct.exceptions import SoulstructError


class EMEVDError(SoulstructError):
    """Error that occurs while loading `EMEVD` class."""


class InstructionNotFoundError(Exception):
    """Indicates that an instruction was not found in some code segment."""


class NoNegateError(Exception):
    """Indicates that a test call has no negated variant in the EMEVD language.

    This is generally handled internally by constructing a condition (which all test types can do) and negating a test
    of that condition's truth value.
    """


class NoSkipOrReturnError(Exception):
    """Indicates that a test call has no skip/return variant in the EMEVD language.

    This is generally handled internally by constructing a condition (which all test types can do) and skipping or
    terminating based on that condition's truth value.
    """


class NumericEmevdError(SoulstructError):
    def __init__(self, lineno, msg):
        super().__init__(f"LINE {lineno}: {msg}")
