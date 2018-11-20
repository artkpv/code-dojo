#!python3

n = int(input().strip())
clouds = [int(i) for i in input().strip().split(' ')]
min_ = [0] * n
INF = 99999
for i in range(1, n):
    if clouds[i] == 0:
        min_[i] = min(
            min_[i-2] if i > 1 and clouds[i-2] == 0 else INF,
            min_[i-1] if clouds[i-1] == 0 else INF
            ) + 1
    else:
        min_[i] = INF
print(min_[n-1])