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
    data = None
    left = None
    right = None

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        """
        If 'data' is less than 'self.data' than it will be set to the left, else it will be set to the right. This will
        will be recursively called, until empty node is found.
        :param data: Should be data type int.
        """
        if not isinstance(data, int):
            return
        if data is None:
            return

        if self.data is None:
            self.data = data
            return self

        if self.data >= data:
            if self.left is None:
                self.left = BSTNode(data)
                return self.right
            return self.left.insert(data)
        else:
            if self.right is None:
                self.right = BSTNode(data)
                return self.right
            return self.right.insert(data)


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
            return self.get_height_actual(self.root)
        else:
            return self.get_height_actual(node)

    def get_height_actual(self, node):
        if node is None:
            return 0
        else:
            return max(self.get_height_actual(node.left),
                       self.get_height_actual(node.right)) + 1

    def get_depth(self, node):
        height = self.get_height(node) - 1
        if height is -1:
            return 0
        else:
            return height

    def has_data(self, data):
        temp_node = self.root
        while temp_node is not None:
            if temp_node.data == data:
                return True
            elif temp_node.data > data:
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
        print(node.data)
        self.print_bst_actual(node.right)

    def insert(self, data):
        return self.root.insert(data)

    def remove_node(self, data):
        if self.root.data == data:
            self.root = self.remove_actual_node(data, self.root)
            return
        self.remove_actual_node(data, self.root)

    def remove_actual_node(self, data, node):
        """
        Removes a node from Binary Tree, first searches for 'data'. Once search is complete
        removes the given 'node', places the nodes left child as new node. If left child is
        empty then places the right child as a new node.
        :param data: Data to be removed.
        :param node: Needed for the recursive call.
        :return:
        """
        if node is None:
            return node

        print("Hello")

        if node.data > data:
            node.left = self.remove_actual_node(data, node.left)
        elif node.data < data:
            node.right = self.remove_actual_node(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.data = node.left.data

            # Rotates the remaining nodes.
            node.left = self.remove_actual_node(node.left.data, node.left)

        return node
