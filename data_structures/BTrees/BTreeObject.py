# B-Tree used with keys as objects.

from data_structures.BTrees.BTree import BTree


class ObjectKey:
    def __init__(self, key, data):
        self.key = key
        self.data = data


class BTreeNode:
    # Constructor
    def __init__(self, keys=[], children=[], is_leaf=True, max_num_keys=5):
        self.keys = keys
        self.children = children
        self.is_leaf = is_leaf
        if max_num_keys < 3:  # max_num_keys must be odd and greater or equal to 3
            max_num_keys = 3
        if max_num_keys % 2 == 0:  # max_num_keys must be odd and greater or equal to 3
            max_num_keys += 1
        self.max_num_keys = max_num_keys

    def is_full(self):
        return len(self.keys) >= self.max_num_keys


# Sorts strings.
def sort_strings(arr):
    # Calling Strings.
    quickSort(arr, 0, len(arr) - 1)


# Functions below were taken from GeeksForGeeks implementation of quicksort.
def quickSort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now
        # at right place.
        pi = partition(arr, low, high)

        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def partition(arr, low, high):
    i = (low - 1)  # Index of smaller element.
    pivot = arr[high].key  # Pivot.

    for j in range(low, high):

        # If current element is smaller than or equal to pivot.
        # The only change of code comes here.
        if arr[j].key <= pivot:
            i += 1
            # Swap them.
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


class BTreeObject(BTree):
    # Constructor
    def __init__(self, max_num_keys=5):
        self.max_num_keys = max_num_keys
        self.root = BTreeNode(max_num_keys=max_num_keys)

    def find_child(self, k, node=None):
        # Determines value of c, such that k must be in subtree node.children[c], if k is in the BTree
        if node is None:
            node = self.root

            for i in range(len(node.keys)):
                if k < node.keys[i].key:
                    return i
                return len(node.keys)
        return None

    def insert_leaf(self, i, node=None):
        if node is None:
            node = self.root

        node.keys.append(i)

