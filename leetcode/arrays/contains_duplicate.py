def contains_duplicate(nums):
    """
    Given an integer array nums,
    return true if any value appears more than once in the array,
    otherwise return false.
    """

    # hashset approach

    # hashsets only store unique elements, use this to look for duplicates
    distinct_values = set()

    # iterate over our input array
    for num in nums:

        # check if current value is in our set, if so return True
        if num in distinct_values:
            return True

        # add curr element to set
        distinct_values.add(num)

    # no duplicates found, return False
    return False


def main():
    test_nums = [1, 2, 3, 3, 2]

    result_contains_duplicate = contains_duplicate(test_nums)

    print(result_contains_duplicate)


if __name__ == "__main__":
    main()
