from __future__ import annotations

__all__ = ["MTD", "MTDBND"]

import logging
import typing as tp
from dataclasses import dataclass
from pathlib import Path

from soulstruct.containers import BinderVersion, EntryNotFoundError
from soulstruct.base.models.mtd import MTD, MTDBND as BaseMTDBND
from soulstruct.games import DARK_SOULS_DSR

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class MTDBND(BaseMTDBND):
    """Holds MTD material definitions."""

    _BUNDLED: tp.ClassVar[MTDBND] = None

    dcx_type = DARK_SOULS_DSR.default_dcx_type
    version: BinderVersion = BinderVersion.V3
    v4_info = None

    @classmethod
    def from_bundled(cls):
        if cls._BUNDLED is None:
            _LOGGER.info(f"Loading bundled `MTDBND` for {MTDBND.get_game().name}.")

            bundled_mtdbnd_path = Path(__file__).parent / "resources/Mtd.mtdbnd.dcx"
            bundled_patch_mtdbnd_path = Path(__file__).parent / "resources/MtdPatch.mtdbnd.dcx"

            base_mtdbnd = cls.from_path(bundled_mtdbnd_path)
            patch_mtdbnd = cls.from_path(bundled_patch_mtdbnd_path)

            # Add Patch entries into main MTDBND. We replace any existing entries, but ignore repeats within Patch.
            added_names = []
            for patch_entry in patch_mtdbnd.entries:
                if patch_entry.name in added_names:
                    continue
                try:
                    base_mtdbnd.remove_entry_name(patch_entry.name)
                except EntryNotFoundError:
                    pass
                base_mtdbnd.entries.append(patch_entry)
                added_names.append(patch_entry.name)

            cls._BUNDLED = base_mtdbnd

        return cls._BUNDLED

    @classmethod
    def from_path_or_bundled(cls, mtdbnd_path: Path):
        if mtdbnd_path.is_file():
            return cls.from_path(mtdbnd_path)
        return cls.from_bundled()
