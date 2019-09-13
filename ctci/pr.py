#!python3

n = int(input().strip())
field = [input().strip() for _ in range(n)]

def rows():
    for r in range(n):
        yield field[r]

def cols():
    for c in range(n):
        yield [row[c] for row in field]

def diagonals():
    yield [field[i][i] for i in range(n)]
    yield [field[i][-i-1] for i in range(n)]

xwins = 0
owins = 0
for generator in rows(), cols(), diagonals():
    for line in generator:
        xnum = sum(1 for c in line if c == 'X')
        onum = n - xnum
        if xnum == n:
            xwins += 1
        elif onum == n:
            owins += 1
if xwins == owins:
    print("DRAW")
else:
    print("X" if xwins > owins else "O")


