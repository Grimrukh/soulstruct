"""Common FromSoft container types: Binder, TPF, and their contents.

NOTE: The C++ library ``Firelink``, with Python bindings ``pyrelink``, should largely replace this submodule.
``pyrelink`` is significantly faster and offers the same methods.
"""
from __future__ import annotations

__all__ = [
    "Binder",
    "BinderVersion",
    "BinderVersion4Info",
    "BinderFlags",
    "BinderError",
    "EntryNotFoundError",
    "BinderEntry",
    "BinderEntryFlags",
    "TPF",
    "TPFTexture",
]

from .core import Binder, BinderVersion, BinderVersion4Info, BinderFlags, BinderError, EntryNotFoundError
from .entry import BinderEntry, BinderEntryFlags
from .tpf import TPF, TPFTexture
