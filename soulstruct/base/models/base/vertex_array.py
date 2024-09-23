from __future__ import annotations

__all__ = [
    "BaseVertexArray",
]

import typing as tp
from dataclasses import dataclass

import numpy as np
from .vertex_array_layout import BaseVertexArrayLayout

LAYOUT_T = tp.TypeVar("LAYOUT_T", bound=BaseVertexArrayLayout)


@dataclass(slots=True)
class BaseVertexArray(tp.Generic[LAYOUT_T]):
    """Wraps a structured NumPy array containing vertex data for a particular FLVER submesh.

    ABC so that `FLVER0` can also use it with different signatures.
    """

    array: np.ndarray
    layout: LAYOUT_T

    def has_field(self, name: str) -> bool:
        return name in self.array.dtype.names

    @property
    def dtype(self) -> np.dtype:
        """Wraps NumPy array dtype."""
        return self.array.dtype

    @property
    def has_normal_w_bone_indices(self):
        """Just checks if ANY `normal_w` values are not 127."""
        return "normal_w" in self.array.dtype.names and not np.all(self.array["normal_w"] == 127)

    def __getitem__(self, key):
        """Wraps NumPy array indexing."""
        return self.array[key]

    def __setitem__(self, key, value):
        """Wraps NumPy array indexing."""
        self.array[key] = value

    def __len__(self):
        """Wraps NumPy array length."""
        return len(self.array)
