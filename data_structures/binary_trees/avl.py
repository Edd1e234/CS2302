from data_structures.binary_trees.BinarySearchTree import BST
from data_structures.binary_trees.BinarySearchTree import BSTNode


# Functions: print2D and print2DUtil were 
COUNT = [10]


# Function to print binary tree in 2D
# It does reverse inorder traversal
def print2DUtil(root, space):
    # Base case
    if root is None:
        return

    # Increase distance between levels
    space += COUNT[0]

    # Process right child first
    print2DUtil(root.right, space)

    # Print current node after space
    # count
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(root.data)

    # Process left child
    print2DUtil(root.left, space)


# Wrapper over print2DUtil()
def print2D(root):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)


class AVLNode(BSTNode):
    height = 0
    parent = None

    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        if data is not None:
            self.height = 1
        else:
            self.height = 0

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
            return

        if self.data >= data:
            if self.left is None:
                self.left = BSTNode(data)
                self.left.parent = self
                return self.left
            return self.left.insert(data)
        else:
            if self.right is None:
                self.right = BSTNode(data)
                self.left.parent = self
                return self.right
            return self.right.insert(data)

    def get_height(self):
        return self.get_height_actual(self)

    def get_height_actual(self, node):
        """
        Will calculate the height along with setting the node height as it goes.
        :param node:
        :return:
        """
        if node is None:
            return 0
        else:
            # Sets the node height.
            self.height = max(self.get_height_actual(node.left),
                              self.get_height_actual(node.right)) + 1
            return self.height


def get_height(node):
    if node is None:
        return 0
    else:
        return node.get_height()


class AVLTree(BST):
    """
    Extends Binary Search Tree. Will use many of the same properties.
    """
    tree_height = 0

    def set_tree_height(self):
        self.tree_height = self.root.get_height()

    def insert(self, data):
        if self.root is None:
            self.root = AVLNode(data)
        else:
            self._insert(data, self.root)
        self.set_tree_height()

    def _insert(self, data, cur_node):
        if cur_node.data > data:
            if cur_node.left is None:
                cur_node.left = AVLNode(data)
                cur_node.left.parent = cur_node
                self.inspect_insertion(cur_node.left, [])
            else:
                self._insert(data, cur_node.left)
        elif cur_node.data < data:
            if cur_node.right is None:
                cur_node.right = AVLNode(data)
                cur_node.right.parent = cur_node
                self.inspect_insertion(cur_node.right, [])
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already in tree.")
        self.tree_height = get_height(self.root)

    def inspect_insertion(self, cur_node, path=None):
        if cur_node.parent is None:
            return
        path.insert(0, cur_node)
        left_height = get_height(cur_node.parent.left)
        right_height = get_height(cur_node.parent.right)

        if abs(left_height - right_height) > 1:
            path.insert(0, cur_node.parent)
            self.rebalance(path[0], path[1], path[2])
            return

        new_height = 1 + cur_node.height
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self.inspect_insertion(cur_node.parent, path)

    def rebalance(self, z, y, x):
        """
        This function will determine which rotation will take place. Check your notes for more info on the different
        cases.
        """
        # This is the left left case.
        if y == z.left and x == y.left:
            self.right_rotate(z)
        # This the left right case.
        elif y == z.left and x == y.right:
            self.left_rotate(y)
            self.right_rotate(z)
        # This is the right right case.
        elif y == z.right and x == y.right:
            self.left_rotate(z)
        elif y == z.right and x == y.left:
            self.right_rotate(y)
            self.left_rotate(z)
        else:
            raise Exception('z,y,x node configuration not recognized')

    def right_rotate(self, z):
        print("Right rotate")
        sub_root = z.parent
        y = z.left
        t3 = y.right
        y.right = z
        z.parent = y
        z.left = t3

        if t3 is not None:
            t3.parent = z
        y.parent = sub_root

        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.get_height()
        y.get_height()

    def left_rotate(self, z):
        print("Left Rotate")
        sub_root = z.parent
        y = z.right
        t2 = y.left
        y.left = z
        z.parent = y
        z.right = t2
        if t2 is not None:
            t2.parent = z
        y.parent = sub_root
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left == z:
                y.parent.left = y
            else:
                y.parent.right = y
        z.get_height()
        y.get_height()

    def print_full_tree(self):
        print2D(self.root)
        self.root.get_height()
        print("Tree height is", self.root.height)
