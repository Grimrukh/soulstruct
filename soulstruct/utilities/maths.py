"""Mathematical classes and functions uses by Soulstruct."""

__all__ = [
    "Vector3",
    "Matrix3",
    "Matrix4",
    "shift_msb_coordinates",
    "shift",
    "matrix_multiply",
    "resolve_rotation",
]

import abc
import math
import typing as tp


class Vector3:
    """Simple [x, y, z] container."""

    PRECISION = 3

    def __init__(self, x=None, y=None, z=None):
        if x is None:
            if y is not None or z is not None:
                raise ValueError("If `x=None`, `y` and `z` must both be left as `None`.")
            x = y = z = 0  # default
        elif y is None and z is None:
            x, y, z = x  # unpack first argument
        elif y is None or z is None:
            raise ValueError(
                "Vector3 must be initialized as `Vector3(x, y, z)`, `Vector3((x, y, z))`, or `Vector3(None)`."
            )
        self.x, self.y, self.z = x, y, z

    @classmethod
    def from_row_mat(cls, row_mat):
        return cls(row_mat[0][0], row_mat[0][1], row_mat[0][2])

    @classmethod
    def from_column_mat(cls, column_mat):
        return cls(column_mat[0][0], column_mat[1][0], column_mat[2][0])

    def to_radians(self):
        return Vector3(math.radians(self.x), math.radians(self.y), math.radians(self.z))

    def to_degrees(self):
        return Vector3(math.degrees(self.x), math.degrees(self.y), math.degrees(self.z))

    def to_mat_column(self):
        return [[self.x], [self.y], [self.z]]

    def to_mat_row(self):
        return [[self.x, self.y, self.z]]

    def transform(self, matrix3):
        return Vector3(list(zip(*matrix_multiply(matrix3, self.to_mat_column())))[0])

    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        raise IndexError("Index of Vector must be between 0 and 2.")

    def __setitem__(self, index, value):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        raise IndexError("Index of Vector must be between 0 and 2.")

    def __eq__(self, other_vector):
        return len(other_vector) == 3 and all(self[i] == other_vector[i] for i in range(3))

    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (list, tuple)):
            if len(other) != 3:
                raise ValueError("List or tuple to add to Vector must have three elements.")
            return Vector3(self.x + other[0], self.y + other[1], self.z + other[2])
        elif isinstance(other, (int, float)):
            return Vector3(self.x + other, self.y + other, self.z + other)
        raise TypeError(f"Vector arithmetic not defined for type {type(other)}")

    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, (list, tuple)):
            if len(other) != 3:
                raise ValueError("List or tuple to add to Vector must have three elements.")
            return Vector3(self.x - other[0], self.y - other[1], self.z - other[2])
        elif isinstance(other, (int, float)):
            return Vector3(self.x - other, self.y - other, self.z - other)
        raise TypeError(f"Vector arithmetic not defined for type {type(other)}")

    def __mul__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (list, tuple)):
            if len(other) != 3:
                raise ValueError("List or tuple to add to Vector must have three elements.")
            return Vector3(self.x * other[0], self.y * other[1], self.z * other[2])
        elif isinstance(other, (int, float)):
            return Vector3(self.x * other, self.y * other, self.z * other)
        raise TypeError(f"Vector arithmetic not defined for type {type(other)}")

    def __truediv__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)
        elif isinstance(other, (list, tuple)):
            if len(other) != 3:
                raise ValueError("List or tuple to add to Vector must have three elements.")
            return Vector3(self.x / other[0], self.y / other[1], self.z / other[2])
        elif isinstance(other, (int, float)):
            return Vector3(self.x / other, self.y / other, self.z / other)
        raise TypeError(f"Vector arithmetic not defined for type {type(other)}")

    def __len__(self):
        return 3

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __repr__(self):
        return f"Vector3({self.x:.{self.PRECISION}f}, {self.y:.{self.PRECISION}f}, {self.z:.{self.PRECISION}f})"

    def copy(self):
        return Vector3(self)

    @classmethod
    def zero(cls):
        return cls(0, 0, 0)

    @classmethod
    def ones(cls):
        return cls(1, 1, 1)


class _Matrix(abc.ABC):
    SIZE = None
    PRECISION = 3
    data: list[list[tp.Union[int, float]]]

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
                except IndexError:
                    raise IndexError(f"Invalid matrix indices: {row}, {col}")
            raise ValueError("Only one index (to set row) or two indices (to set value) are permitted.")
        raise TypeError("Matrix index must be one or two integers.")

    def __repr__(self):
        return "\n".join(f"[{', '.join(f'{v:.{self.PRECISION}}' for v in row)}]" for row in self.data)


class Matrix3(_Matrix):
    SIZE = 3

    def __init__(self, v00, v01, v02, v10, v11, v12, v20, v21, v22):
        super().__init__()
        self.data = [
            [v00, v01, v02],
            [v10, v11, v12],
            [v20, v21, v22],
        ]

    def __matmul__(self, other):
        if isinstance(other, Matrix3):
            return Matrix3(*matrix_multiply(self.data, other.data, flat=True))
        elif isinstance(other, Vector3):
            return Vector3.from_column_mat(matrix_multiply(self.data, other.to_mat_column()))
        raise TypeError(f"Cannot matrix multiply with type {type(other)}.")

    @classmethod
    def identity(cls):
        return cls(1, 0, 0, 0, 1, 0, 0, 0, 1)

    @classmethod
    def from_euler_angles(cls, rx, ry=None, rz=None, radians=False, order="xzy"):
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
    def T(self):
        """Transpose of matrix."""
        return Matrix3.from_nested_lists([list(col) for col in zip(*self.data)])

    def to_euler_angles(self, radians=False, order="xzy") -> Vector3:
        """Only supports order XZY for now (standard FromSoft usage)."""
        if order != "xzy":
            raise ValueError("Can only compute Eular matrix for XZY rotation, as used in DS1 at least.")

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


class Matrix4(_Matrix):
    SIZE = 4

    def __init__(self, v00, v01, v02, v03, v10, v11, v12, v13, v20, v21, v22, v23, v30, v31, v32, v33):
        super().__init__()
        self.data = [
            [v00, v01, v02, v03],
            [v10, v11, v12, v13],
            [v20, v21, v22, v23],
            [v30, v31, v32, v33],
        ]

    @classmethod
    def identity(cls):
        return cls(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)

    def __matmul__(self, other):
        if isinstance(other, Matrix4):
            return Matrix4(*matrix_multiply(self.data, other.data, flat=True))
        elif isinstance(other, Vector3):
            return Vector3.from_column_mat(matrix_multiply(self.data, other.to_mat_column() + [[1]]))
        raise TypeError(f"Cannot matrix multiply with type {type(other)}.")


def shift_msb_coordinates(ry, distance, xyz=(0.0, 0.0, 0.0)):
    """Shift an MSB entity with given x, z, ry coordinates forward or back."""
    ry_rad = math.radians(ry)
    delta_x = -distance * math.sin(ry_rad)
    delta_z = -distance * math.cos(ry_rad)
    return xyz[0] + delta_x, xyz[1], xyz[2] + delta_z


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


def resolve_rotation(rotation: tp.Union[Matrix3, Vector3, list, tuple, int, float], radians=False) -> Matrix3:
    """Return a rotation `Matrix3` from various shortcut input types (e.g. single value or Euler angle vector)."""
    if isinstance(rotation, (int, float)):
        # Single rotation value is a shortcut for Y rotation.
        return Matrix3.from_euler_angles(0.0, rotation, 0.0, radians=radians)
    elif isinstance(rotation, (Vector3, list, tuple)):
        return Matrix3.from_euler_angles(rotation, radians=radians)
    elif isinstance(rotation, Matrix3):
        return rotation
    raise TypeError("`rotation` must be a Matrix3, Vector3/list/tuple, or int/float (for Y rotation only).")
