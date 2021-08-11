from pathlib import Path

from .base.models.flver import FLVER
from .config import *
from soulstruct.containers import Binder
from soulstruct.containers.dcx import DCX


with (Path(__file__).parent / "../VERSION").open("r") as _vfp:
    __version__ = _vfp.read().strip()
