import itertools
import math
T = int(input().strip())

for t in range(T):
    n, H, A = (int(i) for i in input().strip().split(' '))  # (1 ≤ n ≤ 105, 1 ≤ H, A ≤ 109).
    persons = []
    for p in range(n):
        persons += [[int(i) for i in input().strip().split(' ')]]  #  (1 ≤ hi, ai ≤ 109).

    maxLeft = -1
    for p in itertools.permutations(persons, len(persons)):
        health = H
        left = len(p)
        for i in range(len(p)):
            h, a = p[i]
            times = math.ceil(h / A)
            health -= times * a
            if health <= 0:
                break
            left -= 1
        if left > maxLeft:
            maxLeft = left
    print(n - maxLeft if maxLeft > 0 else -1)

