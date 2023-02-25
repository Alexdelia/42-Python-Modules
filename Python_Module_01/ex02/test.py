#!/usr/bin/env python3

import pytest
from vector import Vector

if __name__ == "__main__":
    pytest.main(args=["-v", __file__])


@pytest.fixture(scope="function")
def values_column():
    return [[0.0], [1.0], [2.0], [3.0]]


@pytest.fixture(scope="function")
def values_row():
    return [[0.0, 1.0, 2.0, 3.0]]


@pytest.fixture(scope="function")
def shape_column():
    return (4, 1)


@pytest.fixture(scope="function")
def shape_row():
    return (1, 4)


def test_vector_basic(values_column, values_row, shape_column, shape_row):
    v = Vector(values_column)
    assert v.values == values_column
    assert v.shape == shape_column
    assert str(v) == "Vector([[0.0], [1.0], [2.0], [3.0]])"
    assert repr(v) == "Vector([[0.0], [1.0], [2.0], [3.0]])"

    v = Vector(values_row)
    assert v.values == values_row
    assert v.shape == shape_row
    assert str(v) == "Vector([[0.0, 1.0, 2.0, 3.0]])"
    assert repr(v) == "Vector([[0.0, 1.0, 2.0, 3.0]])"

    neg = [[-v for v in values_row[0]]]
    v = Vector(neg)
    assert v.values == neg
    assert v.shape == shape_row


def test_vector_basic_invalid():
    with pytest.raises(ValueError):
        Vector([[0.0, 1.0], [2.0, 3.0, 4.0]])

    with pytest.raises(ValueError):
        Vector([[]])

    with pytest.raises((TypeError, ValueError)):
        Vector([])

    with pytest.raises(TypeError):
        Vector([[[0.0]]])  # type: ignore

    with pytest.raises(ValueError):
        Vector([[0.0, 1.0], [2.0]])

    with pytest.raises(TypeError):
        Vector([[0, 1.0]])  # type: ignore

    with pytest.raises(TypeError):
        Vector([["0", 1.0]])  # type: ignore

    with pytest.raises(ValueError):
        Vector([[0.0], [], [2.0]])

    with pytest.raises(TypeError):
        Vector()  # type: ignore


def test_vector_size():
    v = Vector(5)
    assert v.values == [[0.0], [1.0], [2.0], [3.0], [4.0]]
    assert v.shape == (5, 1)

    v = Vector(1)
    assert v.values == [[0.0]]
    assert v.shape == (1, 1)


def test_vector_size_invalid():
    with pytest.raises(ValueError):
        Vector(0)

    with pytest.raises(ValueError):
        Vector(-1)

    with pytest.raises(TypeError):
        Vector("1")  # type: ignore

    with pytest.raises(TypeError):
        Vector(1.0)  # type: ignore

    with pytest.raises(TypeError):
        Vector(None)  # type: ignore


def test_vector_range():
    v = Vector((10, 16))
    assert v.values == [[10.0], [11.0], [12.0], [13.0], [14.0], [15.0]]
    assert v.shape == (6, 1)

    v = Vector((1, 2))
    assert v.values == [[1.0]]
    assert v.shape == (1, 1)


def test_vector_range_invalid():
    with pytest.raises(ValueError):
        Vector((1, 0))

    with pytest.raises(ValueError):
        Vector((1, 1))

    with pytest.raises(TypeError):
        Vector((1, "1"))  # type: ignore

    with pytest.raises(TypeError):
        Vector((1, 1.0))  # type: ignore

    with pytest.raises(TypeError):
        Vector((1, None))  # type: ignore

    with pytest.raises((TypeError, ValueError)):
        Vector((1, 1, 1))  # type: ignore


def test_vector_transpose(values_column, values_row, shape_column, shape_row):
    v = Vector(values_column)
    assert v.T().values == values_row
    assert v.T().shape == shape_row

    v = Vector(values_row)
    assert v.T().values == values_column
    assert v.T().shape == shape_column


def test_vector_dot(values_column, values_row):
    v1 = Vector(values_column)
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])

    assert v1.dot(v2) == 18.0

    v1 = Vector(values_row)
    v2 = Vector([[2.0, 1.5, 2.25, 4.0]])

    assert v1.dot(v2) == 18.0

    v1 = Vector([[1.0, 3.0]])
    v2 = Vector([[2.0, 4.0]])

    assert v1.dot(v2) == 14.0

    v1 = Vector([[1.0], [3.0]])
    v2 = Vector([[2.0], [4.0]])

    assert v1.dot(v2) == 14.0


def test_vector_dot_invalid(values_column, values_row):
    v1 = Vector(values_column)
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])

    with pytest.raises(ValueError):
        v1.dot(v2.T())

    with pytest.raises(ValueError):
        v1.T().dot(v2)

    assert v1.T().dot(v2.T()) == 18.0

    v1 = Vector(values_row)
    v2 = Vector([[2.0, 1.5, 2.25, 4.0]])

    with pytest.raises(ValueError):
        v1.dot(v2.T())

    with pytest.raises(ValueError):
        v1.T().dot(v2)

    assert v1.T().dot(v2.T()) == 18.0

    with pytest.raises(TypeError):
        v1.dot(1.0)  # type: ignore

    with pytest.raises(TypeError):
        v1.dot("1")  # type: ignore

    with pytest.raises(TypeError):
        v1.dot(1)  # type: ignore


def test_vector_add(values_column, values_row, shape_column, shape_row):
    v1 = Vector(values_column)
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])

    v3 = v1 + v2
    assert v3.values == [[2.0], [2.5], [4.25], [7.0]]
    assert v3.shape == shape_column

    v3 = v2 + v1
    assert v3.values == [[2.0], [2.5], [4.25], [7.0]]
    assert v3.shape == shape_column

    v1 = Vector(values_row)
    v2 = Vector([[2.0, 1.5, 2.25, 4.0]])

    v3 = v1 + v2
    assert v3.values == [[2.0, 2.5, 4.25, 7.0]]
    assert v3.shape == shape_row

    v3 = v2 + v1
    assert v3.values == [[2.0, 2.5, 4.25, 7.0]]
    assert v3.shape == shape_row


def test_vector_add_invalid(values_column, values_row):
    v1 = Vector(values_column)
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])

    with pytest.raises(ValueError):
        _ = v1 + v2.T()

    with pytest.raises(ValueError):
        _ = v1.T() + v2

    v1 = Vector(values_row)
    v2 = Vector([[2.0, 1.5, 2.25, 4.0]])

    with pytest.raises(ValueError):
        _ = v1 + v2.T()

    with pytest.raises(ValueError):
        _ = v1.T() + v2

    with pytest.raises(TypeError):
        v1 + 1.0  # type: ignore

    with pytest.raises(TypeError):
        v1 + "1"  # type: ignore

    with pytest.raises(TypeError):
        v1 + 1  # type: ignore


def test_vector_sub(values_column, values_row, shape_column, shape_row):
    v1 = Vector(values_column)
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])

    v3 = v1 - v2
    assert v3.values == [[-2.0], [-0.5], [-0.25], [-1.0]]
    assert v3.shape == shape_column

    v3 = v2 - v1
    assert v3.values == [[2.0], [0.5], [0.25], [1.0]]
    assert v3.shape == shape_column

    v1 = Vector(values_row)
    v2 = Vector([[2.0, 1.5, 2.25, 4.0]])

    v3 = v1 - v2
    assert v3.values == [[-2.0, -0.5, -0.25, -1.0]]
    assert v3.shape == shape_row

    v3 = v2 - v1
    assert v3.values == [[2.0, 0.5, 0.25, 1.0]]
    assert v3.shape == shape_row


def test_vector_sub_invalid(values_column, values_row):
    v1 = Vector(values_column)
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])

    with pytest.raises(ValueError):
        _ = v1 - v2.T()

    with pytest.raises(ValueError):
        _ = v1.T() - v2

    v1 = Vector(values_row)
    v2 = Vector([[2.0, 1.5, 2.25, 4.0]])

    with pytest.raises(ValueError):
        _ = v1 - v2.T()

    with pytest.raises(ValueError):
        _ = v1.T() - v2

    with pytest.raises(TypeError):
        v1 - 1.0  # type: ignore

    with pytest.raises(TypeError):
        v1 - "1"  # type: ignore

    with pytest.raises(TypeError):
        v1 - 1  # type: ignore


def test_vector_mul(values_column, values_row, shape_column, shape_row):
    v1 = Vector(values_column)
    v2 = v1 * 5
    RES_COL = [[0.0], [5.0], [10.0], [15.0]]
    assert v2.values == RES_COL
    assert v2.shape == shape_column

    v1 = Vector(values_row)
    v2 = v1 * 5
    RES_ROW = [[0.0, 5.0, 10.0, 15.0]]
    assert v2.values == RES_ROW
    assert v2.shape == shape_row

    v1 = Vector(values_column)
    v2 = 5 * v1
    assert v2.values == RES_COL
    assert v2.shape == shape_column

    v1 = Vector(values_row)
    v2 = 5 * v1
    assert v2.values == RES_ROW
    assert v2.shape == shape_row

    v1 = Vector(values_column)
    v2 = v1 * 5.0
    assert v2.values == RES_COL
    assert v2.shape == shape_column

    v1 = Vector(values_row)
    v2 = v1 * 5.0
    assert v2.values == RES_ROW
    assert v2.shape == shape_row

    v1 = Vector(values_column)
    v2 = 5.0 * v1
    assert v2.values == RES_COL
    assert v2.shape == shape_column

    v1 = Vector(values_row)
    v2 = 5.0 * v1
    assert v2.values == RES_ROW
    assert v2.shape == shape_row

    v1 = Vector(values_column)
    v2 = v1 * -5
    assert v2.values == [[-v[0]] for v in RES_COL]
    assert v2.shape == shape_column

    v1 = Vector(values_row)
    v2 = v1 * -5
    assert v2.values == [[-v for v in RES_ROW[0]]]
    assert v2.shape == shape_row

    v1 = Vector(values_column)
    v2 = v1 * 0
    assert v2.values == [[0.0] for _ in range(len(RES_COL))]
    assert v2.shape == shape_column

    v1 = Vector(values_row)
    v2 = v1 * 0
    assert v2.values == [[0.0 for _ in range(len(RES_ROW[0]))]]
    assert v2.shape == shape_row


def test_vector_mul_invalid(values_column):
    v1 = Vector(values_column)
    v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
    assert v1.shape == v2.shape

    with pytest.raises(TypeError):
        v1 * "1"  # type: ignore

    with pytest.raises(TypeError):
        v1 * [1]  # type: ignore

    with pytest.raises(TypeError):
        v1 * v2  # type: ignore


def test_vector_div(values_column, values_row, shape_column, shape_row):
    v1 = Vector(values_column)
    v2 = v1 / 2
    RES_COL = [[0.0], [0.5], [1.0], [1.5]]
    assert v2.values == RES_COL
    assert v2.shape == shape_column

    v1 = Vector(values_row)
    v2 = v1 / 2
    RES_ROW = [[0.0, 0.5, 1.0, 1.5]]
    assert v2.values == RES_ROW
    assert v2.shape == shape_row

    v1 = Vector(values_column)
    v2 = v1 / 2.0
    assert v2.values == RES_COL
    assert v2.shape == shape_column

    v1 = Vector(values_row)
    v2 = v1 / 2.0
    assert v2.values == RES_ROW
    assert v2.shape == shape_row

    v1 = Vector(values_column)
    v2 = v1 / -2.0
    assert v2.values == [[-v[0]] for v in RES_COL]
    assert v2.shape == shape_column

    v1 = Vector(values_row)
    v2 = v1 / -2.0
    assert v2.values == [[-v for v in RES_ROW[0]]]
    assert v2.shape == shape_row


def test_vector_div_invalid(values_column, values_row):
    v1 = Vector(values_column)
    with pytest.raises(ZeroDivisionError):
        _ = v1 / 0.0

    v1 = Vector(values_row)
    with pytest.raises(ZeroDivisionError):
        _ = v1 / 0.0

    v1 = Vector(values_column)
    with pytest.raises(NotImplementedError):
        _ = 2.0 / v1

    v1 = Vector(values_row)
    with pytest.raises(NotImplementedError):
        _ = 2.0 / v1
