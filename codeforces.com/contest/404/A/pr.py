#!python3

n = int(input())

dc = None  # diagonal char
ndc = None  # non diagonal char
for i in range(n):
    line = input().strip()
    if not dc or not ndc:
        dc = line[0]
        ndc = line[1]
        if dc == ndc:
            print("NO")
            exit()
    for j in range(n):
        if j == i or j == n-i-1:
            if line[j] != dc:
                print("NO")
                exit()
        else:
            if line[j] != ndc:
                print("NO")
                exit()
print("YES")


