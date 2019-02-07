#!python3
for test in range(int(input().strip())):
    b, w = [int(i) for i in input().strip().split(' ')]
    bc, wc, z = [int(i) for i in input().strip().split(' ')]
    print(min(b*bc+w*wc, b*(wc+z)+w*wc, b*bc+w*(bc+z)))
