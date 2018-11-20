def printm(A):
    for i in range(len(A)):
        print(' '.join(map(str, A[i])))

t = int(input())
for test in range(t):
    n, m = map(int, input().strip().split(' '))

    A = []
    for i in range(n):
        A.append(list())
        for j in range(m):
            A[i].append(list())

    """
    6 5
    4 3
    2 1

    6 5 3
    4 2 1

    6 5 4 3 2 1

    4 3
    2 1

    9 8 6
    7 5 3
    4 2 1

    6
    5
    4
    3
    2
    1

    """

    i, j = 0, 0
    r = 0
    for g in range(n*m, 0, -1):
        A[i][j] = g
        if i + 1 >= n or j - 1 < 0 : # bottom or left side:
            r += 1
            # first seat in next row:
            if r < m:  # have space at right at first
                i, j = 0, r
            else:
                i, j = r - m + 1, m - 1
        else:
            i, j = i + 1, j - 1  # filing current angled row

    printm(A)


