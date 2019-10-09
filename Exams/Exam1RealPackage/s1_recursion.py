class Section1:

    # Provide an implementation for the count_even method. This method receives a non-negative int n and returns
    # the number of digits in n that are even (zero is an even number) - Use recursion - no loops.
    #
    # Example1: count_even(285) -> 2
    # Example2: count_even (565891) -> 2
    # Example3: count_even (2468) -> 4
    # Example4: count_even (1357) -> 0
    # Example5: count_even (130570) -> 2

    @staticmethod
    def count_even(n):  # To make a recursive call, do this: Section1.count_even( ... )
        if n < 10:
            if n % 2 == 0:
                return 1
            else:
                return 0

        number = n % 10

        if number % 2 == 0:
            return 1 + Section1.count_even(n // 10)
        else:
            return Section1.count_even(n // 10)

        return 0


def main():
    counter = 0
    print("Hello")

    for i in range(2, 5):
        print(i)

    test_result = Section1.count_even(1273)

    print("test_result = ", test_result)


if __name__ == "__main__":
    main()
