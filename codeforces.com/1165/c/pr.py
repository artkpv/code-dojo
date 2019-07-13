#!python3
n = int(input().strip())
s = input().strip()
deletions = 0
out = []
i = 0
j = 1
while True:
    if not (i <= j < n):
        deletions += (n-i)
        break
    if s[i] == s[j]:
        deletions += 1
        j += 1
    else:  # good
        out += [s[i], s[j]]
        i = j + 1
        j = i + 1
print(deletions)
print(''.join(out))

"""
Ex 1
4
good
i j dels out
0 1 0
2 3 go
4 5 good
> 
0
good

Ex 2
4
aabc
i j dels out




"""