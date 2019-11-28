# Created by Eddie Garcia at 11/28/19

# Topological Sort
# Implementation for Topological Sort in terms of AL and AM graphs. If
# comment says otherwise all code was written by @Edd1e234

from Python.data_structures.Graphs.graph_al import GraphAL
from Python.data_structures.Graphs.graph_am import GraphAM
from Python.data_structures.queue import Queue

##########################################################################
# AM Graph utility functions.
##########################################################################
def compute_indegree_every_vertex_am(graph):
    all_in_degrees = [0] * graph.num_vertices()

    # If the weight is not zero, then the corresponding dest will then be
    # added to.
    for source in range(len(graph.am)):
        for dest in range(len(graph.am[source])):
            if graph.am[source][dest] != 0:
                all_in_degrees[dest] += 1
    return all_in_degrees


def get_adj_vertices_am(graph, src):
    vertices = []

    # Gets all vertices that are connected to 'src'.
    for i in range(len(graph.am[src])):
        if graph.am[src][i] != 0:
            vertices.append(i)
    return vertices


############################################################################
# AL Graph utility functions.
############################################################################

def compute_indegree_every_vertex_al(graph):
    all_in_degrees = [0] * graph.num_vertices()

    for edges in graph.al:
        for edge in edges:
            all_in_degrees[edge.dest] += 1
    return all_in_degrees


def get_adj_vertices_al(graph, src):
    vertices = []

    # Gets all vertices that are connected to out of 'src'.
    for edge in graph.al[src]:
        vertices.append(edge.dest)
    return vertices
#############################################################################


def get_adj_vertices(graph, src):
    """
    Gets all the adj vertices per the corresponding graph. In other words,
    all vertices 'src' is connected to via an edge.
    :param graph: Could be 'GraphAM' or 'GraphAl'.
    :param src: Where the corresponding vertices would be found from.
    :return: List of adjacency vertices.
    """
    if isinstance(graph, GraphAM):
        return get_adj_vertices_am(graph, src)
    elif isinstance(graph, GraphAL):
        return get_adj_vertices_al(graph, src)
    else:
        return None


def topological_sort(graph):
    # This if else block will get the correct indegrees.
    if isinstance(graph, GraphAM):
        all_in_degrees = compute_indegree_every_vertex_am(graph)
    elif isinstance(graph, GraphAL):
        all_in_degrees = compute_indegree_every_vertex_al(graph)
    else:
        return

    # Code below is taken from Blackboard.
    sort_result = []
    q = Queue()

    for i in range(len(all_in_degrees)):
        if all_in_degrees[i] == 0:
            q.put(i)
    while not q.is_empty():
        u = q.put()
        sort_result.append(u)

        for adj_vertex in get_adj_vertices(graph, u):
            all_in_degrees[adj_vertex] += -1

            if all_in_degrees[adj_vertex] == 0:
                q.put(adj_vertex)

    if len(sort_result) != graph.num_vertices():
        return None
    return sort_result
