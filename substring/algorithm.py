def length_of_longest_substring(s):
    char_set = set()
    start = 0
    max_len = 0

    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        max_len = max(max_len, end - start + 1)

    return max_len

# if __name__ == "__main__":
#     s = "abcabcbb"
#     print(length_of_longest_substring(s))  # Output: 3

#     s = "bbbbb"
#     print(length_of_longest_substring(s))  # Output: 1

#     s = "pwwkew"
#     print(length_of_longest_substring(s))  # Output: 3

#     s = ""
#     print(length_of_longest_substring(s))  # Output: 0