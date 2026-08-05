def contains_duplicate(nums):

    seen = set()

    # iterate over every value num in nums array
    for num in nums:

        # check if current value is in hashset
        if num in seen:

            # duplicate found
            return True

        # add value to hashset if not already seen
        seen.add(num)

    # no duplicate found
    return False

    """ O(N^2) solution
    
    input_length = len(nums)

    for i in range(input_length):
        
        for j in range(i + 1, input_length):
            
            # compare values at i and j
            if nums[i] == nums[j]:
                
                # duplicate has been found
                return True
    
    # no duplicate found
    return False
    """


def main():
    test_nums = [1, 2, 3]

    result_contains_duplicate = contains_duplicate(test_nums)

    print(result_contains_duplicate)


if __name__ == "__main__":
    main()
