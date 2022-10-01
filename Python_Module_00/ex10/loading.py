#!/usr/bin/env python3

from math import ceil
from os import get_terminal_size
from time import time
from typing import Any, Generator

_w = get_terminal_size().columns - 72
if _w < 0:
    _w = 3

def ft_progress(listy: 'list[Any]', w: int = _w, fill: str = '=', tip: str = '>') -> Generator[Any, None, None]:
    """
    This function displays a progress bar like this:
    ETA: 8.67s [ 23%][=====> ] 233/1000 | elapsed time 2.33s
    """
    try:
        size = len(listy)
    except TypeError:
        print("ft_progress() argument must be a sequence")
        return
    if size <= 1:
        return
    start = time()
    for i, item in enumerate(listy):
        percent = [i / (size - 1) * 100, 100][i == size - 1]
        perw = ceil(i / (size - 1) * w)
        elapsed = time() - start
        eta = elapsed * size / (i + 1) - elapsed
        print(f"\r\033[1;2;34mETA:\033[0m \033[1;3;34m{eta:.2f}s\033[0m",
              f"\t\033[1m[\033[32m{percent:3.0f}%\033[0m\033[1m]",
              f"[\033[35m{fill * perw}{[tip,fill][i == size - 1]}\033[0m{' ' * (w - perw)}\033[1m]",
              f"\033[3m{i + 1}\033[0m\033[1m/\033[2;3m{size}\033[0m",
              f"\t\033[1m| \033[2;33melapsed time \033[0m\033[1;3;33m{elapsed:.2f}s",
              end="\033[0m")
        yield item

if __name__ == "__main__":
    print(f"{__file__} only contain the function ft_progress:\n{ft_progress.__doc__}")
