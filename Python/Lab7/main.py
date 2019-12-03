# Created by Eddie Garcia at 11/28/19

# Main/ Edit Distance implementation.
# Testing/debugging.
import math


# Utility function to print 2D array.
def print_2D(words):
    string = "[\n"
    for left in range(len(words)):
        string += "\t[ "
        for right in range(len(words[left])):
            string += str(words[left][right]) + ", "
        string += "]\n"
    string += "]"
    print(string)


def get_left_top_corner(words, left, right):
    """
    Returns the values of the top, left and right cells, the corresponding
    value is given by the index's 'left' and 'right'. This function expects
    for the 2D array or 'words' to be filled with ints. If the given indexs
    correspond to either top, left, or right values being out of bounds the
    they will return 'math.inf'.
    :param right:
    :param left:
    :param words: 2D array of ints.
    """
    try:
        left_side = words[left - 1][right]
        if left < 0:
            left_side = math.inf
    except IndexError:
        left_side = math.inf
    try:
        top = words[left][right - 1]
        if right < 0:
            top = math.inf
    except IndexError:
        top = math.inf
    try:
        corner = words[left - 1][right - 1]
        if left < 0 and right < 0:
            corner = math.inf
    except IndexError:
        corner = math.inf

    # Debugging statement.
    if left_side == -math.inf and top == -math.inf and corner == -math.inf:
        print("Something HAS GONE WRONG.")
        print("Left Index", left_side)
        print("Right Index", right)
        return None
    return left_side, top, corner


def check_values(s1, s2):
    if s1 is None or s2 is None:
        print("Cannot take None Values. ")
        return True
    if not isinstance(s1, str) or not isinstance(s2, str):
        print("Need to String data types.")
        return True
    return False


def edit_distance(s1, s2):
    """
    Just to clarify we're transforming s1 -> s2.
    Finds the distance between s1 and s2.
    :param s1: First str to compare.
    :param s2: Second str to compare.
    :return: int, this is the total distance.
    """
    if check_values(s1, s2):
        return None

    # Building the array.
    words = build_2d_array(len(s1) + 1, len(s2) + 1)

    # Should set the outside index.
    for x in range(1, len(words)):
        for y in range(1, len(words[x])):
            left_side, top, corner = get_left_top_corner(words, x, y)
            if s1[x - 1] == s2[y - 1]:
                words[x][y] = corner
            else:
                words[x][y] = min(left_side, top, corner) + 1

    # Returning words for testing purposes.
    return words[len(s1) - 1][len(s2) - 1], words


def build_2d_array(x_size, y_size):
    words = []
    x_counter = 0
    y_counter = 1

    # Each cell in the 2D array needs to be unique, if done the short way
    # then values will repeat.
    # Also added 1, 2, 3... to the top row and left most column.
    for i in range(x_size):
        y_list = []
        for y in range(y_size):
            if i == 0:
                y_list.append(x_counter)
                x_counter += 1
            elif y == 0:
                y_list.append(y_counter)
                y_counter += 1
            else:
                y_list.append(math.inf)

        words.append(y_list)
    return words


def main():
    print_2D(build_2d_array(2, 2))


main()
