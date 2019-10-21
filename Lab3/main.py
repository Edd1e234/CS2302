from data_structures.binary_trees.avl import AVLTree


# Part 1
def read_file_into_tree(file_name, tree):
    """
    Function will open and read a text file, the text file name will be given by 'file_name'.
    Once file is open it will go through and read line by line for employee ID's.

    Bad inputs should be handled.

    :param file_name: Will be the name of file being searched.
    :param tree: Linked List to add all ID's.
    """
    # Checks.
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("File not found")
        return

    count = 0
    words_to_use = []

    print("inserting.....")

    # Inserts words into binary tree.
    # Checks words are actual letters.
    # Checks that there is no bad inputs, in terms of vectors.
    for line in file:
        words = line.split(" ")

        if words[0].isalpha():

            # Checking if there actual float numbers.
            vector_list = []
            for i in words[1:]:
                try:
                    vector_list.append(float(i))
                except ValueError:
                    print("This file does not contain correct data. Does not contain float numbers.")
                    return
            tree.insert(words[0], vector_list)
            words_to_use.append(words[0])
            count += 1
        # if count is 30:
            # break

    file.close()
    # Uncomment to view all words available to use for part 2.
    # print(words_to_use)


# Part 2
def read_file_sim(file_name, tree):
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("File not found")
        return
    print("Printing Words along with their similarities.\n")
    for line in file:
        words = line.split(" ")
        print(words[0], words[1][:len(words[1]) - 1], sim(words[0], words[1][:len(words[1]) - 1], tree))
    print("Finished Part 2.")
    file.close()


# Part of Part 2.
def sim(w1, w2, tree):
    """
    Gets the dot product of w1 and w2. Gets the vectors from the list.
    """
    w1_node = tree.get_node(w1)
    w2_node = tree.get_node(w2)

    dot_product = 0
    for i in range(len(w1_node.data)):
        dot_product += float(w1_node.data[i]) + float(w2_node.data[i])
    return dot_product


# Part of Solution C
def get_words(node, node_keys):
    if node is None:
        return
    node_keys.append(node.key)
    get_words(node.left, node_keys)
    get_words(node.right, node_keys)


# Solution C
def get_all_words(file_name, tree):
    node_keys = []
    get_words(tree.root, node_keys)
    generate_file(file_name, node_keys)
    print("File ", file_name, " generated all keys. ")


# Util function, generates file with name of 'file_name', contents of the file are 'node_keys'.
def generate_file(file_name, node_keys):
    if file_name is None:
        raise ValueError("'file_name' is not present.")
    if node_keys is None or len(node_keys) is 0:
        raise ValueError("'node_keys' has no values, file not created.")
    file = open(file_name, "w+")
    for i in node_keys:
        file.write(i + "\n")


# Part of solution D.
def get_node_at_depth(node, desired_depth, node_keys):
    if node is None:
        return
    if node.height - 1 == desired_depth:
        node_keys.append(node.key)
        return
    else:
        get_node_at_depth(node.left, desired_depth, node_keys)
        get_node_at_depth(node.right, desired_depth, node_keys)


# Solution D.
def get_desired_depth(file_name, tree, desired_depth):
    nodes_keys = []
    get_node_at_depth(tree.root, desired_depth, nodes_keys)
    generate_file(file_name, nodes_keys)
    print("File ", file_name, " generated with keys at depth: ", desired_depth)


def main():
    print("Welcome\n Press 1 for AVL TREE\n Press 2 for Red Black Tree")
    num = input("Enter Here: ")
    tree = None

    if int(num) is 1:
        tree = AVLTree()

    read_file_into_tree("glove.6b.50d.txt", tree)
    read_file_sim("words_to_use.txt", tree)

    get_all_words("all.words.in.list.txt", tree)
    get_desired_depth("words.at.desired.depth.txt", tree, 5)

    print("END OF PROGRAM")


main()
