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
    def group_singletons(self):
        singles = []
        for index in range(len(self.dsf)):
            if self.dsf[index] == -1:
                singles.append(index)

        for index in range(1, len(singles)):
            self.union(singles[0], singles[index])


    # --------------------------------------------------------------------------------------------------------------
    # Problem 25
    # --------------------------------------------------------------------------------------------------------------
    def is_compressed(self):
        for index in range(len(self.dsf)):
            if self.path_(index, 0) > 1:
                return False

        return True

    def path_(self, index, amount):
        if self.dsf[index] == -1:
            return amount
        else:
            return self.path_(self.dsf[index], amount+1)



    # --------------------------------------------------------------------------------------------------------------
    # Problem 26
    # --------------------------------------------------------------------------------------------------------------
    @staticmethod
    def create_dsf(n, k):
        dsf = []  # Feel free to change this line

        # Your code goes here

        for i in range(n):
            if i == k:
                dsf.append(-1)
            else:
                dsf.append(k)

        return dsf
