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

    # --------------------------------------------------------------------------------------------------------------
    # Problem 11
    # --------------------------------------------------------------------------------------------------------------
    def _height(self, node):
        if node is None:
            return -1

        if node.is_leaf:
            return 0

        return 1 + self._height(node.children[0])

    def num_nodes_at_depth(self, d):
        return self._num_nodes_at_depth(d, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 12
    # --------------------------------------------------------------------------------------------------------------
    def _num_nodes_at_depth(self, d, node):
        if node is None:
            return 0

        if d == 0:
            return 1

        num_nodes = 0

        for child in node.children:
            num_nodes += self._num_nodes_at_depth(d-1, child)

        return num_nodes

    def max_val_at_depth(self, d):
        return self._max_val_at_depth(d, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 13
    # --------------------------------------------------------------------------------------------------------------
    def _max_val_at_depth(self, d, node):
        if node is None:
            return -math.inf

        if d == 0:
            return node.keys[-1]

        if node.is_leaf:
            return -math.inf

        return self._max_val_at_depth(d-1, node.children[-1])

    def search(self, k):
        return self._search(k, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 14
    # --------------------------------------------------------------------------------------------------------------
    def _search(self, k, node):
        if node is None:
            return None
        # Returns node where k is, or None if k is not in the tree
        if k in node.keys:
            return node
        if node.is_leaf:
            return None
        return self._search(k, node.children[self.find_child(k, node)])

    def find_child(self, k, node=None):
        # Determines value of c, such that k must be in subtree node.children[c], if k is in the BTree
        if node is None:
            node = self.root

        for i in range(len(node.keys)):
            if k < node.keys[i]:
                return i
        return len(node.keys)
