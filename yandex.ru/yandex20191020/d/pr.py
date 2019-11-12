#!python3

n = int(input().strip())
byend = []
for _ in range(n):
    s, f, w = [int(i) for i in input().strip().split(' ')]
    byend.append((s, f, w))
byend.sort(key=lambda e: e[1])
dp = {}
def c(i, j):
    if i == j:
        return 0
    if (i, j) not in dp:
        lo = byend[i][1] if 0 <= i else -1
        hi = byend[j][0] if j < n else float('inf')
        optimal = 0
        for k in range(n):
            a = byend[k]
            if not (lo <= a[0] and a[1] <= hi):
                continue
            optimal = max(optimal, a[2] + c(i, k) + c(k, j))
        dp[(i, j)] = optimal
    return dp[(i, j)]

print(c(-1, n))

