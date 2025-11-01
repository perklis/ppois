from typing import Generic, TypeVar, Optional
from task2.Edge import Edge
from task2.Vertex import Vertex

T = TypeVar("T")
P = TypeVar("P")


class AdjNode(Generic[T, P]):
    __slots__ = ("owner", "other", "edge", "twin", "prev", "next")

    def __init__(self, owner: Vertex[T, P], other: Vertex[T, P], edge: Edge[T, P]):
        self.owner = owner
        self.other = other
        self.edge = edge
        self.twin: Optional["AdjNode[T, P]"] = None
        self.prev: Optional["AdjNode[T, P]"] = None
        self.next: Optional["AdjNode[T, P]"] = None

    def __repr__(self) -> str:
        return f"AdjNode({self.owner.value!r}->{self.other.value!r})"
