#!python3
"""
E1
0 2 0
3 0 1
0 1 2
1 2 3


E2

0 0 0 5 0 0 0 4 0 0 11
9 2 6 0 8 1 7 0 3 0 10
0 1 2 3 4 5 6 7 8 9 10

-8 0




1. O(n)
"""

from collections import Counter, deque, namedtuple, OrderedDict
from functools import reduce
from itertools import permutations, combinations
from bisect import bisect_left
import math

n = int(input().strip())
hand = Counter(int(i) for i in input().strip().split(' '))
b = [int(i) for i in input().strip().split(' ')]
queue = deque(b)

hard_way = max(i - e + n + 1 for i, e in enumerate(queue) if e > 0)
moves = 0
while hand[0] < n:
    if hand[queue[-1] + 1] > 0:
        queue.append(queue[-1] + 1)
        hand[queue[-1] + 1] -= 1
        hand[queue.popleft()] += 1
        moves += 1
    else:
        break
if hand[0] == n:
    print(moves)
else:
    print(hard_way)
