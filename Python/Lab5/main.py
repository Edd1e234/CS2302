import time

from Python.data_structures.hash_table.lru_cache import LRUCache
from Python.data_structures.DataWrapper import DataWrapper
from Python.Lab5.DataWrapperHeap import WordHeap


def problem_1():
    lru_cache = LRUCache(3)

    lru_cache.put(1, 5)
    lru_cache.put(1, 5)
    lru_cache.put(1, 5)

    lru_cache.print_most_recent()
    print("Printing the full list.")
    lru_cache.nodes.print_list()


def _get_heap(word_dict):
    """
    Receives dict 'word_dict', words as keys and values as int. The values represent the amount
    time the word appeared in the given list.
    :param word_dict: (string, int)
    :return: MaxHeap, with the frequent word being at the top.
    """
    word_heap = WordHeap()

    for i in word_dict:
        item = DataWrapper(word_dict[i], i)
        word_heap.insert(item)
    return word_heap


def _get_dict(words):
    hash_table = dict()
    for word in words:
        if word in hash_table:
            hash_table[word] += 1
        else:
            hash_table[word] = 1
    return hash_table


def problem_2(words, k):
    hast_table = _get_dict(words)
    word_heap = _get_heap(hast_table)
    word_heap.print_k(k)


# Test Case 1.
def run_problem_2(amount, k):
    words = ["Eddie", "Billy", "Jimmy", "Eddie", "Eddie", "Billy", "Hey", "Tim"]
    all_words = []
    while amount != 0:
        amount += -1

        # Adding words.
        for word in words:
            all_words.append(word)
    start_time = time.time()
    problem_2(all_words, k)
    end_time = time.time()

    # Printing amount of time it took.
    print("Time:", end_time - start_time)


def main():
    # run_problem_2(9000, 4)
    # run_problem_2(90000, 4)
    problem_1()


main()
