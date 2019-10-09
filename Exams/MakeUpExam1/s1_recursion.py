class Section1:

    @staticmethod
    def change_x_y(s):  # To make a recursive call, do this: Section1.change_x_y( ... )

        return ""


def main():
    test_result = Section1.change_x_y("codex")

    print("test_result = ", test_result)


if __name__ == "__main__":
    main()
