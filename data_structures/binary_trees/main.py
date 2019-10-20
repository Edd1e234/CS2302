from data_structures.binary_trees.BinarySearchTree import BST
from data_structures.binary_trees.BinarySearchTree import BSTNode
from data_structures.binary_trees.avl import AVLTree
from data_structures.binary_trees.avl import AVLNode


def main():
    print("Working on AVL")

    avl_root = AVLNode(42)
    avl = AVLTree(avl_root)

    # What the list contains
    list_nodes = [28, 37, 41, 96, 15, 88, 32, 50]

    for i in list_nodes:
        avl.insert(i)
    avl.print_full_tree()
    avl.print_bst()

    print(avl.root.data)
    print(avl.root.right.data)





main()
