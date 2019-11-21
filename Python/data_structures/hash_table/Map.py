class Map:
    def __init__(self, set_size=0):
        self.table = [[] for i in range(set_size)]

    def hash(self, k):
        return k % len(self.table)

    def insert(self, k, value):
        bucket = self._get_bucket(k)

        # One of every value.
        if value not in bucket:
            bucket.append(value)

    def __contains__(self, value):

        for bucket in self.table:
            for values in bucket:
                if values is value:
                    return True
        return False

    def _get_bucket(self, k):
        loc = self.hash(k)
        return self.table[loc]

    def contains_pair(self, key, value):
        bucket = self._get_bucket(key)
        if value in bucket:
            return True
        return False

    def remove(self, key, value):
        bucket = self._get_bucket(key)

        # For the most part should only be 1 item per
        # bucket, should be constant for search.
        if value in bucket:
            bucket.remove(value)
