"""

  A B A C A
A 1
B 0
C 0
  ^

ABAAAAAA
ABACA
   ^
   ABACA

  ABACA
    ABACA

"""

def build(p):
    def char_inx(c):
        if c in chars:
            return chars_list.index(c)
        return None
    chars = set(p)
    chars_list = list(sorted(set(p)))
    radix = len(chars)
    transitions = [[None] * len(p) for _ in range(radix)]
    # from 0 state:
    for i in range(radix):
        transitions[i][0] = 0
    transitions[char_inx(p[0])][0] = 1
    state = 0
    for i in range(1, len(p)):
        for r_i in range(radix):
            transitions[r_i][i] = transitions[r_i][state]
        c = char_inx(p[i])
        transitions[c][i] = i+1
        state = transitions[c][state]
    def transition(c, state):
        if c not in chars:
            return 0
        return transitions[char_inx(c)][state]
    return transition


def kmp(t, p):
    if not t:
        return -1
    if not p:
        return 0
    transition = build(p)
    state = 0
    for i, e in enumerate(t):
        state = transition(e, state)
        if state == len(p):
            return i - len(p) + 1
    return -1


import unittest

class Tests(unittest.TestCase):
    def test_5_chars(self):
        self.assertEqual(kmp('ABRAC', 'RA'), 2)

    def test_7_chars(self):
        self.assertEqual(kmp('ABRACAD', 'ACAD'), 3)

    def test_empty(self):
        self.assertEqual(kmp('ABRACAD', ''), 0)
        self.assertEqual(kmp('', 'ABCD'), -1)

    def test_long(self):
        self.assertEqual(kmp('abcd defg abv abc abd dab', 'v a'), 12)

unittest.main()
