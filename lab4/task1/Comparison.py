from typing import Protocol, Self


class Comparison(Protocol):
    def __lt__(self, other: Self, /) -> bool:
        pass
