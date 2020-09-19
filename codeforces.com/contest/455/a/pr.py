#!python3

"""
1 2 1 3 2 2 2 2 3

1 1 2 2 2 2 2 3 3

Ex2
1 2 3
2 5 2
dp
0 2 (2,0+10) (10,2+6)



I1 BF
C(A) - best points for A array
C(A) = max { C(A \ a_i \ all a_i-1, all a_i+2), i=1..n }

C(n) = (n-1)*C(n-1)

n^lg(1, n-1)


I2 DP


"""

from collections import Counter

n = int(input().strip())
a = [int(i) for i in input().strip().split(' ')]
count = Counter(a)
numbers = list(sorted(count.keys()))
dp = [0, count[numbers[0]] * numbers[0]]
for i in range(1, len(numbers)):
    if numbers[i-1] + 1 == numbers[i]:
        dp += [max(dp[-1], dp[-2] + count[numbers[i]] * numbers[i])]
    else:
        dp += [dp[-1] + count[numbers[i]] * numbers[i]]
print(dp[-1])


