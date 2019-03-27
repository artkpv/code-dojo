#!python3

"""


"""

GOOD = 1
BAD = 0

def findplus(field):
    max_length = None
    for i, row in enumerate(field):
        for j, cell in enumerate(row):
            if cell == GOOD:
                length = 1
                while isfit(length + 1, i, j, field):
                    length += 1
                if not max_length or max_length < length:
                    max_length = length
    return (max_length-1)*4 + 1

def fillplus(length, row, col, field, filler):
    # length - radius from middle
    field[row][col] = filler
    for i in range(1, length):
        for x,y in ((0,i), (0,-i), (i,0), (-i,0)):
            if (0 <= row + x < len(field) and
                0 <= col + y < len(field[0])):
                field[row+x][col+y] = filler

def isfit(length, row, col, field):
    # length - radius from middle
    if field[row][col] == BAD:
        return False
    for i in range(1, length):
        for x,y in ((0,i), (0,-i), (i,0), (-i,0)):
            if not (0 <= row + x < len(field)):
                return False
            if not (0 <= col + y < len(field[0])):
                return False
            if field[row + x][col+y] == BAD:
                return False
    return True

def printit(field):
    print('\n'.join(''.join(str(e) for e in row) for row in field))
    print('')

#
# RUN:
#

n, m = [int(i) for i in input().strip().split(' ')]
field = []
for row in range(n):
    field += [[1 if c == 'G' else 0 for c in input().strip()]]

result = 0
for row in range(n):
    for col in range(m):
        if field[row][col] == 1:
            first = 1
            while isfit(first, row, col, field):
                fillplus(first, row, col, field, BAD)
                second = findplus(field)
                fillplus(first, row, col, field, GOOD)
                lenfirst = (first-1)*4+1
                if lenfirst * second > result:
                    result = lenfirst * second
                first += 1
            # first now does not fit
print(result)

