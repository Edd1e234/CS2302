class GraphAM:

    def __init__(self, vertices, weighted=False, directed=False):
        self.am = []

        for i in range(vertices):  # Assumption / Design Decision: 0 represents non-existing edge
            self.am.append([0] * vertices)

        self.directed = directed
        self.weighted = weighted
        self.representation = 'AM'

    def is_valid_vertex(self, u):
        return 0 <= u < len(self.am)

    def insert_vertex(self):
        for lst in self.am:
            lst.append(0)

        new_row = [0] * (len(self.am) + 1)  # Assumption / Design Decision: 0 represents non-existing edge
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
    def num_edges(self):

        count = 0

        for src in range(len(self.am)):
            for dest in range(len(self.am[src])):
                if self.am[src][dest] != 0:
                    count += 1
        return count

        # Your code goes h
    # --------------------------------------------------------------------------------------------------------------
    # Problem 20
    # --------------------------------------------------------------------------------------------------------------
    def compute_in_degree(self, v):
        if not self.is_valid_vertex(v) or not self.is_valid_vertex(v):
            return

        in_degree_count = 0

        for src in range(len(self.am)):
            if self.am[src][v] != 0:
                in_degree_count += 1

        # Your code goes here

        return in_degree_count

    # --------------------------------------------------------------------------------------------------------------
    # Problem 21
    # --------------------------------------------------------------------------------------------------------------
    def num_isolated_vertices(self):
        count = 0

        for i in range(len(self.am)):
            if self.is_isolated_vertices(i):
                count += 1

        return count

    def is_isolated_vertices(self, v):

        for src in range(len(self.am)):
            if self.am[src][v] != 0:
                return False
        for dest in range(len(self.am[v])):
            if self.am[v][dest] != 0:
                return False
        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 22
    # --------------------------------------------------------------------------------------------------------------
    def highest_in_degree_vertex(self):

        max_in_degree = -float("inf")
        max_v = -1

        for src in range(len(self.am)):
            amount = self.amount_of_in_degree(src)

            if amount > max_in_degree:
                max_in_degree = amount
                max_v = src

        return max_v

    def amount_of_in_degree(self, i):

        amount = 0

        for src in range(len(self.am)):
            if self.am[src][i] != 0:
                amount += 1
        return amount
