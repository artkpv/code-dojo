"""

The Fibonacci sequence is defined by the recurrence relation:

, where and

    .

Hence the first

terms will be:

The
th term,

, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain

digits?
"""

a = 1
b = 1

def l(x):
    n = 0
    while x > 0:
        x //= 10
        n += 1
    return n

idx = 2
while l(b) < 1000:
    t = b
    b = a + b
    a = t
    idx += 1
print(idx, b)
