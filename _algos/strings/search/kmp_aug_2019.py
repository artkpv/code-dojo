#!/bin/python3

import unittest
"""
ABRACADABRA

  A B R A C A D A B R A
A 1 1 1 4 1
B 0 2 0 0 2
C 0 0 0 0 5
D 0 0 0 0 0
R 0 0 3 0 0

s 0 0 0 1 0

"""

def kmp(t, p):  # t text, p pattern
    if not t:
        return -1
    n = len(t)
    m = len(p)
    if n < m:
        return -1
    if m == 0:
        return 0
    def construct():
        chars = list(sorted(set(p)))
        def cinx(c): return chars.index(c) if c in chars else -1
        r = len(chars)  # radix
        tt = [[None] * m for _ in range(r)]  # transition table
        for i in range(r):
            tt[i][0] = 0
        tt[cinx(p[0])][0] = 1
        state = 0
        for i, c in enumerate(p):
            if i == 0: continue
            for j in range(r):
                tt[j][i] = tt[j][state]
            tt[cinx(c)][i] = i + 1
            state = tt[cinx(c)][state]
        return lambda s, c: tt[cinx(c)][s] if cinx(c) != -1 else 0

    dfa = construct()
    state = 0
    for i, c in enumerate(t):
        state = dfa(state, c)
        if state == m:
            return i - m + 1
    return -1


class Tests(unittest.TestCase):
    def test_one(self):
        self.assertEqual(kmp("a", "a"), 0)
        self.assertEqual(kmp("a", "b"), -1)
        self.assertEqual(kmp("abracadabra", "cadab"), 4)
        self.assertEqual(kmp("a", ""), 0)
        self.assertEqual(kmp("a", "abc"), -1)
        self.assertEqual(kmp("abracadabra", "raca"), 2)
        self.assertEqual(kmp("abracadabra", "bra"), 1)

unittest.main()
