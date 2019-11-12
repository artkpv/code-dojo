#!python3

alpha = 'abcdefghijklmnopqrstuvwxyz'
i = 0
s = input().strip()
moves = 0
for c in s:
    j = alpha.index(c)
    moves += min(
        abs(i - j),
        abs(len(alpha) + j - i),
        abs(len(alpha) + i - j)
    )
    i = j
print(moves)

