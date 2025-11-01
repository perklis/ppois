from typing import Generic, TypeVar

T = TypeVar("T")
P = TypeVar("P")


class Edge(Generic[T, P]):
    __slots__ = ("left", "right", "data")

    def __init__(self, left, right, data=None) -> None:
        self.left = left
        self.right = right
        self.data = data or {}

    def __repr__(self) -> str:
        return f"Edge({self.left.value!r}, {self.right.value!r})"
