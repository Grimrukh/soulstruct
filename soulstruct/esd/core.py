__all__ = ["ESDType", "ESDError", "ESDSyntaxError", "ESDValueError"]

from enum import Enum

from soulstruct.core import SoulstructError


class ESDType(Enum):
    TALK = "talk"
    CHR = "chr"


class ESDError(SoulstructError):
    """Base exception raised by ESD."""
    def __init__(self, lineno, msg):
        self.lineno = lineno
        super().__init__(f"LINE {lineno}: {msg}")


class ESDSyntaxError(ESDError):
    """Invalid ESD syntax."""


class ESDValueError(ESDError):
    """Invalid ESD value."""
