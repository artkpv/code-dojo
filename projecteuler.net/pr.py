
"""

Sq. spiral. 

Unknown: length of sq spiral when the prime ration falls below 10% for the first time?

nums - 1 2 ... 
diagonal by indx
perimeter = (sz - 1)* 4
diagonal nums: 

I1 BF
Iter all diagonal elems per size of square. Calc the ration.

"""

from tqdm import tqdm

size = 7
primes = 8
last_n = 49

def is_prime(n):
    for k in range(2, int(n**0.5 + 1)):
        if n % k == 0:
            return False
    return True

def gen():
    while True:
        yield 

for _ in tqdm(gen()):
    if primes / (2*size - 1) < 0.1:
        break
    size += 2
    for i in range(4):
        last_n += size - 1
        if is_prime(last_n):
            primes += 1

print(size)


