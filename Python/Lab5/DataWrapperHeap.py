# Created by Eddie Garcia at 11/20/19

# DataWrapperHeap, uses the DataWrapper object as nodes.
# Uses the DataWrapper object as nodes. Nodes place in the heap are
# determined by the 'key' in the DataWrapper object.
import math

from Python.data_structures.Heaps.Heaps import MaxHeap


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
