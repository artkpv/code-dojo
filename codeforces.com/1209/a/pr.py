#!python3
n = int(input().strip())
A = [int(i) for i in input().strip().split(' ')]
D = A.copy()
for i in range(n):
    for j in range(i+1, n):
        if D[i] == D[j]:
            continue
        d = min(D[i], D[j])
        if A[i] % d == 0:
            D[i] = d
        if A[j] % d == 0:
            D[j] = d
print(len(set(D)))


