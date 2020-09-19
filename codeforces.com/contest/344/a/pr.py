#!python3

n = int(input().strip())
count = 1
left = input().strip()
for _ in range(1, n):
    right = input().strip()
    if left[1] == right[0]:
        count += 1
    left = right
print(count)

