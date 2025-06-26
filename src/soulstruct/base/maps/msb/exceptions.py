__all__ = ["MapError", "MapModelError", "MapEventError", "MapRegionError", "MapPartError"]

from soulstruct.exceptions import SoulstructError


class MapError(SoulstructError):
    """Error caused by a map-related file or class."""


class MapModelError(MapError):
    """Error caused by an MSB Model entry."""


class MapEventError(MapError):
    """Error caused by an MSB Event entry."""


class MapRegionError(MapError):
    """Error caused by an MSB Region entry."""


class MapPartError(MapError):
    """Error caused by an MSB Part entry."""
