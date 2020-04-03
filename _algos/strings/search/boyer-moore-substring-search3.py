#!python
"""
boyer moore substring search

N - len of text
M - len of pattern

Best - N/M
O(N*M)
"""


def bmss(pattern, text):
    if not pattern:
        return 0
    n = len(text)
    m = len(pattern)
    pchars = set(pattern)
    i = m-1
    while i < n:
        j = i
        while i - j < m and text[j] == pattern[-(i-j)-1]:
            j -= 1
        if i - j == m:
            return j + 1
        if text[j] in pchars:
            i += 1
        else:
            i = j + m
    return -1

assert bmss("aba", "abbabbaba") == 6
assert bmss("abb", "ababababa") == -1
assert bmss("", "ababababa") == 0
assert bmss("ab", "") == -1
assert bmss("baaa", "abaaabaa") == 1

print('done')
