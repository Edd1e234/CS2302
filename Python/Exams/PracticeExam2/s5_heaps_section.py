# For all questions, use the following class definitions
class MaxHeap(object):
    # Constructor
    def __init__(self):
        self.tree = []

    # --------------------------------------------------------------------------------------------------------------
    # Problem 19
    # --------------------------------------------------------------------------------------------------------------
    def get_max_sibling_gap(self):

        max_sib_gp = -1
        index = 1
        while 2 * index + 1 < len(self.tree) and 2 * index + 1 < len(self.tree):
            left_sibling = self.tree[2 * index + 1]
            right_sibling = self.tree[2 * index + 2]

            sum_value = left_sibling - right_sibling

            if abs(sum_value) > max_sib_gp:
                max_sib_gp = abs(sum_value)
            index += 1

        return max_sib_gp

    # --------------------------------------------------------------------------------------------------------------
    # Problem 20
    # --------------------------------------------------------------------------------------------------------------
    def is_valid(self):
        for i in range(1, len(self.tree)):
            parent_value = self.tree[(i - 1) // 2]

            if parent_value < self.tree[i]:
                return False

        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 21
    # --------------------------------------------------------------------------------------------------------------
    def is_a_node_equal_to_its_parent(self):

        for i in range(1, len(self.tree)):
            parent_value = self.tree[(i - 1) // 2]
            if parent_value == self.tree[i]:
                return True

        return False

    # --------------------------------------------------------------------------------------------------------------
    # Problem 22
    # --------------------------------------------------------------------------------------------------------------
    def print_path(self, i):
        if i < len(self.tree):
            return
        while i != 0:
            print(self.tree[i])
            i = (i - 1) // 2
        print(self.tree[0])
        return
