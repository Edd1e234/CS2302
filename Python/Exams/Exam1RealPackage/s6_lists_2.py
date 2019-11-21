class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_last(self, item):
        return

    def add_first(self, item):
        return

    def add(self, index, item):
        if self.head is None:
            return
        if index == 0:
            new_node = Node(item, self.head)
            self.head = new_node
            return
        if index < 0:
            return

        temp_node = self.head
        for i in range(index-1):
            if temp_node is None:
                return
            temp_node = temp_node.next
        if temp_node is None:
            return
        old_next_node = temp_node.next
        new_node = Node(item, old_next_node)

        temp_node.next = new_node

        return

    def clear(self):
        return

    def contains(self, item):
        if self.head is None:
            return False
        temp_node = self.head

        while temp_node is not None:
            if temp_node.item == item:
                return True
            temp_node = temp_node.next
        return False

    def index_of(self, item):
        return

    def get(self, index):
        if self.head is None:
            return None
        temp_node = self.head

        counter = 0
        while temp_node is not None:
            if counter == index:
                return temp_node.item
            temp_node = temp_node.next
            counter += 1

        return None

    def get_first(self):
        return

    def get_last(self):
        return

    def remove(self, index):
        return

    def remove_first(self):
        return

    def remove_last(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = None
            return
        temp_node = self.head

        while temp_node.next.next is not None:
            temp_node = temp_node.next

        temp_node.next = None
        return

    def size(self):
        return

    def is_empty(self):
        return

    def print_list(self):
        curr = self.head

        while curr is not None:
            print(curr.item)
            curr = curr.next


def main():
    print("You can test here")

    test_list = SinglyLinkedList(Node(2, None))
    test_list.add(0, 1)
    test_list.add(1, 3)
    test_list.add(0,4)
    test_list.add(5,76)
    print("Hello")
    test_list.print_list()


if __name__ == "__main__":
    main()
