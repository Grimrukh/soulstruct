from __future__ import annotations

__all__ = ["BaseNVMBND"]

import abc
from dataclasses import dataclass, field

from soulstruct.containers import Binder, BinderEntry
from .nvm import NVM


@dataclass(slots=True)
class BaseNVMBND(Binder, abc.ABC):
    """Manage `NVM` entries in a Binder. Game-specific subclasses will want to set their own Binder defaults."""

    map_stem: str = ""
    nvms: dict[str, NVM] = field(default_factory=dict)

    def __post_init__(self):
        """Loads FIRST instance of each entry name as an MTD."""
        if self.nvms:
            return  # already passed in

        self.nvms = {}
        for entry in self.entries:
            if entry.name in self.nvms:
                continue  # ignore repeated names silently
            self.nvms[entry.minimal_stem] = entry.to_binary_file(NVM)

    def entry_autogen(self):
        """Generate `NVM` entries from `NVM` instances."""
        self.entries = []
        sorted_nvm_stems = sorted(self.nvms.keys())
        for i, nvm_stem in enumerate(sorted_nvm_stems):
            self.entries.append(
                BinderEntry(bytes(self.nvms[nvm_stem]), entry_id=i, path=self.get_nvm_entry_path(nvm_stem), flags=0x2)
            )

    def get_nvm_entry_path(self, nvm_stem: str) -> str:

        if not self.map_stem:
            if self.path:
                map_stem = self.path.name.split(".")[0]
            else:
                raise ValueError(
                    "NVMBND must have a `map_stem` (or `path` whose stem can be used) for NVM entry paths."
                )
        else:
            map_stem = self.map_stem

        return f"{map_stem}\\{nvm_stem}.nvm"  # no DCX
