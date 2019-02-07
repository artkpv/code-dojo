#!python3
n = int(input().strip())
radix = 100
a = [int(i) for i in input().strip().split(' ')]
counter = [0] * radix
for e in a:
    counter[e-1] += 1
print(n - max(counter))

