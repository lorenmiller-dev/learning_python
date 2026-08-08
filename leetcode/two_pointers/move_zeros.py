def move_zeros(nums: list[int]) -> None:
    """
        given an int array, move all 0 to end while maintaining relative order
        doing so without making a copy of the array
    """


def main():
    test_nums = [1, 2, 3, 0, 4, 5, 6, 0, 7, 8, 0, 9, 10, 0, 11]
    move_zeros(test_nums)
    print("result: ", test_nums)

    test_nums_2 = [0]
    move_zeros(test_nums_2)
    print("result: ", test_nums_2)


if __name__ == "__main__":
    main()
