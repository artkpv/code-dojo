#!/bin/python3

import sys

class Stripper:
    class Rect:
        def __init__(self, y, x, y1, x1):
            self.x=x
            self.y=y
            self.x1=x1
            self.y1=y1

    def __init__(self, A, n, m, k):
        self.A = A
        self.N = n  # Number of rows in the array.
        self.M = m  # Number of columns in the array.
        self.K = k
        self._max = self.max_subarray()
        self.D = {}  # memoization

    def cutAStrip(self):
        max_ = 0
        for i in range(self.N):
            for j in range(self.M):
                z = self.strip_get_max(Stripper.Rect(i, j, i, j))
                if max_ < z:
                    max_ = z
                for l in range(2, self.K+1):
                    z = max( \
                            self.strip_get_max(Stripper.Rect(i, j, min(i+l, self.N-1), min(j+1, self.M-1))), \
                            self.strip_get_max(Stripper.Rect(i, j, min(i+1, self.N-1), min(j+l, self.M-1))))
                    if max_ < z:
                        max_ = z
        return max_

    def intersect(self, a, b):
        return not (a.y < b.y1 or a.y1 > b.y or a.x1 < b.x or a.x > b.x1 )

    def max_with_strip(self, s):
        is_intersect = self.intersect(self._max[1], s)  # si - strip intersect
        if is_intersect:  # max intersected so need to check all board:
            return self.max_subarray()[0]
        else:  # not intersected:
            max_ = self._max[0]
            # consider only those in the strip:
            for i1 in range(0, s.y1+1):
                for j1 in range(0, s.x1+1):
                    for i2 in range(max(i1, s.y), self.N):
                        for j2 in range(max(j1, s.x), self.M):
                            sum_ = 0
                            for i3 in range(i1, i2+1):
                                for j3 in range(j1, j2+1):
                                    sum_ += self.A[i3][j3]
                            if max_ < sum_:
                                max_ = sum_
            return max_

    def max_subarray(self):
        max_ = 0
        subarray = None
        for i1 in range(self.N):
            for j1 in range(self.M):
                for i2 in range(i1, self.N):
                    for j2 in range(j1, self.M):
                        r = Stripper.Rect(i1, j1, i2, j2)
                        sum_ = 0
                        for i3 in range(r.y, r.y1+1):
                            for j3 in range(r.x, r.x1+1):
                                sum_ += self.A[i3][j3]
                        if max_ < sum_:
                            subarray = r
                            max_ = sum_
        return (max_, subarray)


    def strip_get_max(self, s):
        temp = []
        for i in range(s.y, s.y1+1):
            for j in range(s.x, s.x1+1):
                temp += [self.A[i][j]]
                self.A[i][j] = 0

        #print('strip_get_max({},{},{},{})'.format(y, x, l1, l2))
        #print('\n'.join(' '.join(str(i) for i in a) for a in self.A))
        max_ = self.max_with_strip(s)

        # restore:
        for i in range(s.y, s.y1+1):
            for j in range(s.x, s.x1+1):
                self.A[i][j] = temp.pop(0)
        #print(' max:', max_)
        return max_


if __name__ == "__main__":
    n, m, k = [int(i) for i in input().strip().split(' ')]
    A = []
    for A_i in range(n):
       A.append([int(A_temp) for A_temp in input().strip().split(' ')])
    s = Stripper(A, n, m, k)
    print(s.cutAStrip())
