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
    print(root.key)

    # Process left child
    print2DUtil(root.left, space)


# Wrapper over print2DUtil()
def print2D(root):
    # space=[0]
    # Pass initial space count as 0
    print2DUtil(root, 0)


class AVLNode(BSTNode):
    data = None
    height = 0
    parent = None

    def __init__(self, key=None, data=None,
                 left=None, right=None, parent=None):
        self.key = key
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        if key is not None:
            self.height = 1
        else:
            self.height = 0

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


def get_height_set(node):
    if node is None:
        return 0
    else:
        return node.height


class AVLTree(BST):
    """
    Extends Binary Search Tree. Will use many of the same properties.
    """
    # TODO(Edd1e234): When deletion method is added, remember to subtract from this
    #                 Value
    node_total = 0

    def get_node(self, key):
        cur_node = self.root

        while cur_node is not None:
            if cur_node.key == key:
                return cur_node
            elif cur_node.key > key:
                cur_node = cur_node.left
                continue
            elif cur_node.key < key:
                cur_node = cur_node.right
                continue
            else:
                print("Key NOT FOUND")
                return None

    def insert(self, key, data=None):
        # print(key)
        if self.root is None:
            self.root = AVLNode(key, data)
        else:
            self._insert(key, self.root, data)
        self.node_total += 1
        self.root.get_height()

    def _insert(self, key, cur_node, data=None):
        if cur_node.key > key:
            if cur_node.left is None:
                cur_node.left = AVLNode(key, data)
                cur_node.left.parent = cur_node
                self.inspect_insertion(cur_node.left, [])
            else:
                self._insert(key, cur_node.left, data)
        elif cur_node.key < key:
            if cur_node.right is None:
                cur_node.right = AVLNode(key, data)
                cur_node.right.parent = cur_node
                self.inspect_insertion(cur_node.right, [])
            else:
                self._insert(key, cur_node.right, data)
        else:
            print("Value already in tree.")

    def inspect_insertion(self, cur_node, path=None):
        if cur_node.parent is None:
            return
        path.insert(0, cur_node)
        left_height = get_height_set(cur_node.parent.left)
        right_height = get_height_set(cur_node.parent.right)

        if abs(left_height - right_height) > 1:
            path.insert(0, cur_node.parent)
            self.rebalance(path[0], path[1], path[2])
            return

        new_height = 1 + cur_node.height
        if new_height > cur_node.parent.height:
            cur_node.parent.height = new_height

        self.inspect_insertion(cur_node.parent, path)

    def is_balanced(self):
        if self.root is None:
            print("Tree is empty")
            return True
        if abs(get_height_set(self.root.left) - get_height_set(self.root.right)) > 1:
            return True
        else:
            return False

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
