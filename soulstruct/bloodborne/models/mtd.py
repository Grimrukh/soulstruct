from __future__ import annotations

__all__ = ["MTD", "MTDBND"]

import logging
import typing as tp
from dataclasses import dataclass, field
from pathlib import Path

from soulstruct.containers import BinderVersion, BinderVersion4Info
from soulstruct.base.models.mtd import MTD, MTDBND as BaseMTDBND
from soulstruct.games import BLOODBORNE

_LOGGER = logging.getLogger(__name__)


@dataclass(slots=True)
class MTDBND(BaseMTDBND):
    """Holds MTD material definitions."""

    _BUNDLED: tp.ClassVar[MTDBND] = None

    signature: str = "10G29R1"
    flags: int = 0x42
    dcx_type = BLOODBORNE.default_dcx_type
    version: BinderVersion = BinderVersion.V4
    v4_info: BinderVersion4Info = field(default_factory=BinderVersion4Info)  # defaults are correct

    @classmethod
    def from_bundled(cls):
        if cls._BUNDLED is None:
            _LOGGER.info(f"Loading bundled `MTDBND` for {BLOODBORNE.name}.")
            bundled_mtdbnd_path = Path(__file__).parent / "resources/allmaterialbnd.mtdbnd.dcx"
            cls._BUNDLED = cls.from_path(bundled_mtdbnd_path)
        return cls._BUNDLED

    @classmethod
    def from_path_or_bundled(cls, mtdbnd_path: Path):
        if mtdbnd_path.is_file():
            return cls.from_path(mtdbnd_path)
        return cls.from_bundled()
