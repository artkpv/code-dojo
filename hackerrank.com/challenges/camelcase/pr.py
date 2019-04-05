#!python3

s = input('').strip()
count = 1
for c in s[1:]:
    if c.isupper():
        count += 1
print(count)
