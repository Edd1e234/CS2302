class GraphAM:

    def __init__(self, vertices, weighted=False, directed=False):
        self.am = []

        for i in range(
                vertices):  # Assumption / Design Decision: 0 represents non-existing edge
            self.am.append([0] * vertices)

        self.directed = directed
        self.weighted = weighted
        self.representation = 'AM'

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.am)

    def insert_vertex(self):
        for lst in self.am:
            lst.append(0)

        new_row = [0] * (len(
            self.am) + 1)  # Assumption / Design Decision: 0 represents non-existing edge
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

    def vertices_reachable_from(self, src):
        reachable_vertices = set()

        for i in range(len(self.am)):
            if self.am[src][i] != 0:
                reachable_vertices.add(i)

        return reachable_vertices

    def is_identical(self, graph):

        if len(self.am) != len(graph.am):
            return False

        for src in range(len(self.am)):
            for dest in range(len(self.am)):
                if self.am[src][dest] != graph.am[src][dest]:
                    return False

        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 19
    # --------------------------------------------------------------------------------------------------------------
    def is_there_an_edge(self, src, dest):
        if not self.is_valid_vertex(src) or not self.is_valid_vertex(dest):
            return

        return self.am[src][dest] != 0

    # --------------------------------------------------------------------------------------------------------------
    # Problem 20
    # --------------------------------------------------------------------------------------------------------------
    def compute_out_degree(self, v):
        if not self.is_valid_vertex(v) or not self.is_valid_vertex(v):
            return

        out_degree_count = 0
        for dest in self.am[v]:
            if dest != 0:
                out_degree_count += 1

        # Your code goes here

        return out_degree_count

    # --------------------------------------------------------------------------------------------------------------
    # Problem 21
    # --------------------------------------------------------------------------------------------------------------
    def is_isolated(self, v):
        if not self.is_valid_vertex(v) or not self.is_valid_vertex(v):
            return

        for source in range(len(self.am)):
            if self.am[source][v] != 0:
                return False
        for dest in self.am[v]:
            if dest != 0:
                return False

        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 22
    # --------------------------------------------------------------------------------------------------------------
    @staticmethod
    def create_backward_circle_graph(n):
        if n < 3:  # n must be at least 3
            return

        graph = GraphAM(vertices=n, weighted=False,
                        directed=True)  # Feel free to modify this line

        previous_source = 0
        next_dest = n-1

        for source in range(n):
            graph.insert_edge(previous_source, next_dest, 1)
            previous_source = next_dest
            next_dest += -1

        return graph
