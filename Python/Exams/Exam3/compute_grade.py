from Python.Exams.Exam3.s0_name_and_id import Section0
from Python.Exams.Exam3.s1_tracing import TracingSection
from Python.Exams.Exam3.s2_multiple_choice import MultipleChoiceSection
from Python.Exams.Exam3.s3_graph_al import GraphAL
from Python.Exams.Exam3.s4_graph_am import GraphAM
from Python.Exams.Exam3.s5_dsf import DisjointSetForest

import sys

TYPE1_POINTS = 3.0
TYPE2_POINTS = 5.0
TYPE3_POINTS = 7.0
TYPE4_POINTS = 9.0
EXTRA_CREDIT_POINTS = 2.0


def get_vector_similarity(v1, v2):
    count = 0

    try:
        for i in range(len(v1)):
            if v1[i] == v2[i]:
                count += 1
    except:
        print("Irregular 1D array answer")

    return count / len(v1)


def get_matrix_similarity(m1, m2):
    count = 0

    num_rows = len(m1)
    num_cols = len(m1[0])

    try:
        for i in range(num_rows):
            for j in range(num_cols):
                if m1[i][j] == m2[i][j]:
                    count += 1
    except:
        print("Irregular 2D array answer")

    return count / (num_rows * num_cols)


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

    ans_p1 = TracingSection.get_problem_1_answer()

    problem_points = get_vector_similarity([0, 5, 1, 2, 4, 3], ans_p1) * TYPE2_POINTS

    print("[Problem 1]", problem_points, "/", TYPE2_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    ans_p2 = TracingSection.get_problem_2_answer()

    problem_points = get_vector_similarity([0, 1, 4, 2, 3, 5], ans_p2) * TYPE2_POINTS

    print("[Problem 2]", problem_points, "/", TYPE2_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    ans_p3 = TracingSection.get_problem_3_answer()

    problem_points = get_vector_similarity([0, 4, 1, 2, 5, 3], ans_p3) * TYPE2_POINTS

    print("[Problem 3]", problem_points, "/", TYPE2_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    dist, path = TracingSection.get_problem_4_answer()

    problem_points = get_vector_similarity([1, 0, 3, 4, 1], dist) * TYPE2_POINTS / 2

    problem_points += get_vector_similarity([1, -1, 0, 2, 1], path) * TYPE2_POINTS / 2

    print("[Problem 4]", problem_points, "/", TYPE2_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    ans_p5 = TracingSection.get_problem_5_answer()

    p5_solution = [
        # ' H  A  P
        [0, 1, 2, 3],  # '
        [1, 1, 1, 2],  # A
        [2, 2, 2, 1],  # P
        [3, 3, 3, 2],  # P

    ]

    problem_points = get_matrix_similarity(p5_solution, ans_p5) * TYPE2_POINTS

    print("[Problem 5]", problem_points, "/", TYPE2_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    return section_points


def grade_s2(answer_list_points):
    print("\n-- Section 2 --")

    section_points = 0

    problem_points = (MultipleChoiceSection.get_problem_6_answer() == 0) * TYPE2_POINTS
    answer_list_points.append(problem_points)
    section_points += problem_points
    print("[Problem 6]", problem_points, "/", TYPE2_POINTS)

    problem_points = (MultipleChoiceSection.get_problem_7_answer() == 3) * TYPE2_POINTS
    answer_list_points.append(problem_points)
    section_points += problem_points
    print("[Problem 7]", problem_points, "/", TYPE2_POINTS)

    problem_points = (MultipleChoiceSection.get_problem_8_answer() == 1) * TYPE1_POINTS
    answer_list_points.append(problem_points)
    section_points += problem_points
    print("[Problem 8]", problem_points, "/", TYPE1_POINTS)

    problem_points = (MultipleChoiceSection.get_problem_9_answer() == 2) * TYPE1_POINTS
    answer_list_points.append(problem_points)
    section_points += problem_points
    print("[Problem 9]", problem_points, "/", TYPE1_POINTS)

    problem_points = (MultipleChoiceSection.get_problem_10_answer() == 2) * TYPE1_POINTS
    answer_list_points.append(problem_points)
    section_points += problem_points
    print("[Problem 10]", problem_points, "/", TYPE1_POINTS)

    problem_points = (MultipleChoiceSection.get_problem_11_answer() == 2) * TYPE1_POINTS
    answer_list_points.append(problem_points)
    section_points += problem_points
    print("[Problem 11]", problem_points, "/", TYPE1_POINTS)

    problem_points = (MultipleChoiceSection.get_problem_12_answer() == 3) * TYPE1_POINTS
    answer_list_points.append(problem_points)
    section_points += problem_points
    print("[Problem 12]", problem_points, "/", TYPE1_POINTS)

    problem_points = (MultipleChoiceSection.get_problem_13_answer() == 2) * TYPE1_POINTS
    answer_list_points.append(problem_points)
    section_points += problem_points
    print("[Problem 13]", problem_points, "/", TYPE1_POINTS)

    # TODO - Fix this problem - 2 solutions? Maybe?
    problem_points = (MultipleChoiceSection.get_problem_14_answer() == 4 or
                      MultipleChoiceSection.get_problem_14_answer() == 5) * TYPE1_POINTS
    answer_list_points.append(problem_points)
    section_points += problem_points
    print("[Problem 14]", problem_points, "/", TYPE1_POINTS)

    return section_points


def grade_s3(answer_list_points):
    print("\n-- Section 3 --")

    section_points = 0

    # ------------- num_sets tests -------------

    passed_tests = 0
    num_tests = 3

    try:

        graph = GraphAL(vertices=11, directed=True)

        graph.insert_edge(0, 1)
        graph.insert_edge(0, 2)
        graph.insert_edge(0, 3)

        graph.insert_edge(1, 4)
        graph.insert_edge(2, 5)
        graph.insert_edge(3, 6)

        graph.insert_edge(4, 7)
        graph.insert_edge(5, 8)
        graph.insert_edge(6, 9)

        graph.insert_edge(7, 10)
        graph.insert_edge(8, 10)
        graph.insert_edge(9, 10)

        graph2 = GraphAL(vertices=10, directed=True)
        graph2.insert_edge(4, 7)

        graph3 = GraphAL(vertices=10, directed=True, weighted=True)
        for i in range(3):
            graph3.insert_edge(i, i + 1, i * 2 + 2)

        passed_tests += graph.num_edges() == 12
        passed_tests += graph2.num_edges() == 1
        passed_tests += graph3.num_edges() == 3

    except Exception as ex:
        print("[Problem 15] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * TYPE3_POINTS

    print("[Problem 15]", problem_points, "/", TYPE3_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ------------- compute_in_degree tests -------------
    passed_tests = 0
    num_tests = 5

    try:

        graph = GraphAL(vertices=11, directed=True)

        graph.insert_edge(0, 1)
        graph.insert_edge(0, 2)
        graph.insert_edge(0, 3)

        graph.insert_edge(1, 4)
        graph.insert_edge(2, 5)
        graph.insert_edge(3, 6)

        graph.insert_edge(4, 7)
        graph.insert_edge(5, 8)
        graph.insert_edge(6, 9)

        graph.insert_edge(7, 10)
        graph.insert_edge(8, 10)
        graph.insert_edge(9, 10)

        graph3 = GraphAL(vertices=10, directed=True, weighted=True)
        for i in range(5):
            graph3.insert_edge(i, i % 2, i * 2 + 2)

        passed_tests += graph.compute_in_degree(1) == 1
        passed_tests += graph.compute_in_degree(9) == 1
        passed_tests += graph.compute_in_degree(10) == 3

        passed_tests += graph3.compute_in_degree(0) == 3
        passed_tests += graph3.compute_in_degree(1) == 2

    except Exception as ex:
        print("[Problem 16] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * TYPE3_POINTS

    print("[Problem 16]", problem_points, "/", TYPE3_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ------------- num_isolated_vertices tests -------------
    passed_tests = 0
    num_tests = 3

    try:

        graph = GraphAL(vertices=12, directed=True)

        graph.insert_edge(0, 1)
        graph.insert_edge(0, 2)
        graph.insert_edge(0, 3)

        graph.insert_edge(1, 4)
        graph.insert_edge(2, 5)
        graph.insert_edge(3, 6)

        graph.insert_edge(4, 7)
        graph.insert_edge(5, 8)
        graph.insert_edge(6, 9)

        graph.insert_edge(7, 10)
        graph.insert_edge(8, 10)
        graph.insert_edge(9, 10)

        graph2 = GraphAL(vertices=5, directed=True)
        graph3 = GraphAL(vertices=10, directed=True, weighted=True)
        for i in range(3):
            graph3.insert_edge(i, i + 1, i * 2 + 2)

        passed_tests += graph.num_isolated_vertices() == 1
        passed_tests += graph2.num_isolated_vertices() == 5
        passed_tests += graph3.num_isolated_vertices() == 6

    except Exception as ex:
        print("[Problem 17] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * TYPE3_POINTS

    print("[Problem 17]", problem_points, "/", TYPE3_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ------------- highest_in_degree_vertex tests -------------
    passed_tests = 0
    num_tests = 3

    try:

        graph = GraphAL(vertices=11, directed=True)

        graph.insert_edge(0, 1)
        graph.insert_edge(0, 2)
        graph.insert_edge(0, 3)

        graph.insert_edge(1, 4)
        graph.insert_edge(2, 5)
        graph.insert_edge(3, 6)

        graph.insert_edge(4, 7)
        graph.insert_edge(5, 8)
        graph.insert_edge(6, 9)

        graph.insert_edge(7, 10)
        graph.insert_edge(8, 10)
        graph.insert_edge(9, 10)

        graph2 = GraphAL(vertices=11, directed=True)
        graph2.insert_edge(9, 4)

        graph3 = GraphAL(vertices=10, directed=True, weighted=True)
        for i in range(5):
            graph3.insert_edge(i, i % 2, i * 2 + 2)

        passed_tests += graph.highest_in_degree_vertex() == 10
        passed_tests += graph2.highest_in_degree_vertex() == 4
        passed_tests += graph3.highest_in_degree_vertex() == 0

    except Exception as ex:
        print("[Problem 18] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * TYPE3_POINTS

    print("[Problem 18]", problem_points, "/", TYPE3_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    return section_points


def grade_s4(answer_list_points):
    print("\n-- Section 4 --")

    section_points = 0

    # ------------- num_sets tests -------------

    passed_tests = 0
    num_tests = 3

    try:

        graph = GraphAM(vertices=11, directed=True)

        graph.insert_edge(0, 1)
        graph.insert_edge(0, 2)
        graph.insert_edge(0, 3)

        graph.insert_edge(1, 4)
        graph.insert_edge(2, 5)
        graph.insert_edge(3, 6)

        graph.insert_edge(4, 7)
        graph.insert_edge(5, 8)
        graph.insert_edge(6, 9)

        graph.insert_edge(7, 10)
        graph.insert_edge(8, 10)
        graph.insert_edge(9, 10)

        graph2 = GraphAM(vertices=10, directed=True)
        graph2.insert_edge(4, 7)

        graph3 = GraphAM(vertices=10, directed=True, weighted=True)
        for i in range(3):
            graph3.insert_edge(i, i + 1, i * 2 + 2)

        passed_tests += graph.num_edges() == 12
        passed_tests += graph2.num_edges() == 1
        passed_tests += graph3.num_edges() == 3

    except Exception as ex:
        print("[Problem 19] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * TYPE3_POINTS

    print("[Problem 19]", problem_points, "/", TYPE3_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ------------- compute_in_degree tests -------------
    passed_tests = 0
    num_tests = 5

    try:

        graph = GraphAM(vertices=11, directed=True)

        graph.insert_edge(0, 1)
        graph.insert_edge(0, 2)
        graph.insert_edge(0, 3)

        graph.insert_edge(1, 4)
        graph.insert_edge(2, 5)
        graph.insert_edge(3, 6)

        graph.insert_edge(4, 7)
        graph.insert_edge(5, 8)
        graph.insert_edge(6, 9)

        graph.insert_edge(7, 10)
        graph.insert_edge(8, 10)
        graph.insert_edge(9, 10)

        graph3 = GraphAM(vertices=10, directed=True, weighted=True)
        for i in range(5):
            graph3.insert_edge(i, i % 2, i * 2 + 2)

        passed_tests += graph.compute_in_degree(1) == 1
        passed_tests += graph.compute_in_degree(9) == 1
        passed_tests += graph.compute_in_degree(10) == 3
        passed_tests += graph3.compute_in_degree(0) == 3
        passed_tests += graph3.compute_in_degree(1) == 2

    except Exception as ex:
        print("[Problem 20] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * TYPE3_POINTS

    print("[Problem 20]", problem_points, "/", TYPE3_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ------------- num_isolated_vertices tests -------------
    passed_tests = 0
    num_tests = 3

    try:

        graph = GraphAM(vertices=12, directed=True)

        graph.insert_edge(0, 1)
        graph.insert_edge(0, 2)
        graph.insert_edge(0, 3)

        graph.insert_edge(1, 4)
        graph.insert_edge(2, 5)
        graph.insert_edge(3, 6)

        graph.insert_edge(4, 7)
        graph.insert_edge(5, 8)
        graph.insert_edge(6, 9)

        graph.insert_edge(7, 10)
        graph.insert_edge(8, 10)
        graph.insert_edge(9, 10)

        graph2 = GraphAM(vertices=5, directed=True)
        graph3 = GraphAM(vertices=10, directed=True, weighted=True)
        for i in range(3):
            graph3.insert_edge(i, i + 1, i * 2 + 2)

        passed_tests += graph.num_isolated_vertices() == 1
        passed_tests += graph2.num_isolated_vertices() == 5
        passed_tests += graph3.num_isolated_vertices() == 6

    except Exception as ex:
        print("[Problem 21] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * TYPE3_POINTS

    print("[Problem 21]", problem_points, "/", TYPE3_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ------------- highest_in_degree_vertex tests -------------
    passed_tests = 0
    num_tests = 3

    try:

        graph = GraphAM(vertices=11, directed=True)

        graph.insert_edge(0, 1)
        graph.insert_edge(0, 2)
        graph.insert_edge(0, 3)

        graph.insert_edge(1, 4)
        graph.insert_edge(2, 5)
        graph.insert_edge(3, 6)

        graph.insert_edge(4, 7)
        graph.insert_edge(5, 8)
        graph.insert_edge(6, 9)

        graph.insert_edge(7, 10)
        graph.insert_edge(8, 10)
        graph.insert_edge(9, 10)

        graph2 = GraphAM(vertices=11, directed=True)
        graph2.insert_edge(9, 4)

        graph3 = GraphAM(vertices=10, directed=True, weighted=True)
        for i in range(5):
            graph3.insert_edge(i, i % 2, i * 2 + 2)

        passed_tests += graph.highest_in_degree_vertex() == 10
        passed_tests += graph2.highest_in_degree_vertex() == 4
        passed_tests += graph3.highest_in_degree_vertex() == 0

    except Exception as ex:
        print("[Problem 22] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * TYPE3_POINTS

    print("[Problem 22]", problem_points, "/", TYPE3_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    return section_points


def grade_s5(answer_list_points):
    print("\n-- Section 5 --")

    section_points = 0

    # ------------- get_num_sets tests -------------
    passed_tests = 0
    num_tests = 3

    try:
        dsf1 = DisjointSetForest(10)
        dsf2 = DisjointSetForest(8)

        dsf1.dsf[0] = 1
        dsf1.dsf[2] = 3
        dsf1.dsf[9] = 1

        dsf2.dsf[4] = 2
        dsf2.dsf[5] = 2

        dsf2.dsf[0] = 1
        dsf2.dsf[1] = 2

        dsf3 = DisjointSetForest(5)

        passed_tests += dsf1.get_num_sets() == 7
        passed_tests += dsf2.get_num_sets() == 4
        passed_tests += dsf3.get_num_sets() == 5

    except Exception as ex:
        print("[Problem 23] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * TYPE2_POINTS

    print("[Problem 23]", problem_points, "/", TYPE2_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ------------- group_singletons tests -------------
    passed_tests = 0
    num_tests = 3

    try:
        dsf1 = DisjointSetForest(10)
        dsf2 = DisjointSetForest(8)

        dsf1.dsf[0] = 1
        dsf1.dsf[2] = 3
        dsf1.dsf[9] = 1

        dsf2.dsf[4] = 2
        dsf2.dsf[5] = 2

        dsf2.dsf[0] = 1
        dsf2.dsf[1] = 2

        dsf3 = DisjointSetForest(4)

        dsf1.group_singletons()
        dsf2.group_singletons()
        dsf3.group_singletons()

        passed_tests += dsf1.find(3) != dsf1.find(4) and dsf1.find(5) == dsf1.find(6) and \
                        dsf1.find(4) == dsf1.find(5) and dsf1.find(7) == dsf1.find(8) and \
                        dsf1.find(4) == dsf1.find(8) and dsf1.find(1) == dsf1.find(9) and \
                        dsf1.find(0) != dsf1.find(5) and dsf1.find(2) == dsf1.find(3)

        passed_tests += dsf2.find(3) == dsf2.find(6) and dsf2.find(6) == dsf2.find(7) and \
                        dsf2.find(3) == dsf2.find(7) and dsf2.find(1) == dsf2.find(0) and \
                        dsf2.find(4) == dsf2.find(5) and dsf2.find(2) != dsf2.find(3) and \
                        dsf2.find(0) != dsf2.find(6) and dsf2.find(4) != dsf2.find(7)

        passed_tests += dsf3.find(0) == dsf3.find(1) and dsf3.find(1) == dsf3.find(2) and \
                        dsf3.find(2) == dsf3.find(3)

    except Exception as ex:
        print("[Problem 24] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * TYPE4_POINTS

    print("[Problem 24]", problem_points, "/", TYPE4_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ------------- is_compressed tests -------------
    passed_tests = 0
    num_tests = 1

    try:

        dsf1 = DisjointSetForest(10)
        dsf2 = DisjointSetForest(8)

        dsf1.dsf[0] = 2
        dsf1.dsf[2] = 3
        dsf1.dsf[9] = 1

        dsf2.dsf[0] = 1
        dsf2.dsf[2] = 3
        dsf2.dsf[4] = 5

        passed_tests = not dsf1.is_compressed() and dsf2.is_compressed()

    except Exception as ex:
        print("[Problem 25] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * TYPE3_POINTS

    print("[Problem 25]", problem_points, "/", TYPE3_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    # ------------- create_dsf tests -------------
    passed_tests = 0
    num_tests = 3

    try:

        dsf1 = DisjointSetForest.create_dsf(4, 1)
        dsf2 = DisjointSetForest.create_dsf(5, 0)
        dsf3 = DisjointSetForest.create_dsf(6, 5)

        passed_tests += dsf1 == [1, -1, 1, 1]
        passed_tests += dsf2 == [-1, 0, 0, 0, 0]
        passed_tests += dsf3 == [5, 5, 5, 5, 5, -1]

    except Exception as ex:
        print("[Problem 26] Exception thrown: ", ex)

    problem_points = (passed_tests / num_tests) * TYPE3_POINTS

    print("[Problem 26]", problem_points, "/", TYPE3_POINTS)

    section_points += problem_points
    answer_list_points.append(problem_points)

    return section_points


def main():
    total_points = 0

    answer_list_points = []

    s0_points = grade_s0(answer_list_points)
    s1_points = grade_s1(answer_list_points)
    s2_points = grade_s2(answer_list_points)
    s3_points = grade_s3(answer_list_points)
    s4_points = grade_s4(answer_list_points)
    s5_points = grade_s5(answer_list_points)

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
    print("Exam 3 Grade: ", total_points)

    print(len(answer_list_points))
if __name__ == "__main__":
    main()
