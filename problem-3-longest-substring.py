def length_of_longest_substring(input_string):
    i = 0
    seen = {}
    max_len = 0
    for j, input_char in enumerate(input_string):

        if input_char in seen:
            i = max(i, seen[input_char])

        max_len = max(max_len, j - i + 1)
        seen[input_char] = j + 1

    return max_len


print(length_of_longest_substring('abcabcbb'))
print(length_of_longest_substring('abba'))
print(length_of_longest_substring('a'))
print(length_of_longest_substring(' '))