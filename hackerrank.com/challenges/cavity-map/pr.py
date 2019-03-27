#!python3

rows = int(input().strip())
field = []
isbadinput = False
for i in range(rows):
    line = input().strip()
    if len(line.split(' ')) > 1:
        field += [[int(num) for num in line.split(' ')]]
        isbadinput = True
    else:
        field += [[int(c) for c in line]]

cols = len(field[0])
INF = 9999

for i in range(rows):
    for j in range(cols):
        if 0 < i < rows - 1 and 0 < j < cols - 1:
            if all(field[i][j] > field[i+ii[0]][j+ii[1]]
                for ii in ((0,1), (0,-1), (1,0), (-1,0))):
                field[i][j] = INF
    print((' ' if isbadinput else '').join(str(e) if e != INF else 'X' for e in field[i]))
