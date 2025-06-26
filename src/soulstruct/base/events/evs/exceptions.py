"""Exceptions specific to `EVSParser`."""

from __future__ import annotations

__all__ = [
    "NoNegateError",
    "NoSkipOrReturnError",
    "EVSError",
    "EVSSyntaxError",
    "EVSValueError",
    "EVSImportError",
    "EVSImportFromError",
    "EVSCommonFuncImportError",
    "EVSNameError",
    "EVSAttributeError",
    "EVSCallableError",
    "ConditionError",
    "ConditionNameError",
    "ConditionLimitError",
]

import ast
import logging
import typing as tp

_LOGGER = logging.getLogger(__name__)


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


NODE_TYPING = tp.Union[
    ast.AST, ast.Name, ast.Constant, ast.Expr, ast.For, ast.If, ast.Assign, ast.Return, ast.Call, ast.UnaryOp, ast.stmt
]


class EVSError(Exception):
    def __init__(
        self,
        evs_name: str,
        lineno: NODE_TYPING | int,
        msg: str,
    ):
        if isinstance(lineno, ast.AST):
            lineno = lineno.lineno
        self.lineno = lineno
        super().__init__(f"{evs_name} | LINE {lineno}: {msg}")


class EVSSyntaxError(EVSError):
    pass


class EVSValueError(EVSError):
    pass


class EVSImportError(EVSError):
    """Raised when a module cannot be imported."""

    def __init__(self, evs_name, lineno, module, msg):
        super().__init__(
            evs_name,
            lineno,
            f"Could not import {repr(module)}.\nError: {msg}",
        )


class EVSImportFromError(EVSError):
    """Raised when a name cannot be imported from a module."""

    def __init__(self, evs_name, lineno, module, name, msg):
        super().__init__(evs_name, lineno, f"Could not import {repr(name)} from module {repr(module)}. Error: {msg}")


class EVSCommonFuncImportError(EVSError):
    """Raised when a [COMMON_FUNC]-tagged import cannot be completed."""

    def __init__(self, evs_name, module, name, msg):
        if name == "":
            super().__init__(
                evs_name,
                0,
                f"Could not import COMMON_FUNC module {repr(module)}. Error: {msg}",
            )
        else:
            super().__init__(
                evs_name,
                0,
                f"Could not import {repr(name)} from COMMON_FUNC module {repr(module)}. Error: {msg}",
            )


class EVSNameError(EVSError):
    """Raised when an invalid (undefined) name is parsed."""

    def __init__(self, evs_name, lineno, name):
        super().__init__(evs_name, lineno, f"Name {repr(name)} has not been imported or defined.")


class EVSAttributeError(EVSError):
    """Raised when an attribute of an object cannot be retrieved."""

    def __init__(self, evs_name, lineno, name, attribute):
        super().__init__(evs_name, lineno, f"Object {repr(name)} has no attribute {repr(attribute)}.")


class EVSCallableError(EVSError):
    """Raised when an un-callable object is called."""

    def __init__(self, evs_name, lineno, name):
        super().__init__(evs_name, lineno, f"Object {name} is not callable.")


class ConditionError(EVSError):
    pass


class ConditionNameError(ConditionError):
    pass


class ConditionLimitError(ConditionError):
    pass
