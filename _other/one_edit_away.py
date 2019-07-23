#!python3
import unittest


def one_edit(A, B):
    i = 0
    while i < len(A):
        if (i >= len(B) or A[i] != B[i]):
            return A[i:] == B[i+1:] or A[i+1:] == B[i+1:]
        i += 1
    return len(B) == i or len(B) - 1 == i


class Tests(unittest.TestCase):
    def test_one(self):
        self.assertTrue(one_edit('a', 'b'))
        self.assertTrue(one_edit('a', 'a'))
        self.assertTrue(one_edit('ab', 'ab'))
        self.assertTrue(one_edit('', ''))
        self.assertTrue(one_edit('ab', 'a'))
        self.assertTrue(one_edit('ab', 'a'))
        self.assertTrue(one_edit('a', 'ab'))
        self.assertTrue(one_edit('a', 'ab'))

        self.assertFalse(one_edit('abc', 'bb'))
        self.assertFalse(one_edit('abc', 'abcde'))

unittest.main()
