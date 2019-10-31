# This main will be use as workspace for quick tests and for review.

from data_structures.binary_trees.BinarySearchTree import BST, BSTNode


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
def 


def main():
    standard_binary_tree = BST(BSTNode(3))
    standard_binary_tree.insert(2)
    standard_binary_tree.insert(1)
    standard_binary_tree.insert(5)
    standard_binary_tree.insert(8)
    standard_binary_tree.insert(6)
    standard_binary_tree.insert(4)

    found_node = standard_binary_tree.get_node(5)
    print("Found node...", found_node.key)

    print(get_nodes_balance_factor(found_node))
    print(get_total_nodes_at_desired_depth(standard_binary_tree.root, 2))
    print("Works!")


main()
