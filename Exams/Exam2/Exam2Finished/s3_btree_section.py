import math


class BTreeNode:
    # Constructor
    def __init__(self, keys=[], children=[], is_leaf=True, max_num_keys=5):
        self.keys = keys
        self.children = children
        self.is_leaf = is_leaf
        if max_num_keys < 3:  # max_num_keys must be odd and greater or equal to 3
            max_num_keys = 3
        if max_num_keys % 2 == 0:  # max_num_keys must be odd and greater or equal to 3
            max_num_keys += 1
        self.max_num_keys = max_num_keys

    def is_full(self):
        return len(self.keys) >= self.max_num_keys


class BTree:
    # Constructor
    def __init__(self, max_num_keys=5):
        self.max_num_keys = max_num_keys
        self.root = BTreeNode(max_num_keys=max_num_keys)

    def height(self):
        return self._height(self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 11
    # --------------------------------------------------------------------------------------------------------------
    def _height(self, node):
        if self.root is None:
            return -1
        if node is None:
            return 0
        if node.children is None or len(node.children) == 0:
            return 0
        return self._height(node.children[0]) + 1

    def num_nodes(self):
        return self._num_nodes(self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 12
    # --------------------------------------------------------------------------------------------------------------
    def _num_nodes(self, node):
        if self.root is None:
            return 0
        if node is None:
            return 0
        if node.is_leaf:
            return 1
        value = 0
        for i in range(len(node.children)):
            value += self._num_nodes(node.children[i])
        return value + 1

    def sum_at_depth(self, d):
        return self._sum_at_depth(d, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 13
    # --------------------------------------------------------------------------------------------------------------
    def _sum_at_depth(self, d, node):
        if d == 0:
            value = 0
            for i in node.keys:
                value += i
            return value
        if node.is_leaf:
            return 0
        value = 0
        for i in node.children:
            value += self._sum_at_depth(d - 1, i)
        return value  # Feel free to change this line

    def contains(self, k):
        return self._contains(k, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 14
    # --------------------------------------------------------------------------------------------------------------
    def _contains(self, k, node):
        if self.root is None:
            return False
        if k in node.keys:
            return True
        elif node.is_leaf:
            return False
        else:
            for i in range(len(node.keys)):
                if k < node.keys[i]:
                    return self._contains(k, node.children[i])
        return self._contains(k, node.children[len(node.keys)])
