class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.size = 0

    def insert(self, data):
        cur_node = self.head

        while cur_node.next_node is not None:
            cur_node = cur_node.next_node

        self.size += 1
        cur_node.next_node = Node(data)

    def print(self):
        cur_node = self.head

        while cur_node is not None:
            print(cur_node.data)
            cur_node = cur_node.next_node
