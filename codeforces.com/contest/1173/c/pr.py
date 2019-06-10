#!python3

from collections import Counter, deque, namedtuple, OrderedDict
from functools import reduce
from itertools import permutations, combinations
import math

n = int(input().strip())
hand = [int(i) for i in input().strip().split(' ')]
b = [int(i) for i in input().strip().split(' ')]
queue = deque(b)
