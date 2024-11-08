'''
Longest Collatz Sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:turrnk
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1.
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has
not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def chain_n(n):
    steps = 1
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        steps += 1
    return steps

max_n = -1
max_n_i = -1
for i in range(2, 1_000_000):
    cn = chain_n(i)
    if max_n < cn:
        max_n = cn
        max_n_i = i

print(max_n_i)  # 837799

