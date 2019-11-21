class Node(object):
    item = -1
    next = None
    index = None

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
    largest_id = -1
    tail = None
    head = None
    size = 0

    def __init__(self, head):
        self.tail = head
        self.head = head
        self.size += 1

    def get_largest_id(self):
        return self.largest_id

    def check_largest_id(self, id):
        if not isinstance(id, int):
            return
        if id > self.largest_id:
            self.largest_id = id

    def insert(self, item):
        self.check_largest_id(item)
        if self.head.get_data() is None:
            self.tail.set_data(item)
            self.head.set_next(self.tail)
            self.head.set_data(item)
        else:
            node = Node(None, item)
            node.set_next(self.head)
            self.head = node
            self.size += 1

    def insert_at_tail(self, item):
        self.check_largest_id(item)
        if self.head.get_data() is None:
            self.insert(item)
        else:
            node = Node(None, item)
            self.tail.set_next(node)
            self.tail = node
            self.size += 1

    def calculate_size(self):
        self.size = 0

        temp_node = self.head

        while temp_node is not None:
            temp_node = temp_node.get_next()
            self.size += 1

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def set_head(self, data):
        if isinstance(data, Node):
            self.head = data
        else:
            self.head.set_data(data)

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

    def set_tail(self, data):
        if isinstance(data, Node):
            self.tail = data
        else:
            self.tail.set_data(data)

    def clear(self):
        self.head.set_data(None)
        self.tail.set_next(None)
