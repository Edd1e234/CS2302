class Node(object):
    data = None
    next = None

    def __init__(self, next, data):
        print("new node")
        self.next = next
        self.data = data

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class SinglyLinkedList(object):
    head = None
    size = 0

    def __init__(self, head=None):
        self.head = head
        self.size += 1

        if head is None:
            self.size = 0

    def get_size(self):
        return self.size

    def get_head(self):
        return self.head

    def add_first(self, item):
        if self.head is None:
            self.head = Node(None, item)
            return
        node = Node(self.head, item)
        self.head = node

    def get_index_of(self, item):
        temp_node = self.head
        index = 0

        while temp_node is not None:
            if temp_node.get_data is item
                return index
            index += 1

    def get_index(self, index):
        temp_node = self.head

        counter = 0
        while temp_node is not None:
            if counter is index:
                return temp_node.get_data()
            counter += 1
            temp_node = temp_node.get_next()

    def get_first(self):
        return self.head.get_data()

    def get_last(self):
        if self.size is 0:
            return -1
        return self.get_index(self.size -1)

    def remove_first(self):
        self.head = self.head.get_next()

    def remove_last(self):
        temp_node = self.head
        if self.size is 1:
            self.remove_first()
            return

        while temp_node.get_next() is not None:
            temp_node = temp_node.get_next()

        temp_node.set_next(None)
    def is_empty(self):
        if self.size is 0:
            return True
        return False


    def add_last(self, data):
        self.add(self.size, data)

    def add(self, index, item):
        if self.size is 0:
            self.head = Node(None, item)
            self.size += 1
            return
        temp_node = self.head

        for i in range(index - 1):
            if temp_node.get_next() is None:
                temp_node.set_next(Node(None, item))
                return
            temp_node = temp_node.get_next()

        new_node = Node(temp_node.get_next(), item)
        temp_node.set_next(new_node)

        self.size += 1

    def print_list(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.get_data())
            temp_node = temp_node.get_next()

    def reverse_list(self):
        


def main():
    list = SinglyLinkedList()

    list.add(0, 1)
    list.print_list()
    list.add(1, 2)
    list.print_list()
    list.add_first(12)
    print("Adding 3")
    list.add_last(3)
    list.print_list()

    new_list = SinglyLinkedList()
    new_list.add_first(43)

    print("Adding 5 to index 1")
    list.add(0, 5)
    list.print_list()

    for i in range(1):
        print("Loop")


main()
