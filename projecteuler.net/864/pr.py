
"""
<p>Let $C(n)$ be the number of squarefree integers of the form $x^2 + 1$ such that $1 \le x \le n$.</p>

<p>For example, $C(10) = 9$ and $C(1000) = 895$.</p>

<p>Find $C(123567101113)$.</p>

"""

def is_squarefree(x):
    x = x**2 + 1
    primes = set()
    for p in range(2, int(x**.5)+1):
        while x % p == 0:
            if p in primes:
                return False
            primes.add(p)
            x //= p
    return True


def C(n):
    count = 0
    for x in range(1, n+1):
        if is_squarefree(x):
            count +=1
    return count

if __name__ == '__main__':
    import sys
    n = int(sys.argv[1])
    print(C(n))
