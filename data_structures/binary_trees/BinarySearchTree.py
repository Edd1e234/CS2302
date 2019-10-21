def printNode(node):
    if node is None:
        return
    printNode(node.left)
    print(node.data)
    printNode(node.right)


class BSTNode(object):
    """
    BSTNode class is currently geared towards ints. Should be used an example.
    """
    key = None
    left = None
    right = None

    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def insert(self, key):
        """
        If 'key' is less than 'self.key' than it will be set to the left, else it will be set to the right. This will
        will be recursively called, until empty node is found.
        :param key: Should be key type int.
        """
        if not isinstance(key, int):
            return
        if key is None:
            return

        if self.key is None:
            self.key = key
            return self

        if self.key >= key:
            if self.left is None:
                self.left = BSTNode(key)
                return self.right
            return self.left.insert(key)
        else:
            if self.right is None:
                self.right = BSTNode(key)
                return self.right
            return self.right.insert(key)


class BST(object):
    """
    This is the actual Binary Search Tree.
    """
    root = None
    height = None
    depth = None

    def __init__(self, root=None):
        self.root = root

    def get_height(self, node=None):
        if node is None:
            return self._get_height_actual(self.root)
        else:
            return self._get_height_actual(node)

    def _get_height_actual(self, node):
        if node is None:
            return 0
        else:
            return max(self._get_height_actual(node.left),
                       self._get_height_actual(node.right)) + 1

    def get_node_total(self, node=None):
        if node is None:
            return self._get_node_total(self.root)
        else:
            return self._get_node_total(node)

    def _get_node_total(self, node):
        if node is None:
            return 0
        return self._get_node_total(node.left) + self._get_node_total(node.right) + 1

    def get_depth(self, node):
        height = self.get_height(node) - 1
        if height is -1:
            return 0
        else:
            return height

    def has_key(self, key):
        temp_node = self.root
        while temp_node is not None:
            if temp_node.key == key:
                return True
            elif temp_node.key > key:
                temp_node = temp_node.left
            else:
                temp_node = temp_node.right

        return False

    def print_bst(self, node=None):
        """
        If 'node' is None then the program will print starting from root. Else it will
        print from the given 'node'.
        """
        print("Printing Binary Tree")
        if node is None:
            self.print_bst_actual(self.root)
        else:
            self.print_bst_actual(node)
        print("\n")

    def print_bst_actual(self, node):
        if node is None:
            return
        self.print_bst_actual(node.left)
        print(node.key)
        self.print_bst_actual(node.right)

    def insert(self, key):
        return self.root.insert(key)

    def remove_node(self, key):
        if self.root.key == key:
            self.root = self.remove_actual_node(key, self.root)
            return
        self.remove_actual_node(key, self.root)

    def remove_actual_node(self, key, node):
        """
        Removes a node from Binary Tree, first searches for 'key'. Once search is complete
        removes the given 'node', places the nodes left child as new node. If left child is
        empty then places the right child as a new node.
        :param key: key to be removed.
        :param node: Needed for the recursive call.
        :return:
        """
        if node is None:
            return node

        print("Hello")

        if node.key > key:
            node.left = self.remove_actual_node(key, node.left)
        elif node.key < key:
            node.right = self.remove_actual_node(key, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.key = node.left.key

            # Rotates the remaining nodes.
            node.left = self.remove_actual_node(node.left.key, node.left)

        return node

