#!/bin/python3

"""
Boyer-Moore

N / M
"""

import unittest

def bm_ss(s, p):
    n = len(s)
    m = len(p)
    if n < m:
        return -1
    pchars = set(p)
    i = m-1
    while i < n:
        ismatch = True
        for j in range(m):
            if s[i-j] != p[-j-1]:
                ismatch = False
                break
        if ismatch:
            return i-m+1
        if s[i-j] in pchars:
            i += 1  # or some other like in KMP algo
        else:
            i = i - j + m
    return -1

class Tests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(bm_ss('abracadabra', 'acad'), 3)
        self.assertEqual(bm_ss('abracadabra', 'abrac'), 0)
        self.assertEqual(bm_ss('abracadabra', 'abrad'), -1)
        self.assertEqual(bm_ss('', ''), 0)
        self.assertEqual(bm_ss('abcde', ''), 0)
        self.assertEqual(bm_ss('abcde', ''), 0)

    def test_large(self):
        s = 'a' * 10**9
        p = 'b' * 100
        self.assertEqual(bm_ss(s, p), -1)

unittest.main()
