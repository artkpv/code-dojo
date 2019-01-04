#!/usr/bin/python3
"""
n<=500
s_i < 1e4
"""
import sys
fr = open('input.txt')
fw = open('output.txt', 'w')

map_ = {')':'(', ']':'['}
for test in range(int(fr.readline().strip())):
    line = fr.readline().strip()
    correct = True
    j = -1;
    for i,ch in enumerate(line):
        if ch not in map_:
            j = i
        else:
            if j < 0 or map_[ch] != line[j]:
                correct = False
                break
            j -= 1
            if j >= 0 and line[j] in map_:
                j = -1
    if j >= 0:
        correct = False
    fw.write('YES\n' if correct else 'NO\n')
