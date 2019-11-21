from cmath import sqrt

from Python.data_structures.binary_trees.avl import AVLTree
from Python.data_structures.binary_trees.RedBlack import RedBlackTree
import time


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
    if not isinstance(file_name, str):
        raise ValueError("'str required here. Created by @Edd1e234'")

    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("File not found")
        raise FileNotFoundError(file_name + "not found...")

    count = 0

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
                    # Raises Exception
                    raise ValueError("This file does not contain correct data. Does not contain float numbers. "
                                     "Created by @Edd1e234")
            tree.insert(words[0], vector_list)
            count += 1

    print(count)
    file.close()
    # Uncomment to view all words available to use for part 2.
    # print(words_to_use)


# Part 2
def read_file_sim(file_name, tree):
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("File not found")
        raise FileNotFoundError("File not found, Created by @Edd1e234")
    print("Printing Words along with their similarities.\n")
    for line in file:
        words = line.split(" ")
        print(words[0], words[1][:len(words[1]) - 1], sim(words[0], words[1][:len(words[1]) - 1], tree))
    print("\nFinished Part 2.")
    file.close()


# Part of Part 2.
def sim(w1, w2, tree):
    """
    Gets the dot product of w1 and w2. Gets the vectors from the list.
    """

    # Gets vector list.
    w1_node = tree.get_node(w1)
    w2_node = tree.get_node(w2)

    if w1_node is None:
        print(w1, " not found")
        return
    if w2_node is None:
        print(w2, " not found")
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


# Solution A
def get_total_nodes(tree):
    return tree.node_total


# Solution B
def get_tree_height(tree):
    if tree.root is None:
        return 0
    else:
        return tree.root.get_height()


# Solution C
def get_all_words(file_name, tree):
    node_keys = []
    get_words(tree.root, node_keys)
    generate_file(file_name, node_keys)
    print("File '" + file_name + "' generated all keys. ")


# Part of Solution C
def get_words(node, node_keys):
    if node is None:
        return
    node_keys.append(node.key)
    get_words(node.left, node_keys)
    get_words(node.right, node_keys)


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


# Part of solution D.
def get_node_at_depth(node, desired_depth, node_keys):
    if node is None:
        return
    if desired_depth == 0:
        node_keys.append(node.key)
        return
    else:
        get_node_at_depth(node.left, desired_depth - 1, node_keys)
        get_node_at_depth(node.right, desired_depth - 1, node_keys)


# Solution D.
def get_desired_depth(file_name, tree, desired_depth):
    nodes_keys = []
    get_node_at_depth(tree.root, desired_depth, nodes_keys)
    generate_file(file_name, nodes_keys)
    print("File '" + file_name + "' generated with keys at depth: :", desired_depth)


# This function is meant for testing purposes.
def run_program(file_name_root, words_to_use_file, desired_depth, avl_or_rb):
    """
    This function will run all solutions.
    :param file_name_root: Where the words are meant to be read from.
    :param words_to_use_file: Words to check similarities.
    :param desired_depth: What depth to get from.
    :param avl_or_rb: Which tree to use, for example, if 'avl_or_rb' is true then avl will be used.
                        Vice versa.
    :return:
        Write all words to 'all.words.in.list.txt'.
        Write all words found at 'desired_depth' to 'words.at.desired.depth.txt'. If desired depth is None or 0.
            then file will not be outputted.
        NOTE: If files are present this from previous runs.
    """

    # Checks.
    if not isinstance(file_name_root, str) and not isinstance(words_to_use_file, str):
        raise ValueError("'str required here. Created by @Edd1e234'")
    if not isinstance(desired_depth, int) and not isinstance(avl_or_rb, bool):
        raise ValueError("'bool' and 'int' required here. Created by @Edd1e234")

    if avl_or_rb:
        print("AVL Being Used\n")
        tree = AVLTree()
    else:
        print("Red Black Tree being Used")
        tree = RedBlackTree()

    total_time_start = time.time()
    file_read_time_start = time.time()
    read_file_into_tree(file_name_root, tree)
    file_read_time_end = time.time()
    file_read_time = file_read_time_end - file_read_time_start
    print("Finished reading tree: ", file_read_time)

    if tree.root is None:
        print("TREE ROOT IS NONE")

        raise SystemError("Something Went Wrong, tree root is none, text file empty?"
                          "Created by @Edd1e234")

    sim_time_start = time.time()
    read_file_sim(words_to_use_file, tree)
    sim_time_end = time.time()
    sim_time = sim_time_end - sim_time_start

    print("Finished Sim: ", sim_time, "\n")

    print("Solution A")
    print("Total node amount in tree ", tree.node_total)
    print("No time needed this is one operation.\n")

    height_timer_start = time.time()
    print("Tree height is, ", get_tree_height(tree))
    height_timer_end = time.time()

    height_time = height_timer_end - height_timer_start

    print("Get Solution B")
    print("Height timer took ",
          height_time, "\n")

    get_all_words_start = time.time()
    get_all_words("all.words.in.list.txt", tree)
    get_all_words_end = time.time()

    get_all_words_time = get_all_words_end - get_all_words_start

    print("Solution C")
    print("Finished printing all words: ",
          get_all_words_time, "\n")

    desired_depth_time = -1
    # Try to eliminate steps if possible.
    if desired_depth is not None or desired_depth is not 0:
        desired_depth_start = time.time()
        get_desired_depth("words.at.desired.depth.txt", tree, desired_depth)
        desired_depth_end = time.time()
        desired_depth_time = desired_depth_end - desired_depth_start

        print("Solution D:")
        print("Finished Desired Depth: ",
              desired_depth_time, "\n")

    total_time_end = time.time()
    total_time = total_time_end - total_time_start
    print("Total Time is: ", total_time)

    return file_read_time, sim_time, height_time, \
           get_all_words_time, desired_depth_time, total_time, avl_or_rb


def prints_results(keys_at_):
    # Writes the results.
    if keys_at_[-1]:
        print("Avl Tree")
    else:
        print("Red and Black Tree")
    print("Printing Time To Run Job")
    print("Time to read the file: ", keys_at_[0])
    print("Time to search: ", keys_at_[1])
    print("Time to find height: ", keys_at_[2])
    print("Time to go through entire tree: ", keys_at_[3])
    print("Time go get to desired depth: ", keys_at_[4])
    print("Total Time for job to run: ", keys_at_[5])
    print()


def main():
    print("Welcome\nPress 1 for AVL TREE\nPress 2 for Red Black Tree")
    num = input("Enter Here: ")
    try:
        if int(num) is 1:
            avl_or_br = True
        elif int(num) is 2:
            avl_or_br = False
        else:
            raise ValueError("Not sure what you put, but " + num + " is not valid. Created by @Edd1e234")
    except ValueError:
        raise ValueError("Not sure what you put, but '" + num + "' is not valid. Created by @Edd1e234")

    # Run for main solution.
    keys_avl = run_program("glove.6b.50d.txt", "words_to_use.txt", 5, avl_or_br)
    keys_rb = run_program("glove.6b.50d.txt", "words_to_use.txt", 5, not avl_or_br)
    keys_avl_2 = run_program("text_file_1.txt", "words_to_use_2.txt", 1, avl_or_br)
    keys_rb_2 = run_program("text_file_1.txt", "words_to_use_2.txt", 1, not avl_or_br)

    prints_results(keys_avl)
    prints_results(keys_rb)
    prints_results(keys_avl_2)
    prints_results(keys_rb_2)

    print("END OF PROGRAM")


main()
