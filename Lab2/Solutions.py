from Lab2.List import LinkedList
from Lab2.List import Node


def read_file(file_name, full_list):
    """
    Function will open and read a text file, the text file name will be given by 'file_name'.
    Once file is open it will go through and read line by line for employee ID's.

    Bad inputs should be handled.

    :param file_name: Will be the name of file being searched.
    :param full_list: Linked List to add all ID's.
    """

    if not isinstance(full_list, LinkedList):
        return
    try:
        file = open(file_name, "r")
    except FileNotFoundError:
        print("File not found")
        return

    for line in file:

        # This is inefficient but verifies that the file does not have bad inputs.
        employee_id = int(line)
        if not isinstance(employee_id, int):
            print(employee_id, " Not valid ID.")
            return
        full_list.insert(employee_id)

    # TODO(Edd1e234): Comment this out once finished.
    print("List size is", full_list.get_size())
    file.close()


def swap_node(first_node, second_node):
    if not isinstance(first_node, Node) and isinstance(second_node, Node):
        print("Bad inputs")
        return
    if second_node.get_next is None:
        first_node.set_next(None)
    else:
        first_node.set_next(second_node.get_next())

    second_node.set_next(first_node)


def print_list(employee_list):
    if not isinstance(employee_list, LinkedList):
        return

    node = employee_list.get_head()
    for i in range(employee_list.get_size()):
        print(node.get_data())
        node = node.get_next()


def solution_1(employee_list):
    """
    This function will compare every employee ID in the list with every other employee ID and search for
    duplicates. If duplicate is found the ID number is copied into a separate list.

    :param employee_list: Linked List of employee IDS.
    :return: List of duplicate ID's.
    """

    # Checks 'employee_list'.
    if not isinstance(employee_list, LinkedList):
        print("Not the correct data type")
        return None

    duplicate_ids = []
    temp_node = employee_list.get_head()

    for i in range(employee_list.get_size()):
        total_duplicate_number = 0

        # This node will iterate through entire list and be compared to 'temp_node'
        loop_node = employee_list.get_head()

        for j in range(employee_list.get_size()):
            if temp_node.get_data() is loop_node.get_data():
                total_duplicate_number += 1

            loop_node = loop_node.get_next()

        # Comparing using 2 because every ID will at one point compare to itself.
        if total_duplicate_number >= 2:
            duplicate_ids.append(temp_node.get_data())

        # Moves on to the next one.
        temp_node = temp_node.get_next()
    return duplicate_ids


def solution_2(employee_list):
    amount_of_swaps = 1

    while amount_of_swaps is not 0:
        temp_node = employee_list.get_head()
        for i in range(employee_list.get_size()):
            if temp_node.get_next() is None:
                break

            if temp_node.get_data() > temp_node.get_next().get_data():
                swap_node(temp_node, temp_node.get_next())

    print("Solution 2")


def main():
    print("Hello World")
    employee_list = LinkedList(Node(None, None))

    print(employee_list.get_size())

    read_file("test_file_1.txt", employee_list)

    print("Full list size is ", employee_list.get_size())

    duplicate_ids = solution_1(employee_list)
    size_of_duplicate_ids = len(duplicate_ids)
    print("Size of duplicate ID list is: ", size_of_duplicate_ids)

    print_list(employee_list)

    bubble_list = LinkedList(Node(None, None))

    read_file("bubble_sort_test_file_2.txt", bubble_list)
    print("Bubble List:")
    print_list(bubble_list)
    print("End of first bubble list")

    solution_2(bubble_list)

    print("Bubble List:")
    print_list(bubble_list)
    print("End of second bubble list")


main()
