from Python.data_structures.binary_trees.avl import AVLTree
from Python.data_structures.binary_trees.avl import AVLNode


class RBNode(AVLNode):
    """
    Class for implementing the nodes that the tree will use
    For self.color:
        red == False
        black == True
        If the node is a leaf it will either
    """

    def __init__(self, key=None, data=None):
        self.data = data
        self.red = True
        self.parent = None
        self.key = key
        self.left = None
        self.right = None


def RBTreeGetGrandparent(node):
    if node.parent is None:
        return None
    return node.parent.parent


def RBTreeGetUncle(node):
    grandparent = None
    if node.parent is not None:
        grandparent = node.parent.parent
    if grandparent is None:
        return None
    if grandparent.left is node.parent:
        return grandparent.right
    else:
        return grandparent.left


class RedBlackTree(AVLTree):
    """
    Class for implementing a standard red-black trees
    """

    def insert(self, key, data=None):
        if self.root is None:
            self.root = RBNode(key, data)
            self.RBTreeBalance(self.root)
            return
        new_node = RBNode(key, data)
        cur_node = self.root

        while cur_node is not None:
            if cur_node.key > key:
                if cur_node.left is None:
                    cur_node.left = new_node
                    cur_node.left.parent = cur_node
                    break
                else:
                    cur_node = cur_node.left
            elif cur_node.key < key:
                if cur_node.right is None:
                    cur_node.right = new_node
                    cur_node.right.parent = cur_node
                    break
                else:
                    cur_node = cur_node.right
            else:
                print("Value already in tree.")
                return
        self.RBTreeBalance(new_node)
        self.node_total += 1

    def RBTreeBalance(self, node):
        if node.parent is None:
            node.red = False
            return
        if not node.parent.red:
            return

        parent = node.parent
        grandparent = RBTreeGetGrandparent(node)
        uncle = RBTreeGetUncle(node)

        if uncle is not None and uncle.red:
            parent.red = uncle.red = False
            grandparent.red = True
            self.RBTreeBalance(grandparent)
            return

        if node is parent.right and parent is grandparent.left:
            self.left_rotate(parent)
            node = parent
            parent = node.parent

        elif node is parent.left and parent is grandparent.right:
            self.right_rotate(parent)
            node = parent
            parent = node.parent
        parent.red = False
        grandparent.red = True

        if node is parent.left:
            self.right_rotate(grandparent)
        else:
            self.left_rotate(grandparent)
