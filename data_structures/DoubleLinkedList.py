class Node:
    """
    Doubly Linked List Node implementation.
    """

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next_node = next
        self.prev = prev

    def remove(self):
        print("Removing this, ", self.data)

        if self.prev is not None:
            self.prev.next_node = self.next_node
        if self.next_node is not None:
            self.next_node.prev = self.prev

        return self.next_node, self.prev


class DoublyLinkedList:
    size = 0

    def __init__(self, data=None):
        self.head = Node(data)
        self.tail = self.head

        if data is not None:
            self.size = 1

    def append_at_tail(self, data):
        self.tail.next_node = Node(data, None, self.tail)
        self.tail = self.tail.next
        self.size += 1

    def append_node_at_head(self, node):
        if self.head is None:
            self.head = node
            return
        self.head.prev = node
        self.head.prev.next = self.head
        self.head = self.head.prev
        self.size += 1

    def append_at_head(self, data):
        self.head.prev = Node(data, self.head, None)
        self.head = self.head.prev
        self.size += 1

    # Error here.
    def append_at(self, index, data):
        if index > self.size:
            self.append_at_tail(data)
            return
        if index == 0:
            self.append_at_head(data)
            return

        new_node = self.head
        counter = 0

        while new_node is not None:
            if counter == index:
                new_node.add_at(data)
                self.size += 1
                return
            new_node = new_node.next_node
            counter += 1
        self.append_at_tail(data)

    # Works
    def pop(self):
        if self.size == 0:
            print("No Head you Dope.")
            return None
        old_head = self.head
        value = self.head.remove()
        self.head = value[0]
        self.size += -1
        return old_head

    # Works
    def remove_tail(self):
        if self.size == 0:
            print("No Head you dope.")
            return None
        old_tail = self.tail
        value = self.tail.remove()
        self.tail = value[1]
        self.size += -1
        return old_tail

    def print_list(self):

        cur_node = self.head
        for i in range(self.size):
            print(cur_node.data)
            cur_node = cur_node.next_node
