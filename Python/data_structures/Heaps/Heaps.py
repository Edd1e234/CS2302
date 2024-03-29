# Implementation of max heap
# Programmed by Olac Fuentes
# Last modified October 20, 2019

import matplotlib.pyplot as plt
import math


class MaxHeap(object):
    # Constructor
    def __init__(self):
        self.tree = []

    def is_empty(self):
        return len(self.tree) == 0


    def parent(self, i):
        if i == 0:
            return -math.inf
        return self.tree[(i - 1) // 2]

    def left_child(self, i):
        c = 2 * i + 1
        if c >= len(self.tree):
            return -math.inf
        return self.tree[c]

    def right_child(self, i):
        c = 2 * i + 2
        if c >= len(self.tree):
            return -math.inf
        return self.tree[c]

    def insert(self, item):

        self.tree.append(item)
        self._percolate_up(len(self.tree) - 1)

    def _percolate_up(self, i):
        if i == 0:
            return

        parent_index = (i - 1) // 2

        if self.tree[parent_index] < self.tree[i]:
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)

    def extract_max(self):
        if len(self.tree) < 1:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()

        root = self.tree[0]

        self._percolate_down(0)

        return root

    def _percolate_down(self, i):

        if self.tree[i] >= max(self.left_child(i), self.right_child(i)):
            return

        max_child_index = 2 * i + 1 if self.left_child(i) > self.right_child(i) else 2 * i + 2

        self.tree[i], self.tree[max_child_index] = self.tree[max_child_index], self.tree[i]
        self._percolate_down(max_child_index)

    def draw(self):
        if not self.is_empty():
            fig, ax = plt.subplots()
            self.draw_(0, 0, 0, 100, 50, ax)
            ax.axis('off')
            ax.set_aspect(1.0)

            plt.show()

    def draw_(self, i, x, y, dx, dy, ax):
        if self.left_child(i) > -math.inf:
            ax.plot([x, x - dx], [y, y - dy], linewidth=1, color='k')
            self.draw_(2 * i + 1, x - dx, y - dy, dx / 2, dy, ax)
        if self.right_child(i) > -math.inf:
            ax.plot([x, x + dx], [y, y - dy], linewidth=1, color='k')
            self.draw_(2 * i + 2, x + dx, y - dy, dx / 2, dy, ax)
        ax.text(x, y, str(self.tree[i]), size=20,
                ha="center", va="center",
                bbox=dict(facecolor='w', boxstyle="circle"))

    def second_max(self):
        # This function assumes there is at least two elements in 'self.tree'.
        if self.tree[1] < self.tree[2]:
            return self.tree[2]
        else:
            return self.tree[1]

    def is_valid(self):
        for i in range(1, len(self.tree)):
            if self.tree[(i - 1) // 2] < self.tree[i] and \
                    self.tree[(i - 1) // 2] != self.tree[i]:
                return False
        return True

    def try_replace(self, i, val):
        old_value = self.tree[i]
        self.tree[i] = val
        if self.is_valid():
            return
        else:
            self.tree[i] = old_value
