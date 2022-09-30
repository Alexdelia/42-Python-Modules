#!/usr/bin/env python3

from time import time


def ft_progress(listy: list, w: int = 40) -> list:
    """
    This function displays a progress bar like this:
    ETA: 8.67s [ 23%][=====> ] 233/1000 | elapsed time 2.33s
    """
    size = len(listy)
    start = time()
    for i, item in enumerate(listy):
        percent = i / size * 100
        perw = int(i / size * w)
        elapsed = time() - start
        eta = elapsed * size / (i + 1) - elapsed
        print(f"\r\033[1;34mETA: {eta:.2f}s\033[0m",
              f"\t[{percent:3.0f}%]",
              f"[{'=' * perw}>{' ' * (w - perw)}]",
              f"{i + 1}/{size}",
              f"| elapsed time {elapsed:.2f}s",
              end="")
        yield item

if __name__ == "__main__":
    print(f"{__file__} only contain the function ft_progress:\n{ft_progress.__doc__}")
