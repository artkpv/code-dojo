# Next: Решить степенное уравнение: y**(n-1)-n>0, y = 2**(a/b)
# 1/ 1_000_000_000. 10.24

import math

def is_power_of_2(x):
    return x&(x-1) == 0

def find(a, b):


    x = 2
    total = 1
    perfect = 1
    while perfect * b >= total * a:
        total += 1
        x += 1
        if is_power_of_2(x):
            perfect += 1
    return x*(x-1)

q = int(input().strip())
for q_i in range(q):
    a, b = [int(i) for i in input().strip().split(' ')]
    if a > b:
        print(0)
    else:
        print(find(a, b))
