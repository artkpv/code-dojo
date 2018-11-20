#!python3
n = int(input().strip())
scores = [int(i) for i in input().strip().split(' ')]
count = 0
sum_ = sum(scores)
i = 0
EPSILON = 0.00000000001
while (sum_/n - 4.5) < EPSILON and i < n:
    if scores[i] != 5:
        sum_ += 5 - scores[i]
        count += 1
    i += 1

if sum_/n < 4.5:
    raise 'invalid input'
print(count)
