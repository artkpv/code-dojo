#!/bin/python3

#!python3

from collections import deque, Counter
import array
from itertools import combinations, permutations
from math import sqrt
import unittest

######################################################
"""
Given 3 arrays find a triple with minimum absolute difference: abs(max(a,b,c) - min(a,b,c)).

1 2 3 4
5 6 7
1 6 7


1 1e9
1 3
10 20 30

"""

def brute(A, B, C):
    res = float('inf')
    for i in range(len(A)):
        for j in range(len(B)):
            for k in range(len(C)):
                x = abs(max(A[i], B[j], C[k]) - min(A[i], B[j], C[k]))
                if x < res:
                    res = x
                    resi, resj, resk = i, j, k
    return res, resi, resj, resk


class Solution(object):
    def solve(self, A, B, C):
        # print('A' + ' '.join('%d:%d' % (i,d) for i, d in enumerate(A)))
        # print('B' + ' '.join('%d:%d' % (i,d) for i, d in enumerate(B)))
        # print('C' + ' '.join('%d:%d' % (i,d) for i, d in enumerate(C)))
        def isinc(D, i, E, j, F, k):
            if i >= len(D) or j >= len(E) or k >= len(F):
                return False
            if D[i] < min(E[j], F[k]):
                return True
            if D[i] > min(E[j], F[k]):
                return False
            return True

        if not A or not B or not C:
            return 0
        i = 0
        j = 0
        k = 0
        res = float('inf')
        while i < len(A) and j < len(B) and k < len(C):
            x = abs(max(A[i], B[j], C[k]) - min(A[i], B[j], C[k]))
            if x < res:
                res = x
                # print('C', i, j, k, res)
            if isinc(C, k, A, i, B, j):
                k += 1
            elif isinc(B, j, A, i, C, k):
                j += 1
            elif isinc(A, i, B, j, C, k):
                i += 1
            else:
                break
        return res



class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Solution().solve(
            [1, 2, 3, 4],
            [5, 6, 7],
            [1, 6, 7]),
            2)  # 4 5 6

    def test_2(self):
        self.assertEqual(Solution().solve(
            [1, 1, 1, 2],
            [1, 1, 1, 1e9],
            [4, 5]),
            3)

    def test_3(self):
        self.assertEqual(Solution().solve(
            [1, 4, 5, 8, 10],
            [6, 9, 10],
            [2, 3, 6, 10]),
            0)

    def test_4(self):
        self.assertEqual(Solution().solve(
            [ 1, 4, 5, 8, 10 ],
            [ 6, 9, 15 ],
            [ 2, 3, 6, 6 ]),
            1)

    def test_5(self):
        A = [ -72, -39, -20, 19, 34, 49, 85, 94, 107, 121, 167, 209, 216, 261, 275, 287, 299, 315, 332, 361, 386, 393, 394, 414, 445, 481, 492, 514, 562, 598, 615, 655, 696, 726, 760, 763, 782, 827, 868, 888, 925, 960, 988, 1025, 1025, 1054, 1066, 1069, 1076, 1085, 1113, 1130, 1139, 1152, 1181, 1205, 1250, 1264, 1284, 1316, 1357, 1377, 1385, 1406, 1419, 1454, 1498, 1537, 1585, 1610, 1649, 1657, 1664, 1699, 1706, 1712, 1731, 1760, 1765, 1810, 1858, 1905, 1934, 1954, 1958, 1966, 1982, 2002, 2040, 2043, 2090, 2115, 2130, 2167, 2196, 2236, 2249, 2273, 2318, 2362, 2401, 2409, 2455, 2466, 2515, 2550, 2569 ]
        B = [ -82, -54, -40, -16, 14, 46, 65, 80, 102, 125, 172, 221, 251, 271, 273, 312, 323, 327, 359, 361, 404, 424, 434, 450, 478, 508, 529, 538, 555, 594, 605, 616, 628, 667, 688, 720, 756, 762, 799, 809, 822, 870, 915, 947, 987, 1024, 1038, 1061, 1080, 1084, 1125, 1169, 1169, 1170, 1173, 1217, 1238, 1267, 1314, 1363, 1395, 1419, 1431, 1437, 1461, 1480, 1502, 1536, 1538, 1561, 1579, 1614, 1641, 1690, 1727, 1769, 1809, 1843, 1847, 1848, 1859, 1864, 1873, 1905, 1944, 1956, 2004, 2031, 2079, 2111, 2123, 2145, 2185, 2207, 2238, 2276 ]
        C = [ 18, 58, 71, 101, 119, 158, 181, 214, 214, 257, 261, 267, 280, 315, 321, 332, 344, 351, 353, 377, 426, 467, 502, 548, 548, 566, 611, 632, 676, 695, 724, 748, 769, 809, 858, 890, 895, 940, 958, 1006, 1037, 1061, 1072, 1096, 1124, 1148, 1179, 1206, 1234, 1242, 1271, 1308, 1324, 1357, 1398, 1434, 1457, 1464, 1467, 1505, 1531, 1535, 1568, 1589, 1593, 1641, 1651, 1666, 1703, 1706, 1716, 1733, 1769, 1771, 1808, 1853, 1870, 1898, 1927, 1966, 1969, 1998, 2035, 2051, 2062, 2062, 2099, 2132, 2168, 2203, 2252, 2280, 2283, 2306, 2308, 2355, 2379, 2422, 2451, 2479, 2496, 2539, 2552, 2587, 2615, 2639, 2671, 2713, 2744, 2785, 2828, 2861, 2869 ]
        # print(brute(A, B, C))
        self.assertEqual(Solution().solve(A, B, C), 2)

    def test_edges(self):
        self.assertEqual(Solution().solve( [1], [2], [3]), 2)
        self.assertEqual(Solution().solve( [], [2], [3]), 0)
        self.assertEqual(Solution().solve( [1], [], [3]), 0)
        self.assertEqual(Solution().solve( [1], [2], []), 0)
        self.assertEqual(Solution().solve( [1], [1e9], [1e9+1]), 1e9)



if __name__ == '__main__':
    unittest.main()
