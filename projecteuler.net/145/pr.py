"""

n - num of all numbers, 10^9
w - width of a number, 9

I1 BF

T: n * w ~ 10^10

I2 Cache reversed not to check again later.

I3

E + O = O
E + E = E
O + O = E
?
But sum

I4
Binary?

"""

from tqdm import tqdm

def solve_1():
    def iter_int(i):
        while i > 0:
            yield i % 10
            i //= 10

    cache = {}

    last_len = None

    def is_reversible(n):
        nonlocal last_len
        if n in cache:
            return cache[n]
        if n % 10 == 0:
            return False
        digits = list(iter_int(n))
        if last_len is not None and len(digits) > last_len:
            cache.clear()
        iter_n = iter_int(n)
        res = all(
            (l + r) % 2 == 1
            for l, r in zip(list(iter_n), list(reversed(iter_n)))
        )
        cache[r_n] = res
        last_len = len(digits)
        return res


    print(sum(tqdm(
        int(is_reversible(n))
        for n in range(1,10**9+1)
    )))

def solve_2():
    raise Error('wrong: summation')
    n = [1] 
    
    def inc(n):
        for i in range(len(n)):
            if n[i] < 9:
                n[i] += 1
                return n
            n[i] = 0
        n.append(1)
        return n

    def is_r(n):
        return all((l + r) % 2 == 1 for l,r in zip(n, reversed(n)))

    count = 0
    bar = tqdm()
    while len(n) <= 9:
        if is_r(n):
            count += 1
        inc(n)
        bar.desc = f"len n {len(n)}, last {n[-1]}, count {count}"
        bar.update()
    return count

solve_2()
