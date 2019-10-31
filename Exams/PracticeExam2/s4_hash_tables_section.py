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
        loc = hash(k)
        bucket = self.table[loc]

        if k in bucket:
            bucket.append(k)
        return

    # --------------------------------------------------------------------------------------------------------------
    # Problem 16
    # --------------------------------------------------------------------------------------------------------------
    def contains(self, k):
        loc = hash(k)
        bucket = self.table[loc]

        if k in bucket:
            return True
        else:
            return False

    # --------------------------------------------------------------------------------------------------------------
    # Problem 17
    # --------------------------------------------------------------------------------------------------------------
    def get_longest_list(self):
        max_bucket = None
        max_len = 0
        for bucket in self.table:
            if max_len < len(bucket):
                max_len = len(bucket)
                max_bucket = bucket
        return max_bucket

    # --------------------------------------------------------------------------------------------------------------
    # Problem 18
    # --------------------------------------------------------------------------------------------------------------
    def reset_table(self):
        self.table = [[] for i in range(len(self.table))]
        return
