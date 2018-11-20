#!python3

s = input().strip()
c = ['ABC','ACB','BAC','BCA','CAB','CBA']
for i in range(len(s)):
    if s[i:i+3] in c:
        print('Yes')
        exit()
print('No')
