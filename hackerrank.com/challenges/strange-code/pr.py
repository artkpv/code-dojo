#!python3
"""

1: 3 2 1
2: 6 5 4 3 2 1

3 6 12 24

seconds after n-th cycle = 3(2^n-1)
t - seconds
find counter value

log(2,t/3+1) = n




"""
import math

t = int(input('').strip())
cycles = int(math.log(t/3+1, 2))
cycles_seconds = 3*(2**cycles-1)
remain = t - cycles_seconds
if remain == 0:
    print(1)
else:
    initial = 3*2**cycles
    counter = initial - remain + 1
    print(counter)
