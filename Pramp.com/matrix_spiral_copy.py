#!python3
"""

1)
n - rows , m - cols
r,c = f(i) , i=0..(n*m)-1

rr - taken rown
cc - taken cols


Time ~n*m; space ~n*m


00 01 02
10 11 12

00 01 02
10 11 12
20 21 22


Exp1
1 2
3 4
5 6

1 2 4 6 5 3

i - 0..m-1
j -

looping of frames


>>> a = [1]
>>> a2 = [2,3]
>>> a+a2
[1, 2, 3]
>>>


"""

def iterate_border(mat, i, j, n, m):
  a = []
  if m > 0:
    for k in range(m):  # right
      a += [mat[i][j+k]]
  if n > 1:
    for k in range(n-1):  # down
      a += [mat[i+1+k][j+m-1]]
  if n > 1 and m > 1:
    for k in range(m-1):  # left
      a += [mat[i+n-1][j+m-2-k]]
  if n > 1 and m > 1:
    for k in range(n-2):  # up
      a += [mat[i+n-2-k][j]]
  return a

def spiral_copy(mat):
  n, m = len(mat), len(mat[0])  # n - rows, m - cols
  i, j = 0, 0
  arr = []
  while n > 0 and m > 0:
    arr += iterate_border(mat, i, j, n, m)
    n -= 2
    m -= 2
    i, j = i+1, j+1
  return arr


def test1():
    inputMatrix  = [ [1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

    a = spiral_copy(inputMatrix)
    print(a)
    assert( a == [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12])


def test2():
    a = spiral_copy([[1,2]])
    print(a)
    assert(a == [1,2])

if __name__ == '__main__':
    test1()
    test2()
