from __future__ import annotations

__all__ = ["BaseNVMBND"]

import abc
from dataclasses import field

from soulstruct.containers import Binder, EntryNotFoundError
from .nvm import NVM


class BaseNVMBND(Binder, abc.ABC):
    """Manage `NVM` entries in a Binder. Game-specific subclasses will want to set their own Binder defaults."""

    map_stem: str = ""

    # Managed entry file instances.
    _nvms: dict[str, NVM] = field(default_factory=dict)  # should be accessed with `get_nvm()` and `set_nvm()` methods

    def get_nvm(self, model_stem: str) -> NVM:
        """Look for loaded NVM or try to load it from an NVM entry (DCX agnostic)."""
        if model_stem in self._nvms:
            return self._nvms[model_stem]  # already loaded/set

        # Look for entry to load into managed NVM dictionary.
        try:
            entry = self.find_entry_matching_name(rf"{model_stem}\.nvm(\.dcx)?")
        except EntryNotFoundError:
            raise KeyError(f"NVM with model stem '{model_stem}' not loaded in `{self.cls_name}` and no entry found.")

        nvm = entry.to_binary_file(NVM)
        self._nvms[model_stem] = nvm
        return nvm

    def has_nvm(self, model_stem) -> bool:
        """Check if model is in loaded NVMs or is present as an unloaded entry."""
        if model_stem in self._nvms:
            return True

        try:
            self.find_entry_matching_name(rf"{model_stem}\.nvm(\.dcx)?")
        except EntryNotFoundError:
            return False
        return True

    def set_nvm(self, model_stem: str, nvm: NVM):
        """Set NVM in managed dictionary. Will be written to a new/existing entry on `NVMBND` write."""
        self._nvms[model_stem] = nvm

    def remove_nvm(self, model_stem: str):
        """Remove NVM from managed dictionary (if loaded) and/or remove entry from `NVMBND`.

        Raises `KeyError` if NVM is not loaded AND entry is not found.
        """
        removed_nvm = False
        if model_stem in self._nvms:
            del self._nvms[model_stem]
            removed_nvm = True

        # Look for entry to remove.
        try:
            entry = self.find_entry_matching_name(rf"{model_stem}\.nvm(\.dcx)?")
        except EntryNotFoundError:
            if removed_nvm:
                return  # fine, as we removed an NVM that WOULD have been written
            raise KeyError(
                f"Cannot remove NVM with model stem '{model_stem}': not loaded in `{self.cls_name}` and no entry found."
            )

        self.remove_entry(entry)

    def entry_autogen(self):
        """Replace/create NVM Binder entries. Note that existing, non-overwritten entries are NOT removed."""

        if not self._nvms:
            return  # no new/replaced entries to create

        sorted_nvm_stems = sorted(self._nvms.keys())
        first_entry_id = len(self.entries)
        for i, model_stem in enumerate(sorted_nvm_stems):
            nvm = self._nvms[model_stem]
            nvm_name = nvm.dcx_type.process_path(f"{model_stem}.nvm")
            self.set_default_entry(
                entry_spec=nvm_name,
                new_id=first_entry_id + i,
                new_path=nvm.dcx_type.process_path(self.get_nvm_entry_path(model_stem)),
                new_flags=0x2,
            ).set_from_binary_file(nvm)

    def get_nvm_entry_path(self, model_stem: str) -> str:
        """NVM paths tend to be very straightforward."""
        if not self.map_stem:
            if self.path:
                map_stem = self.path.name.split(".")[0]
            else:
                raise ValueError(
                    "NVMBND must have a `map_stem` (or `path` whose stem can be used) for NVM entry paths."
                )
        else:
            map_stem = self.map_stem

        return f"{map_stem}\\{model_stem}.nvm"  # no DCX
