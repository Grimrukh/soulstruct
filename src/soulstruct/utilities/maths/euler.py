"""Euler angle container.

NOTE: These classes do not provide conversion methods to/from matrices or quaternions. They are considered more
primitive; use the methods of those other classes instead.
"""
from __future__ import annotations

__all__ = ["EulerBase", "EulerDeg", "EulerRad", "EULER_DEG_LIKE", "EULER_RAD_LIKE"]

import abc
import ast
import math
import re
import typing as tp

import numpy as np

from .constants import SINGLE_MIN, SINGLE_MAX


# Acceptable types for constructors.
EULER_DEG_LIKE = tp.Union["EulerDeg", np.ndarray, list[float | int], tuple[float | int, ...]]
EULER_RAD_LIKE = tp.Union["EulerRad", np.ndarray, list[float | int], tuple[float | int, ...]]


class EulerBase(abc.ABC):
    """Simple immutable [pitch, yaw, roll] container.

    Applied in XZY (pitch, roll, yaw) order.

    Note that this is just a `Vector3` with different property names. It does not enforce any particular rotation order
    or have any special rotation methods. However, methods can check for `isinstance(..., Euler)` if desired to treat
    it differently from a generic `Vector3` (e.g. rotation transform vs. translate transform).

    This abstract base class is fully implemented by `EulerDeg` and `EulerRad`.
    """
    __slots__ = ("_data",)

    __array_priority__ = 1000  # for numpy array operations
    _RE_FROM_REPR: tp.ClassVar[re.Pattern] = re.compile(r"^(\w+)\((.+)\)$")  # e.g. "EulerDeg(1, 2, 3)"
    REPR_PRECISION: tp.ClassVar[int] = 5
    ORDER = "XZY"

    _data: np.ndarray

    def __init__(self, data: tp.Sequence[float]):
        if len(data) != 3:
            raise ValueError(f"{self.__class__.__name__} must have length 3 (got {len(data)}).")
        if isinstance(data, self.__class__):
            arr = data._data.copy()
        else:
            arr = np.asarray(data, dtype=float)
        object.__setattr__(self, "_data", arr)

    def __array__(self, dtype=None):
        return self._data if dtype is None else self._data.astype(dtype, copy=False)

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

    def copy(self) -> tp.Self:
        """Vector is immutable, so copy is the same as this vector."""
        return self

    def __getstate__(self):
        return tuple(self._data)

    def __setstate__(self, state: tuple[float, ...]):
        object.__setattr__(self, "_data", np.array(state, dtype=float))

    def __len__(self) -> int:
        return 3

    def __getitem__(self, index: int) -> float:
        # noinspection PyTypeChecker
        return self._data[index]

    @abc.abstractmethod
    def __eq__(self, other_euler: EulerBase):
        ...

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

    def __hash__(self) -> int:
        """Hashed by tuple of (immutable) data."""
        return hash(tuple(self._data))

    def allclose(self, other: EulerBase, rtol: float = 1e-05, atol: float = 1e-08) -> bool:
        return np.allclose(self._data, other._data, rtol=rtol, atol=atol)

    # Only basic arithmetic is supported; no vector-specific operations.
    def __add__(self, other: EulerBase) -> tp.Self:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self._data + other._data)

    def __sub__(self, other: EulerBase) -> tp.Self:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.__class__(self._data - other._data)

    def __neg__(self) -> tp.Self:
        return self.__class__(-self._data)

    def __mul__(self, scalar: float) -> tp.Self:
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return self.__class__(self._data * scalar)

    def __rmul__(self, scalar: float) -> tp.Self:
        return self.__mul__(scalar)

    def __truediv__(self, scalar: float) -> tp.Self:
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return self.__class__(self._data / scalar)

    def __rtruediv__(self, scalar: float) -> tp.Self:
        if not isinstance(scalar, (int, float)):
            return NotImplemented
        return self.__class__(scalar / self._data)

    @classmethod
    def zero(cls) -> tp.Self:
        return cls((0.0, 0.0, 0.0))

    @property
    def x(self) -> float:
        return self._data[0]

    @property
    def y(self) -> float:
        return self._data[1]

    @property
    def z(self) -> float:
        return self._data[2]

    @property
    def pitch(self) -> float:
        return self._data[0]

    @property
    def yaw(self) -> float:
        return self._data[1]

    @property
    def roll(self) -> float:
        return self._data[2]

    @classmethod
    def from_repr(cls, s: str) -> tp.Self:
        """Extract numeric payload from `repr`-style string (e.g. for JSON decoding).

        Raises `ValueError` if the string does not match `cls` or if the number of elements is wrong.
        """
        m = cls._RE_FROM_REPR.match(s.strip())
        if not m:
            raise ValueError(f"Cannot parse Euler string {s!r}")
        name, payload = m.groups()

        if name != cls.__name__:
            raise ValueError(f"Cannot parse Euler string: {s!r} is a {name}, not a {cls.__name__}.")

        try:
            values = list(ast.literal_eval(f"({payload})"))
        except Exception as e:
            raise ValueError(f"Cannot parse Euler string: Bad numeric payload in {s!r}") from e

        if len(values) != 3:
            raise ValueError(f"{cls.__name__} needs 3 numbers (got {len(values)}) in string {s!r}).")
        return cls(values)


class EulerDeg(EulerBase):
    """Euler angles in degrees.

    NOTE: Units are not enforced; it is up to the user to use the correct container.
    """

    def __eq__(self, other_euler: EulerDeg):
        return isinstance(other_euler, EulerDeg) and np.array_equal(self._data, other_euler._data)

    def to_rad(self) -> EulerRad:
        """Convert to radians."""
        return EulerRad((math.radians(self.x), math.radians(self.y), math.radians(self.z)))


class EulerRad(EulerBase):
    """Euler angles in radians.

    NOTE: Units are not enforced; it is up to the user to use the correct container.
    """

    def __eq__(self, other_euler: EulerRad):
        return isinstance(other_euler, EulerRad) and np.array_equal(self._data, other_euler._data)

    def to_deg(self) -> EulerDeg:
        """Convert to degrees."""
        return EulerDeg((math.degrees(self.x), math.degrees(self.y), math.degrees(self.z)))
