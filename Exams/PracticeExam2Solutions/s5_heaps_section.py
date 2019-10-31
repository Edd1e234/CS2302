# For all questions, use the following class definitions
class MaxHeap():
    # Constructor
    def __init__(self):
        self.tree = []

    # --------------------------------------------------------------------------------------------------------------
    # Problem 19
    # --------------------------------------------------------------------------------------------------------------
    def get_max_sibling_gap(self):

        max_sib_gp = -1
        i = 0
        while (2 * i) + 2 < len(self.tree):
            left_sib = (2 * i) + 1
            right_sib = (2 * i) + 2

            sib_gp = self.tree[right_sib] - self.tree[left_sib]

            if sib_gp > max_sib_gp:
                max_sib_gp = sib_gp

            i += 1

        return max_sib_gp

    # --------------------------------------------------------------------------------------------------------------
    # Problem 20
    # --------------------------------------------------------------------------------------------------------------
    def is_valid(self):
        for i in range(1, len(self.tree)):
            parent_index = (i - 1) // 2
            if self.tree[parent_index] < self.tree[i]:
                return False

        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 21
    # --------------------------------------------------------------------------------------------------------------
    def is_a_node_equal_to_its_parent(self):

        for i in range(1, len(self.tree)):
            parent_index = (i - 1) // 2
            if self.tree[parent_index] == self.tree[i]:
                return True

        return False

    # --------------------------------------------------------------------------------------------------------------
    # Problem 22
    # --------------------------------------------------------------------------------------------------------------
    def print_path(self, i):

        if len(self.tree) == 0:
            return

        while i > 0:
            print(self.tree[i])
            i = (i - 1) // 2

        print(self.tree[0])
