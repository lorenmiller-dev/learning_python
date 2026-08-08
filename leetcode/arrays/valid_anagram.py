from collections import defaultdict


def valid_anagram(s: str, t: str) -> bool:
    # two pointer approach -> only have to iterate once
    # we can use standard freq counter or default dict

    # check length of both strings, anagrams must have the same amount of characters
    if len(s) != len(t):
        return False

    # count the frequency of each character in both strings
    str_s_char_freq = {}
    str_t_char_freq = {}

    """
    str_s_char_freq = defaultdict(int)
    str_t_char_freq = defaultdict(int)
    """

    for i in range(len(s)):
        # standard freq counter

        # retrieves freq of char at i, if not add to list and set frequency to 0 and increment +1
        str_s_char_freq[s[i]] = 1 + str_s_char_freq.get(s[i], 0)
        str_t_char_freq[t[i]] = 1 + str_t_char_freq.get(t[i], 0)

        # default dict counter

        # str_s_char_freq[s[i]] += 1
        # str_t_char_freq[t[i]] += 1

    # if both freq lists are equal return True, otherwise False
    return str_s_char_freq == str_t_char_freq


def main():
    test_s1 = "carrace"
    test_t1 = "racecar"
    result1 = valid_anagram(test_s1, test_t1)
    print("are ", test_t1, " and ", test_s1, " anagrams? ", result1)

    test_s2 = "jam"
    test_t2 = "jar"
    result2 = valid_anagram(test_s2, test_t2)
    print("T or F that string `s` and `t` are anagrams? \n", result2)


if __name__ == "__main__":
    main()
