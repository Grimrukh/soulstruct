from __future__ import annotations

__all__ = ["BaseANIBND"]

import abc

from soulstruct.containers import Binder


class BaseANIBND(Binder, abc.ABC):
    """Manages the files that appear in ANIBND binders:
        - HKX animation files ('a00_0000.hkx', etc., with digits increasing in later games)
        - Skeleton HKX files (called 'skeleton.hkx' with varying/ignored capitalization)
        - TAE files (Time Action Editor per-animation events)

    NOTE: The `soulstruct-havok` module must be installed to load managed `HKX` skeleton/animation files. Otherwise,
    this class only provides basic animation naming utilities, DCX types, etc. The TAE file format is not yet supported
    in Soulstruct, and may never be, as Meowmaritus's DS Anim Studio program is a far superior tool for editing it.
    """