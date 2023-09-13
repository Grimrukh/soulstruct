
__all__ = [
    "SoulstructError",
    "InvalidFieldValueError",
    "RestoreBackupError",
]


class SoulstructError(Exception):
    """Base class for an error raised by Soulstruct."""


class InvalidFieldValueError(SoulstructError):
    """Field of a data type was set to an invalid value."""
    # TODO: Probably obsolete.


class RestoreBackupError(SoulstructError):
    pass
