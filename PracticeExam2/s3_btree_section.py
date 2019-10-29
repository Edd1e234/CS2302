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
        return 0

    def num_nodes_at_depth(self, d):
        return self._num_nodes_at_depth(d, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 12
    # --------------------------------------------------------------------------------------------------------------
    def _num_nodes_at_depth(self, d, node):
        return 0


    def max_val_at_depth(self, d):
        return self._max_val_at_depth(d, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 13
    # --------------------------------------------------------------------------------------------------------------
    def _max_val_at_depth(self, d, node):
        return 0

    def search(self, k):
        return self._search(k, self.root)

    # --------------------------------------------------------------------------------------------------------------
    # Problem 14
    # --------------------------------------------------------------------------------------------------------------
    def _search(self, k, node):
        return None

