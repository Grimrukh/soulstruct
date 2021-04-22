"""Legacy module support (for pickled projects)."""
__all__ = ["BinderEntryHeader", "BinderEntry", "BNDEntry"]

from ..entry import *

BNDEntry = BinderEntry
