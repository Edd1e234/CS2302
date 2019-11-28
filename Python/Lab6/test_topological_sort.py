# Created by Eddie Garcia at 11/28/19

# Tests for Topological_sort

import unittest

from Python.data_structures.Graphs.graph_al import GraphAL
from Python.data_structures.Graphs.graph_am import GraphAM
from Python.Lab6.topological_sort import compute_indegree_every_vertex_am
from Python.Lab6.topological_sort import compute_indegree_every_vertex_al
from Python.Lab6.topological_sort import get_adj_vertices
from Python.Lab6.topological_sort import topological_sort


def insert_graph(graph):
    # Inserts same data to streamline testing.
    graph.insert_edge(0, 1, 1)
    graph.insert_edge(0, 2, 1)
    graph.insert_edge(1, 3, 1)
    graph.insert_edge(2, 3, 1)
    graph.insert_edge(3, 4, 1)


def insert_cycle(graph):
    graph.insert_edge(0, 1, 1)
    graph.insert_edge(1, 2, 1)
    graph.insert_edge(2, 0, 1)


class TestLab6(unittest.TestCase):
    def setUp(self) -> None:
        self.graph_al = GraphAL(5, weighted=True, directed=True)
        self.graph_am = GraphAM(5, weighted=True, directed=True)
        self.expected_path = [0, 1, 2, 3, 4]
        self.expected_indegrees = [0, 1, 1, 2, 1]

        # Inserting data into graphs.
        insert_graph(self.graph_am)
        insert_graph(self.graph_al)


class TestTopologicalSort(TestLab6):
    def test_compute_indegree_every_vertex_am(self):
        """
        Testing compute_indegrees_every_vertex function, it should returns the
        correct list of indegrees. Expected indegrees are hardcoded.
=        """
        self.assertEqual(self.expected_indegrees,
                         compute_indegree_every_vertex_am(self.graph_am))

    def test_compute_indegree_every_vertex_al(self):
        """
        Testing compute_indegrees_every_vertex function, it should returns the
        correct list of indegrees. Expected indegrees are hardcoded.        :return:
        """
        self.assertEqual(self.expected_indegrees,
                         compute_indegree_every_vertex_al(self.graph_al))

    def test_get_adj_vertices(self):
        """
        Testing get_adj_vertices function, both AL and AM should return the
        same list.
        """
        # Vertices connected to 0.
        expected_vertices = [1, 2]

        # Both should return the same thing.
        self.assertEqual(expected_vertices, get_adj_vertices(
            self.graph_am, 0))
        self.assertEqual(expected_vertices, get_adj_vertices(
            self.graph_al, 0))

    def test_topological_sort_none(self):
        self.assertEqual(None, topological_sort(None))

    def test_topological_sort_cycle(self):
        cycle_graph_am = GraphAM(3, weighted=True, directed=True)
        cycle_graph_al = GraphAL(3, weighted=True, directed=True)

        # Inserting the same edges.
        insert_cycle(cycle_graph_al)
        insert_cycle(cycle_graph_am)

        self.assertEqual(None, topological_sort(cycle_graph_al))
        self.assertEqual(None, topological_sort(cycle_graph_am))

    def test_topological_sort(self):
        # Full End to end test.
        self.assertEqual(self.expected_path, topological_sort(self.graph_al))
        self.assertEqual(self.expected_path, topological_sort(self.graph_am))
