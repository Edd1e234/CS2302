class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def add_last(self, item):
        if self.head is None:
            self.head = Node(item, None)
            return
        temp_node = self.head

        while temp_node.next is not None:
            temp_node = temp_node.next

        temp_node.next = Node(item, None)
        return

    def add_first(self, item):
        return

    def add(self, index, item):
        return

    def clear(self):
        return

    def contains(self):
        return

    def index_of(self, item):
        temp_node = self.head
        index = 0
        while temp_node is not None:
            if temp_node.item == item:
                return index
            index += 1
            temp_node = temp_node.next

        return -1

    def get(self, index):
        return

    def get_first(self):
        return

    def get_last(self):
        if self.head is None:
            return None
        temp_node = self.head

        while temp_node.next is not None:
            temp_node = temp_node.next

        return temp_node.item

    def remove(self, index):
        return

    def remove_first(self):
        return

    def remove_last(self):
        return

    def size(self):
        temp = self.head
        size = 0
        while temp is not None:
            size += 1
            temp = temp.next
        return size

    def is_empty(self):
        return

    def print_list(self):
        temp = self.head

        while temp is not None:
            print(temp.item)
            temp = temp.next
        return


def main():
    print("You can test here")

    single_list = SinglyLinkedList(None)
    single_list.add_last(1)
    single_list.add_last(2)
    single_list.add_last(3)
    single_list.print_list()

    node = single_list.get_last()

    print(node.item)

if __name__ == "__main__":
    main()
