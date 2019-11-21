def two_sum(arr, target):
    hash_set = set()

    for i in arr:
        hash_set.add(i)

    for i in range(len(arr)):
        target_sum = target - arr[i]
        print(target_sum)
        if target_sum in hash_set and target_sum is not arr[i]:
            return target_sum, arr[i]


def repeated_number(arr):
    hash_set = set()
    for i in arr:
        hash_set.add(i)

    # I read online that a set only contains one copy of the element.
    # So if the element is in there, and you remove,
    # the second copy would not be in the set. Thus you found your
    # duplicate.
    for i in range(len(arr)):
        if arr[i] in hash_set:
            hash_set.remove(arr[i])
        else:
            return arr[i]


def most_common_word(str_):
    words = str_.split(" ")
    hast_map = dict()

    for i in words:
        if i not in hast_map:
            hast_map[i] = 0
        else:
            value = hast_map[i]
            value += 1
            hast_map[i] += value

    max_value = 0
    word = None

    for i in words:
        values = hast_map.get(i)
        if values >= max_value:
            max_value = values
            word = i
    return word


def single_number(arr):
    hash_map = dict()

    for i in arr:
        if i not in hash_map:
            print(i)
            hash_map[i] = 1
        else:
            value = hash_map[i]
            value += 1
            hash_map[i] = value

    for i in arr:
        if hash_map[i] is 1:
            return i


def main():
    print("Two Sums: ", two_sum([2, 7, 11, 15], 9))
    print("Repeated Number", repeated_number([3, 4, 6, 1, 3, 10, -1]))
    print("Most common Word",
          most_common_word("hello world hello hello world hi"))
    print("Single Number", single_number([2, 2, 1]))
    print("Works")


main()
