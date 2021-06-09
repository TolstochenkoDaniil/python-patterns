"""
Implementation of the iterator pattern using the iterator protocol from Python

*TL;DR
Traverses a container and accesses the container's elements.
"""


from __future__ import annotations

from typing import Tuple
from copy import deepcopy


class NumberWords:
    _WORD_MAP: Tuple[str, ...] = (
        "one",
        "two",
        "three",
        "four",
        "five"
    )

    def __init__(self, start: int, stop: int) -> None:
        self.index = start
        self.stop = stop

    def __iter__(self) -> NumberWords:   # makes the class an Iterable
        return deepcopy(self)

    def __next__(self) -> str:   # makes the class an Iterator
        if self.index > self.stop or self.index > len(self._WORD_MAP):
            raise StopIteration

        item = self._WORD_MAP[self.index - 1]
        self.index += 1

        return item


def main():
    """
    >>> numObj = NumberWords(start=1, stop=2)
    >>> for number in numObj:
    ...     print(number)
    one
    two
    >>> for number in numObj:
    ...     print(number)
    one
    two
    >>> for number in NumberWords(start=1, stop=5):
    ...     print(number)
    one
    two
    three
    four
    five
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()