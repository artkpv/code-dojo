#!python3
"""
a + b + c
a + b
a + c
b + c
"""
numbers = [int(i) for i in input('').strip().split(' ')]
abcsum = max(numbers)
del numbers[numbers.index(abcsum)]
a_b = min(numbers)
a = abcsum - a_b
b = a_b - a
del numbers[numbers.index(a_b)]
b = numbers[0] - a
c = abcsum - a - b
print(a, b, c)
