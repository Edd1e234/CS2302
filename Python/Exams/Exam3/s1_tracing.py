class TracingSection:
    name = 'Eduardo Garcia'
    utep_id = "88785135"
    class_secret = "xfx7"

    @staticmethod
    def get_problem_1_answer():
        sort_result = [0, 5, 1, 2, 4, 3]  # <- Replace the contents of the
        # array with your answer

        return sort_result

    @staticmethod
    def get_problem_2_answer():
        visited_array = [0, 1, 4, 2, 3, 5]  # <- Replace the contents of the
        # array with your answer
        return visited_array

    @staticmethod
    def get_problem_3_answer():
        visited_array = [0, 4, 1, 2, 5, 3]  # <- Replace the contents of the
        # array with your answer
        return visited_array

    @staticmethod
    def get_problem_4_answer():
        dist = [1, 0, 3, 4, 1]
        path = [1, 0, 0, 2, 1]

        return dist, path

    @staticmethod
    def get_problem_5_answer():
        solution = [
            # ' H  A  P
            [0, 1, 2, 3],  # '
            [1, 1, 1, 2],  # A
            [2, 2, 2, 1],  # P
            [3, 3, 3, 2],  # P
        ]

        return solution
