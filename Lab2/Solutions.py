import sys

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
        try:
            employee_id = int(line)
        except ValueError:
            print(line, "Not valid")
            return
        
        if not isinstance(employee_id, int):
            print(employee_id, " Not valid ID.")
            return

        full_list.insert_at_tail(employee_id)

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
    print("Printing List")

    if not isinstance(employee_list, LinkedList):
        return
    if employee_list.get_head() is not None:
        print("Head is ", employee_list.get_head().get_data(), "\n")

    node = employee_list.get_head()
    while node is not None:
        print(node.get_data())
        node = node.get_next()
    if employee_list.get_tail() is not None:
        print("\ntail is ", employee_list.get_tail().get_data(), "\n")

    print("List size ", employee_list.get_size())
    print("\n")


def print_standard_list(list_):
    print("Printing Standard List \n")
    if not isinstance(list_, list):
        return

    for i in list_:
        print(i)
    print("\n")


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
        start_node = employee_list.get_head()

        for j in range(employee_list.get_size()):
            # print("comparing ", temp_node.get_data(), "and", start_node.get_data())
            if temp_node.get_data() == start_node.get_data():
                # print("Inside IF")
                total_duplicate_number += 1

            start_node = start_node.get_next()

        # Comparing using 2 because every ID will at one point compare to itself.
        if total_duplicate_number == 2:
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
    if not isinstance(employee_list, LinkedList):
        return None
    temp_node = employee_list.get_head()
    duplicate_list = []

    counter = 0
    while temp_node is not None:
        # print("Inside Loop")
        counter += 1
        if temp_node.get_next() is None:
            return duplicate_list
        # print("First one", temp_node.get_data(), "Second one ", temp_node.get_next().get_data())
        if temp_node.get_next().get_data() == temp_node.get_data():
            # print("Inside if statement")
            duplicate_list.append(temp_node.get_data())
            temp_node = temp_node.get_next()
        temp_node = temp_node.get_next()

    return duplicate_list


def merge_sort(employee_list):
    if employee_list.get_size() is 1:
        # print("DONE HERE")
        # print(employee_list.get_head().get_data())
        return
    # print("Starting the merge sort, list seperating is, the size is  ", employee_list.get_size())
    # print_list(employee_list)

    # Nodes that will transverse through tree.
    middle_node = employee_list.get_head()
    temp_node = employee_list.get_head()
    size = 0

    # Finds the middle list.
    if employee_list.get_size() is 2:
        # print("List Only contains two items")
        size = 1
    else:
        while temp_node.get_next() is not None:
            if None is not temp_node.get_next().get_next():
                # print("Went here")
                size += 1
                middle_node = middle_node.get_next()
                temp_node = temp_node.get_next().get_next()
            else:
                break
        size += 1

    # Sets up left tree.
    new_left_list = LinkedList(employee_list.get_head())
    new_left_list.set_size(size)

    new_middle_list = LinkedList(middle_node.get_next())
    middle_node.set_next(None)

    # print_list(employee_list)
    new_middle_list.set_size(employee_list.get_size() - size)

    merge_sort(new_left_list)
    merge_sort(new_middle_list)
    # print("DONE WITH SEPERATING---------------------------")
    # print("Left list")
    # print_list(new_left_list)

    # print("Right List4")
    # print_list(new_middle_list)

    merge(employee_list, new_left_list, new_middle_list)
    # print_list(employee_list)


def merge(employee_list, new_left_list, new_middle_list):
    new_list = LinkedList(Node(None, None))
    left_node = new_left_list.get_head()
    right_node = new_middle_list.get_head()
    # print(left_node.get_data())
    # print(right_node.get_data())
    while left_node is not None and right_node is not None:
        if left_node.get_data() < right_node.get_data():
            # print("LEft")
            # print(left_node.get_data(), "is less than ", right_node.get_data())
            new_list.insert_at_tail(left_node.get_data())
            left_node = left_node.get_next()
        else:
            # print("Right")
            # print(right_node.get_data(), "is less than ", left_node.get_data())
            new_list.insert_at_tail(right_node.get_data())
            right_node = right_node.get_next()

    while left_node is not None:
        new_list.insert_at_tail(left_node.get_data())
        left_node = left_node.get_next()
    while right_node is not None:
        new_list.insert_at_tail(right_node.get_data())
        right_node = right_node.get_next()

    # print("MERGE DONE")
    # print_list(new_list)
    employee_list.set_head(new_list.get_head())
    employee_list.set_tail(new_list.get_tail())
    # print("JUST SET HEAD")


def solution_4(employee_list):
    if not isinstance(employee_list, LinkedList):
        return
    if employee_list.get_head().get_data() is None:
        return
    duplicate_list = []
    boolean_list = []
    counter = 0
    for i in range(employee_list.get_largest_id() + 1):
        boolean_list.append(False)
        counter += 1

    # print("Counter is ", counter)

    # print("Boolean list is this size", boolean_list.__sizeof__())
    # print("Largest employee ID is ", employee_list.get_largest_id())
    temp_node = employee_list.get_head()
    for i in range(employee_list.get_size()):
        if boolean_list[temp_node.get_data()] is True:
            duplicate_list.append(temp_node.get_data())
        else:
            boolean_list[temp_node.get_data()] = True
        temp_node = temp_node.get_next()
    return duplicate_list


def test_all(filename):
    employee_list_brute_test_1 = LinkedList(Node(None, None))
    employee_list_bubble_test_1 = LinkedList(Node(None, None))
    employee_list_merge_test_1 = LinkedList(Node(None, None))
    employee_list_boolean_test_1 = LinkedList(Node(None, None))

    read_file(filename, employee_list_brute_test_1)
    read_file(filename, employee_list_bubble_test_1)
    read_file(filename, employee_list_merge_test_1)
    read_file(filename, employee_list_boolean_test_1)

    print("Bubble Sorted List")
    bubble_sort(employee_list_bubble_test_1)
    print_list(employee_list_bubble_test_1)

    print("Merge Sorted List")
    merge_sort(employee_list_merge_test_1)
    print_list(employee_list_merge_test_1)

    print("Brute Force Solution 1, Duplicated IDS")
    duplicate_list_1 = solution_1(employee_list_brute_test_1)
    print_standard_list(duplicate_list_1)

    print("Bubble Sort Solution 2, Duplicated IDS")
    duplicate_list_2 = solution_2(employee_list_bubble_test_1)
    print_standard_list(duplicate_list_2)

    print("Merge Sort Solution 3, Duplicated IDS")
    duplicate_list_3 = solution_2(employee_list_merge_test_1)
    print_standard_list(duplicate_list_3)

    print("Boolean Array Solution 4, Duplicated IDS ")
    duplicate_list_4 = solution_4(employee_list_boolean_test_1)
    print_standard_list(duplicate_list_4)


def main():
    sys.setrecursionlimit(10000)
    print("Test Case 1, Expecting 999, 888, 222, 111 as duplicates")
    test_all("test_file_1.txt")

    print("Test Case 2, Expecting None as duplicates")
    test_all("test_file_2.txt")

    print("Test Case 3, Expecting 3, 1231 as duplicates")
    test_all("test_file_3.txt")

    print("Test Case 4, Expecting exception error duplicates")
    test_all("Bad input")

    print("Test Case 5, Expecting exception error duplicates")
    test_all("test_file_4.txt")

    final_list_1 = LinkedList(Node(None, None))
    final_list_2 = LinkedList(Node(None, None))
    final_list_3 = LinkedList(Node(None, None))
    final_list_4 = LinkedList(Node(None, None))

    read_file("activision.txt", final_list_1)
    print("activision.txt file read, List size is now ", final_list_1.get_size())

    read_file("vivendi.txt", final_list_1)
    print("vivendi.txt file read, List size is now ", final_list_1.get_size())

    read_file("activision.txt", final_list_2)
    read_file("vivendi.txt", final_list_2)
    read_file("activision.txt", final_list_3)
    read_file("vivendi.txt", final_list_3)
    read_file("activision.txt", final_list_4)
    read_file("vivendi.txt", final_list_4)


    print("solution 1 duplicates are")
    duplicate_list_1 = solution_1(final_list_1)
    print_standard_list(duplicate_list_1)

    print("Solution 2 duplicates are")
    bubble_sort(final_list_2)
    duplicate_list_2 = solution_2(final_list_2)
    print_standard_list(duplicate_list_2)

    print("Solution 3 duplicates are ")
    merge_sort(final_list_3)
    duplicate_list_3 = solution_2(final_list_3)
    print_standard_list(duplicate_list_3)

    print("Solution 4 duplicates are ")
    duplicate_list_4 = solution_4(final_list_4)
    print_standard_list(duplicate_list_4)






main()
