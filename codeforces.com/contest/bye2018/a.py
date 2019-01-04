#!python3
"""
y, b, r
1,2,3 <= 100

rr = max(y+2, b+1, r)
bb = rr-1
yy = bb-1

Ex1.
8 13 9 > 24 
7 8 9 = 24

"""

y,b,r = [int(i) for i in input().strip().split(' ')]
yy = min(y, b-1, r-2)
bb = yy+1
rr = bb+1
print(rr+bb+yy)