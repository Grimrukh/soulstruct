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

    # Managed entry file instances.
    _tpf: TPF | None = None  # not available in all subclasses; loaded on first access
    _flvers: dict[str, FLVER] = field(default_factory=dict)  # should be accessed with `get_flver()` and `set_flver()`

    def get_flver(self, model_stem: str) -> FLVER:
        """Look for loaded FLVER or try to load it from a FLVER entry (DCX agnostic)."""
        if model_stem in self._flvers:
            return self._flvers[model_stem]  # already loaded/set

        # Look for entry to load into managed FLVER dictionary.
        try:
            entry = self.find_entry_matching_name(rf"{model_stem}\.flver(\.dcx)?")
        except EntryNotFoundError:
            raise KeyError(f"FLVER with model stem '{model_stem}' not loaded in `{self.cls_name}` and no entry found.")

        flver = entry.to_binary_file(FLVER)
        self._flvers[model_stem] = flver
        return flver

    def set_flver(self, model_stem: str, flver: FLVER):
        """Set FLVER in managed dictionary. Will be written to a new/existing entry on `FLVERBinder` write."""
        self._flvers[model_stem] = flver

    def entry_autogen(self):
        """Replace/create FLVER and TPF Binder entries. Note that existing, non-overwritten entries are NOT removed."""

        if self._flvers:
            if len(self._flvers) > self.MAX_FLVER_COUNT:
                raise ValueError(f"`{self.cls_name}` can only have up to {self.MAX_FLVER_COUNT} FLVERs.")
            sorted_names = sorted(self._flvers.keys())
            for i, name in enumerate(sorted_names):
                flver = self._flvers[name]
                self.set_default_entry(
                    entry_spec=self.FLVER_FIRST_ENTRY_ID + i,  # TODO: could clash with existing...
                    new_path=self.get_flver_entry_path(name),
                    new_flags=0x2,
                ).set_from_binary_file(flver)

        if self._tpf is not None:
            # Replace/create TPF entry.
            main_model_stem = self._get_model_stem()
            self.set_default_entry(
                entry_spec=self.TPF_ENTRY_ID,
                new_path=self.get_tpf_entry_path(main_model_stem),
                new_flags=0x2,
            ).set_from_binary_file(self.tpf)

    @property
    def flver(self) -> FLVER | None:
        """Shortcut for accessing the main FLVER file (if there is only one)."""
        if self.MAX_FLVER_COUNT != 1:
            raise ValueError(f"Cannot access `flver` property of {self.__class__.__name__} with multiple FLVERs.")
        return self.get_flver(self.model_stem)

    @flver.setter
    def flver(self, value: FLVER):
        if self.MAX_FLVER_COUNT != 1:
            raise ValueError(f"Cannot set `flver` property of {self.__class__.__name__} with multiple FLVERs.")
        self.set_flver(self.model_stem, value)

    @property
    def tpf(self) -> TPF | None:
        if self.TPF_ENTRY_ID < 0:
            raise TypeError(f"Binder subclass `{self.cls_name}` does not support a TPF entry.")
        if not self._tpf:
            # Load TPF.
            try:
                tpf_entry = self.find_entry_id(self.TPF_ENTRY_ID)
            except EntryNotFoundError:
                pass  # TPF optional
            else:
                self._tpf = tpf_entry.to_binary_file(TPF)
        return self._tpf

    @tpf.setter
    def tpf(self, value: TPF | None):
        """TPF can be manually set if an entry is defined."""
        if self.TPF_ENTRY_ID < 0:
            raise TypeError(f"Binder subclass `{self.cls_name}` does not support a TPF entry.")
        if not isinstance(value, TPF) and value is not None:
            raise TypeError(f"TPF must be a `TPF` instance or `None`.")
        self._tpf = value

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
