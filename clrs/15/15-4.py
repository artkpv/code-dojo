#!python3

"""
15-4 Printing neatly
Consider the problem of neatly printing a paragraph with a monospaced font (all characters having the same width) on a printer. The input text is a sequence of n words of lengths ..., measured in characters. We want to print this para- graph neatly on a number of lines that hold a maximum of M characters each. Our criterion of “neatness” is as follows. If a given line contains words i through j, where i <= j, and we leave exactly one space between words, the number of extra space characters at the end of the line is ... , which must be nonnegative so that the words fit on the line. We wish to minimize the sum, over all lines except the last, of the cubes of the numbers of extra space characters at the ends of lines. Give a dynamic-programming algorithm to print a paragraph of n words neatly on a printer. Analyze the running time and space requirements of your algorithm.


Idea 1

For words from i to j, choose some word k=i..j so that
n(n_i..k) + n(n_k+1..j) is minimal and non-negative. Assume that we know n(..).

Number of ways to choose k.
B(1) = 1
B(n) = Sum(B(k) + B(n-k), k=1..n)
Time: 2^n (see 15.2 chapter)



Example 1
abc def ghi jkl
M=4
>
abc_
def_
ghi_
jkl_
empty space = 4

Example 2
abcd efg hi j k l
M = 6
abcd__
efg_hi
j_k_l_
empty space=3

Example 3

aa bbb c dddd e fff g

aa bbb c
dddd_e__
fff_g___

"""

import unittest
import functools


def print_neatly(words, M):
#     assert all(len(w) <= M for w in words)
#
#     @functools.lru_cache
#     def count(i, j):
#         if i == j:
#             return M - len(words[i])
#         min_spaces = float('inf')
#         min_k = None
#         for k in range(i, j + 1):
#             left_spaces, left_breaks = count(i, k)
#             right_spaces, right_breaks = count(i, k)
#
#
#
#     breaks = {}
#     count = {}
#     # put 1 words per line:
#     for i, w in enumerate(words):
#         count[(i, i)] = M - len(w)
#
#     # put m words per line:
#     for m in range(2, len(words)):
#         for i in range(len(words) - m + 1):
#             for k in range(i, i+m+1):
#
#                 spaces = (M
#                         - sum(len(w) for w in words[i:i+m])
#                         - m + 1
#             count[(i,i+m-1)] = spaces
#
    # construct out from breaks
    # count[0, len(words)-1]
    raise Exception('not implemented')

def count_neatlieness(s):
    count = 0
    if not s:
        return count
    for line in s.split('\n'):
        count += len(line) - 1 - next(
                (i for i,e in enumerate(reversed(line))
                if e != ' '), -1)
    return count

class Tests(unittest.TestCase):
    def test_count_neatlieness(self):
        self.assertEqual(count_neatlieness('abc  '), 2)
        self.assertEqual(count_neatlieness('  '), 2)
        self.assertEqual(count_neatlieness(''), 0)
        self.assertEqual(count_neatlieness('abc  \ndef  '), 4)

    def test_4_by_3(self):
        words = ['abc','def','ghi','jkl']
        actual = print_neatly(words, 4)
        actual_empty = count_neatlieness(actual)
        expected = "abc \ndef \nghi \njkl \n"
        expected_empty = count_neatlieness(expected)
        self.assertEqual(actual_empty, expected_empty)

if __name__ == '__main__':
    unittest.main()
