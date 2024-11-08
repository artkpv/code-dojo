#!python3

from collections import deque, Counter
from itertools import combinations, permutations
from math import sqrt, floor, ceil
import unittest


def read_int():
    return int(input().strip())


def read_int_array():
    return [int(i) for i in input().strip().split(' ')]

######################################################

"""
w<=a, h<=b, w/h = x/y, w&h in N.
w-a<=0  0<=b-h
w-a<=b-h
w+h <= a+b
w=x*h/y   y*w = x*h
(x/y+1)*h <= a+b

1 <=  h <= floor(y*(a+b)/(x+y)), h in N
floor(..) = h_num

1 <= y*w/x <= ...

x/y <= w <= x*(a+b)/(x+y)

w_num = floor(x*(a+b)/(x+y) - ceil(x/y) + 1

w = hx/y   h = wy/x

min =

Ex
17 15 5 3
a b x y

h <= 3*33/8  = 12.375
1.666667 = 5/3 <=  w <= 5*33/8 = 20.625



3 6 9

11/3 = 4

Ex2
14 16 7 22

22*30/29-1 = 22.758621-1 _= 21
21 / 22 _= 0

Ex3
1000000000000000000 1000000000000000000 999999866000004473 999999822000007597

"""
from math import gcd

a, b, x, y = read_int_array()

z = gcd(x, y)
x = x//z
y = y//z

if b - a*y/x > 0:  # fills width
    left = max(y, ceil(y/x))
    right = min(floor(y*a/x), floor(b-a*y/x))
    num = max(0, right - left + 1)
    print(left, right, num)
else:  # fills height
    num = max(0, min(floor(b*x/y), floor(a - b*x/y) - max(x, ceil(x/y)) + 1))

print(num)
