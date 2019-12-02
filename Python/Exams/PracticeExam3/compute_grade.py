from Python.Exams.PracticeExam3.s1_tracing import TracingSection
from Python.Exams.PracticeExam3.s2_multiple_choice import MultipleChoiceSection
from Python.Exams.PracticeExam3.s3_graph_al import GraphAL
from Python.Exams.PracticeExam3.s4_graph_am import GraphAM
from Python.Exams.PracticeExam3.s5_dsf import DisjointSetForest

import sys

points_type1_problem = 5
points_type2_problem = 8
points_type3_problem = 3
points_type4_problem = 6
points_extra_credit = 2


def grade_section1():  # 28

    points = 0

    ans_p1 = TracingSection.get_problem_1_answer()

    if ans_p1 == 1234:
        points += points_type1_problem

    ans_p2 = TracingSection.get_problem_2_answer()

    if ans_p2 == 1234:
        points += points_type1_problem

    ans_p3 = TracingSection.get_problem_3_answer()

    if ans_p3 == 1234:
        points += points_type1_problem

    ans_p4 = TracingSection.get_problem_4_answer()

    if ans_p4 == 1234:
        points += points_type2_problem

    ans_p5 = TracingSection.get_problem_5_answer()

    if ans_p5 == 1234:
        points += points_type1_problem

    return points


def grade_section2():  # 27
    points = 0

    ans_p6 = MultipleChoiceSection.get_problem_6_answer()

    if ans_p6 == 1234:
        points += points_type1_problem

    ans_p7 = MultipleChoiceSection.get_problem_7_answer()

    if ans_p7 == 1234:
        points += points_type1_problem

    ans_p8 = MultipleChoiceSection.get_problem_8_answer()

    if ans_p8 == 1234:
        points += points_type3_problem

    ans_p9 = MultipleChoiceSection.get_problem_9_answer()

    if ans_p9 == 1234:
        points += points_type3_problem

    ans_p10 = MultipleChoiceSection.get_problem_10_answer()

    if ans_p10 == 1234:
        points += points_type3_problem

    ans_p11 = MultipleChoiceSection.get_problem_11_answer()

    if ans_p11 == 1234:
        points += points_type3_problem

    ans_p12 = MultipleChoiceSection.get_problem_12_answer()

    if ans_p12 == 1234:
        points += points_type3_problem

    ans_p13 = MultipleChoiceSection.get_problem_13_answer()

    if ans_p13 == 1234:
        points += points_type3_problem

    ans_p14 = MultipleChoiceSection.get_problem_14_answer()

    if ans_p14 == 1234:
        points += points_type1_problem

    return points


def grade_section3():
    points = 0

    # ------------- Problem 15 cholo tests -------------
    # Use actual unit tests in practice, no this guys!
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

        if graph.is_there_an_edge(5, 8) and not graph.is_there_an_edge(5, 7) and not graph.is_there_an_edge(0,
                                                                                                            4) and graph.is_there_an_edge(
                0, 2):
            points += points_type1_problem
            print("Problem 15: Correct")
        else:
            print("Problem 15: Incorrect")
    except Exception as ex:
        print("Error in Problem 15: ", ex)
        print("Problem 15: Incorrect")

    # ------------- Problem 16 cholo tests -------------
    # Use actual unit tests in practice, no this guys!
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

        if graph.compute_out_degree(0) == 3 and graph.compute_out_degree(10) == 0 and \
                graph.compute_out_degree(11) == 0 and graph.compute_out_degree(8) == 1:
            points += points_type1_problem
            print("Problem 16: Correct")
        else:
            print("Problem 16: Incorrect")

    except Exception as ex:
        print("Error in Problem 16: ", ex)
        print("Problem 16: Incorrect")

    # ------------- Problem 17 cholo tests -------------
    # Use actual unit tests in practice, no this guys!
    try:
        graph = GraphAL(vertices=20, directed=True)

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

        if not graph.is_isolated(1) and not graph.is_isolated(10) and graph.is_isolated(11) and graph.is_isolated(17):
            points += points_type4_problem
            print("Problem 17: Correct")
        else:
            print("Problem 17: Incorrect")

    except Exception as ex:
        print("Error in Problem 17: ", ex)
        print("Problem 17: Incorrect")

    # ------------- Problem 18 cholo tests -------------
    # Use actual unit tests in practice, no this guys!
    try:
        graph1 = GraphAL.create_backward_circle_graph(5)

        graph2 = GraphAL.create_backward_circle_graph(3)

        graph3 = GraphAL.create_backward_circle_graph(4)

        graph1test = GraphAL(vertices=5, directed=True)
        graph1test.insert_edge(1, 0)
        graph1test.insert_edge(2, 1)
        graph1test.insert_edge(3, 2)
        graph1test.insert_edge(4, 3)
        graph1test.insert_edge(0, 4)

        graph2test = GraphAL(vertices=3, directed=True)
        graph2test.insert_edge(1, 0)
        graph2test.insert_edge(2, 1)
        graph2test.insert_edge(0, 2)

        graph3test = GraphAL(vertices=4, directed=True)
        graph3test.insert_edge(1, 0)
        graph3test.insert_edge(2, 1)
        graph3test.insert_edge(3, 2)
        graph3test.insert_edge(0, 3)

        if graph1.is_identical(graph1test) and graph2.is_identical(graph2test) and graph3.is_identical(graph3test):
            points += points_type2_problem
            print("Problem 18: Correct")
        else:
            print("Problem 18: Incorrect")

    except Exception as ex:
        print("Error in Problem 18: ", ex)
        print("Problem 18: Incorrect")

    return points


def grade_section4():
    points = 0

    # ------------- Problem 19 cholo tests -------------
    # Use actual unit tests in practice, no this guys!

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

        if graph.is_there_an_edge(5, 8) and not graph.is_there_an_edge(5, 7) and not graph.is_there_an_edge(0,
                                                                                                            4) and graph.is_there_an_edge(
            0, 2):
            points += points_type1_problem
            print("Problem 19: Correct")
        else:
            print("Problem 19: Incorrect")
    except Exception as ex:
        print("Error in Problem 19: ", ex)
        print("Problem 19: Incorrect")

    # ------------- Problem 20 cholo tests -------------
    # Use actual unit tests in practice, no this guys!

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

        if graph.compute_out_degree(0) == 3 and graph.compute_out_degree(10) == 0 and \
                graph.compute_out_degree(11) == 0 and graph.compute_out_degree(8) == 1:
            points += points_type1_problem
            print("Problem 20: Correct")
        else:
            print("Problem 20: Incorrect")
    except Exception as ex:
        print("Error in Problem 20: ", ex)
        print("Problem 20: Incorrect")

    # ------------- Problem 21 cholo tests -------------
    # Use actual unit tests in practice, no this guys!

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

        if not graph.is_isolated(1) and not graph.is_isolated(10) and graph.is_isolated(11):
            points += points_type4_problem
            print("Problem 21: Correct")
        else:
            print("Problem 21: Incorrect")
    except Exception as ex:
        print("Error in Problem 21: ", ex)
        print("Problem 21: Incorrect")

    # ------------- Problem 22 cholo tests -------------
    # Use actual unit tests in practice, no this guys!

    try:
        graph1 = GraphAM.create_backward_circle_graph(5)

        graph2 = GraphAM.create_backward_circle_graph(3)

        graph3 = GraphAM.create_backward_circle_graph(4)

        graph1test = GraphAM(vertices=5, directed=True)
        graph1test.insert_edge(1, 0)
        graph1test.insert_edge(2, 1)
        graph1test.insert_edge(3, 2)
        graph1test.insert_edge(4, 3)
        graph1test.insert_edge(0, 4)

        graph2test = GraphAM(vertices=3, directed=True)
        graph2test.insert_edge(1, 0)
        graph2test.insert_edge(2, 1)
        graph2test.insert_edge(0, 2)

        graph3test = GraphAM(vertices=4, directed=True)
        graph3test.insert_edge(1, 0)
        graph3test.insert_edge(2, 1)
        graph3test.insert_edge(3, 2)
        graph3test.insert_edge(0, 3)

        if graph1.is_identical(graph1test) and graph2.is_identical(graph2test) and graph3.is_identical(graph3test):
            points += points_type2_problem
            print("Problem 22: Correct")
        else:
            print("Problem 22: Incorrect")
    except Exception as ex:
        print("Error in Problem 22: ", ex)
        print("Problem 22: Incorrect")

    return points


def grade_section5():
    points = 0

    # ------------- Problem 23 cholo tests -------------
    # Use actual unit tests in practice, no this guys!

    try:
        dsf1 = DisjointSetForest(10)
        dsf2 = DisjointSetForest(8)

        dsf1.dsf[0] = 1
        dsf1.dsf[2] = 3
        dsf1.dsf[9] = 1

        if dsf1.get_num_sets() == 7 and dsf2.get_num_sets() == 8:
            points += points_type1_problem
            print("Problem 23: Correct")
        else:
            print("Problem 23: Incorrect")
    except Exception as ex:
        print("Error in Problem 23: ", ex)
        print("Problem 23: Incorrect")

    # ------------- Problem 24 cholo tests -------------
    # Use actual unit tests in practice, no this guys!

    try:
        dsf1 = DisjointSetForest.create_dsf(8)
        dsf2 = DisjointSetForest.create_dsf(12)

        if dsf1 == [-1, 0, -1, 2, -1, 4, -1, 6] and dsf2 == [-1, 0, -1, 2, -1, 4, -1, 6, -1, 8, -1, 10]:
            points += points_type1_problem
            print("Problem 24: Correct")
        else:
            print("Problem 24: Incorrect")
    except Exception as ex:
        print("Error in Problem 24: ", ex)
        print("Problem 24: Incorrect")

    return points


def main():
    grade = 0

    grade += grade_section1()

    grade += grade_section2()

    grade += grade_section3()

    grade += grade_section4()

    grade += grade_section5()

    print("Your grade is (not counting the first 2 sections): ", grade)


if __name__ == "__main__":
    main()
