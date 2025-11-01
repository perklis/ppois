from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Self, Union
from task2.iters.ConstContainer import ConstContainer

V = TypeVar("V")


class InterfaceTwoDirIterator(ABC, Generic[V]):
    _index: int
    _items: list[V]

    @property
    def index(self) -> int:
        return self._index

    def __iter__(self) -> Self:
        return self

    @abstractmethod
    def prev(self) -> Union[V, ConstContainer[V]]: ...

    @abstractmethod
    def __next__(self) -> Union[V, ConstContainer[V]]: ...

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, type(self)):
            return False
        return self._items == other._items and self._index == other._index
