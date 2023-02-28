from __future__ import annotations

__all__ = ["Matrix3", "Matrix4"]

import math
from dataclasses import dataclass, field

import numpy as np

from .vector import Vector3, Vector4


@dataclass(slots=True)
class Matrix3:
    """Basic wrapper for 3x3 `np.ndarray` that can be constructed from various input types."""

    _data: np.ndarray = field(default_factory=lambda: np.zeros((3, 3), dtype=np.float32))

    def __init__(self, data: np.ndarray | list | tuple):
        """Construct `Matrix3` from an existing `ndarray` or a input that can be converted to a 3x3 `np.ndarray`."""
        if isinstance(data, np.ndarray):
            if data.shape != (3, 3):
                raise ValueError(f"Input array must be 3x3, but shape is {data.shape}.")
            self._data = data.astype(np.float32)
        elif isinstance(data, (list, tuple)):
            # Nested rows.
            if len(data) == 3 and all(isinstance(row, (list, tuple)) for row in data):
                self._data = np.array(data, dtype=np.float32)
            else:
                raise ValueError(f"Cannot construct Matrix3 from shape of nested lists: {data}.")
        else:
            raise TypeError(f"Cannot construct Matrix3 from type {type(data)}.")

    @property
    def data(self) -> np.ndarray:
        return self._data

    @classmethod
    def from_flat_row_order(cls, data: list | tuple) -> Matrix3:
        """Create `Matrix3` from flattened elements, in row-first order."""
        if len(data) != 9:
            raise ValueError(f"Input list must have 9 elements, but has {len(data)}.")
        return cls(np.array(data, dtype=np.float32).reshape((3, 3)))

    def to_flat_row_order(self) -> list[float]:
        # noinspection PyTypeChecker
        return self._data.flatten().tolist()

    @classmethod
    def from_flat_column_order(cls, data) -> Matrix3:
        """Create `Matrix` from flattened elements, in column-first order."""
        if len(data) != 9:
            raise ValueError(f"Input list must have 9 elements, but has {len(data)}.")
        return cls(np.array(data, dtype=np.float32).reshape((3, 3)).T)

    def to_flat_column_order(self) -> list[int] | list[float]:
        # noinspection PyTypeChecker
        return self._data.T.flatten().tolist()

    def __matmul__(self, other: Matrix3 | Vector3):
        if isinstance(other, Matrix3):
            return Matrix3(self._data * other._data)
        elif isinstance(other, Vector3):
            return Vector3(np.inner(self._data, other))
        raise TypeError(f"Can only multiply `Matrix3` with another `Matrix3` or a `Vector3`, not `{type(other)}`.")

    def __neg__(self):
        return self.__class__(-self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    @classmethod
    def zero(cls) -> Matrix3:
        return cls(np.zeros((3, 3)))

    @classmethod
    def identity(cls) -> Matrix3:
        return cls(np.identity(3))

    @classmethod
    def from_euler_angles(cls, rx, ry=None, rz=None, radians=False, order="xzy") -> Matrix3:
        """Order defaults to XZY as per FromSoft usage (i.e. will be applied to point `p` as `Ry @ Rz @ Rx @ p`)."""
        if ry is None and rz is None:
            rx, ry, rz = rx
        if not radians:
            rx, ry, rz = math.radians(rx), math.radians(ry), math.radians(rz)
        sx, sy, sz = math.sin(rx), math.sin(ry), math.sin(rz)
        cx, cy, cz = math.cos(rx), math.cos(ry), math.cos(rz)
        m = {
            "x": cls.from_flat_row_order([1, 0, 0, 0, cx, -sx, 0, sx, cx]),
            "y": cls.from_flat_row_order([cy, 0, sy, 0, 1, 0, -sy, 0, cy]),
            "z": cls.from_flat_row_order([cz, -sz, 0, sz, cz, 0, 0, 0, 1]),
        }
        return m[order[2]] @ m[order[1]] @ m[order[0]]

    @property
    def T(self) -> Matrix3:
        """Transpose of `Matrix3`."""
        return Matrix3(self._data.T)

    def to_euler_angles(self, radians=False, order="xzy") -> Vector3:
        """Only supports order XZY for now (standard FromSoft usage)."""
        if order != "xzy":
            raise ValueError("Can only compute Euler angles for XZY rotation, as used in DS1 at least.")

        if self[1, 0] < 1:
            if self[1, 0] > -1:
                # Unique solution.
                z = math.asin(self[1, 0])
                y = math.atan2(-self[2, 0], self[0, 0])
                x = math.atan2(-self[1, 2], self[1, 1])
            else:
                # Not a unique solution: x - y = atan2(m[2, 1], m[2, 2])
                z = -math.pi / 2
                y = -math.atan2(self[2, 1], self[2, 2])
                x = 0
        else:
            # Not a unique solution: x + y = atan2(m[2, 1], m[2, 2])
            z = math.pi / 2
            y = math.atan2(self[2, 1], self[2, 2])
            x = 0

        return Vector3([x, y, z]) if radians else Vector3([math.degrees(x), math.degrees(y), math.degrees(z)])


@dataclass(slots=True)
class Matrix4:
    """Basic wrapper for 3x3 `np.ndarray` that can be constructed from various input types."""

    _data: np.ndarray = field(default_factory=lambda: np.zeros((4, 4), dtype=np.float32))

    def __init__(self, data: np.ndarray | list | tuple):
        """Construct `Matrix4` from an existing `ndarray` or a input that can be converted to a 4x4 `np.ndarray`."""
        if isinstance(data, np.ndarray):
            if data.shape != (4, 4):
                raise ValueError(f"Input array must be 4x4, but shape is {data.shape}.")
            self._data = data.astype(np.float32)
        elif isinstance(data, (list, tuple)):
            # Nested rows.
            if len(data) == 4 and all(isinstance(row, (list, tuple)) for row in data):
                self._data = np.array(data, dtype=np.float32)
            else:
                raise ValueError(f"Cannot construct Matrix4 from shape of nested lists: {data}.")
        else:
            raise TypeError(f"Cannot construct Matrix4 from type {type(data)}.")

    @property
    def data(self) -> np.ndarray:
        return self._data

    @classmethod
    def from_flat_row_order(cls, data: list | tuple) -> Matrix4:
        """Create `Matrix4` from flattened elements, in row-first order."""
        if len(data) != 12:
            raise ValueError(f"Input list must have 12 elements, but has {len(data)}.")
        return cls(np.array(data, dtype=np.float32).reshape((4, 4)))

    def to_flat_row_order(self) -> list[float]:
        # noinspection PyTypeChecker
        return self._data.flatten().tolist()

    @classmethod
    def from_flat_column_order(cls, data) -> Matrix4:
        """Create `Matrix` from flattened elements, in column-first order."""
        if len(data) != 12:
            raise ValueError(f"Input list must have 12 elements, but has {len(data)}.")
        return cls(np.array(data, dtype=np.float32).reshape((4, 4)).T)

    def to_flat_column_order(self) -> list[int] | list[float]:
        # noinspection PyTypeChecker
        return self._data.T.flatten().tolist()

    def __matmul__(self, other: Matrix4 | Vector4):
        if isinstance(other, Matrix4):
            return Matrix3(self._data * other._data)
        elif isinstance(other, Vector4):
            return Vector4(np.inner(self._data, other))
        raise TypeError(f"Can only multiply `Matrix4` with another `Matrix4` or a `Vector4`, not `{type(other)}`.")

    def __neg__(self):
        return self.__class__(-self._data)

    def __getitem__(self, key):
        return self._data[key]

    def __setitem__(self, key, value):
        self._data[key] = value

    @classmethod
    def zero(cls) -> Matrix4:
        return cls(np.zeros((4, 4)))

    @classmethod
    def identity(cls) -> Matrix4:
        return cls(np.identity(4))

    @property
    def T(self) -> Matrix4:
        """Transpose of `Matrix4`."""
        return Matrix4(self._data.T)

    # region Homogenous Matrix Methods

    def get_rotation_submatrix(self) -> Matrix3:
        return Matrix3(self._data[:3, :3])

    @classmethod
    def from_translate(cls, translate: Vector3) -> Matrix4:
        return cls(np.array([
            [1.0, 0.0, 0.0, translate.x],
            [0.0, 1.0, 0.0, translate.y],
            [0.0, 0.0, 1.0, translate.z],
            [0.0, 0.0, 0.0, 1.0],
        ]))

    @classmethod
    def from_scale(cls, scale: Vector3) -> Matrix4:
        return cls(np.array([
            [scale.x, 0.0, 0.0, 0.0],
            [0.0, scale.y, 0.0, 0.0],
            [0.0, 0.0, scale.z, 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ]))

    @classmethod
    def from_rotation_matrix3(cls, rotation: Matrix3) -> Matrix4:
        return cls(np.array([
            [rotation[0, 0], rotation[0, 1], rotation[0, 2], 0.0],
            [rotation[1, 0], rotation[1, 1], rotation[1, 2], 0.0],
            [rotation[2, 0], rotation[2, 1], rotation[2, 2], 0.0],
            [0.0, 0.0, 0.0, 1.0],
        ]))

    def get_translate(self) -> Vector3:
        return Vector3(self._data[:3, 3])

    def set_translate(self, translate_vector: Vector3):
        """Set the translate part of the matrix (first three elements of last column)."""
        self._data[:3, 3] = translate_vector

    # endregion
