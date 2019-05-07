#!python3
n, m = [int(i) for i in input().strip().split(' ')]
A = []
for _ in range(n):
    A += [[int(i) for i in input().strip().split(' ')]]
B = []
for _ in range(n):
    B += [[int(i) for i in input().strip().split(' ')]]


def get(M, i, j):
    if not (0 <= i < len(M)) or not (0 <= j < len(M[0])):
        return None
    return M[i][j]


def choose(A, B, i, j):
    max_a = max(get(A, i-1, j) or 0, get(A, i, j-1) or 0)
    max_b = max(get(B, i-1, j) or 0, get(B, i, j-1) or 0)
    if max_a <= max_b:
        A[i][j], B[i][j] = min(A[i][j], B[i][j]), max(A[i][j], B[i][j])
    else:  # max_a > max_b
        A[i][j], B[i][j] = max(A[i][j], B[i][j]), min(A[i][j], B[i][j])
    if not max_a < A[i][j]:
        return False
    elif not max_b < B[i][j]:
        return False
    return True


for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        if not choose(A, B, i, j):
            print("Impossible")
            exit()

print("Possible")
exit()

