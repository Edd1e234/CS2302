class Node(object):
    item = -1
    next = None

    def __init__(self, next, item):
        self.next = next
        self.item = item

    def set_data(self, item):
        self.item = item

    def get_data(self):
        return self.item

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class LinkedList(object):
    head = None
    size = 0

    def __init__(self, head):
        self.head = head
        self.size += 1

    def insert(self, item):
        node = Node(item)
        node.set_next(self.head)
        self.head = node
        self.size += 1

    def get_size(self):
        return self.size
