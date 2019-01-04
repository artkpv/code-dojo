#!/usr/bin/python3
"""
n<=500
s_i < 1e4
"""
import sys
fr = open(sys.argv[1] if len(sys.argv) > 1 else 'input.txt')
fw = open('output.txt', 'w')

for test in range(int(fr.readline().strip())):
    line = fr.readline().strip()
    correct = True
    counter = []
    if line:
        btype = None
        for ch in line:
            if ch in '([':
                if btype is not None and ((btype and ch == '[') or (not btype and ch == '(')):
                    counter[-1] += 1
                else:
                    counter += [1]
                    btype = ch == '['  # 1 - '[', 0 - '('
            else:  # closing 
                if btype is None:
                    correct = False
                else:
                    if (ch == ']' and btype) or (ch == ')' and not btype):
                        counter[-1] -= 1
                    else:
                        correct = False
                        break
                    if counter[-1] == 0:
                        del counter[-1]
                        btype = not btype
                        if not counter:
                            btype = None
    if counter:
        correct = False
    fw.write('YES\n' if correct else 'NO\n')
