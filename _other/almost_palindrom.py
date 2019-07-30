#!python3

import unittest


def isap(s):
    if not s:
        return True
    def ispalindrom(lo, hi):
        l = hi - lo + 1
        if l <= 1:
            return True
        for i in range(l//2):
            if s[lo+i] != s[hi-i]:
                return False
        return True

    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return ispalindrom(i, len(s)-i-2) or ispalindrom(i+1, len(s)-i-1)
    return True


class Tests(unittest.TestCase):
    def test_tests(self):
        self.assertTrue(isap('aba'))
        self.assertTrue(isap('abca'))
        self.assertTrue(isap('acba'))
        self.assertTrue(isap(''))
        self.assertTrue(isap('a'))
        self.assertTrue(isap('zxyyx'))
        self.assertTrue(isap('abeecba'))

        self.assertFalse(isap('abcde'))
        self.assertFalse(isap('beecba'))

unittest.main()
