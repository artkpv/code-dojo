#!python3

from collections import namedtuple
from fractions import Fraction as F

P = namedtuple('P', ['x', 'y'])

class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.slope =

def intersection(p1, p2, p3, p4):
    # First vertical:
    if p1.x - p2.x == 0:
        if p3.x - p4.x == 0:  # parallel or inf
            return 'inf' if p1.y == p3.y else -1
        elif p3.y - p4.y == 0:  # orthogonal
            return (p1.x, p3.y)
        else:  # crosses vertical
            return (
                p1.x,
                float(F((p4.y - p3.y)*(p3.x - p1.x), (p4.x - p3.x)) + F(p3.y))
            )
    # First horizontal:
    elif p1.y - p2.y == 0:
        if p3.y - p4.y == 0:  # parallel or inf
            return 'inf' if p1.x == p3.x else -1
        elif p4.x - p3.x == 0:  # orthogonal
            return (p3.x, p1.y)
        else:  # crosses vertical
            return (
                float(F((p1.y - p3.y)*(p4.x - p3.x), (p4.y - p3.y)) + F(p1.x)),
                p1.y
    else:  # Both under degree to ox and oy.







p1 = P(*[int(i) for i in input().strip().split(' ')])
p2 = P(*[int(i) for i in input().strip().split(' ')])
p3 = P(*[int(i) for i in input().strip().split(' ')])
p4 = P(*[int(i) for i in input().strip().split(' ')])

print(intersection(p1, p2, p3, p4))
