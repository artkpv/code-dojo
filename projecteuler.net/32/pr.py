from itertools import permutations
from time import time

def digits_gen(k):
    digits = list(range(1, k+1))
    i = len(digits) - 1
    while i > -1:
        for p in permutations(digits, k):
            yield p
        if digits[i] == 9 or (i + 1 < len(digits) and digits[i] + 1 == digits[i+1]):
            i -= 1
        if i > -1:
            digits[i] += 1

def atoi(a):
    res = 0
    for e in reversed(a):
        res = res * 10 + e
    return res

pand_sum = 0
start = time()
for k in range(3, 10):
    print(f'{time() - start}s {k}')
    count = 0
    for digits in digits_gen(k):
        if count % 1000_000 == 0:
            print(f'{int(time() - start)}s {k} {count} {pand_sum} {digits}')
        for mi in range(1, k-1):
            for ei in range(mi+2, k):
                count += 1
                prod = atoi(digits[ei:])
                is_pan_identity = atoi(digits[:mi]) * atoi(digits[mi:ei]) == prod
                if is_pan_identity:
                    pand_sum += prod
print(pand_sum)





