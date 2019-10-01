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


def grade_s1():

    print("\n-- Section 1 --")
    correct = True

    try:
        if Section1.count_even(2647) != 3:
            print("[Problem 1 - Test Case] count_even(2647) should return 3")
            correct = False

        if Section1.count_even(0) != 1:
            print("[Problem 1 - Test Case] count_even(0) should return 1")
            correct = False

        if Section1.count_even(1) != 0:
            print("[Problem 1 - Test Case] count_even(1) should return 0")
            correct = False

        if Section1.count_even(6789) != 2:
            print("[Problem 1 - Test Case] count_even(6789) should return 2")
            correct = False

        if Section1.count_even(601850) != 4:
            print("[Problem 1 - Test Case] count_even(601850) should return 4")
            correct = False

        if Section1.count_even(2468) != 4:
            print("[Problem 1 - Test Case] count_even(130570) should return 4")
            correct = False

        if Section1.count_even(1357) != 0:
            print("[Problem 1 - Test Case] count_even(1357) should return 0")
            correct = False
    except Exception as ex:
        print("[Problem 1] Exception thrown: ", ex)
        correct = False

    print("[Problem 1]", (str(P1_POINTS) + " / " + str(P1_POINTS)) if correct else ("0.0 / " + str(P1_POINTS)))

    return P1_POINTS if correct else 0


def grade_s2():
    print("\n-- Section 2 --")

    points = 0

    # Problem 2
    ans = (Section2.get_problem_2_answer() == 0) * P2_12_POINTS
    points += ans
    print("[Problem 2]", ans, "/", P2_12_POINTS)

    # Problem 3
    ans = (Section2.get_problem_3_answer() == 1) * P2_12_POINTS
    points += ans
    print("[Problem 3]", ans, "/", P2_12_POINTS)

    # Problem 4
    ans = (Section2.get_problem_4_answer() == 3) * P2_12_POINTS
    points += ans
    print("[Problem 4]", ans, "/", P2_12_POINTS)

    # Problem 5
    ans = (Section2.get_problem_5_answer() == 2) * P2_12_POINTS
    points += ans
    print("[Problem 5]", ans, "/", P2_12_POINTS)

    return points


def grade_s3():
    print("\n-- Section 3 --")

    points = 0

    # Problem 6
    a, b, k = Section3.get_problem_6_answer()
    ans = (((a == 1) + (b == 4) + (k == 1)) / 3.0) * P2_12_POINTS
    points += ans
    print("[Problem 6]", ans, "/", P2_12_POINTS)

    # Problem 7
    a, b, k = Section3.get_problem_7_answer()
    ans = (((a == 12) + (b == 2) + (k == 0)) / 3.0) * P2_12_POINTS
    points += ans
    print("[Problem 7]", ans, "/", P2_12_POINTS)

    # Problem 8
    a, b, k = Section3.get_problem_8_answer()
    ans = (((a == 2) + (b == 8) + (k == 1)) / 3.0) * P2_12_POINTS
    points += ans
    print("[Problem 8]", ans, "/", P2_12_POINTS)

    # Problem 9
    ans = (Section3.get_problem_9_answer() == 4) * P2_12_POINTS
    points += ans
    print("[Problem 9]", ans, "/", P2_12_POINTS)

    # Problem 10
    ans = (Section3.get_problem_10_answer() == 5) * P2_12_POINTS
    points += ans
    print("[Problem 10]", ans, "/", P2_12_POINTS)

    # Problem 11
    ans = (Section3.get_problem_11_answer() == 0) * P2_12_POINTS
    points += ans
    print("[Problem 11]", ans, "/", P2_12_POINTS)

    # Problem 12
    ans = (Section3.get_problem_12_answer() == 192) * P2_12_POINTS
    points += ans
    print("[Problem 12]", ans, "/", P2_12_POINTS)

    return points


def grade_s4():
    print("\n-- Section 4 --")

    points = 0

    # Problem 13
    ans = (Section4.get_problem_13_answer() == 5) * P13_18_POINTS
    points += ans
    print("[Problem 13]", ans, "/", P13_18_POINTS)

    # Problem 14
    n, x, y = Section4.get_problem_14_answer()
    ans = (((n == 2) + (x == 5) + (y == 3)) / 3.0) * P13_18_POINTS
    points += ans

    print("[Problem 14]", ans, "/", P13_18_POINTS)

    # Problem 15
    ans = (Section4.get_problem_15_answer() == 1) * P13_18_POINTS
    points += ans
    print("[Problem 15]", ans, "/", P13_18_POINTS)
    return points


def grade_s5():
    print("\n-- Section 5 --")

    points = 0

    # Problem 16
    ans = (Section5.get_problem_16_answer() == 3) * P13_18_POINTS
    points += ans
    print("[Problem 16]", ans, "/", P13_18_POINTS)

    # Problem 17
    ans = (Section5.get_problem_17_answer() == 4) * P13_18_POINTS
    points += ans
    print("[Problem 17]", ans, "/", P13_18_POINTS)

    # Problem 18
    ans = (Section5.get_problem_18_answer() == 2) * P13_18_POINTS
    points += ans
    print("[Problem 18]", ans, "/", P13_18_POINTS)

    return points


def grade_s6():
    print("\n-- Section 6 --")

    points = 0

    # remove_last tests
    head = Node(10)
    curr = head
    for i in range(10):
        head = Node(1, head)

    try:
        sll = SinglyLinkedList(head)
        curr.next = Node(20)
        curr.next.next = Node(5)
        sll.remove_last()
        correct = curr.item == 10 and curr.next.item == 20 and curr.next.next is None
        sll.remove_last()
        correct = correct and curr.item == 10 and curr.next is None
        sll = SinglyLinkedList()
        sll.remove_last()
    except Exception as ex:
        print("[Problem 19] Exception thrown: ", ex)
        correct = False

    print("[Problem 19]", (str(P19_22_POINTS) + " / " + str(P19_22_POINTS)) if correct
        else ("0.0 / " + str(P19_22_POINTS)))

    points += P19_22_POINTS if correct else 0

    # contains tests
    head = Node(10)
    for i in range(10):
        head = Node(i, head)

    try:
        sll = SinglyLinkedList(head)
        correct = sll.contains(10)

        correct = correct and sll.contains(0)
        correct = correct and sll.contains(5)
        correct = correct and not sll.contains(-1)
        correct = correct and not sll.contains(99)
    except Exception as ex:
        print("[Problem 20] Exception thrown: ", ex)
        correct = False

    print("[Problem 20]", (str(P19_22_POINTS) + " / " + str(P19_22_POINTS)) if correct
        else ("0.0 / " + str(P19_22_POINTS)))
    points += P19_22_POINTS if correct else 0

    # get tests
    head = Node(0)
    for i in range(10):
        head = Node(i * 2 - 4 * 30, head)

    try:
        sll = SinglyLinkedList(head)

        correct = sll.get(10) == 0 and sll.get(9) == -120 and sll.get(0) == -102 and sll.get(11) is None

        sll = SinglyLinkedList()
        correct = correct and sll.get(0) is None

        head = None
        for i in range(3, -1, -1):
            head = Node(i, head)
        sll = SinglyLinkedList(head)

        correct = correct and sll.get(3) == 3 and sll.get(4) is None

    except Exception as ex:
        print("[Problem 21] Exception thrown: ", ex)
        correct = False

    print("[Problem 21]", (str(P19_22_POINTS) + " / " + str(P19_22_POINTS)) if correct
        else ("0.0 / " + str(P19_22_POINTS)))
    points += P19_22_POINTS if correct else 0

    # add tests
    head = Node(0)
    for i in range(2, 4):
        head = Node(i, head)

    try:
        sll = SinglyLinkedList(head)
        sll.add(1,1)

        correct = head.item == 3 and head.next.item == 1 and head.next.next.next.next is None
        head = head.next
        sll = SinglyLinkedList(head)

        sll.add(0, 0)
        head = sll.head
        correct = correct and head.item == 0 and head.next.next.item == 2 and head.next.next.next.next is None

        sll.add(4, 10)

        correct = correct and head.item == 0 and head.next.next.item == 2 and head.next.next.next.next.item == 10

        sll.add(6,11)

        correct = correct and head.next.next.next.next.next is None

    except Exception as ex:
        print("[Problem 22] Exception thrown: ", ex)
        correct = False

    print("[Problem 22]", (str(P19_22_POINTS) + " / " + str(P19_22_POINTS)) if correct
        else ("0.0 / " + str(P19_22_POINTS)))
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
    print("Exam 1 Grade: ", total_points)


if __name__ == "__main__":
    main()
