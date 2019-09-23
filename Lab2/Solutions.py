from Lab2.List import LinkedList
from Lab2.List import Node


def read_file(file, full_list):
    print("Read file")

    for line in file:
        full_list.insert(int(line))

    print("List size is", full_list.get_size())
    file.close()


def main():
    print("Hello World")
    list = LinkedList(Node(None, None))

    print(list.get_size())

    read_file(open("activision.txt", "r"), list)
    read_file(open("vivendi.txt", "r"), list)

    print("Full list size is ", list.get_size())


main()
