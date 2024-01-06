'''
Quadratic Primes
Problem 27
Euler discovered the remarkable quadratic formula:
n2 + n + 41
It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when
n = 41, 412 + 41 + 41 is clearly divisible by 41.
The incredible formula n2 − 79n + 1601 was discovered, which produces 80 primes for the
consecutive values 0 ≤ n ≤ 79. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:
n2 + an + b, where |a| < 1000 and |b| ≤ 1000
where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum
number of primes for consecutive values of n, starting with n = 0.
'''

def is_prime(a):
    if a < 2:
        return False
    if a % 2 == 0:
        return False
    for b in range(3, int(a**0.5)+1, 2):
        if a % b == 0:
            return False
    return True

def max_chain(a, b):
    n = 0 
    while is_prime(n*n + a * n + b):
        n += 1
    return n

a = -79
b = 1601
print(max_chain(a,b), a, b)

best_a = None
best_b = None
longest = -1
for a in range(-999,1000):
    for b in range(-1000, 1001):
        n = max_chain(a, b)
        if longest < n:
            print(longest, a, b)
            longest = n
            best_a = a
            best_b = b
print(best_a * best_b)


'''
Answer 
-59231
'''
