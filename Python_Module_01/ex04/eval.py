from typing import Sequence


class Evaluator:

    @staticmethod
    def zip_evaluate(
        coefs: Sequence[float | int],
        words: Sequence[str],
    ) -> float | int:
        if not _check_args(coefs, words):
            return -1

        return sum([c * len(w) for c, w in zip(coefs, words)])

    @staticmethod
    def enumerate_evaluate(
        coefs: Sequence[float | int],
        words: Sequence[str],
    ) -> float | int:
        if len(coefs) != len(words):
            return -1

        return sum([coefs[i] * len(w) for i, w in enumerate(words)])


def _check_args(
    coefs: Sequence[float | int],
    words: Sequence[str],
) -> bool:
    if len(coefs) != len(words):
        return False

    # not using enumerate or zip because of subject's requirements
    for i in range(len(words)):
        if not isinstance(words[i], str):
            raise TypeError(
                f"{words[i]} at index {i} in words is not a string"
            )
        if not isinstance(coefs[i], (int, float)):
            raise TypeError(
                f"{coefs[i]} at index {i} in coefs is not an int or float"
            )

    return True
