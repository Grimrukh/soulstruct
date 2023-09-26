from __future__ import annotations

__all__ = ["MSGBND"]

import abc
import typing as tp
from dataclasses import dataclass

from soulstruct.containers import Binder

try:
    Self = tp.Self
except AttributeError:
    Self = "MSGBND"


@dataclass(slots=True)
class MSGBND(Binder, abc.ABC):
    """Subclassed by games to set default binder/entry path."""

    @classmethod
    @abc.abstractmethod
    def get_default_new_entry_path(cls, entry_name: str):
        pass
