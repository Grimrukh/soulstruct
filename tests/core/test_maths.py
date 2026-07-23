"""Pure-unit tests for `soulstruct.utilities.maths`.

No game data required: everything here is numeric logic (vectors, Euler angles, matrices).

Several tests are marked `xfail` where they document genuine library defects; see the audit report
`02-utilities.md` for details. They are deliberately NOT watered down.
"""
from __future__ import annotations

import copy
import math
import pickle

import numpy as np
import pytest
from numpy.testing import assert_allclose

from soulstruct.utilities.maths import (
    AABB,
    SINGLE_MAX,
    SINGLE_MIN,
    BaseVector,
    EulerDeg,
    EulerRad,
    Matrix3,
    Matrix4,
    Vector2,
    Vector3,
    Vector4,
    get_distance,
    get_rotmat3,
    local_translate,
)


# ---------------------------------------------------------------------------
# Reference rotation matrices (right-handed, column-vector convention)
# ---------------------------------------------------------------------------


def _rx(a: float) -> np.ndarray:
    return np.array([[1, 0, 0], [0, math.cos(a), -math.sin(a)], [0, math.sin(a), math.cos(a)]])


def _ry(a: float) -> np.ndarray:
    return np.array([[math.cos(a), 0, math.sin(a)], [0, 1, 0], [-math.sin(a), 0, math.cos(a)]])


def _rz(a: float) -> np.ndarray:
    return np.array([[math.cos(a), -math.sin(a), 0], [math.sin(a), math.cos(a), 0], [0, 0, 1]])


# ===========================================================================
# BaseVector / Vector2 / Vector3 / Vector4
# ===========================================================================


@pytest.mark.parametrize("cls,length", [(Vector2, 2), (Vector3, 3), (Vector4, 4)])
def test_vector_length_enforced(cls: type[BaseVector], length: int):
    assert cls.LENGTH == length
    v = cls(range(length))  # `range` has `len`
    assert len(v) == length
    with pytest.raises(ValueError):
        cls(list(range(length + 1)))
    with pytest.raises(ValueError):
        cls(list(range(length - 1)))


def test_vector_component_properties():
    v2 = Vector2((1.0, 2.0))
    assert (v2.x, v2.y) == (1.0, 2.0)
    assert not hasattr(v2, "z")
    v3 = Vector3((1.0, 2.0, 3.0))
    assert (v3.x, v3.y, v3.z) == (1.0, 2.0, 3.0)
    v4 = Vector4((1.0, 2.0, 3.0, 4.0))
    assert (v4.x, v4.y, v4.z, v4.w) == (1.0, 2.0, 3.0, 4.0)


def test_vector_immutability():
    v = Vector3((1.0, 2.0, 3.0))
    with pytest.raises(AttributeError):
        v.x = 5.0
    with pytest.raises(TypeError):
        v[0] = 5.0
    with pytest.raises(ValueError):
        v.data[0] = 5.0  # underlying array is read-only


def test_vector_copy_is_identity():
    """Vectors are immutable, so `copy`/`deepcopy` intentionally return the same object."""
    v = Vector3((1.0, 2.0, 3.0))
    assert v.copy() is v
    assert copy.copy(v) is v
    assert copy.deepcopy(v) is v


def test_vector_pickle_roundtrip():
    v = Vector4((1.5, -2.5, 3.0, 0.0))
    restored = pickle.loads(pickle.dumps(v))
    assert isinstance(restored, Vector4)
    assert restored == v


def test_vector_arithmetic():
    a = Vector3((1.0, 2.0, 3.0))
    b = Vector3((4.0, 5.0, 6.0))
    assert_allclose((a + b).data, [5.0, 7.0, 9.0])
    assert_allclose((b - a).data, [3.0, 3.0, 3.0])
    assert_allclose((a * 2).data, [2.0, 4.0, 6.0])
    assert_allclose((2 * a).data, [2.0, 4.0, 6.0])
    assert_allclose((a / 2).data, [0.5, 1.0, 1.5])
    assert_allclose((-a).data, [-1.0, -2.0, -3.0])
    # Reflected ops with scalar/array on the left.
    assert_allclose((1 + a).data, [2.0, 3.0, 4.0])
    assert_allclose((10 - a).data, [9.0, 8.0, 7.0])
    assert_allclose((6 / Vector3((1.0, 2.0, 3.0))).data, [6.0, 3.0, 2.0])
    # All results are new `Vector3`s, not mutated operands.
    assert a == Vector3((1.0, 2.0, 3.0))
    assert b == Vector3((4.0, 5.0, 6.0))


def test_vector_arithmetic_returns_same_class():
    for cls, data in ((Vector2, (1.0, 2.0)), (Vector3, (1.0, 2.0, 3.0)), (Vector4, (1.0, 2.0, 3.0, 4.0))):
        v = cls(data)
        assert type(v + v) is cls
        assert type(v * 3) is cls
        assert type(-v) is cls


def test_vector_dot_and_matmul():
    a = Vector3((1.0, 2.0, 3.0))
    b = Vector3((4.0, -5.0, 6.0))
    expected = 1 * 4 + 2 * -5 + 3 * 6
    assert a.dot(b) == pytest.approx(expected)
    assert (a @ b) == pytest.approx(expected)
    assert (a @ [4.0, -5.0, 6.0]) == pytest.approx(expected)
    assert isinstance(a @ b, float)


def test_vector3_cross():
    x = Vector3((1.0, 0.0, 0.0))
    y = Vector3((0.0, 1.0, 0.0))
    assert_allclose(x.cross(y).data, [0.0, 0.0, 1.0], atol=1e-12)
    assert_allclose(y.cross(x).data, [0.0, 0.0, -1.0], atol=1e-12)
    assert isinstance(x.cross(y), Vector3)
    # Cross with itself is zero.
    assert_allclose(x.cross(x).data, [0.0, 0.0, 0.0], atol=1e-12)


def test_vector_magnitude_and_normalize():
    v = Vector3((3.0, 4.0, 0.0))
    assert abs(v) == pytest.approx(5.0)
    assert v.get_magnitude() == pytest.approx(5.0)
    assert v.norm() == pytest.approx(5.0)
    assert v.get_squared_magnitude() == pytest.approx(25.0)
    n = v.normalize()
    assert abs(n) == pytest.approx(1.0)
    assert_allclose(n.data, [0.6, 0.8, 0.0])
    # Original unchanged.
    assert_allclose(v.data, [3.0, 4.0, 0.0])


def test_vector_normalize_zero_raises():
    with pytest.raises(ZeroDivisionError):
        Vector3.zero().normalize()


def test_vector_classmethod_constructors():
    assert_allclose(Vector3.zero().data, [0.0, 0.0, 0.0])
    assert_allclose(Vector4.one().data, [1.0, 1.0, 1.0, 1.0])
    assert_allclose(Vector2.single_max().data, [SINGLE_MAX, SINGLE_MAX])
    assert_allclose(Vector2.single_min().data, [SINGLE_MIN, SINGLE_MIN])
    assert SINGLE_MIN == -SINGLE_MAX


def test_vector_eq_iter_getitem_hash():
    v = Vector3((1.0, 2.0, 3.0))
    assert v == Vector3((1.0, 2.0, 3.0))
    assert v == [1.0, 2.0, 3.0]  # compares against any array-like
    assert v != Vector3((1.0, 2.0, 4.0))
    assert list(v) == [1.0, 2.0, 3.0]
    assert v[1] == 2.0
    assert hash(v) == hash(Vector3((1.0, 2.0, 3.0)))
    assert {v: "a"}[Vector3((1.0, 2.0, 3.0))] == "a"


def test_vector_eq_is_not_type_strict():
    """DOCUMENTS a trap: `BaseVector.__eq__` only compares data, so a `Vector3` equals a same-valued `EulerDeg`.

    (Contrast with `BaseEuler.__eq__`, which IS type-strict.)
    """
    assert Vector3((1.0, 2.0, 3.0)) == EulerDeg((1.0, 2.0, 3.0))
    assert EulerDeg((1.0, 2.0, 3.0)) != Vector3((1.0, 2.0, 3.0))


def test_vector_allclose():
    v = Vector3((1.0, 2.0, 3.0))
    assert v.allclose(Vector3((1.0, 2.0, 3.0 + 1e-12)))
    assert not v.allclose(Vector3((1.0, 2.0, 3.1)))


def test_vector_repr_and_from_repr_roundtrip():
    v = Vector3((1.5, -2.25, 3.125))
    assert repr(v) == "Vector3((1.5, -2.25, 3.125))"
    assert Vector3.from_repr(repr(v)) == v
    assert Vector2.from_repr("Vector2((0.0, 1.0))") == Vector2((0.0, 1.0))
    assert Vector4.from_repr(repr(Vector4((1.0, 2.0, 3.0, 4.0)))) == Vector4((1.0, 2.0, 3.0, 4.0))


def test_vector_from_repr_errors():
    with pytest.raises(ValueError):
        Vector3.from_repr("not a vector")
    with pytest.raises(ValueError):
        Vector3.from_repr("Vector2((1.0, 2.0))")  # wrong class name
    with pytest.raises(ValueError):
        Vector3.from_repr("Vector3((1.0, 2.0))")  # wrong element count
    with pytest.raises(ValueError):
        Vector3.from_repr("Vector3((a, b, c))")  # bad payload


def test_vector_repr_roundtrip_is_lossless():
    v = Vector3((1234567.0, 0.000123456789, -98765.4321))
    assert Vector3.from_repr(repr(v)).allclose(v, rtol=1e-9)


@pytest.mark.xfail(
    reason="BUG: `__repr__` emits `<SINGLE_MAX>`/`<SINGLE_MIN>` placeholders that `from_repr` cannot parse, "
           "so `AABB.invalid()`-style vectors cannot be repr-serialized and restored.",
    strict=False,
)
def test_vector_repr_roundtrip_single_max():
    v = Vector3.single_max()
    assert Vector3.from_repr(repr(v)) == v


@pytest.mark.xfail(
    reason="BUG: `BaseVector.__init__` calls `arr.flags.writeable = False` on a NumPy array it does not own "
           "(`np.asarray` does not copy float64 input), permanently freezing the CALLER's array.",
    strict=False,
)
def test_vector_construction_does_not_freeze_source_array():
    source = np.array([1.0, 2.0, 3.0])
    Vector3(source)
    source[0] = 5.0  # currently raises ValueError: assignment destination is read-only
    assert source[0] == 5.0


def test_vector_construction_from_vector_copies():
    a = Vector3((1.0, 2.0, 3.0))
    b = Vector3(a)
    assert b == a
    assert not np.shares_memory(a.data, b.data)


def test_vector3_get_as_axes():
    v = Vector3((1.0, 2.0, 3.0))
    assert Vector3(v.get_as_axes("xyz")) == v
    assert v.get_as_axes("zyx") == Vector3((3.0, 2.0, 1.0))
    assert v.get_as_axes("-x-zy") == Vector3((-1.0, -3.0, 2.0))
    assert v.get_as_axes("xy") == Vector2((1.0, 2.0))
    assert isinstance(v.get_as_axes("xy"), Vector2)
    with pytest.raises(ValueError):
        v.get_as_axes("xxy")  # repeated axis
    with pytest.raises(ValueError):
        v.get_as_axes("xyq")  # invalid character
    with pytest.raises(ValueError):
        v.get_as_axes("x")  # too few axes


def test_vector3_to_xzy():
    assert Vector3((1.0, 2.0, 3.0)).to_xzy() == Vector3((1.0, 3.0, 2.0))


def test_vector3_vector4_conversion():
    v3 = Vector3((1.0, 2.0, 3.0))
    v4 = Vector4.from_vector3(v3)
    assert v4 == Vector4((1.0, 2.0, 3.0, 1.0))
    assert Vector4.from_vector3(v3, w=0.0).w == 0.0
    assert Vector3.from_vector4(v4) == v3


def test_vector_numpy_interop():
    v = Vector3((1.0, 2.0, 3.0))
    arr = np.asarray(v)
    assert arr.shape == (3,)
    assert_allclose(arr, [1.0, 2.0, 3.0])
    assert_allclose(np.asarray(v, dtype=np.float32), [1.0, 2.0, 3.0])


# ===========================================================================
# EulerDeg / EulerRad
# ===========================================================================


def test_euler_basic_properties():
    e = EulerDeg((10.0, 20.0, 30.0))
    assert len(e) == 3
    assert (e.x, e.y, e.z) == (10.0, 20.0, 30.0)
    assert (e.pitch, e.yaw, e.roll) == (10.0, 20.0, 30.0)
    assert e.ORDER == "XZY"
    assert list(e) == [10.0, 20.0, 30.0]
    with pytest.raises(ValueError):
        EulerDeg((1.0, 2.0))


def test_euler_immutability_and_copy():
    e = EulerRad((0.1, 0.2, 0.3))
    with pytest.raises(AttributeError):
        e.x = 1.0
    with pytest.raises(TypeError):
        e[0] = 1.0
    assert copy.deepcopy(e) is e
    assert pickle.loads(pickle.dumps(e)) == e


def test_euler_deg_rad_conversion():
    deg = EulerDeg((0.0, 90.0, 180.0))
    rad = deg.to_rad()
    assert isinstance(rad, EulerRad)
    assert_allclose(np.asarray(rad), [0.0, math.pi / 2, math.pi])
    assert rad.to_deg().allclose(deg)


def test_euler_has_no_data_property():
    """DOCUMENTS an API inconsistency: `BaseVector` exposes `.data`, but `BaseEuler` does not.

    Use `np.asarray(euler)` or `euler[i]` instead.
    """
    assert not hasattr(EulerDeg((1.0, 2.0, 3.0)), "data")
    assert hasattr(Vector3((1.0, 2.0, 3.0)), "data")


def test_euler_eq_is_type_strict():
    assert EulerDeg((1.0, 2.0, 3.0)) == EulerDeg((1.0, 2.0, 3.0))
    assert EulerDeg((1.0, 2.0, 3.0)) != EulerRad((1.0, 2.0, 3.0))
    assert hash(EulerDeg((1.0, 2.0, 3.0))) == hash(EulerRad((1.0, 2.0, 3.0)))  # hash is NOT type-aware


def test_euler_arithmetic():
    a = EulerDeg((10.0, 20.0, 30.0))
    b = EulerDeg((1.0, 2.0, 3.0))
    assert (a + b) == EulerDeg((11.0, 22.0, 33.0))
    assert (a - b) == EulerDeg((9.0, 18.0, 27.0))
    assert (-a) == EulerDeg((-10.0, -20.0, -30.0))
    assert (a * 2) == EulerDeg((20.0, 40.0, 60.0))
    assert (2 * a) == EulerDeg((20.0, 40.0, 60.0))
    assert (a / 2) == EulerDeg((5.0, 10.0, 15.0))
    assert EulerDeg.zero() == EulerDeg((0.0, 0.0, 0.0))


def test_euler_arithmetic_type_errors():
    a = EulerDeg((1.0, 2.0, 3.0))
    with pytest.raises(TypeError):
        _ = a + EulerRad((1.0, 2.0, 3.0))
    with pytest.raises(TypeError):
        _ = a - [1.0, 2.0, 3.0]
    with pytest.raises(TypeError):
        _ = a * EulerDeg((1.0, 1.0, 1.0))


def test_euler_repr_roundtrip():
    e = EulerDeg((1.5, -2.25, 0.0))
    assert repr(e) == "EulerDeg((1.5, -2.25, 0.0))"
    assert EulerDeg.from_repr(repr(e)) == e
    with pytest.raises(ValueError):
        EulerRad.from_repr(repr(e))  # class mismatch
    with pytest.raises(ValueError):
        EulerDeg.from_repr("EulerDeg((1.0, 2.0))")


# ===========================================================================
# Matrix3
# ===========================================================================


def test_matrix3_construction():
    m = Matrix3([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert_allclose(m.data, np.arange(1, 10).reshape(3, 3))
    assert m[0, 2] == 3.0
    with pytest.raises(ValueError):
        Matrix3(np.zeros((2, 2)))
    with pytest.raises(ValueError):
        Matrix3([[1, 2, 3], [4, 5, 6]])
    with pytest.raises(TypeError):
        Matrix3("not a matrix")


def test_matrix3_identity_zero_transpose():
    assert_allclose(Matrix3.identity().data, np.identity(3))
    assert_allclose(Matrix3.zero().data, np.zeros((3, 3)))
    m = Matrix3.from_flat_row_order(list(range(9)))
    assert_allclose(m.T.data, np.arange(9).reshape(3, 3).T)


def test_matrix3_flat_order_roundtrips():
    flat = [float(i) for i in range(9)]
    m = Matrix3.from_flat_row_order(flat)
    assert m.to_flat_row_order() == flat
    assert m[0, 1] == 1.0  # row-major
    mc = Matrix3.from_flat_column_order(flat)
    assert mc.to_flat_column_order() == flat
    assert mc[1, 0] == 1.0  # column-major
    assert_allclose(mc.data, m.data.T)
    with pytest.raises(ValueError):
        Matrix3.from_flat_row_order(list(range(8)))
    with pytest.raises(ValueError):
        Matrix3.from_flat_column_order(list(range(10)))


def test_matrix3_inverse_and_composition():
    m = Matrix3.from_euler_angles_deg(EulerDeg((10.0, 20.0, 30.0)))
    inv = m.inverse()
    assert_allclose((m @ inv).data, np.identity(3), atol=1e-12)
    # Rotation matrix inverse == transpose.
    assert_allclose(inv.data, m.data.T, atol=1e-12)
    # Matrix product is associative and matches NumPy.
    n = Matrix3.from_euler_angles_deg(EulerDeg((-5.0, 45.0, 12.0)))
    assert_allclose((m @ n).data, m.data @ n.data)
    assert isinstance(m @ n, Matrix3)


def test_matrix3_negation_and_setitem():
    m = Matrix3.identity()
    assert_allclose((-m).data, -np.identity(3))
    m[0, 0] = 5.0
    assert m[0, 0] == 5.0


def test_matrix3_matmul_vector3():
    m = Matrix3.from_euler_angles_deg(EulerDeg((10.0, 20.0, 30.0)))
    v = Vector3((1.0, 2.0, 3.0))
    result = m @ v
    assert isinstance(result, Vector3)
    assert_allclose(result.data, m.data @ v.data)


def test_matrix3_matmul_ndarray():
    m = Matrix3.identity()
    arr1d = np.array([1.0, 2.0, 3.0])
    assert isinstance(m @ arr1d, Vector3)
    assert_allclose((m @ arr1d).data, arr1d)
    arr2d = np.arange(9, dtype=float).reshape(3, 3)
    assert isinstance(m @ arr2d, Matrix3)
    assert_allclose((m @ arr2d).data, arr2d)


def test_matrix3_matmul_euler_returns_euler():
    m = Matrix3.from_euler_angles_deg(EulerDeg((0.0, 90.0, 0.0)))
    e = EulerDeg((0.0, 45.0, 0.0))
    combined = m @ e
    assert isinstance(combined, EulerDeg)
    assert combined.allclose(EulerDeg((0.0, 135.0, 0.0)), atol=1e-9)
    r = EulerRad((0.0, math.pi / 4, 0.0))
    combined_rad = m @ r
    assert isinstance(combined_rad, EulerRad)
    assert combined_rad.allclose(EulerRad((0.0, 3 * math.pi / 4, 0.0)), atol=1e-9)


def test_ndarray_matmul_matrix3_is_unsupported():
    """DOCUMENTS a trap: `Matrix3`/`Matrix4` do not set `__array_priority__`/`__array_ufunc__`, so NumPy
    handles `ndarray @ Matrix3` itself (and fails) instead of deferring to `Matrix3.__rmatmul__`."""
    a = Matrix3.identity()
    with pytest.raises(ValueError):
        _ = np.identity(3) @ a


@pytest.mark.xfail(
    reason="BUG: `@dataclass(slots=True)`-generated `Matrix3.__eq__` compares NumPy arrays, returning an array "
           "instead of a bool; `bool(m1 == m2)` raises 'truth value of an array is ambiguous'.",
    strict=False,
)
def test_matrix3_equality_returns_bool():
    assert bool(Matrix3.identity() == Matrix3.identity()) is True
    assert bool(Matrix3.identity() == Matrix3.zero()) is False


# ---------------------------------------------------------------------------
# Euler <-> Matrix3 conversions (FromSoft XZY convention)
# ---------------------------------------------------------------------------


def test_from_euler_angles_rad_uses_ry_rz_rx_order():
    """FromSoft convention: rotation applied to point `p` as `Ry @ Rz @ Rx @ p`."""
    rx, ry, rz = 0.3, -0.7, 1.1
    m = Matrix3.from_euler_angles_rad(EulerRad((rx, ry, rz)))
    assert_allclose(m.data, _ry(ry) @ _rz(rz) @ _rx(rx), atol=1e-14)


def test_from_euler_angles_deg_matches_rad():
    deg = EulerDeg((10.0, 20.0, 30.0))
    assert_allclose(
        Matrix3.from_euler_angles_deg(deg).data,
        Matrix3.from_euler_angles_rad(deg.to_rad()).data,
    )


def test_from_euler_single_axis_matrices():
    # Y rotation of 90 degrees maps +Z to +X (right-handed, Y-up).
    m = Matrix3.from_euler_angles_deg(EulerDeg((0.0, 90.0, 0.0)))
    assert_allclose((m @ Vector3((0.0, 0.0, 1.0))).data, [1.0, 0.0, 0.0], atol=1e-15)
    # X rotation of 90 degrees maps +Y to +Z.
    m = Matrix3.from_euler_angles_deg(EulerDeg((90.0, 0.0, 0.0)))
    assert_allclose((m @ Vector3((0.0, 1.0, 0.0))).data, [0.0, 0.0, 1.0], atol=1e-15)
    # Z rotation of 90 degrees maps +X to +Y.
    m = Matrix3.from_euler_angles_deg(EulerDeg((0.0, 0.0, 90.0)))
    assert_allclose((m @ Vector3((1.0, 0.0, 0.0))).data, [0.0, 1.0, 0.0], atol=1e-15)


@pytest.mark.parametrize(
    "euler",
    [
        (0.0, 0.0, 0.0),
        (10.0, 20.0, 30.0),
        (-45.0, 170.0, 88.0),
        (1.0, 2.0, 3.0),
        (-179.0, 179.0, -89.0),
        (33.3, -120.5, 44.4),
    ],
)
def test_euler_matrix_roundtrip_deg(euler):
    e = EulerDeg(euler)
    m = Matrix3.from_euler_angles_deg(e)
    back = m.to_euler_angles_deg()
    assert isinstance(back, EulerDeg)
    assert back.allclose(e, atol=1e-9)


@pytest.mark.parametrize("euler", [(0.0, 0.0, 90.0), (0.0, 30.0, 90.0), (0.0, 30.0, -90.0), (20.0, 0.0, 90.0)])
def test_euler_matrix_roundtrip_gimbal_lock(euler):
    """At |roll| == 90 degrees the decomposition is non-unique; the MATRIX must still round-trip."""
    m = Matrix3.from_euler_angles_deg(EulerDeg(euler))
    m2 = Matrix3.from_euler_angles_deg(m.to_euler_angles_deg())
    assert_allclose(m2.data, m.data, atol=1e-9)


def test_euler_matrix_roundtrip_rad():
    e = EulerRad((0.1, -0.9, 1.4))
    m = Matrix3.from_euler_angles_rad(e)
    assert isinstance(m.to_euler_angles_rad(), EulerRad)
    assert m.to_euler_angles_rad().allclose(e, atol=1e-12)


def test_to_euler_angles_rejects_unknown_order():
    m = Matrix3.identity()
    with pytest.raises(ValueError):
        m.to_euler_angles_rad(order="zyx")
    with pytest.raises(ValueError):
        m.to_euler_angles_deg(order="yxz")


def test_to_euler_angles_xyz_order_roundtrip():
    """The (TODO-flagged) XYZ branch decomposes as `Rz @ Ry @ Rx`."""
    rx, ry, rz = 0.2, -0.5, 0.9
    m = Matrix3(_rz(rz) @ _ry(ry) @ _rx(rx))
    e = m.to_euler_angles_rad(order="xyz")
    assert_allclose(np.asarray(e), [rx, ry, rz], atol=1e-12)


def test_matrix3_to_swapped_yz():
    m = Matrix3.from_flat_row_order([float(i) for i in range(9)])
    swapped = m.to_swapped_yz()
    p = np.array([[1.0, 0.0, 0.0], [0.0, 0.0, 1.0], [0.0, 1.0, 0.0]])
    assert_allclose(swapped.data, p @ m.data @ p)
    # Involution.
    assert_allclose(swapped.to_swapped_yz().data, m.data)


def test_matrix3_to_matrix4():
    m = Matrix3.from_euler_angles_deg(EulerDeg((10.0, 20.0, 30.0)))
    m4 = m.to_matrix4()
    assert isinstance(m4, Matrix4)
    assert_allclose(m4.data[:3, :3], m.data)
    assert_allclose(m4.data[3], [0.0, 0.0, 0.0, 1.0])
    assert_allclose(m4.data[:3, 3], [0.0, 0.0, 0.0])


# ===========================================================================
# Matrix4
# ===========================================================================


def test_matrix4_construction():
    m = Matrix4(np.identity(4))
    assert_allclose(m.data, np.identity(4))
    assert_allclose(Matrix4([[1.0] * 4] * 4).data, np.ones((4, 4)))
    with pytest.raises(ValueError):
        Matrix4(np.zeros((3, 3)))
    with pytest.raises(ValueError):
        Matrix4([[1, 2, 3, 4]])
    with pytest.raises(TypeError):
        Matrix4(5)


def test_matrix4_flat_order_roundtrips():
    flat = [float(i) for i in range(16)]
    m = Matrix4.from_flat_row_order(flat)
    assert m.to_flat_row_order() == flat
    mc = Matrix4.from_flat_column_order(flat)
    assert mc.to_flat_column_order() == flat
    assert_allclose(mc.data, m.data.T)
    with pytest.raises(ValueError):
        Matrix4.from_flat_row_order(flat[:15])
    with pytest.raises(ValueError):
        Matrix4.from_flat_column_order(flat + [0.0])


def test_matrix4_identity_zero_transpose_negate():
    assert_allclose(Matrix4.identity().data, np.identity(4))
    assert_allclose(Matrix4.zero().data, np.zeros((4, 4)))
    m = Matrix4.from_flat_row_order([float(i) for i in range(16)])
    assert_allclose(m.T.data, np.arange(16, dtype=float).reshape(4, 4).T)
    assert_allclose((-m).data, -m.data)


def test_matrix4_translate_scale_rotation():
    t = Vector3((1.0, 2.0, 3.0))
    mt = Matrix4.from_translate(t)
    assert mt.get_translate() == t
    assert_allclose((mt @ Vector3((0.0, 0.0, 0.0))).data, [1.0, 2.0, 3.0])

    ms = Matrix4.from_scale(Vector3((2.0, 3.0, 4.0)))
    assert_allclose((ms @ Vector3((1.0, 1.0, 1.0))).data, [2.0, 3.0, 4.0])

    r3 = Matrix3.from_euler_angles_deg(EulerDeg((0.0, 90.0, 0.0)))
    mr = Matrix4.from_rotation_matrix3(r3)
    assert_allclose(mr.get_rotation_submatrix().data, r3.data)
    assert_allclose((mr @ Vector3((0.0, 0.0, 1.0))).data, [1.0, 0.0, 0.0], atol=1e-15)


def test_matrix4_trs_composition():
    """Standard TRS composition: `T @ R @ S` applied to a point."""
    t = Matrix4.from_translate(Vector3((10.0, 0.0, 0.0)))
    r = Matrix4.from_rotation_matrix3(Matrix3.from_euler_angles_deg(EulerDeg((0.0, 90.0, 0.0))))
    s = Matrix4.from_scale(Vector3((2.0, 2.0, 2.0)))
    trs = t @ r @ s
    # (0, 0, 1) -> scale -> (0, 0, 2) -> rotate 90 about Y -> (2, 0, 0) -> translate -> (12, 0, 0)
    assert_allclose((trs @ Vector3((0.0, 0.0, 1.0))).data, [12.0, 0.0, 0.0], atol=1e-12)
    assert trs.get_translate() == Vector3((10.0, 0.0, 0.0))


def test_matrix4_set_translate():
    m = Matrix4.identity()
    m.set_translate(Vector3((5.0, 6.0, 7.0)))
    assert m.get_translate() == Vector3((5.0, 6.0, 7.0))
    assert_allclose(m.data[:3, :3], np.identity(3))


def test_matrix4_inverse():
    t = Matrix4.from_translate(Vector3((1.0, 2.0, 3.0)))
    r = Matrix4.from_rotation_matrix3(Matrix3.from_euler_angles_deg(EulerDeg((10.0, 20.0, 30.0))))
    m = t @ r
    assert_allclose((m @ m.inverse()).data, np.identity(4), atol=1e-12)
    p = Vector3((4.0, -5.0, 6.0))
    assert_allclose((m.inverse() @ (m @ p)).data, p.data, atol=1e-12)


def test_matrix4_matmul_vector4():
    m = Matrix4.from_translate(Vector3((1.0, 2.0, 3.0)))
    v = Vector4((1.0, 1.0, 1.0, 1.0))
    result = m @ v
    assert isinstance(result, Vector4)
    assert_allclose(result.data, m.data @ v.data)


def test_matrix4_matmul_vector3_is_homogeneous_point():
    """`Matrix4 @ Vector3` implicitly appends w=1 (point transform), then drops w."""
    m = Matrix4.from_translate(Vector3((1.0, 2.0, 3.0)))
    assert_allclose((m @ Vector3((0.0, 0.0, 0.0))).data, [1.0, 2.0, 3.0])
    assert isinstance(m @ Vector3((0.0, 0.0, 0.0)), Vector3)


def test_matrix4_repr_contains_rows():
    r = repr(Matrix4.identity())
    assert r.startswith("Matrix4([")
    assert r.count("\n") == 5
    assert repr(Matrix3.identity()).startswith("Matrix3([")


# ===========================================================================
# maths.misc: get_rotmat3 / local_translate / get_distance
# ===========================================================================


def test_get_rotmat3_none_is_identity():
    assert_allclose(get_rotmat3(None).data, np.identity(3))


def test_get_rotmat3_euler_types():
    e = EulerDeg((10.0, 20.0, 30.0))
    assert_allclose(get_rotmat3(e).data, Matrix3.from_euler_angles_deg(e).data)
    r = EulerRad((0.1, 0.2, 0.3))
    assert_allclose(get_rotmat3(r).data, Matrix3.from_euler_angles_rad(r).data)


def test_get_rotmat3_matrix_passthrough():
    m = Matrix3.from_euler_angles_deg(EulerDeg((1.0, 2.0, 3.0)))
    assert get_rotmat3(m) is m


def test_get_rotmat3_rejects_bad_type():
    with pytest.raises(TypeError):
        get_rotmat3("nope")


@pytest.mark.parametrize("rotation", [45.0, 45, [0.0, 45.0, 0.0], (0.0, 45.0, 0.0), Vector3((0.0, 45.0, 0.0))])
def test_get_rotmat3_degree_shortcuts(rotation):
    expected = Matrix3.from_euler_angles_rad(EulerRad((0.0, math.radians(45.0), 0.0)))
    assert_allclose(get_rotmat3(rotation).data, expected.data, atol=1e-12)


def test_get_rotmat3_radians_flag_for_sequences():
    """`radians=True` avoids the `to_rad()` bug, so this path DOES work for raw sequences."""
    assert_allclose(
        get_rotmat3([0.0, math.pi / 2, 0.0], radians=True).data,
        Matrix3.from_euler_angles_rad(EulerRad((0.0, math.pi / 2, 0.0))).data,
    )
    assert_allclose(
        get_rotmat3(math.pi / 2, radians=True).data,
        Matrix3.from_euler_angles_rad(EulerRad((0.0, math.pi / 2, 0.0))).data,
    )


def test_local_translate_zero_distance_returns_pos():
    pos = Vector3((1.0, 2.0, 3.0))
    assert local_translate(pos, EulerDeg.zero(), 0.0) == pos


def test_local_translate_default_axis_is_negative_z():
    pos = Vector3((0.0, 0.0, 0.0))
    result = local_translate(pos, EulerDeg.zero(), 5.0)
    assert_allclose(result.data, [0.0, 0.0, -5.0], atol=1e-12)


def test_local_translate_with_rotation():
    """Yaw of 90 degrees turns local -Z into local -X."""
    result = local_translate(Vector3((0.0, 0.0, 0.0)), EulerDeg((0.0, 90.0, 0.0)), 2.0)
    assert_allclose(result.data, [-2.0, 0.0, 0.0], atol=1e-12)


def test_local_translate_custom_axis_is_normalized():
    result = local_translate(Vector3((1.0, 1.0, 1.0)), EulerDeg.zero(), 3.0, local_axis=Vector3((0.0, 10.0, 0.0)))
    assert_allclose(result.data, [1.0, 4.0, 1.0], atol=1e-12)


def test_local_translate_with_float_rotation():
    result = local_translate(Vector3((0.0, 0.0, 0.0)), 90.0, 2.0)
    assert_allclose(result.data, [-2.0, 0.0, 0.0], atol=1e-12)


def test_get_distance():
    a = Vector3((0.0, 0.0, 0.0))
    b = Vector3((3.0, 4.0, 0.0))
    assert get_distance(a, b) == pytest.approx(5.0)
    assert get_distance(a, b, squared=True) == pytest.approx(25.0)
    # Accepts raw sequences too.
    assert get_distance((0.0, 0.0, 0.0), [1.0, 2.0, 2.0]) == pytest.approx(3.0)
    assert get_distance(a, a) == 0.0


# ===========================================================================
# AABB
# ===========================================================================


def test_aabb():
    box = AABB(Vector3((0.0, 0.0, 0.0)), Vector3((1.0, 2.0, 3.0)))
    assert box.min == Vector3.zero()
    assert box.max == Vector3((1.0, 2.0, 3.0))
    assert "AABB(min=" in repr(box)


def test_aabb_invalid():
    box = AABB.invalid()
    assert box.min == Vector3.single_max()
    assert box.max == Vector3.single_min()
    # 'Invalid' means min > max on every axis, so any real point expands the box.
    assert all(mn > mx for mn, mx in zip(box.min, box.max))
