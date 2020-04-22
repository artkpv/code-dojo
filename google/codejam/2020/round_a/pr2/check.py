#!python3 

N = 50
pascal = [[None] * (N+1) for _ in range(N+1)]
pascal[1][1] = 1
for r in range(2, N):
    pascal[r][1] = 1
    pascal[r][r] = 1
    for c in range(2, r):
        pascal[r][c] = pascal[r-1][c-1] + pascal[r-1][c]

casenum = input()
sum_ = 0

while True:
    try:
        in_ = input()
    except:
        break

    if not in_:
        break

    if in_.startswith("Case"):
        print(sum_)
        sum_ = 0
        continue

    r, c = [int(e) for e in in_.strip().split(' ')]
    if r == 1 or r == c:
        sum_ += 1
    else:
        if len(pascal) <= r:
            raise Exception("out of range")
        sum_ += pascal[r][c]

print(sum_)


