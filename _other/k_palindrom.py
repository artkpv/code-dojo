#!python3
"""
s, k
if k-palindrom? by removal of at most k chars

I 1
Time: k * (n, n-k) * n
n*(n-1)*(n-2).. / (n-k)!
n*k*n!/(n-k)!


I 2
For all centers check left subseq == right subseq.
???

I 3
left_i   right_i
while left_i < right_i:
    match : move
    not match:
        move left, k-1 -> palindrom left_i+1 .. right_i
        move right, k-1 -> palindrom lleft_i .. right_i -1
Recursive

Time: at most k branches, 2^k. O(2^k) , ~10^9


I 4
P(s[l..r]) =
 min(
    or P(s[l+1..r-1])
    or P(s[l+1..r])+1
    or P(s[l..r-1])+1
 )

"""

import unittest


def is_palindrom(s, k, lo=None, hi=None):
    if lo is None:
        lo = 0
    if hi is None:
        hi = len(s) - 1
    if lo >= hi:
        return True
    if s[lo] == s[hi]:
        return is_palindrom(s, k, lo+1, hi-1)
    if k == 0:
        return False
    if is_palindrom(s, k-1, lo+1, hi):
        return True
    return is_palindrom(s, k-1, lo, hi-1)


def is_palindrom_iter(s, k):
    stack = [(0, len(s)-1, k)]
    while stack:
        lo, hi, k = stack.pop()
        if lo >= hi:
            return True
        if s[lo] == s[hi]:
            stack += [(lo+1, hi-1, k)]
            continue
        if k == 0:
            continue
        stack += [(lo+1, hi, k-1)]
        stack += [(lo, hi-1, k-1)]
    return False

"""
abxa 1

(0 3 1)
(1 2 1)
(2 2 0) (1 1 0) > True

abdxa 1
(0 4 1)
(1 3 1)
(2 3 0) (1 2 0)
(2 3 0)
return False




lo hi k
0  3  1
1  2  1
2  2  0
True

abdxa 1
lo hi k
0  4  1
1  3  1
2  3  0 >false
1  2  0 > false
> false




"""


class Tests(unittest.TestCase):
    def test_tests(self):
        for f in [is_palindrom, is_palindrom_iter]:
            self.assertTrue(f('abxa', 1))
            self.assertTrue(f('a', 1))
            self.assertTrue(f('', 0))
            self.assertTrue(f('ab', 1))
            self.assertFalse(f('ab', 0))
            self.assertFalse(f('abdxa', 1))
            self.assertTrue(f('aaaaaaaaaa', 0))
            self.assertTrue(f('abcdefgfedcba', 0))
            self.assertTrue(f('abcdefgfedcba', 0))
            self.assertTrue(f('abcdefgfedcba', 0))


unittest.main()
