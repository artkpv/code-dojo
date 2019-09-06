#!python3

for _ in range(int(input().strip())):
    n = int(input().strip())
    C = [int(i) for i in input().strip().split(' ')]
    count = 0
    min_ = C[-1]
    for i in range(n-2, -1, -1):
        if C[i] > min_:
            count += 1
        else:
            min_ = C[i]
    print(count)

