# Created by Eddie Garcia at 11/25/19

# Lab 6.
# Implement the following graph algorithms:
#       Kruskal's algorithm.
#       Topological sort.

from Python.data_structures.Graphs.graph_al import GraphAL
from Python.data_structures.Graphs.graph_am import GraphAM
from Python.data_structures.Graphs.DisjointSet import DisjointSet


class EdgeSortObject:

    def __init__(self, source, dest, weight):
        self.source = source
        self.dest = dest
        self.weight = weight

    def print(self):
        print("( ", self.source, ", ", self.dest, ", ", self.weight, ")")


########################################################
# AL Graph Kruskals implementation below.
#######################################################

def remove_edge_al(graph, edge_sort_object):
    """
    Utility function to 'sort_list_al'.
    Given an edge, this function finds the opposite of this edge and removes it
    from the graph. To eliminate it being counted again.
    :param graph:
    :param edge_sort_object:
    :return: The popped value.
    """
    index = 0
    for edge in graph.al[edge_sort_object.dest]:
        if edge.dest == edge_sort_object.source:
            # Returning the value for testing purposes.
            return graph.al[edge_sort_object.dest].pop(index)
        index += 1


# Returns a sorted list for AL graph.
def sort_list_al(graph):
    edge_list = []

    # Insert edges into list.
    source = 0
    for edges in graph.al:
        for edge in edges:
            edge_object = EdgeSortObject(source, edge.dest, edge.weight)
            # Removes the corresponding edge.
            remove_edge_al(graph, edge_object)
            edge_list.append(edge_object)
        source += 1

    sort_edge_object(edge_list, 0, len(edge_list) - 1)
    return edge_list


def print_graph_al(graph):
    print("Printing AL graph. ")
    index = 0
    for edges in graph.al:
        string_edges = str(index) + "-> "
        for edge in edges:
            string_edges += "(src= " + str(index) + ", dest= " + str(
                edge.dest) + ", weight= " + str(edge.weight) + ") "
        print(string_edges)
        index += 1


#########################################################

# Quick Sort.
def sort_edge_object(edge_object_list, low, high):
    if low < high:
        pi = partition(edge_object_list, low, high)

        sort_edge_object(edge_object_list, low, pi - 1)
        sort_edge_object(edge_object_list, pi + 1, high)


def partition(edge_object_list, low, high):
    i = (low - 1)
    pivot = edge_object_list[high].weight

    for j in range(low, high):
        if edge_object_list[j].weight <= pivot:
            i += 1
            edge_object_list[i], edge_object_list[j] = \
                edge_object_list[j], edge_object_list[i]
    edge_object_list[i + 1], edge_object_list[high] = \
        edge_object_list[high], edge_object_list[i + 1]
    return i + 1


##########################################################
# Graph AM implementation below.
##########################################################

def remove_edge_am(graph, edge_object):
    # Testing purposes.
    old_value = graph.am[edge_object.dest][edge_object.source]
    graph.am[edge_object.dest][edge_object.source] = 0
    return old_value


def sort_list_am(graph):
    edge_list = []
    for sources in range(len(graph.am)):
        for dest in range(len(graph.am[sources])):
            weight = graph.am[sources][dest]

            # This is going off the assumption that if the 'weight' is 0 then
            # there is no edge there.
            if weight != 0:
                edge_object = EdgeSortObject(sources, dest, weight)
                edge_list.append(edge_object)
                remove_edge_am(graph, edge_object)
    sort_edge_object(edge_list, 0, len(edge_list) - 1)
    return edge_list


def print_graph_am(graph):
    print("Printing AM Graph.")
    for source in range(len(graph.am)):
        string_edges = ""
        for dest in range(len(graph.am[source])):
            weight = graph.am[source][dest]
            if weight != 0:
                string_edges += "(source= " + str(source) + ",dest= " + str(
                    dest) + ", weight= " + str(weight) + ") "
        print(string_edges)


######################################################

def kruskals_algorithm(graph):
    if graph is None:
        return None
    if isinstance(graph, GraphAL):
        edge_list = sort_list_al(graph)
        new_graph = GraphAL(graph.num_vertices(), weighted=True)
    elif isinstance(graph, GraphAM):
        edge_list = sort_list_am(graph)
        new_graph = GraphAM(graph.num_vertices(), weighted=True)
    else:
        return None

    disjoint_set = DisjointSet(graph.num_vertices())
    for edge_object in edge_list:

        # Checks if they're in the same set.
        source_find = disjoint_set.find(edge_object.source)
        dest_find = disjoint_set.find(edge_object.dest)

        if source_find != dest_find or source_find == -1 and dest_find == -1:
            new_graph.insert_edge(edge_object.source,
                                  edge_object.dest, edge_object.weight)
            # Adding to the disjoint set.
            disjoint_set.union(edge_object.source, edge_object.dest)
    return new_graph  # Returns new graph.

