"""DSR inherits most of its classes directly from PTDE, as the MSB formats, enums, etc. are exactly identical."""

__all__ = ["ALL_MAPS", "get_map", "MSB", "MSBEntry", "MapStudioDirectory", "NavInfo", "NVM"]

from soulstruct.base.maps.msb.msb_entry import MSBEntry
from .constants import ALL_MAPS, get_map
from .map_studio_directory import MapStudioDirectory
from .msb import MSB
from .navinfo import NavInfo
from .nvm import NVM
