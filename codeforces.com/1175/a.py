#!python3
import math

for test in range(int(input().strip())):
    n, k = [int(i) for i in input().strip().split(' ')]
    count = 0
    while n > 0:
        if n % k**5 == 0:
            n //= k**5
            count += 5
        elif n % k == 0:
            n //= k
            count += 1
        else:
            count += n % k
            n -= (n % k)
    print(count)