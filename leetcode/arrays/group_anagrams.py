from typing import List
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Given an array of strings strs, group all anagrams together into sublists.
    You may return the output in any order.

    An anagram is a string that contains the exact same characters as another string,
    but the order of the characters can be different.
    """

    # apply similar concepts as valid_anagram

    map_of_anagrams = defaultdict(list)

    for word in strs:
        # frequency array of size 26 for letters `a` - `z`
        word_char_count = [0] * 26

        # go through each char in current word
        for char in word:
            # map char to index using ASCII offset
            char_index = ord(char) - ord('a')

            # at character index increment 1
            word_char_count[char_index] += 1

        # convert array to tuple to use as a dictionary key, then append word to map
        map_of_anagrams[tuple(word_char_count)].append(word)

    # return list of grouped anagrams
    return list(map_of_anagrams.values())


def main():
    test_strs1 = ["act", "pots", "tops", "cat", "stop", "hat"]
    result1 = group_anagrams(test_strs1)
    print(result1)

    test_strs2 = ["x"]
    result2 = group_anagrams(test_strs2)

    print(result2)

    test_strs3 = [""]
    result3 = group_anagrams(test_strs3)
    print(result3)


if __name__ == "__main__":
    main()
