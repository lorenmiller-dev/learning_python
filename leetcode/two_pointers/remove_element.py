def remove_element(nums: list[int], val: int) -> int:
    write_index = 0

    for read_index in range(len(nums)):
        if nums[read_index] != val:
            nums[write_index] = nums[read_index]
            write_index += 1

    return write_index


def main():
    test_1 = [2, 3, 2, 3]
    test_val1 = 3
    k1 = remove_element(test_1, test_val1)
    print("K: ", k1)
    print("result: ", test_1[:k1])


if __name__ == "__main__":
    main()
