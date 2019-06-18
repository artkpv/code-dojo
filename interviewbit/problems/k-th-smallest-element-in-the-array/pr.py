#!python3
"""
Don't modify array. Constant extra space.

Idea 1
Find next element by prev inx and prev val:
    i : a[i] = min { a[j], (a[j] == a[prev] and prev < j and first) or a[j] > prev_val }
Time : O(n^2)
Space: 1

Idea 2:
    Quicksort.
    But modifies array.
    Time: O(n)
    S: O(1)

Idea 2 Binary search


"""
from random import Random
import unittest

class Solution:
    def kthsmallest(self, A, B):
        randint = Random().randint
        max_ = max(A)
        min_ = min(A)
        pivot = A[randint(0, len(A)-1)]
        while True:
            lt, eq, gt = 0, 0, 0
            for e in A:
                if not (min_ <= e <= max_):
                    continue
                if e < pivot:
                    lt += 1
                elif e > pivot:
                    gt += 1
                else:
                    eq += 1
            if lt < B <= lt + eq:
                return pivot


            if B <= lt:
                pivot_new = [e for e in A if min_ <= e < pivot][randint(0, lt-1)]
                max_ = pivot - 1
                pivot = pivot_new
            else:
                pivot_new = [e for e in A if pivot < e <= max_][randint(0, gt-1)]
                min_ = pivot + 1
                pivot = pivot_new
                B -= (lt + eq)


class Tests(unittest.TestCase):
    def test_five_elements(self):
        self.assertEqual(Solution().kthsmallest([2,1,2,3,4], 3), 2)

    def test_long(self):
        array = [8, 16, 80, 55, 32, 8, 38, 40, 65, 18, 15, 45, 50, 38, 54, 52, 23, 74, 81, 42, 28, 16, 66, 35, 91, 36, 44, 9, 85, 58, 59, 49, 75, 20, 87, 60, 17, 11, 39, 62, 20, 17, 46, 26, 81, 92 ]
        self.assertEqual(Solution().kthsmallest(array, 9), 17)

        """
        [8, 8, 9, 11, 15, 16, 16, 17, 17, 18, 20, 20, 23, 26, 28, 32, 35, 36, 38, 38, 39, 40, 42, 44, 45, 46, 49, 50, 52, 54, 55, 58, 59, 60, 62, 65, 66, 74, 75, 80, 81, 81, 85, 87, 91, 92]
        """


unittest.main()
