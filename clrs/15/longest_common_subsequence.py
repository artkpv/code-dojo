#!python3
import unittest


def lcs(X, Y):
    """ Longest common subsequence of X and Y. """
    # print(X, Y)
    n = len(X)
    m = len(Y)
    # Longest common subsequence length:
    sl = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            x = X[i-1]
            y = Y[j-1]
            sl[i][j] = max(
                (sl[i-1][j-1] + 1) if x == y else 0,
                sl[i-1][j],
                sl[i][j-1]
            )
    # print('\n'.join(
        # ' '.join(str(e) for e in sl[i]) for i in range(len(sl)))
    # )
    s = []  # The subsequence.
    i = n
    j = m
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            s += [X[i-1]]
            i -= 1
            j -= 1
        elif sl[i-1][j] > sl[i][j-1]:
            i -= 1
        else:
            j -= 1
        # print(i, j, s)

    return sl[n][m], ''.join(reversed(s))


class Tests(unittest.TestCase):
    def test_one(self):
        """
    a b c b d a b
  0 0 0 0 0 0 0 0
b 0 0 1 0 1 0 0 1
d 0 0 1 1 1 2 2 2
c 0 0 1 2 2 2 2 2
a 0 1 1 2 2 2 3 3
b 0 1 2 2 3 3 3 _4
a 0 2 2 2 3 3 4 4

Answer: ab
        """
        slen, s = lcs("abcbdab", "bdcaba")
        print('test 1. Answer:', slen, s)
        self.assertEqual(slen, 4)
        self.assertEqual(s, "bdab")


    def test_two(self):
        slen, s = lcs("ACCGGTCGAGTGCGCGGAAGCCGGCCGAA", "GTCGTTCGGAATGCCGTTGCTCTGTAAA")
        expected = "GTCGTCGGAAGCCGGCCGAA"
        self.assertEqual(s, expected)
        self.assertEqual(slen, len(expected))


unittest.main()
