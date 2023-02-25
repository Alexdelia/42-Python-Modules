from __future__ import annotations

from typing import Any, Optional, TypeAlias

VectorValues: TypeAlias = list[list[float]]
VectorShape: TypeAlias = tuple[int, int]


class Vector:

    def __init__(self, values: VectorValues | int | tuple[int, int]):
        if Vector._check_values_vector(values):
            assert isinstance(values, list), \
                Vector._check_values_vector.__name__ \
                + f" returned True but values: '{values}' is not a {list}"
            self.values = values
        elif Vector._check_values_int(values):
            assert isinstance(values, int), \
                Vector._check_values_int.__name__ \
                + f" returned True but values: '{values}' is not a {int}"
            self.values = [[float(i)] for i in range(values)]
        elif Vector._check_values_range(values):
            assert isinstance(values, tuple), \
                Vector._check_values_range.__name__ \
                + f" returned True but values: '{values}'" \
                + f" is not a {VectorShape} (range)"
            self.values = [[float(i)] for i in range(*values)]
        else:
            raise TypeError(
                f"Vector values must be {VectorValues}, int or range"
            )

    @staticmethod
    def _check_values_vector(values: Any) -> bool:
        if not isinstance(values, list) \
                or not values \
                or not isinstance(values[0], list):
            return False

        if Vector._check_column_vector(values):
            return True
        elif Vector._check_row_vector(values):
            return True
        else:
            raise ValueError("Vector cannot be empty")

    @staticmethod
    def _check_column_vector(values: list[list[Any]]) -> bool:
        if len(values) <= 1:
            return False

        for i, v in enumerate(values):
            if not isinstance(v, list):
                raise TypeError(_error(v, i, holder="values", t=list))

            if len(v) != 1:
                raise ValueError(
                    _error(
                        v,
                        i,
                        holder="values",
                        msg=f"should only have 1 element, found {len(v)}"
                    )
                )

            if not isinstance(v[0], float):
                raise TypeError(_error(v[0], i, holder="values[0]", t=float))

        return True

    @staticmethod
    def _check_row_vector(values: list[list[Any]]) -> bool:
        if len(values) != 1:
            return False
        elif len(values[0]) < 1:
            return False

        for i, v in enumerate(values[0]):
            if not isinstance(v, float):
                raise TypeError(_error(v, i, holder="values[0]", t=float))

        return True

    @staticmethod
    def _check_values_int(values: Any) -> bool:
        if not isinstance(values, int):
            return False

        if values <= 0:
            raise ValueError("Vector size must be greater than 0")

        return True

    @staticmethod
    def _check_values_range(values: Any) -> bool:
        if not isinstance(values, tuple):
            return False

        if len(values) != 2:
            raise ValueError("Vector range must be a tuple of 2 elements")

        for i, v in enumerate(values):
            if not isinstance(v, int):
                raise TypeError(_error(v, i, holder="values", t=int))

        if values[0] >= values[1]:
            raise ValueError(
                f"{values[0]} must be less than {values[1]}\
 for values to be a range"
            )

        return True

    @property
    def shape(self) -> VectorShape:
        return (len(self.values), len(self.values[0]))

    def dot(self, other: Vector) -> float:
        _is_type(other, Vector, op="dot product")

        if self.shape != other.shape:
            raise ValueError(_error_shape("dot", self.shape, other.shape))

        if self.shape[0] == 1:
            return sum(
                [sv * ov for sv, ov in zip(self.values[0], other.values[0])]
            )
        else:
            return sum(
                [sv[0] * ov[0] for sv, ov in zip(self.values, other.values)]
            )

    def T(self) -> Vector:
        # Transpose:
        # [[1, 2, 3]] -> [[1], [2], [3]]    # row to column
        # [[1], [2], [3]] -> [[1, 2, 3]]    # column to row
        if self.shape[0] == 1:
            return Vector([[v] for v in self.values[0]])
        else:
            return Vector([[v[0] for v in self.values]])

    def __str__(self) -> str:
        return f"Vector({self.values})"

    def __repr__(self) -> str:
        return f"Vector({self.values})"

    def __add__(self, other: Vector) -> Vector:
        _is_type(other, Vector, op="add")

        if self.shape != other.shape:
            raise ValueError(_error_shape("add", self.shape, other.shape))

        if self.shape[0] == 1:
            return Vector(
                [[sv + ov for sv, ov in zip(self.values[0], other.values[0])]]
            )
        else:
            return Vector(
                [[sv[0] + ov[0]] for sv, ov in zip(self.values, other.values)]
            )

    def __radd__(self, other: Vector) -> Vector:
        return self + other

    def __sub__(self, other: Vector) -> Vector:
        _is_type(other, Vector, op="sub")

        if self.shape != other.shape:
            raise ValueError(_error_shape("sub", self.shape, other.shape))

        if self.shape[0] == 1:
            return Vector(
                [[sv - ov for sv, ov in zip(self.values[0], other.values[0])]]
            )
        else:
            return Vector(
                [[sv[0] - ov[0]] for sv, ov in zip(self.values, other.values)]
            )

    def __rsub__(self, other: Vector) -> Vector:
        return self - other

    def __truediv__(self, other: float | int) -> Vector:
        _is_type(other, (float, int), op="truediv")

        # automatic raise ZeroDivisionError
        if self.shape[0] == 1:
            return Vector([[sv / other for sv in self.values[0]]])
        else:
            return Vector([[sv[0] / other] for sv in self.values])

    def __rtruediv__(self, other: float | int) -> Vector:
        raise NotImplementedError(
            "Division of a scalar by a Vector is not defined here."
        )

    def __mul__(self, other: float | int) -> Vector:
        _is_type(other, (float, int), op="mul")

        if self.shape[0] == 1:
            return Vector([[sv * other for sv in self.values[0]]])
        else:
            return Vector([[sv[0] * other] for sv in self.values])

    def __rmul__(self, other: float | int) -> Vector:
        return self * other


def _error(
    v: Any,
    i: int,
    holder: Optional[str] = None,
    t: Optional[type] = None,
    msg: Optional[str] = None,
) -> str:
    return f"{v} at index {i}\
{' in ' + holder if holder is not None else ''}\
{' is not a ' + str(t) if t is not None else ''}\
{' ' + msg if msg is not None else ''}"


def _error_shape(
    op: str,
    s1: VectorShape,
    s2: VectorShape,
) -> str:
    return f"cannot {op} vectors of different shapes: {s1} != {s2}"


def _is_type(
    v: object,
    t: type | tuple[type, ...],
    r: bool = True,
    op: Optional[str] = None,
) -> bool:
    if not isinstance(t, tuple):
        t = (t,)
    assert len(t) > 0, "t must have at least one type"

    for i in t:
        if isinstance(v, i):
            return True

    if r:
        if op:
            raise TypeError(f"can only {op} with {t} not with {type(v)}: {v}")
        else:
            raise TypeError(f"expected {t} not {type(v)}: {v}")

    return False
