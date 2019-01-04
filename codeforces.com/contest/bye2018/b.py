#!python3
n = int(input().strip())
sum_x, sum_y = 0,0
for i in range(2*n):
    xa, xb = [int(i) for i in input().strip().split(' ')]
    sum_x += xa
    sum_y += xb
print(sum_x//n, sum_y//n)


