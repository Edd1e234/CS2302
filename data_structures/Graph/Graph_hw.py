"""
Homework for graphs.

1.
Adjacency List:
0 -> (dest = 1, weight = 1), (dest = 2, weight = 2), (dest = 3, weight = 3)
1 -> (dest = 0, weight = 1), (dest = 2, weight = 3), (dest = 3, weight = 4)
2 -> (dest = 0, weight = 2), (dest = 1, weight = 3), (dest = 3, weight = 5)
3 -> (dest = 1, weight = 3), (dest = 2, weight = 5), (dest = 3, weight = 4)

Adjacency Matrix:
[
[None, 1, 2, 3]
[1, None, 3, 4]
[2, 3, None, 5]
[3, 4, 5, None]
]

Edge List:
(weight = 1, vertices = 0, 1)
(weight = 2, vertices = 0, 2)
(weight = 3, vertices = 0, 3)
(weight = 3, vertices = 2, 1)
(weight = 5, vertices = 2, 3)
(weight = 4, vertices = 3, 1)

2.
Adjacency List:
0 -> (dest = 1, weight = 1), (dest = 3, weight = 2), (dest = 4, weight = 5)
1 -> (dest = 2, weight = 7), (dest = 4, weight = 3)
2 ->
3 -> (dest = 4, weight = 1)
4 -> (dest = 5, weight = 1), (dest = 2, weight = 5)
4 -> (dest = 2, weight = 1)

Adjacency Matrix:
[None, 1, None, 2, 5, None]
[None, None, 7, None, 3, None]
[None, None, None, None, None, None]
[None, None, None, None, 1, None]
[None, None, 5, None, None, 1]
[None, None, 1, None, None, 1]

Edge List:
(weight = 1, vertices = 0, 1)
(weight = 5, vertices = 0, 4)
(weight = 2, vertices = 0, 3)
(weight = 1, vertices = 3, 4)
(weight = 3, vertices = 1, 4)
(weight = 7, vertices = 1, 2)
(weight = 5, vertices = 4, 2)
(weight = 1, vertices = 4, 5)
(weight = 1, vertices = 5, 2)

"""

from scipy.interpolate import interp1d


class Edge(object):

    pass


class GraphAM:
    def __init__(self, vertices, weighted=False, directed=False):
        self.am = []

        # Assumption / Design Decision: 0 represents non-existing edge.
        for i in range(vertices):
            self.am.append([0] * vertices)
        self.directed = directed
        self.weighted = weighted
        self.representation = 'AM'

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.am)

    def insert_vertex(self):
        for lst in self.am:
            lst.append(0)

        # Assumption / Design Decision: 0 represents non-existing edge
        new_row = [0] * (len(self.am) + 1)
        self.am.append(new_row)

        return len(self.am) - 1  # Return new vertex id

    def insert_edge(self, src, dest, weight=1):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        self.am[src][dest] = weight

        if not self.directed:
            self.am[dest][src] = weight

    def delete_edge(self, src, dest):
        self.insert_edge(src, dest, 0)

    def num_vertices(self):
        return len(self.am)

    def display(self):
        print('[', end='')
        for i in range(len(self.am)):
            print('[', end='')
            for j in range(len(self.am[i])):
                edge = self.am[i][j]
                if edge != 0:
                    print('(' + str(j) + ',' + str(edge) + ')', end='')
            print(']', end=' ')
        print(']')

    # Number 2.
    def get_highest_cost_edge(self):
        max_edge = 0

        for i in range(len(self.am)):
            for j in range(len(self.am[i])):
                if self.am[i][j] is not None:
                    if self.am[i][j] > max_edge:
                        max_edge = self.am[i][j]
        return max_edge

    class GraphAL:
        # Constructor
        def __init__(self, vertices, weighted=False, directed=False):
            self.al = [[] for i in range(vertices)]
            self.weighted = weighted
            self.directed = directed
            self.representation = 'AL'

        def is_valid_vertex(self, u):
            return 0 <= u < len(self.al)

        def insert_vertex(self):
            self.al.append([])

            return len(self.al) - 1  # Return id of new vertex

        def insert_edge(self, source, dest, weight=1):
            if not self.is_valid_vertex(source) or not self.is_valid_vertex(dest):
                print('Error, vertex number out of range')
            elif weight != 1 and not self.weighted:
                print('Error, inserting weighted edge to unweighted graph')
            else:
                self.al[source].append(Edge(dest, weight))
                if not self.directed:
                    self.al[dest].append(Edge(source, weight))

        def delete_edge(self, source, dest):
            if source >= len(self.al) or dest >= len(self.al) or source < 0 or dest < 0:
                print('Error, vertex number out of range')
            else:
                deleted = self._delete_edge(source, dest)
                if not self.directed:
                    deleted = self._delete_edge(dest, source)
                if not deleted:
                    print('Error, edge to delete not found')

        def _delete_edge(self, source, dest):
            i = 0
            for edge in self.al[source]:
                if edge.dest == dest:
                    self.al[source].pop(i)
                    return True
                i += 1
            return False

        def num_vertices(self):
            return len(self.al)

        def display(self):
            print('[', end='')
            for i in range(len(self.al)):
                print('[', end='')
                for edge in self.al[i]:
                    print('(' + str(edge.dest) + ',' + str(edge.weight) + ')', end='')
                print(']', end=' ')
            print(']')

