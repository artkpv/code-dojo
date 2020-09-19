fw = open('c.inputmax.txt', 'w')
fw.write('25000\n')
for i in range(25_000):
    fw.write('(' * 10)
    fw.write(')' * 10)
    fw.write('\n')

