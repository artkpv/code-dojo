#!python3
"""
1<=h,w<=100
1<=a_ij<=100
> 3d surf. area

1)
Time: H*W*4

c_ij = 2 + cmp(i-1, j, i, j) + cmp(i-1,j-1, i,j) + ...  # 4 sides


E1
1 1
1
> 6

E2
3 3
1 3 4
2 2 3
1 2 4
> 60
?
left 2+3+4
behind 4+3+4
right 2+3+4
front 4+3+4
top 9
bottom 9
sum: 29+9+11+9=58?  NOT

1 4+8+12 24
2 6+2+6  14
3 4+5+13 22
= 60

"""

h,w = [int(i) for i in input().strip().split(' ')]
a = []
for i in range(h):
    a += [[int(i) for i in input().strip().split(' ')]]

def diff(i1, j1, i2, j2):
    global a, h, w
    if i1 < 0 or i1 >= h or j1 < 0 or j1 >= w:
        return a[i2][j2]
    if a[i1][j1] >= a[i2][j2]:
        return 0
    return a[i2][j2] - a[i1][j1]


cost = 0
for i in range(h):
    for j, v in enumerate(a[i]):
        cost += 2 + \
                diff(i-1, j, i, j) + \
                diff(i, j-1, i, j) + \
                diff(i+1, j, i, j) + \
                diff(i, j+1, i, j)
print(cost)




