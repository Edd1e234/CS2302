# For all questions, use the following class definitions
class DisjointSetForest:
    def __init__(self, n):
        self.dsf = [-1] * n

    def is_index_valid(self, index):
        return 0 <= index <= len(self.dsf)

    def find(self, a):
        if not self.is_index_valid(a):
            return -1

        if self.dsf[a] < 0:
            return a

        return self.find(self.dsf[a])

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)

        self.dsf[rb] = ra

    # --------------------------------------------------------------------------------------------------------------
    # Problem 23
    # --------------------------------------------------------------------------------------------------------------
    def get_num_sets(self):
        count = 0

        for i in self.dsf:
            if i == -1:
                count += 1

        return count

    # --------------------------------------------------------------------------------------------------------------
    # Problem 24
    # --------------------------------------------------------------------------------------------------------------
    @staticmethod
    def create_dsf(n):
        dsf = [-1] * n

        # Assuming the n will always at least be 2.
        head = 0
        subset = 1

        for i in range(len(dsf)):
            try:
                dsf[subset] = head
            except IndexError:
                continue
            subset += 2
            head += 2

        return dsf

