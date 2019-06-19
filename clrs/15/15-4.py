#!python3

"""
15-4 Printing neatly
Consider the problem of neatly printing a paragraph with a monospaced font (all characters having the same width) on a printer. The input text is a sequence of n words of lengths ..., measured in characters. We want to print this para- graph neatly on a number of lines that hold a maximum of M characters each. Our criterion of “neatness” is as follows. If a given line contains words i through j, where i <= j, and we leave exactly one space between words, the number of extra space characters at the end of the line is ... , which must be nonnegative so that the words fit on the line. We wish to minimize the sum, over all lines except the last, of the cubes of the numbers of extra space characters at the ends of lines. Give a dynamic-programming algorithm to print a paragraph of n words neatly on a printer. Analyze the running time and space requirements of your algorithm.


Idea

Let m(i,j) be minimal break of i..j words.
m(i,j) = min{ m(i..k) + m(k+1..j), for some k=i..j-1 }

Number of ways to choose k.
B(1) = 1
B(n) = Sum(B(k) + B(n-k), k=1..n)
Time: 2^n (see 15.2 chapter)


"""

import unittest
import functools

INF = float('inf')


def print_neatly(words, M):
    """
    Get how to print neatly words.
    @words: array of words.
    @M: line width.
    Returns: cost to print, array of breaks.
    """
    assert all(len(w) <= M for w in words)
    def extra(i, j):
        """ Extra spaces to print words at i+1..j. """
        return M - (j - i - 1) - sum(len(w) for w in words[i+1:j+1])

    cost = [INF] * (len(words)+1)  # Cost to optimally print words.
    breaks = [None] * len(words)  # Rightmost break at word for words.
    cost[0] = 0
    for j in range(1, len(words)+1):
        for i in range(j):
            spaces = extra(i-1, j-1)
            if j == len(words) and spaces >= 0:  # last
                spaces = 0
            elif spaces < 0:
                spaces = INF
            spaces += cost[i]
            if spaces < cost[j]:
                cost[j] = spaces
                breaks[j-1] = i-1
    return cost[len(words)], breaks


def line_neatlieness(line):
    return len(line) - 1 - next(
        (i for i, e in enumerate(reversed(line))
         if e != ' '), -1)


def join_words(words, breaks, line_width):
    text = []
    j = len(words)-1
    while j >= 0:
        i = breaks[j]
        line = ' '.join(words[i+1:j+1])
        assert len(line) <= line_width
        line += ' ' * (line_width - len(line))
        text += [line]
        j = i
    return '\n'.join(reversed(text))


class Tests(unittest.TestCase):
    """ UT """
    def test_count_neatlieness(self):
        self.assertEqual(line_neatlieness('abc  '), 2)
        self.assertEqual(line_neatlieness('  '), 2)
        self.assertEqual(line_neatlieness(''), 0)

    def test_4_by_3(self):
        words = ['abc','def','ghi','jkl']
        line_width = 4
        count, breaks = print_neatly(words, line_width)
        actual = join_words(words, breaks, line_width)
        expected = "abc \ndef \nghi \njkl "
        expected_empty = 3
        self.assertEqual(actual, expected)
        self.assertEqual(count, expected_empty)

    def test_three(self):
        expected = "aaaa bb  \ncc dddd  \neee fffff"
        expected_empty = 4
        width = 9
        words = []
        for line in expected.split('\n'):
            words += [w.strip() for w in line.strip().split(' ') if w]
        count, breaks = print_neatly(words, width)
        actual = join_words(words, breaks, width)
        self.assertEqual(actual, expected)
        self.assertEqual(count, expected_empty)



if __name__ == '__main__':
    unittest.main()
