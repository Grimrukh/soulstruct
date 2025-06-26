from __future__ import annotations

__all__ = ["BaseVector", "Vector2", "Vector3", "Vector4"]

import abc
import ast
import math
import re
import typing as tp
from dataclasses import dataclass

import numpy as np

from .constants import SINGLE_MIN, SINGLE_MAX

if tp.TYPE_CHECKING:
    from .matrix import Matrix3, Matrix4


@dataclass(slots=True)
class BaseVector(abc.ABC):
    """Simple numpy row vector wrapper."""
    LENGTH: tp.ClassVar[int]
    REPR_PRECISION: tp.ClassVar[int] = 5

    _data: np.ndarray

    def __init__(self, data: np.ndarray | list | tuple):
        if len(data) != self.LENGTH:
            raise ValueError(f"Vector must have length {self.LENGTH} (got {len(data)})")
        if isinstance(data, np.ndarray):
            self._data = data.astype(float)
        else:
            self._data = np.array(data, dtype=float)

    @property
    def data(self) -> np.ndarray:
        return self._data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value: float):
        self._data[index] = value

    def __eq__(self, other_vector: BaseVector):
        return np.array_equal(self._data, other_vector._data)

    def __add__(self, other) -> tp.Self:
        return self.__class__(np.add(self, other))

    def __radd__(self, other) -> tp.Self:
        return self.__class__(np.add(other, self))

    def __sub__(self, other) -> tp.Self:
        return self.__class__(np.subtract(self, other))

    def __mul__(self, other) -> tp.Self:
        return self.__class__(np.multiply(self, other))

    def __rmul__(self, other) -> tp.Self:
        return self.__class__(np.multiply(other, self))

    def __truediv__(self, other) -> tp.Self:
        return self.__class__(np.true_divide(self, other))

    def __rtruediv__(self, other) -> tp.Self:
        return self.__class__(np.true_divide(other, self))

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        elements = []
        for x in self._data:
            if x == SINGLE_MIN:
                elements.append("<SINGLE_MIN>")
            elif x == SINGLE_MAX:
                elements.append("<SINGLE_MAX>")
            else:
                elements.append(f"{x:.{self.REPR_PRECISION}}")
        return f"{self.__class__.__name__}(({', '.join(elements)}))"

    def __abs__(self) -> float:
        """Get norm of `Vector`."""
        return math.sqrt(np.sum(np.power(self._data, 2)))

    def __hash__(self):
        """Simply hashed by tuple of data."""
        return hash(tuple(self._data))

    def get_magnitude(self) -> float:
        return abs(self)

    def get_squared_magnitude(self) -> float:
        return sum(v ** 2 for v in self._data)

    def normalize(self) -> tp.Self:
        """Return a copy of this `Vector` with unit magnitude."""
        return self.copy() / abs(self)

    def __neg__(self) -> tp.Self:
        return self.__class__(-self._data)

    def dot(self, other_vector: BaseVector) -> float:
        return float(np.inner(self._data, other_vector._data))

    def copy(self) -> tp.Self:
        return self.__class__(self._data.copy())

    def is_close(self, other: BaseVector, rtol: float = 1e-05, atol: float = 1e-08) -> bool:
        return np.allclose(self._data, other._data, rtol=rtol, atol=atol)

    @classmethod
    def zero(cls) -> tp.Self:
        return cls(np.zeros(cls.LENGTH, dtype=float))

    @classmethod
    def one(cls) -> tp.Self:
        return cls(np.ones(cls.LENGTH, dtype=float))

    @classmethod
    def single_min(cls) -> tp.Self:
        return cls(np.full(cls.LENGTH, SINGLE_MIN, dtype=float))

    @classmethod
    def single_max(cls) -> tp.Self:
        return cls(np.full(cls.LENGTH, SINGLE_MAX, dtype=float))

    @property
    def x(self) -> float:
        return self._data[0]

    @x.setter
    def x(self, value: float):
        self._data[0] = value

    @property
    def y(self):
        return self._data[1]

    @y.setter
    def y(self, value: float):
        self._data[1] = value


@dataclass(slots=True, init=False, repr=False, eq=False)
class Vector2(BaseVector):
    """Simple [x, y] container."""
    LENGTH: tp.ClassVar[int] = 2

    @classmethod
    def from_repr(cls, repr_string: str) -> Vector2:
        """For JSON decoding."""
        if (match := re.match(r"^Vector2(\([\d .,]+\))", repr_string)) is not None:
            return cls(ast.literal_eval(match.group(1)))
        raise ValueError(f"Cannot read `Vector2` string: {repr_string}")


@dataclass(slots=True, init=False, repr=False, eq=False)
class Vector3(BaseVector):
    """Simple [x, y, z] container."""
    LENGTH: tp.ClassVar[int] = 3

    @property
    def z(self):
        return self._data[2]

    @z.setter
    def z(self, value: float):
        self._data[2] = value

    @classmethod
    def from_vector4(cls, vector4: Vector4) -> Vector3:
        return cls((vector4.x, vector4.y, vector4.z))

    @classmethod
    def from_repr(cls, repr_string: str) -> Vector3:
        """For JSON decoding."""
        if (match := re.match(r"^Vector3(\([-\d., ]+\))", repr_string)) is not None:
            return cls(ast.literal_eval(match.group(1)))
        raise ValueError(f"Cannot read `Vector3` string: {repr_string}")

    def cross(self, other_vector: Vector3) -> Vector3:
        return Vector3(np.cross(self._data, other_vector._data))

    def multiply_by_matrix(self, matrix3: Matrix3):
        return Vector3(np.inner(matrix3.data, self._data))

    # noinspection PyPackageRequirements
    def is_same_euler_rotation(self, other_euler: Vector3, order="xzy", tolerance: float = 1e-6) -> bool:
        """Checks if two Euler rotations are the same, within a tolerance.

        Typically only needed for debugging. Requires either `scipy` or Blender `mathutils` to be installed. Note that
        the exact meaning of `tolerance` depends on which one happens (angle tolerance or rot-mat element tolerance).
        """
        try:
            from scipy.spatial.transform import Rotation
        except ImportError:
            try:
                from mathutils import Euler
            except ImportError:
                raise ImportError(
                    "Either `scipy` or Blender `mathutils` must be installed to use `Vector3.is_same_euler_rotation()`."
                )
            else:
                # mathutils method: compare quaternion angles
                this_quat = Euler(self._data).to_quaternion()
                other_quat = Euler(other_euler._data).to_quaternion()
                angle = this_quat.rotation_difference(other_quat).angle
                return angle < tolerance or angle < (2 * math.pi - tolerance)
        else:
            # scipy method: compare all rotation matrix elements
            this_mat = Rotation.from_euler(order, self._data).as_matrix()
            other_mat = Rotation.from_euler(order, other_euler._data).as_matrix()
            return np.allclose(this_mat, other_mat, atol=tolerance)

    def get_as_axes(self, axes: str) -> Vector2 | Vector3:
        """Reorder and/or negate axes, e.g. `get_as_axes("-x-zy")`."""
        new_data = []
        axes_done = set()
        negate = False
        for c in axes:
            if c == "-":
                negate = not negate
            elif c in {"x", "y", "z"}:
                if c in axes_done:
                    raise ValueError(f"Axis '{c}' appears multiple times in `axes` string.")
                axes_done.add(c)
                new_data.append(-getattr(self, c) if negate else getattr(self, c))
                negate = False
            else:
                raise ValueError(f"Invalid `axes` character: '{c}'. Should be '-' or in 'xyz'.")
        if len(new_data) == 2:
            return Vector2(new_data)
        elif len(new_data) == 3:
            return Vector3(new_data)
        else:
            raise ValueError(f"Not enough axes given in `axes`: '{axes}'. Must be at least 2.")

    def to_xzy(self) -> Vector3:
        return Vector3([self._data[0], self._data[2], self._data[1]])


@dataclass(slots=True, init=False, repr=False, eq=False)
class Vector4(BaseVector):
    """Simple [x, y, z, w] container."""
    LENGTH: tp.ClassVar[int] = 4

    @property
    def z(self):
        return self._data[2]

    @z.setter
    def z(self, value: float):
        self._data[2] = value

    @property
    def w(self):
        return self._data[3]

    @w.setter
    def w(self, value: float):
        self._data[3] = value

    @classmethod
    def from_vector3(cls, vector3: Vector3, w=1.0) -> Vector4:
        return cls((vector3.x, vector3.y, vector3.z, w))

    @classmethod
    def from_repr(cls, repr_string: str) -> Vector4:
        """For JSON decoding."""
        if (match := re.match(r"^Vector4(\([\d .,]+\))", repr_string)) is not None:
            return cls(ast.literal_eval(match.group(1)))
        raise ValueError(f"Cannot read `Vector4` string: {repr_string}")

    def multiply_by_matrix(self, matrix4: Matrix4) -> Vector4:
        return Vector4(np.inner(matrix4.data, self._data))
