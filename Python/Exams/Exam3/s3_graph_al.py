class Edge:
    def __init__(self, dest, weight=1):
        self.dest = dest
        self.weight = weight


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
        if source >= len(self.al) or dest >= len(
                self.al) or source < 0 or dest < 0:
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

    def vertices_reachable_from(self, src):
        reachable_vertices = set()

        for edge in self.al[src]:
            reachable_vertices.add(edge.dest)

        return reachable_vertices

    def is_identical(self, graph):

        if len(self.al) != len(graph.al):
            return False

        for i in range(len(self.al)):
            s1 = set()
            s2 = set()

            for edge in self.al[i]:
                s1.add(edge.dest)

            for edge in graph.al[i]:
                s2.add(edge.dest)

            if len(s1.intersection(s2)) != len(s1.union(s2)):
                return False

        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 15
    # Done.
    # --------------------------------------------------------------------------------------------------------------
    def num_edges(self):

        count = 0

        for i in range(len(self.al)):
            count += len(self.al[i])

        return count

    # --------------------------------------------------------------------------------------------------------------
    # Problem 16
    # --------------------------------------------------------------------------------------------------------------
    def compute_in_degree(self, v):
        if not self.is_valid_vertex(v) or not self.is_valid_vertex(v):
            return

        in_degree_count = 0

        for lst in self.al:
            for edge in lst:
                if edge.dest == v:  # Replace False with your answer
                    in_degree_count += 1

        return in_degree_count

    # --------------------------------------------------------------------------------------------------------------
    # Problem 17
    # --------------------------------------------------------------------------------------------------------------
    def num_isolated_vertices(self):
        count = 0

        for i in range(len(self.al)):
            if self.isolated_vertices(i):
                count += 1
        return count

    def isolated_vertices(self, v):

        if len(self.al[v]) != 0:
            return False

        for edges in self.al:
            for edge in edges:
                if edge.dest == v:
                    return False
        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 18
    # --------------------------------------------------------------------------------------------------------------
    def highest_in_degree_vertex(self):
        max_in_degree = -float("inf")
        max_v = -1

        for v in range(len(self.al)):
            amount = self.amount_of_in_degree(v)
            if amount > max_in_degree:
                max_in_degree = amount
                max_v = v

        return max_v

    def amount_of_in_degree(self, i):
        amount = 0
        for edges in self.al:
            for edge in edges:
                if edge.dest == i:
                    amount += 1
        return amount
