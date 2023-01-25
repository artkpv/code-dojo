
def f(n):
    res = [1]
    d = 2
    while d * d <= n:
        q, r = divmod(n, d)
        if r == 0:
            res += [d]
            res += [q]
        d += 1
    return sum(res)

hs = {}
amicables = set()
for i in range(1, 10001):
    if i not in hs:
        hs[i] = f(i)
    ii = hs[i]
    if ii not in hs:
        hs[ii] = f(ii)
    if hs[ii] == i and i != ii:
        amicables.add(i)
        amicables.add(ii)

print(f(220))
print(f(284))
print(sum(amicables))



