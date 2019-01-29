#!python3

for query in range(int(input().strip())):
    n = int(input().strip())
    s = input().strip()
    if int(s[0]) >= int(s[1:]):
        print("NO")
    else:
        print("YES")
        print("2")
        print(s[0], s[1:])
