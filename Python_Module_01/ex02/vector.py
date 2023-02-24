from typing import Any, Optional, TypeAlias

VectorValues: TypeAlias = list[list[float]]


class Vector:

    def __init__(self, values: VectorValues | int | range):
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
            assert isinstance(values, range), \
                Vector._check_values_range.__name__ \
                + f" returned True but values: '{values}' is not a {range}"
            self.values = [[float(i)] for i in values]
        else:
            raise ValueError(
                f"Vector values must be {VectorValues}, int or range"
            )

    @staticmethod
    def _check_values_vector(values: Any) -> bool:
        if not isinstance(values, list) or not isinstance(values[0], list):
            return False

        if Vector._check_column_vector(values):
            return True
        if Vector._check_row_vector(values):
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
        if len(values[0]) != 1:
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
        if not isinstance(values, range):
            return False

        if len(values) <= 0:
            raise ValueError("Vector size must be greater than 0")

        return True


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
