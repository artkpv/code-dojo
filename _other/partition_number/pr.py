
def partition(n):
    s = [(n, n)]
    res = 0
    while s:
        nn, m = s.pop()
        if nn < 0:
            continue
        if nn == 0 or m == 1:
            res += 1
        else:
            s += [(nn, m - 1), (nn - m, m)]
    return res


for n in range(1, 100):
    print(n, partition(n))

