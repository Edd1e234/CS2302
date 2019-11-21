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
        return

    def contains(self):
        return

    def index_of(self, item):
        return

    def get(self, index):
        return

    def get_first(self):
        return

    def get_last(self):
        return

    def remove_first(self):  # Problem 19
        return

    def has_duplicates(self):  # Problem 20
        return False

    def clear(self):  # Problem 21
        return

    def remove(self, index):  # Problem 22
        return

    def remove_last(self):
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


if __name__ == "__main__":
    main()

