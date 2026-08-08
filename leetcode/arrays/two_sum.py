def two_sum(nums, target):

    """
    Given an array of integers nums and an integer target,
    return the indices i and j such that nums[i] + nums[j] == target and i != j.

    You may assume that every input has exactly one pair of indices
    i and j that satisfy the condition.

    Return the answer with the smaller index first.
    """

    # hashmap approach
    num_to_index = {}

    # iterate through our input array
    for i, num in enumerate(nums):
        print("i: ", i, " num: ", num)

        # calculate our complement using complement = target - num[i]
        complement = target - num
        print("complement: ", complement)

        # check to see if complement is in hashmap, if so return both indices
        if complement in num_to_index:

            # store the complement, and it's index as key : value pair
            return [num_to_index[complement], i]

        print(num_to_index)
        # if not, add it to our hashmap
        num_to_index[num] = i


def main():
    test_nums = [4, 6, 3, 3, 6]
    test_target = 9

    result = two_sum(test_nums, test_target)

    print("result: ", result)


if __name__ == "__main__":
    main()
