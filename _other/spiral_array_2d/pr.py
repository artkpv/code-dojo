
'''
3 
123
894
765

1
1

2
12
43


...

I1
vector

'''


def spiral(n):
    if n == 1:
        return [[1]]
    a = [[None] * n for _ in range(n)]
    a[0][0] = 1
    i, j = 0, 0
    v = (0,1)
    while True:
        for u in (v, (0, 1), (1, 0), (0, -1), (-1, 0)):
            ii, jj = i + u[0], j + u[1]
            if 0 <= ii < n and 0 <= jj < n and a[ii][jj] is None:
                break
        else:
            break
        a[ii][jj] = a[i][j] + 1
        i, j = ii, jj
    return a


'''

2
12
43

i 1
j 0
vector 0 0
< 


'''

assert spiral(1) == [[1]]
assert spiral(2) == [[1, 2], [4, 3]] , spiral(2)
assert spiral(3) == [[1, 2, 3],[8, 9, 4], [7, 6, 5]], spiral(3) 
print('\n'.join(' '.join(str(e) for e in l) for l in spiral(8)))
print('pass')

