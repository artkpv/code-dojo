#!python3
"""

I1
46 free
46 41




 1
111
 12
 222
  2

 1
1112
 1222
   2
"""


def tryfill(field, i, j):
    cells = ((i, j), (i+1, j), (i+2, j), (i+1, j+1), (i+1, j-1))
    n = len(field)
    if any(not(0 <= row < n and 0 <= col < n
               and field[row][col] == '.')
           for row, col in cells):
        return False
    for row, col in cells:
        field[row][col] = '#'
    return True


n = int(input('').strip())
field = []
filled = 0
for _ in range(n):
    row = [c for c in input('').strip()]
    filled += sum(1 for c in row if c == '#')
    field += [row]


def fillme(field, filled):
    n = len(field)
    for i, row in enumerate(field):
        for j, cell in enumerate(row):
            if cell == '.':
                if not tryfill(field, i, j):
                    return False
                filled += 5
            if filled == n*n:
                return True
    return False


print("YES" if fillme(field, filled) else "NO")
