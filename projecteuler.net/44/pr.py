# https://projecteuler.net/problem=44
def solve():
    MAX = 100000
    min_p = (None, None)
    min_d = float('inf')
    for i in range(1, MAX-1):
        for j in range(i+1, MAX):
            pi = i*(3*i - 1) // 2
            pj = j*(3*j - 1) // 2
            s = pi + pj
            d = abs(pi - pj)
            if isp(s) and isp(d) and min_d > d:
                min_p = (i, j)
                min_d = d
                print(f'found {i=} {pi=}, {j=} {pj=}, {min_d=}')

def isp(p):
    sqrtd = (24 * p + 1)**.5
    return sqrtd % 1.0 == 0.0 and (1 + sqrtd) % 6 == 0

if __name__ == '__main__':
    solve()
