from typing import TypeVar, Generic
from task2.iters.InterfaceTwoDirIterator import InterfaceTwoDirIterator
from task2.iters.ConstContainer import ConstContainer

V = TypeVar("V")


class ConstReverseTwoDirIterator(InterfaceTwoDirIterator[V], Generic[V]):
    def __init__(self, items: list[V], start: int | None = None) -> None:
        self._items: list[V] = items
        self._index: int = start or len(items)

    def __next__(self) -> ConstContainer[V]:
        self._index -= 1
        if self._index < 0:
            raise StopIteration
        return ConstContainer(self._items[self._index])

    def prev(self) -> ConstContainer[V]:
        self._index += 1
        if self._index >= len(self._items):
            raise StopIteration
        return ConstContainer(self._items[self._index])
