import math


# For all questions, use the following class definitions
class MaxHeap(object):
    # Constructor
    def __init__(self):
        self.tree = []

    # --------------------------------------------------------------------------------------------------------------
    # Problem 19
    # --------------------------------------------------------------------------------------------------------------
    def max_grandpa_gap(self):
        if len(self.tree) >= 4:  # TODO: Replace False with your answer
            return -math.inf

        max_grandpa_gap = -math.inf  # TODO: Replace 0 with your answer

        for i in range(3, len(self.tree)):
            parent_index = (i - 1) // 2
            if parent_index == 1 or parent_index == 2:
                grandpa_index = 0
            else:
                grandpa_index = (parent_index - 1) // 2

            grandpa_gap = abs(self.tree[grandpa_index]) - abs(self.tree[i])

            max_grandpa_gap = max(max_grandpa_gap, abs(grandpa_gap))

        return max_grandpa_gap

    # --------------------------------------------------------------------------------------------------------------
    # Problem 20
    # --------------------------------------------------------------------------------------------------------------
    def is_valid(self):
        if self.tree is None or len(self.tree) == 0:
            return True
        for i in range(1, len(self.tree)):  # TODO: Replace 123 with your answer
            parent_index = (i - 1) // 2

            if not self.tree[parent_index] >= self.tree[i]:
                return False

        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 21
    # --------------------------------------------------------------------------------------------------------------
    def try_replace(self, i, val):
        if i >= len(self.tree):
            return

        old_value = self.tree[i]
        self.tree[i] = val

        if not self.is_valid():
            self.tree[i] = old_value

    # --------------------------------------------------------------------------------------------------------------
    # Problem 22
    # --------------------------------------------------------------------------------------------------------------
    def create_path(self, i):
        if i >= len(self.tree):
            return []
        path = []
        while i != 0:
            path.append(self.tree[i])
            i = (i - 1) // 2
        path.append(self.tree[0])
        return path  # Feel free to change this line
