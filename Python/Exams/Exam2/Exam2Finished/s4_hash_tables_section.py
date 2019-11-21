import math


class HashTable:
    # Builds a hash table of size 'size'
    def __init__(self, size):
        self.table = [[] for i in range(size)]

    def hash(self, k):
        return k % len(self.table)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 15
    # --------------------------------------------------------------------------------------------------------------
    def insert(self, k):
        loc = self.hash(k)
        bucket = self.table[loc]

        if k in bucket:
            return
        else:
            bucket.append(k)
        return

    # --------------------------------------------------------------------------------------------------------------
    # Problem 16
    # --------------------------------------------------------------------------------------------------------------
    def search(self, k):
        loc = self.hash(k)
        bucket = self.table[loc]

        if k in bucket:
            return bucket
        else:
            return None

    # --------------------------------------------------------------------------------------------------------------
    # Problem 17
    # --------------------------------------------------------------------------------------------------------------
    def min_key (self):
        if self.table is None:
            return math.inf
        min_value = math.inf

        for bucket in self.table:
            for keys in bucket:
                if keys < min_value:
                    min_value = keys
        return min_value  # Feel free to change this line.

    # --------------------------------------------------------------------------------------------------------------
    # Problem 18
    # --------------------------------------------------------------------------------------------------------------
    def load_factor(self):
        if self.table is None:
            return 0

        num_elements = 0

        for bucket in self.table:
            num_elements += len(bucket)

        return num_elements / len(self.table)
