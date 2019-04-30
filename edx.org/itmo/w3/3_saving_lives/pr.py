#!python3

fr = open('input.txt')
fw = open('output.txt', 'w')

n = int(fr.readline().strip())
types = []
for i in range(n):
    types += [tuple(int(ii) for ii in fr.readline().strip().split(' '))]
types.sort(key=lambda i: i[0])
w = int(fr.readline().strip())
lives = 0
i = n-1
while w > 0 and i >= 0:
    taken = min(w, types[i][1])
    lives += types[i][0] * taken
    w -= taken
    i -= 1
fw.write("%d\n" % lives)
