
"""
https://projecteuler.net/problem=36
The decimal number,

(binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base
and base

.

(Please note that the palindromic number, in either base, may not include leading zeros.)


ANSWER: 
6255639  ?


I1
Remove 0 from right side. Check if palindrom.
Time : O(n^2) = ~10^12 --- WRONG
Time: O(n)  = ~10^6


I2
Skip non palindromic?

1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9 

I3
Dynamic prog.

For base 10:
For m positional = 9 * for m-2 positional
Plus padding at right till 7 positions occupied.

For 10^6 - 7 positions.

count(m)  - num of possible palindromic numbers with m non zero occupying up to 7 positions.

count(m) = 9 * count(m-2) * (n - m + 1)

I4
Bottom up
Base 10:
count 0 = 1
count 1 = 9 * 7 = 63
count 2 = 9 * 1 * 6 = 54
count 3 = 9 * 63 * 5 = 2835
count 4 = 9 * 54 * 4 = 1944
count 5 = 9 * 54 ...
1000000
0123456

jklnopuy;m,.
"""

def palindrom(m, b):
    # Skip traling zeros:
    while m > 0 and m % b == 0:
        m //= b
    # Get length
    l = 0
    x = m
    while x > 0:
        l += 1
        x //= b
    # Is palindrom:
    i = 0
    while i <= l // 2:
        if (m // b**i) % b != (m // b**(l-i-1)) % b:
            return False
        i += 1
    return True

def solve(n):
    res = 0
    for m in range(1, n):
        if palindrom(m, 10) and palindrom(m, 2):
            print(m, f"{m:b}")
            res += m
    return res


def solve_WRONG(n):
    ## TODO:  Bug fix. It should be both base 10 and base 2 palindroms.
    cache = {}
    def count(m, base):

        nonlocal n
        if (m, base) not in cache:
            print(m, base)
            if m < 1:
                cache[(m,base)] = 1
            else:
                cache[(m,base)] = (base - 1) * count(m - 2, base) * (8 - m + 1)
        return cache[(m,base)]
    res = 0
    for i in range(0, 8):
        res += count(i, 10)
    for i in range(0, 8):
        res += count(i, 2)
    return res

print(solve(1_000_000))


