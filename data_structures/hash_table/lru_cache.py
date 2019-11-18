"""
All operations run in constant time, except for searching for nodes in a bucket. This runs in N time relative to bucket
size.
"""

from data_structures.DoubleLinkedList import DoublyLinkedList as DLL
from data_structures.DoubleLinkedList import Node as DLLNode
from data_structures.hash_table.hash_table import HashTable


class LRUCache(HashTable):

    def __init__(self, size):
        super().__init__(size)
        self.set_size = size
        self.nodes = DLL()

    def remove(self, k):
        print("This operation is not supported, NOTHING DONE.")
        return

    def insert(self, k):
        return self.remove(k)

    def _get_bucket(self, key):
        return self.table[self.hash(key)]

    def get(self, key):
        # Gets the value using the key. If 'bucket' contains more than one node pointer
        # it will return a list.
        if key is None:
            print("Key is NONE.")
            return

        bucket = self._get_bucket(key)
        if len(bucket) == 1:
            return bucket[0].data[1]
        elif len(bucket) != 0:
            return bucket
        else:
            return -1

    def contains_pair(self, key, value):
        nodes = self._get_bucket(key)

        # Checking if it contains the value and key.
        for node in nodes:
            if node.data[0] == key and node.data[1] == value:
                print("Found the values.", key, value)
                node.remove()
                self.nodes.size += -1
                return

    def put(self, key, value):
        self.contains_pair(key, value)
        bucket = self._get_bucket(key)

        # Creates new node and inserts it to the 'bucket'.
        # Stores list of 'key' and 'value' into 'data'.
        new_node = DLLNode([key, value])
        bucket.append(new_node)

        if self.nodes.size == self.set_size:
            self.nodes.remove_tail()
        self.nodes.append_node_at_head(new_node)

    def print_most_recent(self):

        cur = self.nodes.head
        for i in range(self.nodes.size):
            print(cur.data)
            cur = cur.next

    def size(self):
        return self.nodes.size()

    def max_capacity(self):
        return self.set_size
