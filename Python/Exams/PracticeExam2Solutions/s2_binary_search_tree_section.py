import math

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
        if node is None:
            return -1
        return max(self._height(node.left), self._height(node.right)) + 1

    def num_nodes_at_depth(self, d):
        return self._num_nodes_at_depth(d, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 8
    # --------------------------------------------------------------------------------------------------------------
    def _num_nodes_at_depth(self, d, node):
        if node is None:
            return 0

        if d == 0:
            return 1

        return self._num_nodes_at_depth(d-1, node.left) + self._num_nodes_at_depth(d-1, node.right)

    def min_val(self):
        return self._min_val(self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 9
    # --------------------------------------------------------------------------------------------------------------
    def _min_val(self, node):
        if node is None:
            return math.inf

        if node.left is None:
            return node.item

        return self._min_val(node.left)

    def max_val_at_depth(self, d):
        return self._max_val_at_depth (d, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 10
    # --------------------------------------------------------------------------------------------------------------
    def _max_val_at_depth (self, d, node):
        if node is None:
            return -math.inf

        if d == 0:
            return node.item

        return max(self._max_val_at_depth(d - 1, node.left), self._max_val_at_depth(d-1, node.right))


