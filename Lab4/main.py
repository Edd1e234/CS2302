from cmath import sqrt

from data_structures.BTrees.BTreeObject import BTreeObject as BTree
from data_structures.BTrees.BTreeObject import ObjectKey
import time


# Part 1.
def read_file_into_tree(file_name, tree):
    """
    Opens file using 'file_name', reads each line and separates by key and data. Embeddings will be
    the data, while the actual word will be the string. Embeddings will be converts from strings to floats.
    Function will have a controlled crash if there is a bad input.
    :param file_name: str, that contains file path.
    :param tree: BTree Datatype.
    :return: Only edits BTree.
    """
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
                    raise ValueError("This file does not contain correct data. Does not contain float numbers. '", i,
                                     "' Created by @Edd1e234")
            # Creates the object wrapper class.
            key = ObjectKey(words[0], vector_list)
            tree.insert(key)
            count += 1
    print(count)
    file.close()


# Part 2.
def read_file_sim(file_name, tree):
    """
    Opens file using 'file_name' as a path. Reads file line by line, each line contains words looking to compare.
    Once words are read from file they're searched for in 'sim' function and compared.
    :param file_name: str, path to file with words to compare.
    :param tree: BTree datatype, contains populated Btree.
    :return: Returns nothing, prints to the console.
    """
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
    """
    Searches for 'w1' and 'w2' in 'tree', compares them using the algorithm given in the document.
    :param w1: str, first word to look for.
    :param w2: str, second word to look for.
    :param tree: Btree datatype.
    :return: returns the answer using the the algorithm given.
    """
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
    # Gets the height of the tree using class function.
    return tree.height()


# Solution C.
def get_all_words(file_name, tree):
    """
    Goal is to get all words in the tree. Generate a file, and write all the words into the file.
    :param file_name: str, name of the file to be generated.
    :param tree: Btree object, where all the words live.
    :return: Builds file.
    """
    node_keys = []
    get_words(tree.root, node_keys)
    generate_file(file_name, node_keys)
    print("File '" + file_name + "' generated all keys. ")


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


# Part of Solution C.
def get_words(node, node_keys):
    # 'node_keys' is where all the words will be placed.
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
    """
    Builds a file with all keys that are at depth 'desired_depth', using 'tree' of course.
    :param file_name: str, builds a file with this name.
    :param tree: Btree object, where all the keys will live.
    :param desired_depth: The wanted depth.
    :return: Builds a file with words at 'desired_depth'.
    """
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
def run_program(file_name_root, words_to_use_file, desired_depth, max_size):
    """
    This function will run all solutions.
    :param max_size: Size of the tree keys.
    :param file_name_root: Where the words are meant to be read from.
    :param words_to_use_file: Words to check similarities.
    :param desired_depth: What depth to get from.
    :return:
        List of times for each task.
        Write all words to 'all.words.in.list.txt'.
        Write all words found at 'desired_depth' to 'words.at.desired.depth.txt'. If desired depth is None or 0.
            then file will not be outputted.
    """

    # Checks.
    if not isinstance(file_name_root, str) and not isinstance(words_to_use_file, str):
        raise ValueError("'str required here. Created by @Edd1e234'")
    if not isinstance(desired_depth, int) and not isinstance(max_size, int):
        raise ValueError("'bool' and 'int' required here. Created by @Edd1e234")

    tree = BTree(max_size)

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
    print("Total node amount in tree ", tree.total_nodes)
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

    return file_read_time, sim_time, height_time, get_all_words_time, desired_depth_time, total_time


def prints_results(keys_at_):
    # Writes the results.
    print("Printing Time To Run Job")
    print("Time to read the file: ", keys_at_[0])
    print("Time to search: ", keys_at_[1])
    print("Time to find height: ", keys_at_[2])
    print("Time to go through entire tree: ", keys_at_[3])
    print("Time go get to desired depth: ", keys_at_[4])
    print("Total Time for job to run: ", keys_at_[5])
    print()


def main():
    keys_at_5 = run_program("/Users/greywind/"
                            "Desktop/CS3/CS2302/Lab3/"
                            "glove.6B.50d.txt", "words_to_use.txt", 2, 5)
    keys_at_50 = run_program("/Users/greywind/"
                             "Desktop/CS3/CS2302/Lab3/"
                             "glove.6B.50d.txt", "words_to_use.txt", 2, 50)
    prints_results(keys_at_5)
    prints_results(keys_at_50)

    print("WORKS!")


main()
