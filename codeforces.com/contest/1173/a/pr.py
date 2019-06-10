#!python3

from collections import Counter, deque, namedtuple, OrderedDict
from functools import reduce
from itertools import permutations, combinations
import math

# n = int(input().strip())
pluses, minuses, unknown = [int(i) for i in input().strip().split(' ')]

if pluses - minuses - unknown > 0:
    print('+')
elif minuses - pluses - unknown > 0:
    print('-')
elif unknown == 0 and minuses == pluses:
    print('0')
else:
    print('?')

