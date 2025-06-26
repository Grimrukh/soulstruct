import importlib.metadata

from soulstruct.config import *
from soulstruct.containers import Binder, EntryNotFoundError

# Convenience imports (must be done after the above to avoid `GameFile` import circularity).
from soulstruct.base.models.flver import FLVER


try:
    __version__ = importlib.metadata.version("soulstruct")
except FileNotFoundError:
    __version__ = "UNKNOWN"
