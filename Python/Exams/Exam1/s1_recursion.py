class Section1:

    # Given a non-negative int n, return the number
    # of digits in n that are less than or equal
    # to 5 - Use recursion - no loops.

    # Example1: count(285) -> 2
    # Example2: count(565891) -> 3

    @staticmethod
    def count(n):
        if n < 10:
            if n <= 5:
                return 1
            else:
                return 0

        number = n % 10
        if number <= 5:
            return 1 + Section1.count(n // 10)
        else:
            return Section1.count(n // 10)


def main():
    test_result = Section1.count(601850)

    print("test_result = ", test_result)


if __name__ == "__main__":
    main()
