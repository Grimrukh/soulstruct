from pathlib import Path

# Set up loggers.
import soulstruct._logging

from soulstruct.config import *
from soulstruct.containers import Binder, EntryNotFoundError

# Convenience imports (must be done after the above to avoid `GameFile` import circularity).
from soulstruct.base.models.flver import FLVER


try:
    with (Path(__file__).parent / "../VERSION").open("r") as _vfp:
        __version__ = _vfp.read().strip()
except FileNotFoundError:
    __version = "UNKNOWN"
