#!/bin/python3
"""
https://www.hackerrank.com/contests/w36/challenges/expert-computation

"""

import sys
import bisect

class FArray:
    def __init__(self, a=None, n=None):
        self.a = a
        self.n = len(a) if a else n

    def __lt__(self, other):
        return self.n < other.n

    def __le__(self, other):
        return self.n <= other.n

    def __gt__(self, other):
        return self.n > other.n

    def __ge__(self, other):
        return self.n >= other.n

    def __eq__(self, other):
        return self.n == other.n

    def __repr__(self):
        return str(self.a or '') + str(self.n)


class ExpertComputation:
    def __init__(self, n, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.n = n
        self.MOD = 10**9+7
        self.f = [None] * n
        self.h = [None] * n
        self.c = [None] * n
        self.l = [None] * n
        self.g = [None] * n
        self.f_arrays = []  # list of arrays for F(i)

    def H(self, i):
        assert i > 0
        if self.h[i-1] == None:
            h = self.x[i-1]
            self.h[i-1] = h if i == 1 else h ^ self.G(i-1)
        return self.h[i-1]

    def C(self, i):
        assert i > 0
        if self.c[i-1] == None:
            c = self.y[i-1]
            self.c[i-1] = c if i == 1 else c ^ self.G(i-1)
        return self.c[i-1]

    def L(self, i):
        assert i > 0
        if self.l[i-1] == None:
            l = self.z[i-1]
            self.l[i-1] = l if i == 1 else l ^ self.G(i-1)
        return self.l[i-1]

    def FOld(self, i):
        if self.f[i-1] == None:
            sys.stdout.write('F(%d) ' % i)
            h_i = self.H(i)
            c_i = self.C(i)
            l_i = self.L(i)
            j_top = i - l_i
            max_ = self.H(1)*c_i - self.C(1)*h_i
            for j in range(2, j_top+1):
                v = self.H(j)*c_i - self.C(j)*h_i
                sys.stdout.write(' %d:%d' % (j, v))
                if v > max_:
                    max_ = v
            sys.stdout.write('\n')
            self.f[i-1] = max_
        return self.f[i-1]

    def F(self, i):
        # BUG. Figure out why it won't call cached arrays
        h_i = self.H(i)
        c_i = self.C(i)
        l_i = self.L(i)
        j_top = i - l_i  # 1 <= j <= j_top
        j_top = 1 if j_top < 1 else j_top

        if len(self.f_arrays) == 0:
            self.f_arrays += [FArray([self.H(1)*c_i - self.C(1)*h_i])]

        f_inx = bisect.bisect_left(self.f_arrays, FArray(n=j_top))
        farray = None  # array of j_top+1 len or less
        if f_inx < len(self.f_arrays) and self.f_arrays[f_inx].n == j_top:  # found
            farray = self.f_arrays[f_inx].a
        else:
            # no such and f_inx at the smallest larger array
            # or all are less
            farray = self.f_arrays[f_inx-1].a  # at largest smaller array

        if len(farray) < j_top:  # then fill cached array to the required
            farray = farray.copy()
            for j in range(len(farray)+1, j_top+1):
                # BUG we can not use f_arrays prev. arrays as values are different.
                #  Ex. 1.  Not all variants taken:
                #   i = 2
                #     3*4 + 4*9
                #     3*9 + 4*4
                v = self.H(j)*c_i - self.C(j)*h_i
                v_inx = bisect.bisect_left(farray, v)  # keeping in sorted order
                farray.insert(v_inx, v)
            assert len(farray) == j_top
            inx = bisect.bisect_left(self.f_arrays, FArray(farray))
            self.f_arrays.insert(inx, FArray(farray))  # cache for later use

        return farray[-1]  # max

    def G(self, u):
        if self.g[u-1] == None:
            self.g[u-1] = sum(self.FOld(i)%self.MOD for i in range(1, u+1))%self.MOD
        return self.g[u-1]

if __name__ == "__main__":
    n = int(input().strip())
    x = [int(i) for i in input().strip().split(' ')]
    y = [int(i) for i in input().strip().split(' ')]
    z = [int(i) for i in input().strip().split(' ')]
    print(ExpertComputation(n, x, y, z).G(n))
