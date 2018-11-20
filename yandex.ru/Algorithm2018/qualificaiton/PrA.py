#!python3

lucky = [int(i) for i in input().strip().split(" ")]
n = int(input().strip())
for i in range(n):
    bilet = [int(i) for i in input().strip().split(" ")]
    hits = 0
    for j in bilet:
        if j in lucky:
            hits += 1
        if hits >= 3:
            break
    print("Lucky" if hits >= 3 else "Unlucky")


