# Created by Eddie Garcia at 11/28/19

# Main
# Testing/Demo for Lab 6.

from Python.data_structures.Graphs.graph_am import GraphAM
from Python.Lab6.topological_sort import compute_indegree_every_vertex_am
from Python.Lab6.topological_sort import topological_sort


def main():
    graph = GraphAM(5, weighted=True, directed=True)
    graph.insert_edge(0, 1, 1)
    graph.insert_edge(0, 2, 1)
    graph.insert_edge(1, 3, 1)
    graph.insert_edge(2, 3, 1)
    graph.insert_edge(3, 4, 1)

    print(compute_indegree_every_vertex_am(graph))
    print(topological_sort(graph))

    print("Hello World")


main()
