"""

"""

#!python3

import sys

INT_MIN = -99999999 # ? -250 <= Ai <= 250

def matrixLandTD(A, D, row, l, r): # wrong
    global INT_MIN
    if row < 0:
        return 0
    if l > r:
        return 0
    if D[row] == None:
        cols = len(A[0])
        D[row] = [INT_MIN] * cols
        # iterate all intervals:
        for i in range(cols):
            sum_ = 0
            for j in range(i, cols):
                sum_ += A[row][j]  # sum of all cells
                max_upper = matrixLandTD(A, D, row-1, i, j)
                interval_max = sum_ + max_upper
                for k in range(i, j+1):
                    if D[row][k] < interval_max:
                        D[row][k] = interval_max

    return max(D[row][l:r+1])

def matrixLand(A):
    global INT_MIN
    rows = len(A)
    cols = len(A[0])
    D = [None] * rows  # B[1] for A[0], additional to optimize
    res = matrixLandTD(A, D, rows-1, 0, cols-1)
    # print(D)
    return res

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    A = []
    for A_i in range(n):
       A_t = [int(A_temp) for A_temp in input().strip().split(' ')]
       A.append(A_t)
    result = matrixLand(A)
    print(result)
