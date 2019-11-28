# Created by Eddie Garcia at 11/26/19

# Disjoint set forest.

# Enter scenario name here
# Enter steps here

class DisjointSet(object):
    def __init__(self, size):
        self.forest = [-1] * size

    # Using the path compression technique.
    def find(self, item):
        if self.forest[item] == -1:
            return item
        return self.find(self.forest[item])

    def union(self, a, b):
        root1 = self.find(a)
        root2 = self.find(b)
        self.forest[root1] = root2
