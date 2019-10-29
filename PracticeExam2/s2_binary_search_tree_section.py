# For all questions, use the following class definitions
class BinaryTreeNode:

    def __init__(self, item=0, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def height(self):
        return self._height(self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 7
    # --------------------------------------------------------------------------------------------------------------
    def _height(self, node):
        return 0

    def num_nodes_at_depth(self, d):
        return self._num_nodes_at_depth(d, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 8
    # --------------------------------------------------------------------------------------------------------------
    def _num_nodes_at_depth(self, d, node):
        return 0

    def min_val(self):
        return self._min_val(self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 9
    # --------------------------------------------------------------------------------------------------------------
    def _min_val(self, node):
        return 0

    def max_val_at_depth(self, d):
        return self._max_val_at_depth (d, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 10
    # --------------------------------------------------------------------------------------------------------------
    def _max_val_at_depth (self, d, node):
        return 0


