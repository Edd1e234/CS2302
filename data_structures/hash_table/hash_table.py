class HashTable:
    """
    This is more of a set if anything. 
    """
    num_of_elements = 0

    # Builds a hash table of size 'size'
    def __init__(self, size):
        self.table = [[] for i in range(size)]

    def hash(self, k):
        return k % len(self.table)

    # Inserts k in the appropriate bucket if k is not already there
    def insert(self, k):
        loc = self.hash(k)
        bucket = self.table[loc]

        if k not in bucket:
            self.num_of_elements += 1
            bucket.append(k)

    # Removes k if it is in the table. If k is not in the table, an Exception is raised
    def remove(self, k):
        loc = self.hash(k)
        bucket = self.table[loc]
        if k in bucket:
            self.num_of_elements += -1
            bucket.remove(k)
        else:
            raise ValueError('hashtable.remove(k): k is not in the table')

    def find(self, k):
        # Returns bucket and index where k is stored in the table
        # If k is not in table, return None and -1 as the bucket and index
        loc = self.hash(k)
        bucket = self.table[loc]

        if k in bucket:
            index = bucket.index(k)
            return bucket, index

        return None, -1

    def __str__(self):
        s = ""
        for i in range(len(self.table)):
            bucket = self.table[i]
            s += str(i) + ": "
            s += str(bucket)
            s += "\n"
        s += "size is " + str(len(self.table)) + "\n"
        s += "number of elements is " + str(self.num_of_elements) + "\n"
        return s

    def load_factor(self):  # Problem 2
        return self.num_of_elements / len(self.table)

    def size_longest_list(self):  # Problem 3
        max_bucket = 0

        for bucket in self.table:
            if len(bucket) > max_bucket:
                max_bucket = len(bucket)
        return max_bucket

    def is_valid(self):  # Problem 4
        for bucket in self.table:
            for i in bucket:
                loc = self.hash(i)

                if self.table[loc] != bucket:
                    return False
        return True

    def insert_asc(self, k):  # Problem 5
        return

    def largest_key(self):  # Problem 6
        max_key = 0
        for bucket in self.table:
            for i in bucket:
                if i > max_key:
                    max_key = i
        return max_key

    def resize(self, size):  # Problem 7
        old_table = self.table
        self.table = [[] for i in range(size)]
        for bucket in old_table:
            for i in bucket:
                self.insert(i)
        return

    def get_all_keys(self, keys):
        for bucket in self.table:
            for i in bucket:
                keys.append(i)
        return keys

    def is_equal(self, hash_table):  # Problem 8
        hash_table_keys = hash_table.get_all_keys()
        self_keys = self.get_all_keys()

        for i in range(len(hash_table_keys)):
            if i < len(self_keys):
                return False
            if hash_table_keys[i] is not self_keys[i]:
                return False
        return True

