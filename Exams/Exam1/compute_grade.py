from s0_name_and_id import Section0
from s1_recursion import Section1
from s2_iterative_time_complexity import Section2
from s3_recursive_time_complexity import Section3
from s4_activation_records import Section4
from s5_lists_1 import Section5
from s6_lists_2 import Node, SinglyLinkedList

P1_POINTS = 10
P2_12_POINTS = 4
P13_18_POINTS = 5
P19_22_POINTS = 7


def grade_s1():

    correct = True

    try:
        if Section1.count(2647) != 2:
            print("[Problem 1 - Test Case] count(2647) should return 2")
            correct = False

        if Section1.count(0) != 1:
            print("[Problem 1 - Test Case] count(0) should return 1")
            correct = False

        if Section1.count(6789) != 0:
            print("[Problem 1 - Test Case] count(6789) should return 0")
            correct = False

        if Section1.count(601850) != 4:
            print("[Problem 1 - Test Case] count(601850) should return 4")
            correct = False
    except Exception as ex:
        print("[Problem 1] Exception thrown: ", ex)
        correct = False

    print("[Problem 1]", "Correct" if correct else "Incorrect")

    return P1_POINTS if correct else 0


def grade_s2():
    points = 0

    return points


def grade_s3():
    points = 0

    return points


def grade_s4():
    points = 0

    return points


def grade_s5():
    points = 0

    return points


def grade_s6():
    points = 0

    # addLast tests
    head = Node(10)
    curr = head
    for i in range(10):
        head = Node(1, head)

    try:
        sll = SinglyLinkedList(head)
        sll.add_last(30)
        correct = curr.next.item == 30
        curr = curr.next
        sll.add_last(-34)
        correct = correct and curr.next.item == -34
        sll = SinglyLinkedList()
        sll.add_last(1)
        correct = correct and sll.head.item == 1
    except Exception as ex:
        print("[Problem 19] Exception thrown: ", ex)
        correct = False

    print("[Problem 19]", "Correct" if correct else "Incorrect")

    points += P19_22_POINTS if correct else 0

    # index_of tests
    head = Node(10)
    for i in range(10):
        head = Node(i, head)

    try:
        sll = SinglyLinkedList(head)
        correct = sll.index_of(10) == 10

        correct = correct and sll.index_of(0) == 9
        correct = correct and sll.index_of(5) == 4
        correct = correct and sll.index_of(-1) == -1
        correct = correct and sll.index_of(99) == -1
    except Exception as ex:
        print("[Problem 20] Exception thrown: ", ex)
        correct = False

    print("[Problem 20]", "Correct" if correct else "Incorrect")

    points += P19_22_POINTS if correct else 0

    # get_last tests
    head = Node(0)
    for i in range(10):
        head = Node(i, head)

    try:
        sll = SinglyLinkedList(head)
        correct = sll.get_last() == 0

        sll = SinglyLinkedList()
        correct = correct and sll.get_last() is None

        head = None
        for i in range(3, -1, -1):
            head = Node(i, head)
        sll = SinglyLinkedList(head)

        correct = correct and sll.get_last() == 3

    except Exception as ex:
        print("[Problem 21] Exception thrown: ", ex)
        correct = False

    print("[Problem 21]", "Correct" if correct else "Incorrect")

    points += P19_22_POINTS if correct else 0

    # size tests
    head = Node(0)
    for i in range(10):
        head = Node(i, head)

    try:
        sll = SinglyLinkedList(head)

        correct = sll.size() == 11

        sll = SinglyLinkedList()
        correct = correct and sll.size() == 0

        head = None
        for i in range(3, -1, -1):
            head = Node(i, head)
        sll = SinglyLinkedList(head)

        correct = correct and sll.size() == 4

    except Exception as ex:
        print("[Problem 22] Exception thrown: ", ex)
        correct = False

    print("[Problem 22]", "Correct" if correct else "Incorrect")

    points += P19_22_POINTS if correct else 0

    return points


def main():
    total_points = 0
    s1_points = grade_s1()
    s2_points = grade_s2()
    s3_points = grade_s3()
    s4_points = grade_s4()
    s5_points = grade_s5()
    s6_points = grade_s6()

    total_points += s1_points
    total_points += s2_points
    total_points += s3_points
    total_points += s4_points
    total_points += s5_points
    total_points += s6_points

    print("-----------------------")
    print("Section 1 Grade: ", s1_points)
    print("Section 2 Grade: ", s2_points)
    print("Section 3 Grade: ", s3_points)
    print("Section 4 Grade: ", s4_points)
    print("Section 5 Grade: ", s5_points)
    print("Section 6 Grade: ", s6_points)
    print("-----------------------")
    print()
    print("Exam 1 Grade: ", total_points)


if __name__ == "__main__":
    main()
