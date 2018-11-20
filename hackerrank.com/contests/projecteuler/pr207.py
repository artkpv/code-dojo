#!python3

"""
https://www.hackerrank.com/contests/projecteuler/challenges/euler207/submissions/code/71712787
https://projecteuler.net/problem=207

1 <= q <= 3*10^5
1 <= a,b <= 10^18

След. См. для 1/12345 (на продж. Ейлере).

1 example:

>2
2 3
9 20

<6
30

"""

from bisect import bisect_left
from math import floor, log, sqrt, gcd
from threading import Timer
from time import time

class Proportion:
    def __init__(self, p, c, k2=None):  # p - perfect, c - count
        d = gcd(p, c)
        self.p = int(p/d)
        self.c = int(c/d)
        self.k2 = k2

    def __lt__(self, r):
        if self.c == r.c:
            return self.p < r.p
        return (self.p * r.c) < (r.p * self.c)

    def __str__(self):
        return '({}/{} {})'.format(self.p, self.c, self.k2)

    def __repr__(self):
        return self.__str__()


M = [Proportion(1, 1, 3)]  # min (p, m) so far

start = time()
t = None
def print_progress():
    global start, M, t
    print("{} sec {} count, {} last ".format(int(time() - start), len(M), M[0]))
    t = Timer(5.0, print_progress)
    t.start()

#print_progress()



def find_update(p_ab):
    global last_p, M
    k2 = M[0].k2 + 2
    count = M[0].c
    perf = M[0].p
    while not M[0] < p_ab:
        k  = (k2**2-1)/4
        count += 1
        t = log((k2+1)/2, 2)
        if floor(t) == t:
            perf += 1
        print("{}\t{}\t{}".format(int(k),perf,count))
        last_p = Proportion(perf, count, k2)
        if last_p < M[0]:
            M.insert(0, last_p)
        k2 += 2
    y_i = bisect_left(M, p_ab)
    return int((M[y_i-1].k2**2-1)/4)

q = int(input().strip())
for q_i in range(q):
    a, b = [int(i) for i in input().strip().split(' ')]
    if a > b:
        print(0)
    else:
        print("m\tp\tc")
        min_ = find_update(Proportion(a, b))
        print(min_)
if t:
    t.cancel()
