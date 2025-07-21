from __future__ import annotations

__all__ = ["VECTOR_LIKE", "BaseVector", "Vector2", "Vector3", "Vector4"]

import abc
import ast
import math
import re
import typing as tp

import numpy as np

from .constants import SINGLE_MIN, SINGLE_MAX


# Acceptable types for `BaseVector()` constructor.
VECTOR_LIKE = tp.Union["BaseVector", np.ndarray, list[float | int], tuple[float | int, ...]]


class BaseVector(abc.ABC):
    """Simple immutable NumPy row vector wrapper.

    Does little more than enforce length, expose `x`, `y`, etc. getters, and offer a few other convenient methods.

    For large numbers of vectors (e.g. mesh vertices), direct NumPy array operations are strongly recommended instead.
    See `FLVER.Mesh` class for an example.
    """
    __slots__ = ("_data",)
    __array_priority__ = 1000  # for numpy array operations
    _RE_FROM_REPR = re.compile(r"^(\w+)\((.+)\)$")  # e.g. "Vector3(1, 2, 3)"

    LENGTH: tp.ClassVar[int]
    REPR_PRECISION: tp.ClassVar[int] = 5

    _data: np.ndarray

    def __init__(self, data: VECTOR_LIKE):
        if len(data) != self.LENGTH:
            raise ValueError(f"Vector must have length {self.LENGTH} (got {len(data)}).")
        if isinstance(data, BaseVector):
            arr = data._data.copy()
        else:
            arr = np.asarray(data, dtype=float)
        arr.setflags(write=False)  # read-only
        object.__setattr__(self, "_data", arr)

    def __array__(self, dtype=None):
        return self._data if dtype is None else self._data.astype(dtype, copy=False)

    # READ-ONLY

    def __setattr__(self, name: str, value: tp.Any):
        raise AttributeError(f"{self.__class__.__name__} is immutable.")

    def __setitem__(self, index: int, value: tp.Any):
        raise TypeError(f"{self.__class__.__name__} is immutable")

    def __copy__(self) -> tp.Self:
        """Vector is immutable, so shallow copy is the same as this vector."""
        return self

    def __deepcopy__(self, memo: tp.Dict[int, tp.Any]) -> tp.Self:
        """Vector is immutable, so deep copy is the same as this vector."""
        return self

    # NUMPY ARRAY-LIKE OPERATIONS

    def __add__(self, other) -> tp.Self:
        return self.__class__(np.add(self._data, other))

    def __radd__(self, other) -> tp.Self:
        return self.__class__(np.add(other, self._data))

    def __sub__(self, other) -> tp.Self:
        return self.__class__(np.subtract(self._data, other))

    def __rsub__(self, other) -> tp.Self:
        return self.__class__(np.subtract(other, self._data))

    def __mul__(self, other) -> tp.Self:
        return self.__class__(np.multiply(self._data, other))

    def __rmul__(self, other) -> tp.Self:
        return self.__class__(np.multiply(other, self._data))

    def __truediv__(self, other) -> tp.Self:
        return self.__class__(np.true_divide(self._data, other))

    def __rtruediv__(self, other) -> tp.Self:
        return self.__class__(np.true_divide(other, self._data))

    def __neg__(self) -> tp.Self:
        return self.__class__(np.negative(self._data))

    def __matmul__(self, other: VECTOR_LIKE) -> float | tp.Self:
        """Dot product with another vector."""
        if isinstance(other, self.__class__):
            return float(self._data @ other._data)
        try:
            other_vec = self.__class__(other)
        except (ValueError, TypeError):
            return NotImplemented  # Python will try `__rmatmul__` on `other`
        return float(self._data @ other_vec._data)

    # No need to implement `__rmatmul__`, as all compatible Matrix/Vector types will define identical `__matmul__`.

    # BASICS

    def __len__(self) -> int:
        return self.LENGTH

    def __getitem__(self, index: int) -> float:
        # noinspection PyTypeChecker
        return self._data[index]

    def __eq__(self, other_vector: BaseVector):
        return np.array_equal(self._data, other_vector._data)

    def __iter__(self) -> tp.Iterator[float]:
        return iter(self._data)

    def __repr__(self) -> str:
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
        return float(np.linalg.norm(self._data))

    get_magnitude = __abs__
    norm = __abs__

    def __hash__(self) -> int:
        """Hashed by tuple of (immutable) data."""
        return hash(tuple(self._data))

    def get_squared_magnitude(self) -> float:
        return sum(v ** 2 for v in self._data)

    def normalize(self) -> tp.Self:
        """Return a copy of this `Vector` with unit magnitude.

        Raises `ZeroDivisionError` if this vector is zero.
        """
        n = abs(self)
        if n == 0.0:
            raise ZeroDivisionError("Cannot normalize a zero vector.")
        return self / n

    def dot(self, other_vector: BaseVector) -> float:
        return float(np.inner(self._data, other_vector._data))

    def allclose(self, other: BaseVector, rtol: float = 1e-05, atol: float = 1e-08) -> bool:
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
        # noinspection PyTypeChecker
        return self._data[0]

    @property
    def y(self) -> float:
        # noinspection PyTypeChecker
        return self._data[1]

    @classmethod
    def from_repr(cls, s: str) -> tp.Self:
        """Extract numeric payload from `repr`-style string (e.g. for JSON decoding).

        Raises `ValueError` if the string does not match `cls` or if the number of elements is wrong.
        """
        m = cls._RE_FROM_REPR.match(s.strip())
        if not m:
            raise ValueError(f"Cannot parse vector string {s!r}")
        name, payload = m.groups()

        if name != cls.__name__:
            raise ValueError(f"Cannot parse vector string: {s!r} is a {name}, not a {cls.__name__}.")

        try:
            values = list(ast.literal_eval(f"({payload})"))
        except Exception as e:
            raise ValueError(f"Cannot parse vector string: Bad numeric payload in {s!r}") from e

        if len(values) != cls.LENGTH:
            raise ValueError(f"{cls.__name__} needs {cls.LENGTH} numbers (got {len(values)}) in string {s!r}).")
        return cls(values)


class Vector2(BaseVector):
    """Simple [x, y] container."""
    LENGTH: tp.ClassVar[int] = 2


class Vector3(BaseVector):
    """Simple [x, y, z] container."""
    LENGTH: tp.ClassVar[int] = 3

    @property
    def z(self) -> float:
        # noinspection PyTypeChecker
        return self._data[2]

    @classmethod
    def from_vector4(cls, vector4: Vector4) -> Vector3:
        """Drop the `w` component from a `Vector4` to create a `Vector3`."""
        return cls((vector4.x, vector4.y, vector4.z))

    def cross(self, other_vector: Vector3) -> Vector3:
        return Vector3(np.cross(self._data, other_vector._data))

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
        """Swap Y and Z axes, so that the vector is in XZY order."""
        # noinspection PyTypeChecker
        return Vector3([self._data[0], self._data[2], self._data[1]])


class Vector4(BaseVector):
    """Simple [x, y, z, w] container."""
    LENGTH: tp.ClassVar[int] = 4

    @property
    def z(self) -> float:
        # noinspection PyTypeChecker
        return self._data[2]

    @property
    def w(self) -> float:
        # noinspection PyTypeChecker
        return self._data[3]

    @classmethod
    def from_vector3(cls, vector3: Vector3, w=1.0) -> Vector4:
        """Create a `Vector4` from a `Vector3`, adding a `w` component."""
        return cls((vector3.x, vector3.y, vector3.z, w))
