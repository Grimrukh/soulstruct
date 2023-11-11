from __future__ import annotations

__all__ = ["MTD", "MTDBND"]

import logging
import typing as tp
from dataclasses import dataclass
from pathlib import Path

from soulstruct.containers import BinderVersion
from soulstruct.base.models.mtd import MTD, MTDBND as BaseMTDBND
from soulstruct.games import DARK_SOULS_PTDE

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class MTDBND(BaseMTDBND):
    """Holds MTD material definitions."""

    _BUNDLED: tp.ClassVar[MTDBND] = None

    dcx_type = DARK_SOULS_PTDE.default_dcx_type
    version: BinderVersion = BinderVersion.V3
    v4_info = None

    @classmethod
    def from_bundled(cls):
        if cls._BUNDLED is None:
            _LOGGER.info(f"Loading bundled `MTDBND` for {MTDBND.get_game().name}.")
            bundled_mtdbnd_path = Path(__file__).parent / "resources/mtd.mtdbnd"
            cls._BUNDLED = cls.from_path(bundled_mtdbnd_path)
        return cls._BUNDLED

    @classmethod
    def from_path_or_bundled(cls, mtdbnd_path: Path):
        if mtdbnd_path.is_file():
            return cls.from_path(mtdbnd_path)
        return cls.from_bundled()
