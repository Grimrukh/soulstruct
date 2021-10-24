
__all__ = [
    "SoulstructError",
    "InvalidFieldValueError",
    "GameFileDictSupportError",
    "InvalidGameFileTypeError",
]


class SoulstructError(Exception):
    """Base class for an error raised by Soulstruct."""


class InvalidFieldValueError(SoulstructError):
    """Field of a data type was set to an invalid value."""


class GameFileDictSupportError(SoulstructError):
    """Exception raised when trying to use `load_dict()` or `to_dict()` on an unsupported `GameFile` subclass."""


class InvalidGameFileTypeError(SoulstructError):
    """Exception raised from an unhandled `file_source` type passed to `GameFile` constructor."""
