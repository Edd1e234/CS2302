import math

from data_structures.hash_table.lru_cache import LRUCache
from data_structures.Heaps.Heaps import MaxHeap
from data_structures.DataWrapper import DataWrapper


class WordHeap(MaxHeap):
    """
    This class requires you to use 'DataWrapper' object to insert.
    """

    def parent(self, i):
        if i == 0:
            return -math.inf
        return i - 1 // 2

    def left_child(self, i):
        c = 2 * i + 1
        if c >= len(self.tree):
            return -math.inf
        return c

    def right_child(self, i):
        c = 2 * i + 2
        if c >= len(self.tree):
            return -math.inf
        return c

    def insert(self, item):
        if not isinstance(item, DataWrapper):
            print("Needs to be 'DataWrapper' object. ")
            return
        for i in range(len(self.tree)):
            if self.tree[i].object_data == item.object_data:
                self.tree[i].key += 1
                self._percolate_up(i)
                return
        # We don't need to percolate up anymore.
        self.tree.append(item)

    def _percolate_up(self, i):
        if i == 0:
            return

        parent_index = (i - 1) // 2

        if self.tree[parent_index].key < self.tree[i].key:
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)
        if self.tree[parent_index].key == self.tree[i].key:
            if self.tree[parent_index].object_data > self.tree[i]:
                self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
                self._percolate_up(parent_index)

    def extract_max(self):
        if len(self.tree) < 1:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()
        root = self.tree[0]
        self.tree[0] = self.tree.pop()
        self._percolate_down(0)
        return root

    def _percolate_down_helper(self, i, index):
        if self.tree[i].key == self.tree[index].key:
            if self.tree[i].object_data < self.tree[index].object_data:
                self.tree[i], self.tree[index] = self.tree[index], self.tree[i]
                self._percolate_down(index)
                return

    def _percolate_down(self, i):
        left_child_index = self.left_child(i)
        right_child_index = self.right_child(i)

        if left_child_index == -math.inf and right_child_index == -math.inf:
            return

        # TODO(Edd1e234): Refactor this, needs to be cleaner.
        if left_child_index == -math.inf and right_child_index != -math.inf:
            if self.tree[i].key == self.tree[right_child_index].key:
                if self.tree[i].object_data < self.tree[right_child_index].object_data:
                    self.tree[i], self.tree[right_child_index] = self.tree[right_child_index], self.tree[i]
                    self._percolate_down(right_child_index)
                    return
            elif self.tree[i].key < self.tree[right_child_index].key:
                self.tree[i], self.tree[right_child_index] = self.tree[right_child_index], self.tree[i]
                self._percolate_down(right_child_index)
                return
            else:
                return
        if right_child_index == -math.inf and left_child_index != -math.inf:
            if self.tree[i].key == self.tree[left_child_index].key:
                if self.tree[i].object_data < self.tree[left_child_index].object_data:
                    self.tree[i], self.tree[left_child_index] = self.tree[left_child_index], self.tree[i]
                    self._percolate_down(right_child_index)
                    return
            elif self.tree[i].key < self.tree[left_child_index].key:
                self.tree[i], self.tree[left_child_index] = self.tree[left_child_index], self.tree[i]
                self._percolate_down(left_child_index)
                return
            else:
                return

        # TODO(Edd1e234): Find the bug so that these if blocks are not necessary.
        # These two if blocks are here for a small bug that has yet to be found.
        if left_child_index == -math.inf:
            return
        if right_child_index == -math.inf:
            return
        if self.tree[i].key > max(self.tree[left_child_index].key, self.tree[right_child_index].key):
            return

        max_child_index = None
        if self.tree[left_child_index].key == self.tree[right_child_index].key:
            if self.tree[left_child_index].object_data < self.tree[right_child_index].object_data:
                max_child_index = 2 * i + 1
        elif self.tree[left_child_index].key > self.tree[right_child_index].key:
            max_child_index = 2 * i + 1
        else:
            max_child_index = 2 * i + 2

        if max_child_index is None:
            return
        if max_child_index >= len(self.tree):
            return

        self.tree[i], self.tree[max_child_index] = self.tree[max_child_index], self.tree[i]
        self._percolate_down(max_child_index)

    def is_valid(self):
        for i in range(1, len(self.tree)):
            if self.tree[(i - 1) // 2].key < self.tree[i] and \
                    self.tree[(i - 1) // 2] != self.tree[i]:
                return False
        return True

    def print_k(self, k):
        if not isinstance(k, int):
            return

        for i in range(k):
            item = self.extract_max()
            if item is not None:
                print(item.object_data, item.key)
            else:
                return


def problem_2(words, k):
    word_heap = WordHeap()

    for i in words:
        item = DataWrapper(1, i)
        word_heap.insert(item)

    word_heap.print_k(k)



def problem_2_print(word_heap):
    for i in range(len(word_heap.tree)):
        item = word_heap.extract_max()
        print(item.object_data, item.key)


def problem_1():
    lru_cache = LRUCache(3)

    lru_cache.put(1, 5)
    lru_cache.put(1, 5)
    lru_cache.put(1, 5)

    lru_cache.print_most_recent()
    print("Printing the full list.")
    lru_cache.nodes.print_list()


def main():
    words = ["Eddie", "Billy", "Jimmy", "Eddie", "Eddie", "Billy", "Hey", "Tim"]
    problem_2(words, 3)

    print("Works")


main()
