__all__ = ["MapError"]

from soulstruct.core import SoulstructError


class MapError(SoulstructError):
    """Error caused by a map-related file or class."""
