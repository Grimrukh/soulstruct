from pathlib import Path

from soulstruct.config import *
from soulstruct.containers import Binder
from soulstruct.containers.dcx import DCX

# Convenience imports (must be done after the above to avoid `GameFile` import circularity).
from soulstruct.base.models.flver.core import FLVER


try:
    with (Path(__file__).parent / "../VERSION").open("r") as _vfp:
        __version__ = _vfp.read().strip()
except FileNotFoundError:
    __version = "UNKNOWN"
