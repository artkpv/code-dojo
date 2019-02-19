#!python3
n = int(input().strip())
adj = { 0:(4,6), 1:(6,8), 2:(7,9), 3:(4,8), 4:(3,9,0),
        5:tuple(), 6:(1,7,0), 7:(2,6), 8:(1,3), 9:(2,4)}
def count(start, n):
    if n < 0:
        return -1
    current = [0] * 10
    prev = [1] * 10
    hops = 1
    while hops <= n:
        current = [0] * 10
        hops += 1
        for i in range(10):
            for j in adj[i]:
                current[i] += prev[j]
        prev = current
    return current[start]


res = 0
for i in range(10):
    if i == 5:
        res += 1
    else:
        res += count(i, n)
print(res)
