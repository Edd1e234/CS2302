# Created by Eddie Garcia at 11/26/19

# Testing Lab 6 functions
# Enter feature description here
import math
import unittest

from Python.Lab6.kruskal import remove_edge_al
from Python.Lab6.kruskal import remove_edge_am
from Python.data_structures.Graphs.graph_al import GraphAL
from Python.data_structures.Graphs.graph_am import GraphAM
from Python.Lab6.kruskal import EdgeSortObject
from Python.Lab6.kruskal import sort_list_al
from Python.Lab6.kruskal import sort_list_am
from Python.Lab6.kruskal import kruskals_algorithm
from Python.Lab6.kruskal import print_graph_am
from Python.Lab6.kruskal import print_graph_al


def insert_graph(graph):
    graph.insert_edge(0, 1, 1)
    graph.insert_edge(1, 2, 5)
    graph.insert_edge(1, 3, 2)
    graph.insert_edge(2, 3, 3)
    graph.insert_edge(0, 2, 3)  # Remove this.
    graph.insert_edge(3, 5, 4)
    graph.insert_edge(5, 4, 6)
    graph.insert_edge(2, 4, 7)


class TestLab6(unittest.TestCase):
    def setUp(self) -> None:
        self.edge_object_list_al = []
        self.edge_object_list_am = []
        self.graph_al = GraphAL(6, weighted=True)
        self.graph_am = GraphAM(6, weighted=True)

        insert_graph(self.graph_am)
        insert_graph(self.graph_al)


def print_edge_object_list(edge_object_list):
    for edge_object in edge_object_list:
        edge_object.print()


class TestKruskal(TestLab6):

    def print_graph(self):

        print("Printing the graph. ")
        index = 0
        for edges in self.graph_al.al:
            string_edges = ""
            for edge in edges:
                string_edges += "(" + str(index) + ", " + str(
                    edge.dest) + ", " + str(edge.weight) + ") "
            print(string_edges)
            index += 1

    def check_sorted_edge_object_list(self, sorted_edge_object_list):

        previous = math.inf
        for edge_object in sorted_edge_object_list:
            if edge_object.weight <= previous:
                return False, edge_object.weight, previous
            previous = edge_object.weight
        return True, None,

    # Testing whether the remove function removes corresponding edges so
    # they're not counted twice.
    def test_remove_edge_al(self):
        edge_object = EdgeSortObject(0, 2, 3)

        length = len(self.graph_al.al[edge_object.dest])
        popped_edge = remove_edge_al(self.graph_al, edge_object)

        self.assertEqual(edge_object.weight, popped_edge.weight)
        self.assertEqual(edge_object.source, popped_edge.dest)
        self.assertEqual(len(self.graph_al.al[edge_object.dest]), length - 1)

    def test_edge_sort_al(self):
        """
        Testing if 'AL' edge sort sorts the edges properly.
        :return:
        """
        sorted_list = sort_list_al(self.graph_al)
        check_sorted_edge_object_list = \
            self.check_sorted_edge_object_list(sorted_list)

        self.assertTrue(True, check_sorted_edge_object_list[0])

    def test_kruskals_al(self):
        """
        Testing if Kruskals_algorithm runs.
        :return: There is no clear way of testing whether the algorithm got
        the minimum spanning tree. So I just print the previous graph and
        print the new graph.
        """
        print_graph_al(self.graph_al)
        new_graph = kruskals_algorithm(self.graph_al)
        print_graph_al(new_graph)

    def test_remove_edge_am(self):
        """
        Testing remove edge function, I have the 'remove_edge_am' return the
        value it popped, that way we just compare.
        """
        edge_object = EdgeSortObject(0, 2, 3)

        value = remove_edge_am(self.graph_am, edge_object)

        # Removed the right value.
        self.assertEqual(edge_object.weight, value)
        self.assertEqual(0, self.graph_am.am[edge_object.dest][
            edge_object.source])

    def test_edge_sort_am(self):
        """
        Testing if my edge sort.
        """
        sorted_list = sort_list_am(self.graph_am)
        check_sorted_edge_object_list = \
            self.check_sorted_edge_object_list(sorted_list)
        self.assertTrue(True, check_sorted_edge_object_list[0])

    def test_kruskals_am(self):
        """
        Testing if kruskals algorithm runs.
        :return: There is no clear way testing whether the algorithm got the
        minimum spanning tree. So we just print it and have the test check.
        """
        print()
        print_graph_am(self.graph_am)
        new_graph = kruskals_algorithm(self.graph_am)
        print_graph_am(new_graph)

    def test_kruskals(self):
        # Testing the program will not crash if None value is passed.
        self.assertEqual(None, kruskals_algorithm(None))
