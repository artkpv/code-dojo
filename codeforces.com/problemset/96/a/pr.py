#!python3

s = input().strip()
counter = 1
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        counter += 1
    else:
        if counter >= 7:
            break
        counter = 1

print("YES" if counter >= 7 else "NO")
