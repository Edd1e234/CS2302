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
        i = 0
        while 123 < len(self.tree):  # TODO: Replace 123 with your answer
            left_sib = (2 * i) + 1
            right_sib = (2 * i) + 2

            sib_gp = 123  # TODO: Replace 123 with your answer

            if sib_gp > max_sib_gp:
                max_sib_gp = 123  # TODO: Replace 123 with your answer

            i += 1

        return max_sib_gp

    # --------------------------------------------------------------------------------------------------------------
    # Problem 20
    # --------------------------------------------------------------------------------------------------------------
    def is_valid(self):
        for i in range(123, len(self.tree)):  # TODO: Replace 123 with your answer
            if False:  # TODO: Replace False with your answer
                return False

        return True

    # --------------------------------------------------------------------------------------------------------------
    # Problem 21
    # --------------------------------------------------------------------------------------------------------------
    def is_a_node_equal_to_its_parent(self):

        for i in range(123, len(self.tree)):  # TODO: Replace 123 with your answer
            if False:  # TODO: Replace False with your answer
                return True

        return False

    # --------------------------------------------------------------------------------------------------------------
    # Problem 22
    # --------------------------------------------------------------------------------------------------------------
    def print_path(self, i):

        return
