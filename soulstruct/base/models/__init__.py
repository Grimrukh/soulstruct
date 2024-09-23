"""Two FLVER versions are supported:
    `FLVER0`: Demon's Souls and other old FromSoft games (not otherwise supported by Soulstruct).
    `FLVER`: all FromSoft games since Dark Souls: PTDE (2011), with only a few modifications handled within-class.
"""

__all__ = [
    "BaseFLVER",
    "Dummy",
    "FLVERBone",
    "FaceSetFlags",
    "FaceSet",
    "FLVERVersion",
    "FLVER",
    "FLVER0",
    "MTD",
    "MTDBND",
    "MATBIN",
    "MATBINBND",
    "MatDef",
]

from .base import *
from .flver import FLVER
from .flver0 import FLVER0
from .mtd import MTD, MTDBND
from .matbin import MATBIN, MATBINBND
from .shaders import MatDef
