#!python3

n = int(input().strip())
steps = input().strip()
altitude = 0
valleys = 0
for s in steps:
    if s == 'D' and altitude == 0:
        valleys += 1
    altitude += (1 if s == 'U' else -1)
print(valleys)
