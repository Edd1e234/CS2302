from s0_name_and_id import Section0
from s1_multiple_choice import MultipleChoiceSection
from s2_binary_search_tree_section import BinaryTreeNode, BinarySearchTree
from s3_btree_section import BTreeNode, BTree
from s4_hash_tables_section import HashTable
from s5_heaps_section import MaxHeap

import math

EXTRA_CREDIT_POINTS = 2.0
MULTIPLE_CHOICE_POINTS = 4.0
CODING_POINTS = 6.0


def grade_s0(answer_list_points):
    section_points = 0
    if Section0.utep_id == "Your UTEP ID goes here":
        for i in range(100):
            print("Section0: You forgot to type your UTEP ID. Please do that now")

    elif len(Section0.utep_id) != 8:
        for i in range(100):
            print("Section0: Your UTEP ID is incorrect. Please fix it")

    print("\n-- Section 0 --")

    problem_points = Section0.i_earned_extra_credit() * EXTRA_CREDIT_POINTS
    answer_list_points.append(problem_points)
    section_points += problem_points
    print("[Extra Credit]", problem_points, "/", EXTRA_CREDIT_POINTS)

    return problem_points


def grade_s1(answer_list_points):

    print("\n-- Section 1 --")
    section_points = 0

    print("Unable to grade this section right now")

    return section_points


def grade_s2(answer_list_points):
    print("\n-- Section 2 --")

    section_points = 0

    # ---------- _sum tests ----------
    passed_tests = 0
    num_tests = 6

    try:
        root = BinaryTreeNode(2)
        tree = BinarySearchTree()
        tree.root = root
        passed_tests += tree._sum(tree.root) == 2
        root.left = BinaryTreeNode(4)

        passed_tests += tree._sum(tree.root) == 6
        root.left.right = BinaryTreeNode(3)
        root.left.right.left = BinaryTreeNode(4)
        root.left.right.right = BinaryTreeNode(2)

        passed_tests += tree._sum(tree.root) == 15
        root.left.left = BinaryTreeNode(10)

        passed_tests += tree._sum(tree.root) == 25

        root = BinaryTreeNode(10)
        tree.root = root
        num_iterations = 2
        for i in range(num_iterations):
            if i % 2 == 0:
                root.left = BinaryTreeNode(i)

                passed_tests += tree._sum(tree.root) == i + root.item
                root = root.left
            else:
                root.right = BinaryTreeNode(i)

                passed_tests += tree._sum(tree.root) == i + tree.root.item

    except Exception as ex:
        print("[Problem 7] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 7]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ---------- _sum_at_depth tests ----------

    passed_tests = 0
    num_tests = 10

    try:
        root = BinaryTreeNode(23)
        tree = BinarySearchTree()
        passed_tests += tree._sum_at_depth(0, tree.root) == 0

        tree.root = root
        passed_tests += tree._sum_at_depth(0, tree.root) == 23
        passed_tests += tree._sum_at_depth(10, tree.root) == 0
        root.left = BinaryTreeNode(12)
        root.left.right = BinaryTreeNode(2)
        root.left.right.left = BinaryTreeNode(-3)
        root.left.right.right = BinaryTreeNode(-102)
        passed_tests += tree._sum_at_depth(0, tree.root) == 23

        passed_tests += tree._sum_at_depth(3, tree.root) == -105
        passed_tests += tree._sum_at_depth(2, tree.root) == 2
        old_root = root
        root = BinaryTreeNode(root.item - root.item//2)
        tree.root = root

        passed_tests += tree._sum_at_depth(0, tree.root) == 12
        old_root.left = root
        tree.root = old_root


        passed_tests += tree._sum_at_depth(4, tree.root) == 0
        passed_tests += tree._sum_at_depth(1, tree.root) == 12
        passed_tests += tree._sum_at_depth(0, tree.root) == 23


    except Exception as ex:
        print("[Problem 8] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 8]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ---------- _max_val tests ----------

    passed_tests = 0
    num_tests = 6

    try:
        root = BinaryTreeNode(2)
        tree = BinarySearchTree()

        passed_tests += tree._max_val(tree.root) == -math.inf

        tree.root = root

        passed_tests += tree._max_val(tree.root) == 2
        root.left = BinaryTreeNode(4)
        root.right = BinaryTreeNode(1)

        passed_tests += tree._max_val(tree.root) == 1

        root.left.right = BinaryTreeNode(3)
        root.left.right.left = BinaryTreeNode(4)
        passed_tests += tree._max_val(tree.root) == 1

        root.right.right = BinaryTreeNode(32)

        root.right.right.left = BinaryTreeNode(2)

        passed_tests += tree._max_val(tree.root) == 32
        root.right.right.right = BinaryTreeNode(2)

        passed_tests += tree._max_val(tree.root) == 2
    except Exception as ex:
        print("[Problem 9] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 9]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ---------- _search tests ----------

    passed_tests = 0
    num_tests = 8

    try:
        root = BinaryTreeNode(9)
        tree = BinarySearchTree()
        tree.root = root
        nodes = []
        nodes2 = []
        for i in range(10, 14):
            nodes.append(BinaryTreeNode(i))
            nodes2.append(BinaryTreeNode(-i))

        root.right = nodes[0]
        root.right.right = nodes[1]
        root.right.right.right = nodes[2]
        root.right.right.right.right = nodes[3]

        root.left = nodes2[0]
        root.left.left = nodes2[1]
        root.left.left.left = nodes2[2]
        root.left.left.left.left = nodes2[3]

        passed_tests += tree._search(10, tree.root).item == 10
        passed_tests += tree._search(9, tree.root).item == 9
        passed_tests += tree._search(-13, tree.root).item == -13
        passed_tests += tree._search(14, tree.root) is None
        passed_tests += tree._search(8, tree.root) is None

        root.right = nodes2[0]
        root.right.right = nodes2[1]
        root.right.right.right = nodes2[2]
        root.right.right.right.right = nodes2[3]

        root.left = nodes[0]
        root.left.left = nodes[1]
        root.left.left.left = nodes[2]
        root.left.left.left.left = nodes[3]

        passed_tests += tree._search(10, tree.root) is None
        passed_tests += tree._search(-10, tree.root) is None

        root.right.left = nodes2[3]

        passed_tests += tree._search(nodes2[3].item, root.right).item == nodes2[3].item

    except Exception as ex:
        print("[Problem 10] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 10]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    return section_points


def grade_s3(answer_list_points):
    print("\n-- Section 3 --")

    section_points = 0

    # ---------- _height tests ----------
    passed_tests = 0
    num_tests = 3

    try:
        max_num_keys = 3
        root = BTreeNode(keys=[], children=[], is_leaf=True, max_num_keys=max_num_keys)
        tree = BTree(max_num_keys=max_num_keys)
        tree.root = root
        passed_tests += tree._height(tree.root) == 0
        root.is_leaf = False

        for i in range(max_num_keys):
            node = BTreeNode(keys=[], children=[], is_leaf=True, max_num_keys=max_num_keys)
            root.children.append(node)

        passed_tests += tree._height(tree.root) == 1

        for i in range(max_num_keys):
            root.children[i].is_leaf = False

            for j in range(max_num_keys):
                node = BTreeNode(keys=[], children=[], is_leaf=True, max_num_keys=max_num_keys)
                root.children[i].children.append(node)

        passed_tests += tree._height(tree.root) == 2

    except Exception as ex:
        print("[Problem 11] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 11]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ---------- _num_nodes tests ----------
    passed_tests = 0
    num_tests = 5

    try:
        max_num_keys = 3
        root = BTreeNode(keys=[], children=[], is_leaf=True, max_num_keys=max_num_keys)
        tree = BTree(max_num_keys=max_num_keys)
        tree.root = root


        passed_tests += tree._num_nodes (tree.root) == 1
        root.is_leaf = False

        for i in range(max_num_keys):
            node = BTreeNode(keys=[], children=[], is_leaf=True, max_num_keys=max_num_keys)
            root.children.append(node)



        passed_tests += tree._num_nodes(tree.root) == 4

        for i in range(max_num_keys):
            root.children[i].is_leaf = False

            for j in range(max_num_keys):
                node = BTreeNode(keys=[], children=[], is_leaf=True, max_num_keys=max_num_keys)
                root.children[i].children.append(node)

        passed_tests += tree._num_nodes(tree.root) == 13

        root.children.pop()

        passed_tests += tree._num_nodes(tree.root) == 9
        root.children[0].children.pop()
        root.children[0].children.pop()
        root.children[0].children.pop()

        passed_tests += tree._num_nodes(tree.root) == 6

    except Exception as ex:
        print("[Problem 12] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 12]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ---------- _num_nodes tests ----------
    passed_tests = 0
    num_tests = 10

    try:

        for i in range(4):
            max_num_keys = (i + 3) * 2 - 1
            root = BTreeNode(keys=[i for i in range(max_num_keys)], children=[], is_leaf=True, max_num_keys=max_num_keys)
            tree = BTree(max_num_keys=max_num_keys)
            tree.root = root
            passed_tests += tree._sum_at_depth (0, tree.root) == max_num_keys * (max_num_keys - 1) // 2

        passed_tests += tree._sum_at_depth(1, tree.root) == 0

        root.is_leaf = False

        for i in range(2):
            root.children = []

            max_num_keys = (i + 3) * 2 - 1
            root.max_num_keys = max_num_keys

            root.keys = [i for i in range(max_num_keys, 2 * max_num_keys)]

            for j in range(max_num_keys):
                node = BTreeNode(keys=[i for i in range(max_num_keys)], children=[], is_leaf=True, max_num_keys=max_num_keys)
                root.children.append(node)

            if i == 0:
                passed_tests += tree._sum_at_depth(0, tree.root) == 35
                passed_tests += tree._sum_at_depth(1, tree.root) == 50
            else:
                passed_tests += tree._sum_at_depth(0, tree.root) == 70
                passed_tests += tree._sum_at_depth(1, tree.root) == 147

        passed_tests += tree._sum_at_depth(2, tree.root) == 0

    except Exception as ex:
        print("[Problem 13] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 13]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ---------- _contains tests ----------
    passed_tests = 0
    num_tests = 8

    try:
        max_num_keys = 3
        root = BTreeNode(keys=[10,20,30], children=[], is_leaf=False, max_num_keys=max_num_keys)
        tree = BTree(max_num_keys=max_num_keys)
        tree.root = root

        root.children.append(BTreeNode(keys=[25,80,100], children=[], is_leaf=True, max_num_keys=max_num_keys))
        root.children.append(BTreeNode(keys=[12, 15, 18], children=[], is_leaf=True, max_num_keys=max_num_keys))
        root.children.append(BTreeNode(keys=[12, 15, 18], children=[], is_leaf=True, max_num_keys=max_num_keys))
        root.children.append(BTreeNode(keys=[40, 50, 60], children=[], is_leaf=True, max_num_keys=max_num_keys))

        passed_tests += tree._contains(20, tree.root)
        passed_tests += not tree._contains(25, tree.root)
        passed_tests += tree._contains(60, tree.root)
        passed_tests += not tree._contains(80, tree.root)
        passed_tests += tree._contains(20, tree.root)
        passed_tests += not tree._contains(-1, tree.root)
        passed_tests += tree._contains(40, tree.root)
        passed_tests += not tree._contains(100, tree.root)

    except Exception as ex:
        print("[Problem 14] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 14]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    return section_points


def grade_s4(answer_list_points):
    print("\n-- Section 4 --")

    section_points = 0

    # ---------- insert tests ----------
    passed_tests = 0
    num_tests = 10

    try:
        ht1 = HashTable(5)
        ht2 = HashTable(7)

        for i in range(10,15 * 2, 4):
            ht1.insert(i)
            ht2.insert(i)
            passed_tests += i in ht1.table[i % 5]
            passed_tests += i in ht2.table[i % 7]

    except Exception as ex:
        print("[Problem 15] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 15]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ---------- search tests ----------
    passed_tests = 0
    num_tests = 14

    try:
        ht1 = HashTable(5)
        ht2 = HashTable(7)

        for i in range(10,15 * 2, 4):
            ht1.table[i % 5].append(i)
            ht2.table[i % 7].append(i)

            passed_tests += ht1.search(i) == ht1.table[i % 5]
            passed_tests += ht2.search(i) == ht2.table[i % 7]

        for i in range(11, 13):
            passed_tests += ht1.search(i) is None
            passed_tests += ht2.search(i) is None

    except Exception as ex:
        print("[Problem 16] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 16]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ---------- min_key tests ----------
    passed_tests = 0
    num_tests = 12

    try:
        ht1 = HashTable(3)
        ht2 = HashTable(11)

        for i in range(10, 15):
            ht1.table[i % 3].append(i)
            ht2.table[i % 11].append(i)

            passed_tests += ht1.min_key() == i - i % 2
            passed_tests += ht2.min_key() == i - i % 2

            if i % 2 == 1:
                ht1 = HashTable(3)
                ht2 = HashTable(11)

        ht1 = HashTable(3)
        ht2 = HashTable(11)

        passed_tests += ht1.min_key() == math.inf
        passed_tests += ht2.min_key() == math.inf

    except Exception as ex:
        print("[Problem 17] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 17]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ---------- load_factor tests ----------
    passed_tests = 0
    num_tests = 8

    try:
        ht1 = HashTable(3)
        ht2 = HashTable(11)

        stack = [3.272727272727273, 12.0, 2.0,7.333333333333333,0.9090909090909091,3.3333333333333335]
        for i in range(10, 15, 2):
            for j in range(i):
                ht1.table[i % 3].append(j)
                ht2.table[i % 11].append(j)

            passed_tests += abs(ht1.load_factor() - stack.pop()) < 0.001
            passed_tests += abs(ht2.load_factor() - stack.pop()) < 0.001

            if i % 2 == 1:
                ht1 = HashTable(3)
                ht2 = HashTable(11)

        ht1 = HashTable(3)
        ht2 = HashTable(11)

        passed_tests += ht1.load_factor() == 0
        passed_tests += ht2.load_factor() == 0

    except Exception as ex:
        print("[Problem 18] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 18]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    return section_points


def grade_s5(answer_list_points):
    print("\n-- Section 5 --")

    section_points = 0

    # ---------- max_grandpa_gap tests ----------
    passed_tests = 0
    num_tests = 12

    try:
        heap = MaxHeap()

        heap.tree = [60,40,50,10,23]
        stack = [3,12,20,28,36,45,53,61,69]
        stack = stack[::-1]
        passed_tests += heap.max_grandpa_gap() == 50

        for i in range(9):
            j = 10 * i + i + 4

            heap.tree = range(j, 0, -1)

            passed_tests += heap.max_grandpa_gap() == stack.pop()
        heap = MaxHeap()
        passed_tests += heap.max_grandpa_gap() == -math.inf
        heap.tree = [50, 11, 23]
        passed_tests += heap.max_grandpa_gap() == -math.inf

    except Exception as ex:
        print("[Problem 19] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 19]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ---------- is_valid tests ----------
    passed_tests = 0
    num_tests = 13

    try:
        heap = MaxHeap()

        passed_tests += heap.is_valid()

        for i in range(6):
            j = 10 * i + i + 4
            heap.tree = list(range(j, 0, -1))
            passed_tests += heap.is_valid()

        for i in range(6):
            j = 10 * i + i + 4

            heap.tree = list(range(j, 0, -1))

            heap.tree[j // 2] = heap.tree[(j // 2 - 1) // 2] + 2

            passed_tests += not heap.is_valid()

    except Exception as ex:
        print("[Problem 20] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 20]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ---------- try_replace tests ----------
    passed_tests = 0
    num_tests = 8

    try:
        heap = MaxHeap()
        heap.tree = list(range(50, 0, -10))
        heap.try_replace(0, 60)
        passed_tests += heap.tree[1:] == list(range(40, 0, -10)) and heap.tree[0] == 60
        heap.tree = list(range(50, 0, -10))
        heap.try_replace(len(heap.tree) - 1, 0)
        passed_tests += heap.tree[:len(heap.tree) - 1] == list(range(50, 10, -10)) and heap.tree[-1] == 0

        heap.tree = list(range(50, 0, -10))
        heap.try_replace(0, 1)
        passed_tests += heap.tree == list(range(50, 0, -10))
        heap.tree = list(range(50, 0, -10))
        heap.try_replace(len(heap.tree) - 1, 100)
        passed_tests += heap.tree == list(range(50, 0, -10))

        heap.tree = list(range(50, 0, -10))
        heap.try_replace(1, 45)
        l = list(range(50, 0, -10))
        l[1] = 45
        passed_tests += heap.tree == l

        heap.tree = list(range(50, 0, -5))
        l = list(range(50, 0, -5 ))
        heap.try_replace(2, 1)
        passed_tests += heap.tree == l

        heap = MaxHeap()
        heap.try_replace(2, 1)
        passed_tests += len(heap.tree) == 0

        heap.tree = list(range(50, 0, -10))
        l = list(range(50, 0, -10))
        heap.try_replace(len(heap.tree ), -100000)
        passed_tests += heap.tree == l

    except Exception as ex:
        print("[Problem 21] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 21]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ---------- create_path tests ----------
    passed_tests = 0
    num_tests = 11

    try:
        heap = MaxHeap()

        stack = [
            [2, 4],
            [1, 3, 4],
            [3, 4],
            [8, 12, 14, 15],
            [2, 9, 13, 15],
            [12, 14, 15],
            [13, 20, 24, 26],
            [3, 15, 21, 24, 26],
            [20, 24, 26],
            [26]
        ]
        stack.reverse()
        for i in range(3):
            j = 10 * i + i + 4

            heap.tree = list(range(j, 0, -1))

            passed_tests += heap.create_path(j // 2) == stack.pop()

            passed_tests += heap.create_path(len(heap.tree) - i - 1) == stack.pop()

            passed_tests += heap.create_path(j // 4) == stack.pop()

        passed_tests += len(heap.create_path(0)) == 1 and heap.create_path(0) == [26]
        passed_tests += heap.create_path(1000000) == []

    except Exception as ex:
        print("[Problem 22] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * CODING_POINTS

    print("[Problem 22]", problem_points, "/", CODING_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    return section_points


def main():
    total_points = 0

    answer_list_points = []

    s1_points = grade_s1(answer_list_points)
    s2_points = grade_s2(answer_list_points)
    s3_points = grade_s3(answer_list_points)
    s4_points = grade_s4(answer_list_points)
    s5_points = grade_s5(answer_list_points)
    s0_points = grade_s0(answer_list_points)

    total_points += s0_points
    total_points += s1_points
    total_points += s2_points
    total_points += s3_points
    total_points += s4_points
    total_points += s5_points

    print("\n-- Final Results --")

    print("-----------------------")
    print("Section 0 Grade: ", s0_points)
    print("Section 1 Grade: ", s1_points)
    print("Section 2 Grade: ", s2_points)
    print("Section 3 Grade: ", s3_points)
    print("Section 4 Grade: ", s4_points)
    print("Section 5 Grade: ", s5_points)
    print("-----------------------")
    print()
    print("Exam 2 Grade: ", total_points)




if __name__ == "__main__":
    main()
