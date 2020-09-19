#!python3

for _ in range(int(input().strip())):
    b, p, f = [int(i) for i in input().strip().split(' ')]
    h, c = [int(i) for i in input().strip().split(' ')]
    if h >= c:
        hmade = min(b//2, p)
        pr = hmade * h
        b -= hmade * 2
        cmade = min(b//2, f)
        pr += cmade * c
    else:
        cmade = min(b//2, f)
        pr = cmade * c
        b -= cmade * 2
        hmade = min(b//2, p)
        pr += hmade * h
    print(pr)




