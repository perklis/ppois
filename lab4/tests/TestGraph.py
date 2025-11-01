import unittest
from task2.Graph import Graph
from task2.exceptions import (
    GraphError,
    EdgeNotFoundError,
    VertexNotFoundError,
)


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.g = Graph()

    def test_add_vertex(self):
        v = self.g.add_vertex("A", 10)
        self.assertTrue(self.g.is_vertex_exists("A"))
        self.assertEqual(self.g.vertex_count(), 1)
        self.assertEqual(v.value, "A")
        self.assertEqual(v.props, 10)

    def test_add_existing_vertex_raises(self):
        self.g.add_vertex("A", 1)
        with self.assertRaises(GraphError):
            self.g.add_vertex("A", 2)

    def test_add_edge(self):
        self.g.add_vertex("A", 0)
        self.g.add_vertex("B", 0)
        e = self.g.add_edge("A", "B")

        self.assertTrue(self.g.is_edge_exists("A", "B"))
        self.assertEqual(self.g.edge_count(), 1)
        self.assertEqual(e.left.value, "A")
        self.assertEqual(e.right.value, "B")

    def test_add_edge_no_vertices(self):
        with self.assertRaises(VertexNotFoundError):
            self.g.add_edge("A", "B")

    def test_add_existing_edge_raises(self):
        self.g.add_vertex("A", 0)
        self.g.add_vertex("B", 0)
        self.g.add_edge("A", "B")
        with self.assertRaises(GraphError):
            self.g.add_edge("A", "B")

    def test_adjacent_vertices(self):
        self.g.add_vertex("A", 0)
        self.g.add_vertex("B", 0)
        self.g.add_vertex("C", 0)
        self.g.add_edge("A", "B")
        self.g.add_edge("A", "C")

        adj = {v.value for v in self.g.get_adjacent_vertices("A")}
        self.assertEqual(adj, {"B", "C"})

    def test_incident_edges(self):
        self.g.add_vertex("A", 0)
        self.g.add_vertex("B", 0)
        self.g.add_vertex("C", 0)
        self.g.add_edge("A", "B")
        self.g.add_edge("A", "C")

        inc = self.g.get_incident_edges("A")
        ends = {(node.owner.value, node.other.value) for node in inc}

        self.assertEqual(ends, {("A", "B"), ("A", "C")})

    def test_remove_edge(self):
        self.g.add_vertex("A", 0)
        self.g.add_vertex("B", 0)
        self.g.add_edge("A", "B")

        self.g.remove_edge("A", "B")
        self.assertFalse(self.g.is_edge_exists("A", "B"))
        self.assertEqual(self.g.edge_count(), 0)

    def test_remove_edge_not_exists(self):
        self.g.add_vertex("A", 0)
        self.g.add_vertex("B", 0)
        with self.assertRaises(EdgeNotFoundError):
            self.g.remove_edge("A", "B")

    def test_remove_vertex(self):
        self.g.add_vertex("A", 0)
        self.g.add_vertex("B", 0)
        self.g.add_edge("A", "B")

        self.g.remove_vertex("A")

        self.assertFalse(self.g.is_vertex_exists("A"))
        self.assertEqual(self.g.vertex_count(), 1)
        self.assertFalse(self.g.is_edge_exists("A", "B"))

    def test_remove_vertex_not_exists(self):
        with self.assertRaises(VertexNotFoundError):
            self.g.remove_vertex("X")

    def test_get_vertex_degree(self):
        self.g.add_vertex("A", 0)
        self.g.add_vertex("B", 0)
        self.g.add_vertex("C", 0)
        self.g.add_edge("A", "B")
        self.g.add_edge("A", "C")

        self.assertEqual(self.g.get_vertex_degree("A"), 2)
        self.assertEqual(self.g.get_vertex_degree("B"), 1)

    def test_get_edge_degree(self):
        self.g.add_vertex("A", 0)
        self.g.add_vertex("B", 0)
        self.g.add_edge("A", "B")

        self.assertEqual(self.g.get_edge_degree("A", "B"), 2)

    def test_get_edge_degree_not_exists(self):
        self.g.add_vertex("A", 0)
        self.g.add_vertex("B", 0)
        with self.assertRaises(EdgeNotFoundError):
            self.g.get_edge_degree("A", "B")

    def test_iter_vertices(self):
        self.g.add_vertex("A", 0)
        self.g.add_vertex("B", 0)
        it = self.g.vertices_iter()
        values = {v.value for v in it}
        self.assertEqual(values, {"A", "B"})

    def test_iter_edges(self):
        self.g.add_vertex("A", 0)
        self.g.add_vertex("B", 0)
        self.g.add_edge("A", "B")
        it = self.g.edges_iter()
        pairs = {(e.left.value, e.right.value) for e in it}
        self.assertEqual(pairs, {("A", "B")})

    def test_graph_equality(self):
        g1 = Graph()
        g2 = Graph()

        g1.add_vertex("A", 0)
        g1.add_vertex("B", 0)
        g1.add_edge("A", "B")

        g2.add_vertex("A", 0)
        g2.add_vertex("B", 0)
        g2.add_edge("A", "B")

        self.assertEqual(g1, g2)

    def test_graph_less(self):
        g1 = Graph()
        g2 = Graph()

        g1.add_vertex("A", 0)
        g1.add_vertex("B", 0)
        g1.add_edge("A", "B")

        g2.add_vertex("A", 0)
        g2.add_vertex("B", 0)

        self.assertFalse(g1 < g2)
        self.assertTrue(g2 < g1)

    def test_deepcopy(self):
        self.g.add_vertex("A", 10)
        self.g.add_vertex("B", 20)
        self.g.add_edge("A", "B")

        import copy

        g2 = copy.deepcopy(self.g)

        self.assertEqual(self.g, g2)

        self.g.remove_vertex("A")
        self.assertNotEqual(self.g, g2)
