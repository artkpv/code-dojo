#!/bin/python3

"""
Graph w/o loops
Path.
Find min subseq. of vert from path.

p
v
shortest subseq

Ex1
4
0110
0010
0001
1000
4
1 2 3 4


"""
n = int(input().strip())
A = []
for _ in range(n):
    A += [['1' == e for e in input().strip()]]
m = int(input().strip())
P = [int(i) for i in input().strip().split(' ')]
