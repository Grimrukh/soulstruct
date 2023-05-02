from __future__ import annotations

__all__ = ["BaseVector", "Vector2", "Vector3", "Vector4"]

import abc
import ast
import math
import re
import typing as tp
from dataclasses import dataclass

import numpy as np

try:
    Self = tp.Self
except AttributeError:
    Self = "Vector"

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

    def __add__(self, other) -> Self:
        return self.__class__(np.add(self, other))

    def __radd__(self, other) -> Self:
        return self.__class__(np.add(other, self))

    def __sub__(self, other) -> Self:
        return self.__class__(np.subtract(self, other))

    def __mul__(self, other) -> Self:
        return self.__class__(np.multiply(self, other))

    def __rmul__(self, other) -> Self:
        return self.__class__(np.multiply(other, self))

    def __truediv__(self, other) -> Self:
        return self.__class__(np.true_divide(other, self))

    def __rtruediv__(self, other) -> Self:
        return self.__class__(np.true_divide(other, self))

    def __iter__(self):
        return iter(self._data)

    def __repr__(self):
        elements = []
        for x in self._data:
            if x == 340282346638528859811704183484516925440.0:
                elements.append("<SINGLE_MAX>")
            elif x == -340282346638528859811704183484516925440.0:
                elements.append("<SINGLE_MIN>")
            else:
                elements.append(f"{x:.{self.REPR_PRECISION}}")
        return f"{self.__class__.__name__}({', '.join(elements)})"

    def __abs__(self) -> float:
        """Get norm of `Vector`."""
        return math.sqrt(sum(v ** 2 for v in self._data))

    def __hash__(self):
        """Simply hashed by tuple of data."""
        return hash(tuple(self._data))

    def get_magnitude(self) -> float:
        return abs(self)

    def get_squared_magnitude(self) -> float:
        return sum(v ** 2 for v in self._data)

    def normalize(self) -> Self:
        """Return a copy of this `Vector` with unit magnitude."""
        return self.copy() / abs(self)

    def __neg__(self) -> Self:
        return self.__class__(-self._data)

    def dot(self, other_vector: BaseVector) -> float:
        return float(np.inner(self._data, other_vector._data))

    def copy(self) -> Self:
        return self.__class__(self._data.copy())

    @classmethod
    def zero(cls) -> Self:
        return cls(np.zeros(cls.LENGTH, dtype=float))

    @classmethod
    def one(cls) -> Self:
        return cls(np.ones(cls.LENGTH, dtype=float))

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
        return Vector3(np.inner(matrix3, self._data))

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


@dataclass(slots=True, init=False)
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
        return Vector4(np.inner(matrix4, self._data))
