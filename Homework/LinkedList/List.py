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

    def add_last(self, data):
        self.add(0, data)

    def add(self, index, item):
        if self.size is 0:
            self.head = Node(None, item)
            self.size += 1
            return
        temp_node = self.head

        for i in range(index - 1):
            if temp_node is None:
                temp_node = Node(None, item)
                return
            temp_node = temp_node.get_next()
        new_node = Node(temp_node.get_next(), item)
        temp_node.set_next(new_node)

        self.size += 1


def main():
    list = SinglyLinkedList()

    list.add(0, 1)
    list.add(1, 2)
    print(list.size)
    list.add_last(3)

    node = list.get_head()
    print(node.get_data())
    print(node.get_next().get_data())

    for i in range(1):
        print("Loop")


main()
