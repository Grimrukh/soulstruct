__all__ = ["ESDError", "ESDTypeError", "ESDScriptError", "ESDSyntaxError", "ESDValueError"]

from soulstruct.exceptions import SoulstructError


class ESDError(SoulstructError):
    """Base exception raised by ESD."""


class ESDTypeError(ESDError):
    """Wrong type of ESD used/encountered."""


class ESDScriptError(ESDError):
    """Base exception raised by ESD during ESP script compilation."""
    def __init__(self, lineno, msg):
        self.lineno = lineno
        super().__init__(f"LINE {lineno}: {msg}")


class ESDSyntaxError(ESDScriptError):
    """Invalid ESD syntax."""


class ESDValueError(ESDScriptError):
    """Invalid ESD value."""
