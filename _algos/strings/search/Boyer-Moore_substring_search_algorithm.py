'''
BM ss search.

check from back. If i-th char not in pattern check from i+len(pattern). Thus time is Big Omega(N/M) and Big O(N*M)
'''


def bm_ss_search(t, p):
    n = len(t)
    m = len(p)
    if m == 0:
        return 0
    pchars = set(p)
    i = m-1
    while i < n:
        j = 0
        while j < m:
            if t[i-j] == p[-j-1]:
                j += 1
            else:
                break
        if j == m:
            return i-m+1
        elif t[i-j] in pchars:
            i += 1
        else:
            i = i-j+m
    return -1

def myassert(t, p, e):
    print(f'TEST: {t} text, {p} pattern')
    r = bm_ss_search(t, p)
    assert r == e, f'Expected {e}, result: {r}'
    print('PASS')

myassert("A", "BB", -1)
myassert("A", "A", 0)
myassert("B", "A", -1)
myassert("BB", "BB", 0)
myassert("ABRACADABRA", "ABRA", 0)
myassert("ABRACADABRA", "", 0)
myassert("ABRACADABRA", "ACA", 3)
myassert("ABRACADABRA", "ACAD", 3)
myassert("ABRACADABRA", "RAC", 2)




