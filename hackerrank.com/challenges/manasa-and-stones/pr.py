#!python3

for test in range(int(input().strip())):
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())
    result = set()
    for i in range(n):
        result.add(sum([a] * i + [b] * (n-1-i)))
    print(' '.join(str(num) for num in sorted(result)))

