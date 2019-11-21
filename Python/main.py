# This main will be use as workspace for quick tests and for review.

def two_sum(nums, target):
    hash_table = dict()
    for i in range(len(nums)):
        hash_table[nums[i]] = i

    for i in range(len(nums)):
        sum_value = target - nums[i]
        print(sum_value)
        if sum_value in hash_table:
            if hash_table[sum_value] != i:
                return [hash_table[sum_value], i]


def three_sum(nums):
    hash_table = dict()
    triplets = []

    for i in range(len(nums)):
        hash_table[nums[i]] = i
    for i in range(len(nums) -1):
        sum_value = nums[i] + nums[i+1]
        sum_value *= -1

        if sum_value in hash_table:
            if hash_table[sum_value] != i:
                if three_sum_helper(triplets, nums[i],
                                    nums[i+1], sum_value):
                    triplets.append([nums[i], nums[i+1], sum_value])
    return triplets


def three_sum_helper(triplets, a1, a2, a3):
    for triplet in triplets:
        if a1 in triplet and a2 in triplet and a3 in triplet:
            return False
    return True

def main():
    print(three_sum([3,-2,1,0]))


main()
