'''
string of 1, -1, or ?
0 - init len 

max len? 

left - num of ? to left
then ans is max for s[i] + - left


'''
import math


def solve(s):
    left = 0
    ans = 0
    cur = 0
    for e in s:
        if e == 'R':
            cur += 1
        elif e == 'L':
            cur -= 1
        elif e == '?':
            left += 1
        else:
            raise ValueError("Invalid character in input string")
        ans = max(ans, abs(cur + left), abs(cur - left))
    return ans
    

def main():
    ans = solve(input().strip())

    print(ans)

if __name__ == "__main__":
    main()
