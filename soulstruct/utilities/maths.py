"""Mathematical classes and functions uses by Soulstruct."""
from __future__ import annotations

__all__ = [
    "Vector",
    "Vector2",
    "Vector3",
    "Vector4",
    "Matrix3",
    "Matrix4",
    "shift_msb_coordinates",
    "shift",
    "matrix_multiply",
    "resolve_rotation",
    "get_distance",
]

import abc
import ast
import math
import re
import typing as tp
from dataclasses import dataclass


@dataclass(slots=True)
class Vector(abc.ABC):
    """Simple float container."""

    REPR_PRECISION = 3

    _data: list[float, ...]

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value: float):
        self._data[index] = value

    def to_mat_column(self):
        return [[x] for x in self._data]

    def to_mat_row(self):
        return [list(self._data)]

    def __eq__(self, other_vector: Vector):
        return self._data == other_vector._data

    def __add__(self, other):
        return self._arithmetic(other, float.__add__, "add to")

    def __radd__(self, other):
        return self._arithmetic(other, float.__radd__, "add to")

    def __sub__(self, other):
        return self._arithmetic(other, float.__sub__, "subtract from")

    def __mul__(self, other):
        return self._arithmetic(other, float.__mul__, "multiply")

    def __rmul__(self, other):
        return self._arithmetic(other, float.__rmul__, "multiply")

    def __truediv__(self, other):
        return self._arithmetic(other, float.__truediv__, "divide")

    def __rtruediv__(self, other):
        return self._arithmetic(other, float.__rtruediv__, "divide")

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
        return math.sqrt(sum(v ** 2 for v in self))

    def __hash__(self):
        """Simply hashed by data."""
        return hash(tuple(self._data))

    def is_identity(self) -> bool:
        return all(v == 1.0 for v in self._data)

    def get_magnitude(self) -> float:
        return abs(self)

    def get_squared_magnitude(self) -> float:
        return sum(v ** 2 for v in self)

    def normalize(self):
        """Return a copy of this `Vector` with unit magnitude."""
        return self.copy() / abs(self)

    @abc.abstractmethod
    def __neg__(self):
        pass

    @abc.abstractmethod
    def _arithmetic(self, other, op_func: tp.Callable[[float, float], float], op_name: str) -> Vector:
        pass

    @abc.abstractmethod
    def dot(self, other_vector: Vector) -> float:
        pass

    @abc.abstractmethod
    def copy(self):
        pass

    @classmethod
    @abc.abstractmethod
    def zero(cls):
        pass

    @classmethod
    @abc.abstractmethod
    def ones(cls):
        pass

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


class Vector2(Vector):
    """Simple [x, y] container."""

    def __init__(self, x, y):
        self._data = [float(x), float(y)]

    def __neg__(self):
        return Vector2(-self._data[0], -self._data[1])

    def _arithmetic(self, other, op_func: tp.Callable[[float, float], float], op_name: str):
        if isinstance(other, Vector2):
            x, y = [op_func(self._data[i], other._data[i]) for i in range(2)]
        elif isinstance(other, (list, tuple)):
            if len(other) != 2:
                raise ValueError(f"List or tuple to {op_name} `Vector2` must have 2 elements.")
            x, y = [op_func(self._data[i], other[i]) for i in range(2)]
        elif isinstance(other, (int, float)):
            x, y = [op_func(x, other) for x in self._data]
        else:
            raise TypeError(f"`Vector2` arithmetic not defined for type {type(other)}.")
        return Vector2(x, y)

    def dot(self, other_vector) -> float:
        if len(other_vector) != 2:
            raise TypeError(f"Cannot only use `dot` with another Vector/sequence of length 2.")
        return sum(self[i] * other_vector[i] for i in range(2))

    def copy(self):
        return Vector2(*self._data)

    @classmethod
    def from_repr(cls, repr_string: str) -> Vector2:
        """For JSON decoding."""
        if (match := re.match(r"^Vector2(\([\d .,]+\))", repr_string)) is not None:
            return cls(*ast.literal_eval(match.group(1)))
        raise ValueError(f"Cannot read `Vector2` string: {repr_string}")

    @classmethod
    def zero(cls):
        return Vector2(0.0, 0.0)

    @classmethod
    def ones(cls):
        return Vector2(1.0, 1.0)


class Vector3(Vector):
    """Simple [x, y, z] container."""

    def __init__(self, x, y, z):
        self._data = [float(x), float(y), float(z)]

    @property
    def y(self):
        return self._data[1]

    @y.setter
    def y(self, value: float):
        self._data[1] = value

    @property
    def z(self):
        return self._data[2]

    @z.setter
    def z(self, value: float):
        self._data[2] = value

    @classmethod
    def from_row_mat(cls, row_mat):
        return cls(row_mat[0][0], row_mat[0][1], row_mat[0][2])

    @classmethod
    def from_column_mat(cls, column_mat):
        return cls(column_mat[0][0], column_mat[1][0], column_mat[2][0])

    @classmethod
    def from_repr(cls, repr_string: str) -> Vector3:
        """For JSON decoding."""
        if (match := re.match(r"^Vector3(\([-\d., ]+\))", repr_string)) is not None:
            return cls(*ast.literal_eval(match.group(1)))
        raise ValueError(f"Cannot read `Vector3` string: {repr_string}")

    def cross(self, other_vector: Vector3) -> Vector3:
        if len(other_vector) != 3:
            raise TypeError("Cannot only use `cross` with another Vector3 or sequence of length 3.")
        return Vector3(
            self.y * other_vector.z - self.z * other_vector.y,
            self.z * other_vector.x - self.x * other_vector.z,
            self.x * other_vector.y - self.y * other_vector.x,
        )

    def transform(self, matrix3: Matrix3):
        return Vector3(*list(zip(*matrix_multiply(matrix3, self.to_mat_column())))[0])

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
            return Vector2(*new_data)
        elif len(new_data) == 3:
            return Vector3(*new_data)
        else:
            raise ValueError(f"Not enough axes given in `axes`: '{axes}'. Must be at least 2.")

    def to_xzy(self) -> Vector3:
        return Vector3(self.x, self.z, self.y)

    def __neg__(self):
        return Vector3(-self._data[0], -self._data[1], -self._data[2])

    def _arithmetic(self, other, op_func: tp.Callable[[float, float], float], op_name: str):
        if isinstance(other, Vector3):
            x, y, z = [op_func(self._data[i], other._data[i]) for i in range(3)]
        elif isinstance(other, (list, tuple)):
            if len(other) != 3:
                raise ValueError(f"List or tuple to {op_name} `Vector3` must have 3 elements.")
            x, y, z = [op_func(self._data[i], other[i]) for i in range(3)]
        elif isinstance(other, (int, float)):
            x, y, z = [op_func(x, other) for x in self._data]
        else:
            raise TypeError(f"`Vector3` arithmetic not defined for type {type(other)}.")
        return Vector3(x, y, z)

    def dot(self, other_vector) -> float:
        if len(other_vector) != 3:
            raise TypeError(f"Cannot only use `dot` with another Vector/sequence of length 3.")
        return sum(self[i] * other_vector[i] for i in range(3))

    def copy(self):
        return Vector3(*self._data)

    @classmethod
    def zero(cls):
        return Vector3(0.0, 0.0, 0.0)

    @classmethod
    def ones(cls):
        return Vector3(1.0, 1.0, 1.0)


class Vector4(Vector):
    """Simple [x, y, z, w] container."""

    def __init__(self, x, y, z, w):
        self._data = [float(x), float(y), float(z), float(w)]

    @property
    def y(self):
        return self._data[1]

    @y.setter
    def y(self, value: float):
        self._data[1] = value

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
    def from_row_mat(cls, row_mat):
        return Vector4(row_mat[0][0], row_mat[0][1], row_mat[0][2], row_mat[0][3])

    @classmethod
    def from_column_mat(cls, column_mat):
        return cls(column_mat[0][0], column_mat[1][0], column_mat[2][0], column_mat[3][0])

    @classmethod
    def from_repr(cls, repr_string: str) -> Vector4:
        """For JSON decoding."""
        if (match := re.match(r"^Vector4(\([\d .,]+\))", repr_string)) is not None:
            return cls(*ast.literal_eval(match.group(1)))
        raise ValueError(f"Cannot read `Vector4` string: {repr_string}")

    def __neg__(self):
        return Vector4(-self._data[0], -self._data[1], -self._data[2], -self._data[3])

    def _arithmetic(self, other, op_func: tp.Callable[[float, float], float], op_name: str):
        if isinstance(other, Vector4):
            x, y, z, w = [op_func(self._data[i], other._data[i]) for i in range(4)]
        elif isinstance(other, (list, tuple)):
            if len(other) != 4:
                raise ValueError(f"List or tuple to {op_name} `Vector4` must have 4 elements.")
            x, y, z, w = [op_func(self._data[i], other[i]) for i in range(4)]
        elif isinstance(other, (int, float)):
            x, y, z, w = [op_func(x, other) for x in self._data]
        else:
            raise TypeError(f"`Vector4` arithmetic not defined for type {type(other)}.")
        return Vector4(x, y, z, w)

    def dot(self, other_vector) -> float:
        if len(other_vector) != 4:
            raise TypeError(f"Cannot only use `dot` with another Vector/sequence of length 4.")
        return sum(self[i] * other_vector[i] for i in range(4))

    def copy(self):
        return Vector4(*self._data)

    @classmethod
    def zero(cls):
        return Vector4(0.0, 0.0, 0.0, 0.0)

    @classmethod
    def ones(cls):
        return Vector4(1.0, 1.0, 1.0, 1.0)


class Matrix(abc.ABC):
    SIZE = None
    PRECISION = 3
    EPSILON = 0.0001  # for printing only
    data: list[list[float]]

    @abc.abstractmethod
    def __init__(self):
        ...

    @classmethod
    @abc.abstractmethod
    def identity(cls):
        ...

    @classmethod
    def from_nested_lists(cls, data):
        m = cls.identity()
        m.data = data
        return m

    @classmethod
    def from_flat_row_order(cls, data):
        """Create `Matrix` from flattened elements, in row-first order."""
        if len(data) != cls.SIZE ** 2:
            raise ValueError(f"`data` should be {cls.SIZE ** 2} elements.")
        m = cls.identity()
        for row in range(cls.SIZE):
            m.data[row] = data[row * cls.SIZE:(row + 1) * cls.SIZE]
        return m

    def to_flat_row_order(self) -> list[int] | list[float]:
        flat = []
        for row in self.data:
            flat.extend(row)
        return flat

    @classmethod
    def from_flat_column_order(cls, data) -> Matrix:
        """Create `Matrix` from flattened elements, in column-first order."""
        if len(data) != cls.SIZE ** 2:
            raise ValueError(f"`data` should be {cls.SIZE ** 2} elements.")
        m = cls.identity()
        for row in range(cls.SIZE):
            m.data[row] = [data[i * cls.SIZE + row] for i in range(cls.SIZE)]
        return m

    def to_flat_column_order(self) -> list[int] | list[float]:
        flat = []
        for c in range(self.SIZE):
            flat.extend([row[c] for row in self.data])
        return flat

    def __getitem__(self, indices):
        if isinstance(indices, int):
            return self.data[indices]
        elif isinstance(indices, tuple):
            if len(indices) == 2:
                row, col = indices
                try:
                    return self.data[row][col]
                except IndexError:
                    raise IndexError(f"Invalid matrix indices: {row}, {col}")
            raise ValueError("Only one index (to retrieve row) or two indices (to retrieve value) are permitted.")
        raise TypeError("Matrix index must be one or two integers.")

    def __setitem__(self, indices, value):
        if isinstance(indices, int):
            if len(value) == self.SIZE:
                self.data[indices] = list(value)
            raise ValueError("Row assigned to Matrix3 must have length 3.")
        elif isinstance(indices, tuple):
            if len(indices) == 2:
                row, col = indices
                try:
                    self.data[row][col] = value
                    return
                except IndexError:
                    raise IndexError(f"Invalid matrix indices: {row}, {col}")
            raise ValueError("Only one index (to set row) or two indices (to set value) are permitted.")
        raise TypeError("Matrix index must be one or two integers.")

    def __repr__(self):
        rows = []
        for row in self.data:
            row_values = [col if abs(col) >= self.EPSILON else 0.0 for col in row]
            rows.append(", ".join(f'{v:>10.{self.PRECISION}}' for v in row_values))
        rows_string = "\n  ".join(rows)
        return f"[\n  {rows_string}\n]"


class Matrix3(Matrix):
    SIZE = 3

    def __init__(self, v00, v01, v02, v10, v11, v12, v20, v21, v22):
        super().__init__()
        self.data = [
            [float(v) for v in (v00, v01, v02)],
            [float(v) for v in (v10, v11, v12)],
            [float(v) for v in (v20, v21, v22)],
        ]

    def __matmul__(self, other):
        if isinstance(other, Matrix3):
            return Matrix3(*matrix_multiply(self.data, other.data, flat=True))
        elif isinstance(other, Vector3):
            return Vector3.from_column_mat(matrix_multiply(self.data, other.to_mat_column()))
        raise TypeError(f"Cannot matrix multiply with type {type(other)}.")

    def __neg__(self):
        return self.__class__(*[
            -x
            for row in self.data
            for x in row
        ])

    @classmethod
    def zero(cls) -> Matrix3:
        return cls(0, 0, 0, 0, 0, 0, 0, 0, 0)

    @classmethod
    def identity(cls) -> Matrix3:
        return cls(1, 0, 0, 0, 1, 0, 0, 0, 1)

    @classmethod
    def from_euler_angles(cls, rx, ry=None, rz=None, radians=False, order="xzy") -> Matrix3:
        """Order defaults to XZY as per FromSoft usage (i.e. Rx @ Ry @ Rz @ p)."""
        if ry is None and rz is None:
            rx, ry, rz = rx
        if not radians:
            rx, ry, rz = math.radians(rx), math.radians(ry), math.radians(rz)
        sx, sy, sz = math.sin(rx), math.sin(ry), math.sin(rz)
        cx, cy, cz = math.cos(rx), math.cos(ry), math.cos(rz)
        m = {
            "x": cls(1, 0, 0, 0, cx, -sx, 0, sx, cx),
            "y": cls(cy, 0, sy, 0, 1, 0, -sy, 0, cy),
            "z": cls(cz, -sz, 0, sz, cz, 0, 0, 0, 1),
        }
        return m[order[2]] @ m[order[1]] @ m[order[0]]

    @property
    def T(self) -> Matrix3:
        """Transpose of matrix."""
        return Matrix3.from_nested_lists([list(col) for col in zip(*self.data)])

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

        return Vector3(x, y, z) if radians else Vector3(math.degrees(x), math.degrees(y), math.degrees(z))


class Matrix4(Matrix):
    SIZE = 4

    def __init__(self, v00, v01, v02, v03, v10, v11, v12, v13, v20, v21, v22, v23, v30, v31, v32, v33):
        super().__init__()
        self.data = [
            [float(v) for v in (v00, v01, v02, v03)],
            [float(v) for v in (v10, v11, v12, v13)],
            [float(v) for v in (v20, v21, v22, v23)],
            [float(v) for v in (v30, v31, v32, v33)],
        ]

    @classmethod
    def zero(cls):
        return cls(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    @classmethod
    def identity(cls):
        return cls(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)

    def __matmul__(self, other):
        if isinstance(other, Matrix4):
            return Matrix4(*matrix_multiply(self.data, other.data, flat=True))
        elif isinstance(other, Vector3):
            return Vector3.from_column_mat(matrix_multiply(self.data, other.to_mat_column() + [[1]]))
        elif isinstance(other, Vector4):
            return Vector4.from_column_mat(matrix_multiply(self.data, other.to_mat_column()))
        raise TypeError(f"Cannot matrix multiply with type {type(other)}.")

    def __neg__(self):
        return self.__class__(*[
            -x
            for row in self.data
            for x in row
        ])

    def get_scale(self) -> Vector3:
        return Vector3(self.data[0][0], self.data[1][1], self.data[2][2])

    def set_scale(self, scale_vector: Vector3 | list | tuple | int | float):
        """Set the scale part of the matrix (diagonal of top-left 3x3 sub-matrix)."""
        if isinstance(scale_vector, (list, tuple)):
            scale_vector = Vector3(*scale_vector)
        elif isinstance(scale_vector, (int, float)):
            scale_vector = Vector3(scale_vector, scale_vector, scale_vector)

        if isinstance(scale_vector, Vector3):
            for i in range(3):
                self.data[i][i] = scale_vector[i]
        else:
            raise TypeError("`scale_vector` must be a Vector3, list, tuple, int, or float.")

    def get_rotation_submatrix(self) -> Matrix3:
        return Matrix3(
            self[0][0], self[0][1], self[0][2],
            self[1][0], self[1][1], self[1][2],
            self[2][0], self[2][1], self[2][2],
        )

    @classmethod
    def from_translate(cls, translate: Vector3) -> Matrix4:
        return cls(
            1.0, 0.0, 0.0, translate.x,
            0.0, 1.0, 0.0, translate.y,
            0.0, 0.0, 1.0, translate.z,
            0.0, 0.0, 0.0, 1.0,
        )

    @classmethod
    def from_scale(cls, scale: Vector3) -> Matrix4:
        return cls(
            scale.x, 0.0, 0.0, 0.0,
            0.0, scale.y, 0.0, 0.0,
            0.0, 0.0, scale.z, 0.0,
            0.0, 0.0, 0.0, 1.0,
        )

    @classmethod
    def from_rotation_matrix3(cls, rotation: Matrix3) -> Matrix4:
        return cls(
            rotation[0][0], rotation[0][1], rotation[0][2], 0.0,
            rotation[1][0], rotation[1][1], rotation[1][2], 0.0,
            rotation[2][0], rotation[2][1], rotation[2][2], 0.0,
            0.0, 0.0, 0.0, 1.0,
        )

    def get_translate(self) -> Vector3:
        return Vector3(self.data[0][3], self.data[1][3], self.data[2][3])

    def set_translate(self, translate_vector: Vector3 | list | tuple | int | float):
        """Set the translate part of the matrix (first three elements of last column)."""
        if isinstance(translate_vector, (list, tuple)):
            translate_vector = Vector3(*translate_vector)
        elif isinstance(translate_vector, (int, float)):
            translate_vector = Vector3(translate_vector, translate_vector, translate_vector)
        elif not isinstance(translate_vector, Vector3):
            raise TypeError("`translate_vector` must be a Vector3, list, tuple, int, or float.")
        for i in range(3):
            self.data[i][3] = float(translate_vector[i])


def shift_msb_coordinates(distance: float, translate=(0.0, 0.0, 0.0), ry=0.0):
    """Shift an MSB entity forward (if `distance > 0` or backward (if `distance < 0`)."""
    ry_rad = math.radians(ry)
    delta_x = -distance * math.sin(ry_rad)
    delta_z = -distance * math.cos(ry_rad)
    return translate[0] + delta_x, translate[1], translate[2] + delta_z


def shift(rel_x, rel_z, origin=(0, 0), rotation=0):
    rot_rad = math.radians(rotation)
    r, th = math.hypot(rel_x, rel_z), math.atan2(rel_z, rel_x)
    th += rot_rad
    dx, dz = r * -math.sin(th), r * -math.cos(th)
    return origin[0] + dx, origin[1] + dz


def matrix_multiply(a, b, flat=False):
    zip_b = list(zip(*b))
    m = [[sum(ele_a * ele_b for ele_a, ele_b in zip(row_a, col_b)) for col_b in zip_b] for row_a in a]
    if flat:
        m_flat = []
        for row in m:
            m_flat.extend(row)
        return m_flat
    return m


def resolve_rotation(rotation: Matrix3 | Vector3 | list | tuple | int | float, radians=False) -> Matrix3:
    """Return a rotation `Matrix3` from various shortcut input types (e.g. single value or Euler angle vector)."""
    if isinstance(rotation, (int, float)):
        # Single rotation value is a shortcut for Y rotation.
        return Matrix3.from_euler_angles(0.0, rotation, 0.0, radians=radians)
    elif isinstance(rotation, (Vector3, list, tuple)):
        return Matrix3.from_euler_angles(rotation, radians=radians)
    elif isinstance(rotation, Matrix3):
        return rotation
    raise TypeError("`rotation` must be a Matrix3, Vector3/list/tuple, or int/float (for Y rotation only).")


def get_distance(x1: Vector3, x2: Vector3, squared=False):
    if not isinstance(x1, Vector3):
        x1 = Vector3(*x1)
    if not isinstance(x2, Vector3):
        x2 = Vector3(*x2)
    squared_distance = (x2.x - x1.x) ** 2 + (x2.y - x1.y) ** 2 + (x2.z - x1.z) ** 2
    if squared:
        return squared_distance
    return math.sqrt(squared_distance)
