import random
from typing import Generator, Literal, Optional

Option = Literal["shuffle", "unique", "ordered"]


def generator(
    text: str,
    sep: str = " ",
    option: Optional[Option] = None,
) -> Generator[str, None, None]:
    """
        Splits the text according to sep value and yield the substrings.
        option precise if a action is performed\
 to the substrings before it is yielded.
    """
    if not isinstance(text, str) or not isinstance(sep, str):
        yield "ERROR"
        return

    ws = text.split(sep)

    match option:
        case "shuffle":
            ws = sorted(ws, key=lambda x: random.random())
        case "unique":
            seen = set()
            ws = [x for x in ws if x not in seen and not seen.add(x)]
        case "ordered":
            ws = sorted(ws)
        case None:
            pass
        case _:
            yield "ERROR"
            return

    for word in ws:
        yield word


if __name__ == "__main__":
    text = "some text with several words"
    for word in generator(text):
        print(word)
    print()
