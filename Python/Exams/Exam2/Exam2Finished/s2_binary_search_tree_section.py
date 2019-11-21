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

    def sum(self):
        return self._sum(self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 7
    # --------------------------------------------------------------------------------------------------------------
    def _sum(self, node):
        if node is None:
            return 0

        return node.item + self._sum(node.left) + self._sum(node.right)  # Feel free to change this line.

    def sum_at_depth(self, d):
        return self._sum_at_depth(d, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 8
    # --------------------------------------------------------------------------------------------------------------
    def _sum_at_depth(self, d, node):
        if d == 0 and node is not None:
            return node.item
        if node is None:
            return 0

        return self._sum_at_depth(d - 1, node.left) + self._sum_at_depth(d - 1, node.right)

    def max_val(self):
        return self._max_val(self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 9
    # --------------------------------------------------------------------------------------------------------------
    def _max_val(self, node):
        if self.root is None:
            return -math.inf
        cur_node = self.root

        while cur_node.right is not None:
            cur_node = cur_node.right
        return cur_node.item

    def search(self, k):
        return self._search(k, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 10
    # --------------------------------------------------------------------------------------------------------------
    def _search(self, k, node):
        cur_node = node

        while cur_node is not None:
            if cur_node.item == k:
                return cur_node
            elif cur_node.item < k:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left
        return None
