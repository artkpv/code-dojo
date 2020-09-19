#!python3

n = int(input().strip())
a = [int(i) for i in input().strip().split(' ')]
even = sum(1 for c in a if c % 2 == 0)
print(min(even, n - even))

