#!python3
t = int(input().strip())
for test in range(t):
    s,a,b,c = [int(i) for i in input().strip().split(' ')]
    bars = int(s/c)
    bars += int(bars/a)*b
    print(bars)


