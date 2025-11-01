from typing import Generic, TypeVar, Optional

T = TypeVar("T")
P = TypeVar("P")


class Vertex(Generic[T, P]):
    __slots__ = ("value", "props", "first_adj")

    def __init__(self, value: T, props: P) -> None:
        self.value = value
        self.props = props
        self.first_adj: Optional["AdjNode[T, P]"] = None

    def __repr__(self) -> str:
        return f"Vertex({self.value!r})"
