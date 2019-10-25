from data_structures.DoubleLinkedList import DoublyLinkedList as DLL
from data_structures.DoubleLinkedList import Node as DLLNode
from data_structures.hash_table.Map import Map


class LRUCache(Map):

    def __init__(self, size):
        super().__init__(size)
        self.set_size = size
        self.nodes = DLL()

    def _remove(self, key, value):
        bucket = self._get_bucket(key)

        print("Hello")
        if bucket[0].data[0] == value.data[0]:
            node = bucket.remove(bucket)
            print("Value in bucket", node.data.data)
            node.remove()

    def contains_pair(self, key, value):
        bucket = self._get_bucket(key)

        print("Helllooooo")
        if len(bucket) == 1:
            if bucket[0].data[1] == value:
                return True
        return False

    def insert(self, k, value):
        if self.contains_pair(k, value):
            print("Hello")
            self._remove(k, value)
        bucket = self._get_bucket(k)

        new_node = DLLNode([k, value])
        bucket.append(new_node)

        if self.nodes.size == self.set_size:
            self.nodes.remove_tail()
        self.nodes.append_at_head(new_node)

    def print_most_recent(self):

        cur = self.nodes.head
        for i in range(self.nodes.size):
            print(cur.data.data)
            cur = cur.next


