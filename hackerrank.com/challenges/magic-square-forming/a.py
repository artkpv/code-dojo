#!python3
n = 3
a = []
for i in range(3):
    a += [[int(i) for i in input().strip().split(' ')]]

squares = [
[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
[[6, 1, 8], [7, 5, 3], [2, 9, 4]],
[[4, 9, 2], [3, 5, 7], [8, 1, 6]],
[[2, 9, 4], [7, 5, 3], [6, 1, 8]],
[[8, 3, 4], [1, 5, 9], [6, 7, 2]],
[[4, 3, 8], [9, 5, 1], [2, 7, 6]],
[[6, 7, 2], [1, 5, 9], [8, 3, 4]],
[[2, 7, 6], [9, 5, 1], [4, 3, 8]],
]

min_ = 1000000
for s in squares:
    dist = 0
    for r in range(n):
        for c in range(n):
            dist += abs(s[r][c] - a[r][c])
    if dist < min_:
        min_ = dist

print(min_)

