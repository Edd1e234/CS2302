from cmath import sqrt

from data_structures.BTrees.BTreeObject import BTreeObject as BTree
from data_structures.BTrees.BTreeObject import ObjectKey
import time


# TODO(Edd1e234): Write comments for all comments.
# Part 1.
def read_file_into_tree(file_name, tree):
    if not isinstance(file_name, str):
        raise ValueError("'str required here. Created by @Edd1e234'")

    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("File not found")
        raise FileNotFoundError(file_name + "not found...")

    count = 0

    print("Inserting")

    for line in file:
        words = line.split(" ")
        if words[0].isalpha():
            # Checking if there actual float numbers.
            vector_list = []
            for i in words[1:]:
                try:
                    vector_list.append(float(i))
                except ValueError:
                    # Raises Exception
                    raise ValueError("This file does not contain correct data. Does not contain float numbers. "
                                     "Created by @Edd1e234")
            key = ObjectKey(words[0], vector_list)
            tree.insert(key)
            count += 1
    print(count)
    file.close()


# Part 2.
def read_file_sim(file_name, tree):
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("File not found")
        raise FileNotFoundError("File not found, Created by @Edd1e234")
    print("Printing Words along with their similarities.\n")
    for line in file:
        words = line.split(" ")
        value = sim(words[0], words[1][:len(words[1]) - 1], tree)
        print(words[0], words[1][:len(words[1]) - 1], value)
    print("\nFinished Part 2.")
    file.close()


# Part of Part 2.
def sim(w1, w2, tree):
    w1_node = tree.search(w1)
    w2_node = tree.search(w2)

    if w1_node is None or w2_node is None:
        return

    sum_of_w1 = 0
    sum_of_w2 = 0
    dot_product = 0
    for i in range(len(w1_node.data)):
        sum_of_vector = float(w1_node.data[i]) * float(w2_node.data[i])

        sum_of_w1 += (float(w1_node.data[i]) * float(w1_node.data[i]))
        sum_of_w2 += (float(w2_node.data[i]) * float(w2_node.data[i]))

        dot_product += sum_of_vector
    return dot_product / (sqrt(sum_of_w1) * sqrt(sum_of_w2))


# Solution A.
def get_total_nodes(tree):
    return tree.total_nodes


# Solution B.
def get_tree_height(tree):
    return tree.height()


# Solution C.
def get_all_words(file_name, tree):
    node_keys = []
    get_words(tree.root, node_keys)
    generate_file(file_name, node_keys)
    print("File '" + file_name + "' generated all keys. ")


# Part of Solution C.
def get_words(node, node_keys):
    # Used the same logic as the 'print' function in the parent class of 'BTreeObject'.
    if node.is_leaf:
        for t in node.keys:
            node_keys.append(t.key)
    else:
        for i in range(len(node.keys)):
            get_words(node.children[i], node_keys)
            node_keys.append(node.keys[i].key)
        get_words(node.children[len(node.keys)], node_keys)


# Solution D.
def get_desired_depth(file_name, tree, desired_depth):
    node_keys = []
    get_nodes_at_depth(tree.root, desired_depth, node_keys)
    generate_file(file_name, node_keys)
    print("File '" + file_name + "' generated with keys at depth: :", desired_depth)


# Part of solution D.
def get_nodes_at_depth(node, desired_depth, node_keys):
    if desired_depth == 0:
        for i in node.keys:
            node_keys.append(i.key)
    elif node.is_leaf:
        return
    else:
        for i in range(len(node.keys)):
            get_nodes_at_depth(node.children[i],
                               desired_depth - 1, node_keys)
        get_nodes_at_depth(node.children[len(node.keys)], desired_depth - 1, node_keys)


# Util function, generates file with name of 'file_name', contents of the file are 'node_keys'.
def generate_file(file_name, node_keys):
    """
    Generates a file with the name 'file_name', the file is populated with 'node_keys'.
    :param file_name: Name of the file wanted generated.
    :param node_keys: The keys to be written in file.
    :return: Will raise Value Error if 'node_keys' is none or 'file_name' is None.
    """
    if file_name is None:
        raise ValueError("'file_name' is not present. This was created by @Edd1e234")
    if node_keys is None or len(node_keys) is 0:
        raise ValueError("'node_keys' has no values. This was created by @Edd1e234")

    file = open(file_name, "w+")
    for i in node_keys:
        file.write(i + "\n")


def main():
    tree = BTree(40)
    read_file_into_tree("/Users/greywind/"
                        "Desktop/CS3/CS2302/Lab3/"
                        "glove.6B.50d.txt", tree)
    read_file_sim("words_to_use.txt", tree)
    print("Total Nodes are.", get_total_nodes(tree))
    get_all_words("all.words.in.Btree.txt", tree)
    print("The height of the tree", get_tree_height(tree))
    get_desired_depth("words.at.desired.depth.txt", tree, 1)
    print("WORKS!")


if __name__ == "__main__":
    main()
