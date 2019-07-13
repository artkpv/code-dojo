#!python3
n, x, y = [int(i) for i in input().strip().split(' ')]
s = input().strip()
changes = 0
i = 0
while i < x:
    if i == y:
        if s[-i-1] != '1':
            changes += 1
    elif s[-i-1] == '1':
        changes += 1
    i += 1
print(changes)

"""
5 2
11010100101
i changes
0 0
1 1 
2 1
3 1
4 1
5 1
end
res: 1

5 1
11010100101
0 0


"""