from pathlib import Path
from pkg_resources import require

from .base.models.flver import FLVER
from .config import *
from soulstruct.containers import Binder
from soulstruct.containers.dcx import DCX

soulstruct_pkg = require("soulstruct")
if soulstruct_pkg is not None:
    __version__ = soulstruct_pkg[0].version
else:
    with (Path(__file__).parent / "../VERSION").open("r") as _vfp:
        __version__ = _vfp.read().strip()
