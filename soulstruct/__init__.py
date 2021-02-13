from pathlib import Path

from .config import *
from soulstruct.containers.bnd import BND
from soulstruct.containers.dcx import DCX


with (Path(__file__).parent / "../VERSION").open("r") as _vfp:
    __version__ = _vfp.read().strip()
