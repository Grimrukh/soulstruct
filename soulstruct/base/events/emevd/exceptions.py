from __future__ import annotations

__all__ = [
    "EMEVDError",
    "InstructionNotFoundError",
    "NumericEmevdError",
]

from soulstruct.exceptions import SoulstructError


class EMEVDError(SoulstructError):
    """Error that occurs while loading `EMEVD` class."""


class InstructionNotFoundError(Exception):
    """Indicates that an instruction was not found in some code segment."""


class NumericEmevdError(SoulstructError):
    def __init__(self, lineno, msg):
        super().__init__(f"LINE {lineno}: {msg}")
