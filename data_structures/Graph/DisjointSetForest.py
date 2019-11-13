"""
1. Trace
 [-1, -1, -1, -1, -1, -1, -1]
 [-1, -1, -1, 2, -1, -1, -1]
 [3, -1, -1, 2, -1, -1, -1]
 [3, -1, -1, 2, -1, 4, -1]
 [3, -1, -1, 2, 3, 4, -1]
 [3, 4, -1, 2, 3, 4, -1]
"""


# Number 8.
def build_dsf(n):
    dsf = DisjointSetForest(n)

    for i in range(n):
        if i % 2 == 0:
            dsf.union(0, i)
        else:
            dsf.union(1, i)


class DisjointSetForest:
    def __init__(self, size):
        self.forest = [-1] * size

    def find(self, a, amount_runs=0):
        # Finds the root 'a'.
        if a >= len(self.forest):
            print(a, " Too big.")
            return -1

        if amount_runs > len(self.forest):
            return -1

        if self.forest[a] < 0:
            return a
        return self.find(self.forest[a], amount_runs + 1)

    def union(self, a, b):
        if self.forest[a] == self.forest[b]:
            print("Part of the same Set")
        root_a = self.find(a)
        root_b = self.find(b)

        self.forest[root_b] = root_a

    def in_same_set(self, a, b):
        return self.find(a) == self.find(b)

    def num_sets(self):
        one_sets = 0

        for i in self.forest:
            if i == -1:
                one_sets += 1
        return one_sets

    def same(self, dsf):
        if len(self.forest) != len(dsf.forest):
            return False

        index = 0
        for i in self.forest:
            if i != dsf.forest[index]:
                return False
            index += 1
        return True

    def get_set(self, a):
        set_ = [a]
        temp = None
        while temp != -1:
            temp = self.forest[temp]
            set_.append(temp)
        return temp
