#!python3
s = input().strip()

for i in range(len(s)):
    for j in range(len(s)-1, i, -1):
        for k in range(0, (j-i+1)//2):
            if s[i+k] != s[j-k]:
                print(j-i+1)
                exit()
print(0)
