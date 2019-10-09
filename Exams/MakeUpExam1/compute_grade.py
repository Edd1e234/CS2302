from s0_name_and_id import Section0
from s1_recursion import Section1
from s2_iterative_time_complexity import Section2
from s3_recursive_time_complexity import Section3
from s4_activation_records import Section4
from s5_lists_1 import Section5
from s6_lists_2 import Node, SinglyLinkedList


P1_POINTS = 10.0
P2_12_POINTS = 4.0
P13_18_POINTS = 5.0
P19_22_POINTS = 7.0


def grade_s1(answer_list_points):

    print("\n-- Section 1 --")
    correct = True

    try:
        if Section1.change_x_y("codex") != "codex".replace("x","y"):
            print("[Problem 1 - Test Case] change_x_y('codex') should return 'codey'")
            correct = False

        if Section1.change_x_y("cxxodex") != "cxxodex".replace("x","y"):
            print("[Problem 1 - Test Case] change_x_y('cxxodex') should return 'cyyodey'")
            correct = False

        if Section1.change_x_y("xxhixx") != "xxhixx".replace("x","y"):
            print("[Problem 1 - Test Case] change_x_y('xxhixx') should return 'codey'")
            correct = False

        if Section1.change_x_y("xyx") != "xyx".replace("x","y"):
            print("[Problem 1 - Test Case] change_x_y('xyx') should return 'yyy'")
            correct = False

        if Section1.change_x_y("x") != "x".replace("x","y"):
            print("[Problem 1 - Test Case] change_x_y('x') should return 'y'")
            correct = False

        if Section1.change_x_y("xhixhix") != "xhixhix".replace("x","y"):
            print("[Problem 1 - Test Case] change_x_y('xhixhix') should return 'yhiyhiy'")
            correct = False

        if Section1.change_x_y("") != "".replace("x","y"):
            print("[Problem 1 - Test Case] change_x_y('') should return ''")
            correct = False
    except Exception as ex:
        print("[Problem 1] Exception thrown: ", ex)
        correct = False

    print("[Problem 1]", (str(P1_POINTS) + " / " + str(P1_POINTS)) if correct else ("0.0 / " + str(P1_POINTS)))

    answer_list_points.append(P1_POINTS if correct else 0)

    return P1_POINTS if correct else 0


def grade_s2(answer_list_points):
    print("\n-- Section 2 --")

    points = 0

    return points


def grade_s3(answer_list_points):
    print("\n-- Section 3 --")

    points = 0

    return points


def grade_s4(answer_list_points):
    print("\n-- Section 4 --")

    points = 0

    return points


def grade_s5(answer_list_points):
    print("\n-- Section 5 --")

    points = 0

    return points


def grade_s6(answer_list_points):
    print("\n-- Section 6 --")

    points = 0

    # remove_first tests
    head = Node(10)
    curr = head
    for i in range(10):
        head = Node(i, head)

    try:
        sll = SinglyLinkedList(head)
        curr.next = Node(20)
        curr.next.next = Node(5)

        sll.remove_first()

        correct = sll.head.item == 8 and curr.next.item == 20 and sll.head.next.next.item == 6
        for i in range(11):
            sll.remove_first()
        correct = correct and sll.head.item == 5 and sll.head.next is None

        for i in range(2):
            sll.remove_first()

        correct = correct and sll.head is None

        sll = SinglyLinkedList()
        sll.remove_first()
    except Exception as ex:
        print("[Problem 19] Exception thrown: ", ex)
        correct = False

    print("[Problem 19]", (str(P19_22_POINTS) + " / " + str(P19_22_POINTS)) if correct
        else ("0.0 / " + str(P19_22_POINTS)))

    answer_list_points.append(P19_22_POINTS if correct else 0)

    points += P19_22_POINTS if correct else 0

    # has_duplicates tests
    head = Node(10)
    for i in range(10):
        head = Node(i, head)

    try:
        sll = SinglyLinkedList(head)
        correct = not sll.has_duplicates()

        sll.head = Node(10, sll.head)

        correct = correct and sll.has_duplicates()

        sll = SinglyLinkedList()

        correct = correct and not sll.has_duplicates()

        head = None
        for i in range(9):
            head = Node(i % 3, head)
        sll = SinglyLinkedList(head)

        correct = correct and sll.has_duplicates()

    except Exception as ex:
        print("[Problem 20] Exception thrown: ", ex)
        correct = False

    print("[Problem 20]", (str(P19_22_POINTS) + " / " + str(P19_22_POINTS)) if correct
        else ("0.0 / " + str(P19_22_POINTS)))
    answer_list_points.append(P19_22_POINTS if correct else 0)
    points += P19_22_POINTS if correct else 0

    # clear tests
    head = Node(0)
    for i in range(10):
        head = Node(i * 2 - 4 * 30, head)

    try:
        sll = SinglyLinkedList(head)

        correct = sll.head is not None

        sll.clear()

        correct = correct and sll.head is None

        sll = SinglyLinkedList()

        sll.clear()

        correct = correct and sll.head is None
    except Exception as ex:
        print("[Problem 21] Exception thrown: ", ex)
        correct = False

    print("[Problem 21]", (str(P19_22_POINTS) + " / " + str(P19_22_POINTS)) if correct
        else ("0.0 / " + str(P19_22_POINTS)))
    answer_list_points.append(P19_22_POINTS if correct else 0)
    points += P19_22_POINTS if correct else 0

    # remove tests
    head = Node(0)
    curr = head
    temp = None
    for i in range(2, 10):
        head = Node(i, head)

        if i == 2:
            temp = head

    try:
        sll = SinglyLinkedList(head)
        sll.remove(2)

        correct = sll.head.item == 9 and sll.head.next.item == 8 and sll.head.next.next.item == 6 and curr.item == 0

        sll.remove(0)

        correct = correct and sll.head.item == 8 and sll.head.next.next.item == 5 and curr.item == 0

        sll.remove(6)

        correct = correct and sll.head.item == 8 and temp.item == 2 and temp.next is None

        sll.remove(6)
        sll.remove(10)

        correct = correct and sll.head.item == 8 and temp.item == 2 and temp.next is None

        for i in range(10):
            sll.remove(0)

        correct = correct and sll.head is None

    except Exception as ex:
        print("[Problem 22] Exception thrown: ", ex)
        correct = False

    print("[Problem 22]", (str(P19_22_POINTS) + " / " + str(P19_22_POINTS)) if correct
        else ("0.0 / " + str(P19_22_POINTS)))
    answer_list_points.append(P19_22_POINTS if correct else 0)
    points += P19_22_POINTS if correct else 0

    return points


def main():
    total_points = 0

    answer_list_points = []

    s1_points = grade_s1(answer_list_points)
    s2_points = grade_s2(answer_list_points)
    s3_points = grade_s3(answer_list_points)
    s4_points = grade_s4(answer_list_points)
    s5_points = grade_s5(answer_list_points)
    s6_points = grade_s6(answer_list_points)

    total_points += s1_points
    total_points += s2_points
    total_points += s3_points
    total_points += s4_points
    total_points += s5_points
    total_points += s6_points

    print("\n-- Final Results --")

    print("-----------------------")
    print("Section 1 Grade: ", s1_points)
    print("Section 2 Grade: ", s2_points)
    print("Section 3 Grade: ", s3_points)
    print("Section 4 Grade: ", s4_points)
    print("Section 5 Grade: ", s5_points)
    print("Section 6 Grade: ", s6_points)
    print("-----------------------")
    print()
    print("Make Up Exam 1 Grade: ", total_points)


if __name__ == "__main__":
    main()
