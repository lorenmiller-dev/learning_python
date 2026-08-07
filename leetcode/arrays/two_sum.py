def two_sum(nums, target):
    seen_elements = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen_elements:
            return [seen_elements[complement], i]

        seen_elements[num] = i


# O(N^2) Solution
"""
    input_length = len(nums)

   for i in range(input_len):
        for j in range(i + 1, input_len):
            current_sum = nums[i] + nums[j]

            if target == current_sum:
                return [i, j]
"""


def main():
    test_nums = [4, 7, 3, 3, 6]
    test_target = 9

    result = two_sum(test_nums, test_target)

    print(result)


if __name__ == "__main__":
    main()
