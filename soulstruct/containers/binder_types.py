"""Pre-configured types of Binders that recur in one or more games."""
from __future__ import annotations

__all__ = [
    "FLVERBinder",
]

import abc
import logging
import typing as tp
from dataclasses import dataclass, field

from soulstruct.base.models.flver import FLVER
from .core import Binder, EntryNotFoundError
from .tpf import TPF

_LOGGER = logging.getLogger("soulstruct")


@dataclass(slots=True)
class FLVERBinder(Binder, abc.ABC):
    """Base class for Binders that contain one or more FLVER files and an optional TPF file."""

    TPF_ENTRY_ID: tp.ClassVar[int] = 100  # -1 if no TPF ever exists
    FLVER_FIRST_ENTRY_ID: tp.ClassVar[int] = 200
    MAX_FLVER_COUNT: tp.ClassVar[int] = 1

    model_stem: str = ""  # will be extracted from `path` field if left empty
    tpf: TPF | None = None  # not available in all subclasses
    flvers: dict[str, FLVER] = field(default_factory=dict)

    def __post_init__(self):
        if not self.tpf and self.TPF_ENTRY_ID >= 0:
            try:
                tpf_entry = self.find_entry_id(self.TPF_ENTRY_ID)
            except EntryNotFoundError:
                pass  # TPF optional
            else:
                self.tpf = tpf_entry.to_binary_file(TPF)
        if not self.flvers:
            for entry in self.find_entries_matching_name(r".*\.flver(\.dcx)?"):
                self.flvers[entry.minimal_stem] = entry.to_binary_file(FLVER)
            if len(self.flvers) >= self.MAX_FLVER_COUNT:
                _LOGGER.warning(f"More than {self.MAX_FLVER_COUNT} FLVERs loaded from Binder with path '{self.path}'.")

    def entry_autogen(self):
        """Replace/create FLVER and TPF Binder entries."""

        if self.tpf:
            main_model_stem = self._get_model_stem()
            self.set_default_entry(
                entry_spec=self.TPF_ENTRY_ID,
                new_path=self.get_tpf_entry_path(main_model_stem),
                new_flags=0x2,
            ).set_from_binary_file(self.tpf)

        if self.flvers:
            if len(self.flvers) > self.MAX_FLVER_COUNT:
                raise ValueError(f"`{self.cls_name}` can only have up to {self.MAX_FLVER_COUNT} FLVERs.")
            sorted_names = sorted(self.flvers.keys())
            for i, name in enumerate(sorted_names):
                flver = self.flvers[name]
                self.set_default_entry(
                    entry_spec=self.FLVER_FIRST_ENTRY_ID + i,
                    new_path=self.get_flver_entry_path(name),
                    new_flags=0x2,
                ).set_from_binary_file(flver)

    @property
    def flver(self) -> FLVER | None:
        """Shortcut for accessing the main FLVER file (if there is only one)."""
        if self.MAX_FLVER_COUNT != 1:
            raise ValueError(f"Cannot access `flver` property of {self.__class__.__name__} with multiple FLVERs.")
        return self.flvers[self.model_stem] if self.flvers else None

    @flver.setter
    def flver(self, value: FLVER):
        if self.MAX_FLVER_COUNT != 1:
            raise ValueError(f"Cannot set `flver` property of {self.__class__.__name__} with multiple FLVERs.")
        self.flvers[self.model_stem] = value

    def get_tpf_entry_path(self, model_stem: str) -> str:
        return self.get_default_entry_path(f"{model_stem}\\{model_stem}.tpf")

    def get_flver_entry_path(self, model_stem: str) -> str:
        return self.get_default_entry_path(f"{model_stem}\\{model_stem}.flver")

    def _get_model_stem(self) -> str:
        """Get model stem from `model_stem` field or `path` name as a backup."""
        if self.model_stem:
            return self.model_stem
        if stem := self.path_minimal_stem:
            return stem
        raise ValueError(f"`model_stem` or `path` must be set to determine model stem of {self.cls_name}`.")
