

with open('input.txt') as f:
    a,b,c = [int(i) for i in f.readline().strip().split(' ')]
    with open('output.txt', mode='w') as fw:
        fw.write(str((a+b+c)/6))


