#!python3

import sys

if __name__ == "__main__":
    n = int(input().strip())
    min_num = None
    min_name = None
    for a0 in range(n):
        s, n = input().strip().split(' ')
        sevens = 0
        fours = 0
        for d in n:
            if d == '7':
                sevens += 1
            elif d == '4':
                fours += 1
            else:
                break
        if sevens == fours and sevens + fours == len(n):
            if min_num == None or min_num > int(n):
                min_num = int(n)
                min_name = s
    print(min_name if min_name else str(-1))



