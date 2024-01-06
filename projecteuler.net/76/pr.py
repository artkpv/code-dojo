'''
I1. BF. Visit all leaves while tracking upper path (stack)?
But overlapping?
5:
2 + 1 + 2
1 + 2 + 2

I2 BF. Divisions till mid?
2 divisions: 1+4, 2+3, (omit 3+2)
3 divisions: 1+1+3, 1+2+2,  
4: 2+1+1+1
and so on.
That is given a number n and k how many unique k divisions we can make?

I3 Merging numbers
At begining: 1x5. Then 4 items can be by merging two ones: 2x1 1x3. Then 3 items by merging 2 with any 1 or by merging 1 and 1 (any group >1 with any group): 2x2 1x1 or 3x1 1x2. Then for that repeat. So tra


'''
from collections import Counter
def solve(n):
    ways = [[0]*(n+1)]
    ways[0][1] = 2  # 1+1
    for i in range(2,n+1):
        nways = []
        for w in ways:
            if sum(e for e in w) == 2:
                for a, c in enumerate(w):
                    if c > 0:
                        nw = w.copy()
                        nw[a] -= 1
                        nw[a+1] = 1
                        nways.append(nw)
            w[1] += 1
            nways.append(w)
        ways = nways
        print(i)
        for w in ways:
            print(' + '.join(f"{j}*{a}" for (j,a) in enumerate(w) if a > 0))
    return len(ways)



def solve_wrong(n):
    ways = set([
        ((1,2),) # For 2 it is 1+1.
    ])
    for i in range(2,n+1):
        n_ways = []
        for way in ways:
            # Convert to Counter:
            way = Counter({a:k for (a,k) in way})
            # Two addends into new way (1+1 -> 2+1, e.g.):
            if sum(way.values()) == 2:
                for (a, k) in way.items():
                    n_way = way.copy()
                    n_way[a+1] += 1
                    n_ways.append(n_way)
            n_way = way.copy()
            n_way[1] += 1  # All prev are given 1.
            n_ways.append(n_way)
        # Convert back to set of tuples:
        ways = set(
            tuple((a,k) for (a,k) in sorted(n_way.items()) )
            for n_way in sorted(n_ways)
        )
        print(ways)
    return len(ways)


def solveBF(n):
    counter = 0
    cache = {}
    def inc(d, k):
        d[k] = d.get(k, 0) + 1
    def dec(d, k):
        if k in d:
            if d[k] == 1:
                del d[k]
            else:
                d[k] -= 1
    def c(d, l):
        nonlocal counter
        counter += 1
        dfs = frozenset(sorted(d.items()))
        if dfs in cache:
            return 0
        res = 1
        skeys = sorted(d.keys())
        dl = len(skeys)
        for ki in range(dl):
            k = skeys[ki]
            if d[k] <= 1:
                continue
            for k2i in range(ki, dl):
                k2 = skeys[k2i]
                if d[k2] < 1:
                    continue
                k3 = k + k2
                dec(d, k)
                dec(d, k2)
                inc(d, k3)
                res += c(d, l+1)
                inc(d, k)
                inc(d, k2)
                dec(d, k3)
        cache[dfs] = res
        if counter % 100_000 == 0:
            print(counter, l, res, len(d), d)
        return res
    ans = c({1:n}, 0)
    return ans
    

def solveWRONG(n=100):
    visited = set()
    mem = {}
    def count(n, rest):
        k = tuple(sorted([n] + rest))
        if k in visited:
            return 0
        visited.add(k)
        res = 1  # n + rest
        for m in range(n-1, 0, -1):
            res += count(m, [n-m] + rest)
        mem[k] = res
        return res
    res = 0
    for m in range(n-1, 0, -1):
        res += count(m, [n-m])
    return res


if __name__ == '__main__':
    import sys
    print(solve(int(sys.argv[1])))
