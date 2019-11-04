# This main will be use as workspace for quick tests and for review.

from data_structures.binary_trees.BinarySearchTree import BST, BSTNode
from data_structures.BTrees.BTree import BTree


def get_binary_node_height(node):
    if node is None:
        return 0
    return max(get_binary_node_height(node.left),
               get_binary_node_height(node.right)) + 1


# Question 3 on the quiz.
def get_nodes_balance_factor(node):
    left_node = get_binary_node_height(node.left)
    right_node = get_binary_node_height(node.right)
    value = abs(left_node - right_node)
    if value == 0 or value == 1:
        return True, value
    else:
        return False, value


# Question 4 on the quiz.
def get_total_nodes_at_desired_depth(node, d):
    if node is None:
        return 0
    if d == 0:
        return 1
    return get_total_nodes_at_desired_depth(node.left, d - 1) + \
           get_total_nodes_at_desired_depth(node.right, d - 1)


# Question 5 on the quiz.
def count_even(node):
    if node.is_leaf:
        value = 0
        for k in node.keys:
            if k % 2 == 0 or k == 0:
                value += 1
        return value
    # Not leaf.
    value = 0
    for i in range(len(node.keys)):
        value += count_even(node.children[i])
        if node.keys[i] % 2 == 0 or node.keys[i] == 0:
            value += 1
    return value + count_even(node.children[len(node.keys)])


def search_at_depth(k, d, node):
    if d == 0:
        if k in node.keys:
            return node
        else:
            return None
    if node.is_leaf:
        return None

    for child in node.children:
        found_node = search_at_depth(k, d - 1, child)
        # There is only one instance that function will not return a None type.
        if found_node is not None:
            return found_node


def main():

    print("Works")


main()
