#!python3
n = int(input().strip())
a = [int(i) for i in input().strip().split(' ')]
a.sort()
days = 0
for i in range(n):
    if a[i] >= days+1:
        days += 1
print(days)

"""
3 1 4 1
1 1 3 4
days i 
0    0 
1    0
1    1

    


"""
