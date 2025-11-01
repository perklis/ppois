from typing import Generic, TypeVar, List
from task2.Vertex import Vertex
from task2.Edge import Edge
from task2.AdjNode import AdjNode
import copy
from task2.exceptions import (
    GraphError,
    EdgeNotFoundError,
    VertexNotFoundError,
)
from task2.iters.TwoDirIterator import TwoDirIterator
from task2.iters.ReverseTwoDirIterator import ReverseTwoDirIterator
from task2.iters.ConstTwoDirIterator import ConstTwoDirIterator
from task2.iters.ConstReverseTwoDirIterator import ConstReverseTwoDirIterator
from task2.iters.ConstContainer import ConstContainer


T = TypeVar("T")
P = TypeVar("P")

IMMUT = (int, float, str, bytes, tuple, frozenset, bool)


class Graph(Generic[T, P]):
    def __init__(self):
        self._vertices: dict[T, Vertex[T, P]] = {}
        self._edges: List[Edge[T, P]] = []

    def _wrap(self, x):
        return x if isinstance(x, IMMUT) else ConstContainer(x)

    def _get_v(self, value: T) -> Vertex[T, P]:
        if value not in self._vertices:
            raise VertexNotFoundError(f"Вершина {value!r} не существует")
        return self._vertices[value]

    def is_vertex_exists(self, value: T) -> bool:
        return value in self._vertices

    def is_edge_exists(self, u: T, v: T) -> bool:
        if not self.is_vertex_exists(u) or not self.is_vertex_exists(v):
            return False
        u_v = self._get_v(u)
        v_v = self._get_v(v)
        cur = u_v.first_adj
        while cur:
            if cur.other is v_v:
                return True
            cur = cur.next
        return False

    def is_empty(self) -> bool:
        return len(self._vertices) == 0

    def vertex_count(self) -> int:
        return len(self._vertices)

    def edge_count(self) -> int:
        return len(self._edges)

    def clear(self) -> None:
        self._vertices.clear()
        self._edges.clear()

    def get_vertex_degree(self, value: T) -> int:
        vert = self._get_v(value)
        count = 0
        cur = vert.first_adj
        while cur:
            count += 1
            cur = cur.next
        return count

    def get_edge_degree(self, u: T, v: T) -> int:
        if not self.is_edge_exists(u, v):
            raise EdgeNotFoundError("Ребра не существует")
        return 2

    def get_adjacent_vertices(self, value: T) -> list[Vertex[T, P]]:
        vert = self._get_v(value)
        result = []
        cur = vert.first_adj
        while cur:
            result.append(cur.other)
            cur = cur.next
        return result

    def get_incident_edges(self, value: T) -> list[AdjNode[T, P]]:
        vert = self._get_v(value)
        result = []
        cur = vert.first_adj
        while cur:
            result.append(cur)
            cur = cur.next
        return result

    def get_edges(self) -> list[tuple[T, T]]:
        return [(e.left.value, e.right.value) for e in self._edges]

    def add_vertex(self, value: T, props: P):
        if self.is_vertex_exists(value):
            raise GraphError("Вершина уже существует")
        v = Vertex(value, props)
        self._vertices[value] = v
        return v

    def add_edge(self, u: T, v: T, data=None):
        if not self.is_vertex_exists(u) or not self.is_vertex_exists(v):
            raise VertexNotFoundError("Одна или обе вершины не существуют")

        if self.is_edge_exists(u, v):
            raise GraphError("Ребро уже есть")

        u_v = self._get_v(u)
        v_v = self._get_v(v)

        e = Edge(u_v, v_v, data)
        self._edges.append(e)

        a1 = AdjNode(u_v, v_v, e)
        a2 = AdjNode(v_v, u_v, e)
        a1.twin = a2
        a2.twin = a1

        a1.next = u_v.first_adj
        if u_v.first_adj:
            u_v.first_adj.prev = a1
        u_v.first_adj = a1

        a2.next = v_v.first_adj
        if v_v.first_adj:
            v_v.first_adj.prev = a2
        v_v.first_adj = a2

        return e

    def _unlink(self, node: AdjNode[T, P]):
        v = node.owner
        if node.prev:
            node.prev.next = node.next
        else:
            v.first_adj = node.next

        if node.next:
            node.next.prev = node.prev

    def remove_edge(self, u: T, v: T):
        if not self.is_edge_exists(u, v):
            raise EdgeNotFoundError("Ребра не существует")

        u_v = self._get_v(u)
        v_v = self._get_v(v)

        cur = u_v.first_adj
        while cur:
            if cur.other is v_v:
                twin = cur.twin
                if twin:
                    self._unlink(twin)
                self._unlink(cur)
                self._edges.remove(cur.edge)
                return
            cur = cur.next

    def remove_vertex(self, value: T):
        if not self.is_vertex_exists(value):
            raise VertexNotFoundError("Вершина не существует")

        vert = self._get_v(value)
        cur = vert.first_adj
        nodes = []

        while cur:
            nodes.append(cur)
            cur = cur.next

        for node in nodes:
            if node.twin:
                self._unlink(node.twin)
            self._unlink(node)
            if node.edge in self._edges:
                self._edges.remove(node.edge)

        del self._vertices[value]

    def vertices_iter(self):
        return TwoDirIterator(list(self._vertices.values()))

    def reverse_vertices_iter(self):
        return ReverseTwoDirIterator(list(self._vertices.values()))

    def const_vertices_iter(self):
        return ConstTwoDirIterator([self._wrap(v) for v in self._vertices.values()])

    def edges_iter(self):
        return TwoDirIterator(self._edges[:])

    def reverse_edges_iter(self):
        return ReverseTwoDirIterator(self._edges[:])

    def const_edges_iter(self):
        return ConstTwoDirIterator([self._wrap(e) for e in self._edges])

    def incident_edges_iter(self, value: T):
        return TwoDirIterator(self.get_incident_edges(value))

    def adjacent_vertices_iter(self, value: T):
        return TwoDirIterator(self.get_adjacent_vertices(value))

    def const_reverse_vertices_iter(self, position: int | None = None):
        items = [ConstContainer(v) for v in self._vertices.values()]
        return ConstReverseTwoDirIterator(items, position)

    def const_reverse_edges_iter(self, position: int | None = None):
        items = [ConstContainer(e) for e in self._edges]
        return ConstReverseTwoDirIterator(items, position)

    def const_reverse_adjacent_vertices_iter(
        self, value: T, position: int | None = None
    ):
        verts = self.get_adjacent_vertices(value)
        items = [ConstContainer(v) for v in verts]
        return ConstReverseTwoDirIterator(items, position)

    def const_reverse_incident_edges_iter(self, value: T, position: int | None = None):
        edges = self.get_incident_edges(value)
        items = [ConstContainer(e) for e in edges]
        return ConstReverseTwoDirIterator(items, position)

    def remove_vertex_by_iterator(self, it):
        v = it._items[it.index]
        if isinstance(v, ConstContainer):
            v = v._wrapped
        self.remove_vertex(v.value)

    def remove_edge_by_iterator(self, it):
        e = it._items[it.index]
        if isinstance(e, ConstContainer):
            e = e._wrapped
        self.remove_edge(e.left.value, e.right.value)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return False
        return set(self._vertices.keys()) == set(other._vertices.keys()) and set(
            self.get_edges()
        ) == set(other.get_edges())

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Graph):
            return False
        return self.edge_count() < other.edge_count()

    def __deepcopy__(self, memo):
        new = Graph[T, P]()

        for val, v in self._vertices.items():
            new.add_vertex(copy.deepcopy(val), copy.deepcopy(v.props))

        for e in self._edges:
            new.add_edge(copy.deepcopy(e.left.value), copy.deepcopy(e.right.value))

        return new

    def __str__(self):
        verts = ", ".join(str(v.value) for v in self._vertices.values())
        edges = ", ".join(f"({e.left.value},{e.right.value})" for e in self._edges)
        return f"Graph(vertices=[{verts}], edges=[{edges}])"
