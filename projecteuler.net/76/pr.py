'''
I1. BF. Visit all leaves while tracking upper path (stack).

'''
def solve(n=100):
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
    print(visited)
    return res


if __name__ == '__main__':
    print(solve(100))
