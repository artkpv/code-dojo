"""
https://projecteuler.net/problem=69
Totient maximum
Problem 69
Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1	1	2
3	1,2	2	1.5
4	1,3	2	2
5	1,2,3,4	4	1.25
6	1,5	2	3
7	1,2,3,4,5,6	6	1.1666...
8	1,3,5,7	4	2
9	1,2,4,5,7,8	6	1.5
10	1,3,7,9	4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.


----------------------

NEXT:
    - Видимо, нужно разложить на множители эти числа, потом по формуле :
\varphi(n)=n\prod_{p\mid n}\left(1-\frac{1}{p}\right),\;\;n>1,
    - seep up:
 n=3 in 0s (0 n/s)max found: n=6 phi=2 n/phi=3.0
max found: n=30 phi=8 n/phi=3.75
max found: n=210 phi=48 n/phi=4.375
 n=2003 in 2s (1001 n/s)max found: n=2310 phi=480 n/phi=4.8125
 n=11856 in 90s (131 n/s)

See
https://ru.wikipedia.org/wiki/Функция_Эйлера  (Euler's totient function)

"""

def coprime(k, v):
    if v == 1:
        return True
    if v == 0:
        return False
    return coprime(v, k % v)


def phi(n):
    count = 1  # for 1
    for i in range(2, n):
        if coprime(n, i):
            count += 1
    return count



max_n = 2
max_n_div_phi = 2

n = 3

# to print progress:
import timeit, sys, threading
start = timeit.default_timer()
def print_progress():
    global n
    time = int(timeit.default_timer() - start)
    speed = n // time if time > 0 else 0
    sys.stdout.write("\r n={} in {}s ({} n/s)".format(n, time, speed ))
    threading.Timer(1, print_progress).start()
print_progress()

while True:
    if n == 1_000_000 + 1:
        break
    p = phi(n)
    if max_n_div_phi < (n / p):
        max_n_div_phi = (n / p)
        max_n = n
        print('max found: n=' + str(n) + ' phi=' + str(p) +' n/phi=' + str(n/p))
    n += 1

print(max_n)

