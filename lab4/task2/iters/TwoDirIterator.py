from task2.iters.InterfaceTwoDirIterator import InterfaceTwoDirIterator
from typing import TypeVar, Generic

V = TypeVar("V")


class TwoDirIterator(InterfaceTwoDirIterator[V], Generic[V]):
    def __init__(self, items: list[V], start_pos: int | None = None) -> None:
        self._items: list[V] = items
        self._index: int = start_pos if start_pos is not None else -1

    def __next__(self) -> V:
        self._index += 1
        if self._index >= len(self._items):
            raise StopIteration
        return self._items[self._index]

    def prev(self) -> V:
        self._index -= 1
        if self._index < 0:
            raise StopIteration
        return self._items[self._index]
