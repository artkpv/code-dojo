# Hackerrank. https://www.hackerrank.com/challenges/insertionsort1/problem
n = int(input().strip())
A = [int(i) for i in input().strip().split(' ')]

i = n - 1  # unsorted el.
v = A[i]
while i > 0 and A[i - 1] > v:
    A[i] = A[i - 1]
    i -= 1
    print(' '.join(str(el) for el in A))

# i - 1 points to the last el. less or equal to v
A[i] = v
print(' '.join(str(el) for el in A))

