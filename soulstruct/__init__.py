from pathlib import Path
from pkg_resources import require, DistributionNotFound

from .base.models.flver import FLVER
from .config import *
from soulstruct.containers import Binder
from soulstruct.containers.dcx import DCX

try:
    soulstruct_pkg = require("soulstruct")
    __version__ = soulstruct_pkg[0].version
except DistributionNotFound:
    with (Path(__file__).parent / "../VERSION").open("r") as _vfp:
        __version__ = _vfp.read().strip()
