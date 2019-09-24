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

    # Swaps Data.
    temp_data = first_node.get_data()
    first_node.set_data(second_node.get_data())
    second_node.set_data(temp_data)


def print_list(employee_list):
    print("Printing List \n\n")
    if not isinstance(employee_list, LinkedList):
        return

    node = employee_list.get_head()
    for i in range(employee_list.get_size()):
        print(node.get_data())
        node = node.get_next()
    print("\n\n")


def print_standard_list(list_):
    print("Printing Standard List \n\n")
    if not isinstance(list_, list):
        return

    for i in list_:
        print(i)
    print("\n\n")


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


def bubble_sort(employee_list):
    amount_of_swaps = 1
    while amount_of_swaps is not 0:
        amount_of_swaps = 0
        temp_node = employee_list.get_head()
        # print("Does this run")
        for i in range(employee_list.get_size() - 1):
            if temp_node.get_next() is None:
                break

            if temp_node.get_data() > temp_node.get_next().get_data():
                # print("First Node ", temp_node.get_data())
                # print("Second Node ", temp_node.get_next().get_data(), "\n\n")
                swap_node(temp_node, temp_node.get_next())
                # print("After Swap")
                # print_list(employee_list)
                # print("Temp is ", temp_node.get_data())
                # print("And points to ", temp_node.get_next().get_data())
                amount_of_swaps += 1

                # print("The head is this", employee_list.get_head().get_data())

            # print("End of inner loop")
            temp_node = temp_node.get_next()
        # print("One iteration done")

    print("Bubble Sort complete")


# TODO(Edd1e234): Comment all of this.
def solution_2(employee_list):
    print("Solution 2 Running")
    if not isinstance(employee_list, LinkedList):
        return None
    temp_node = employee_list.get_head()
    duplicate_list = []

    counter = 0
    while temp_node is not None:
        counter += 1
        if temp_node.get_next() is None:
            return duplicate_list

        if temp_node.get_next().get_data() == temp_node.get_data():
            print("Got here")
            duplicate_list.append(temp_node.get_data())
            temp_node = temp_node.get_next()
        temp_node = temp_node.get_next()

    return duplicate_list


def merge_sort(employee_list, left_list, middle_list):
    print("Merge Sort")


def main():
    print("Hello World")

    bubble_list = LinkedList(Node(None, None))
    employee_list_test_1 = LinkedList(Node(None, None))
    employee_list_test_2 = LinkedList(Node(None, None))

    read_file("bubble_sort_test_file_2.txt", bubble_list)
    read_file("test_file_1.txt", employee_list_test_1)
    read_file("test_file_1.txt", employee_list_test_2)

    bubble_sort(employee_list_test_1)
    print_list(employee_list_test_1)

    print("employee list test 1")
    duplicate_ids = solution_1(employee_list_test_1)
    print_list(employee_list_test_1)
    print_standard_list(duplicate_ids)
    print("Size of duplicate ID list is: ", len(duplicate_ids))

    print("employee list test 2")
    bubble_sort(employee_list_test_2)

    print_list(employee_list_test_2)
    duplicate_ids_2 = solution_2(employee_list_test_2)
    print_standard_list(duplicate_ids_2)
    print("Size of duplicate ID list is ", len(duplicate_ids_2))


main()
