#!python3

x = 0
stack = []
MAX = 2**32-1

def last(): return stack[-1] if stack else 1

for _ in range(int(input().strip())):
    line = input().strip()
    if line.startswith('for'):
        times = int(line.split(' ')[1])
        if last() * times > MAX:
            stack += [0]
        else:
            stack += [last() * times]
    elif line.startswith('end'):
        del stack[-1]
    elif line.startswith('add'):
        if last() == 0:
            print('OVERFLOW!!!')
            exit()
        x += last()
        if x > MAX:
            print('OVERFLOW!!!')
            exit()
print(x)
