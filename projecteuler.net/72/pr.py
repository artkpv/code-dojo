"""
https://projecteuler.net/problem=72

"""
from tqdm import tqdm
from fractions import Fraction as F

d = 1_000_000

is_prime = [True] * (d+1)  # Is prime
p = 2
while p <= d:
    assert is_prime[p] == True
    i = 2
    while p*i <= d:
        is_prime[p*i] = False
        i += 1
    p += 1
    while p <= d and not is_prime[p]:
        p += 1

print(' '.join(str(p) for (p, isp) in enumerate(is_prime[:100]) if isp))

phi = [F(n) for n in range(d+1)]
for p in tqdm(range(2, d+1)):
    if not is_prime[p]:
        continue
    phi[p] = p - 1
    for i in range(2*p, d+1, p):
        phi[i] = phi[i] * (p-1) // p

print(8, sum(phi[i] for i in range(2, 9)))

res = sum(phi[i] for i in range(2, d+1))
print(res, float(res))  # 303964152391  WRONG?!
for n in range(2, 15):
    print(n, sum(phi[i] for i in range(2, n+1)))

