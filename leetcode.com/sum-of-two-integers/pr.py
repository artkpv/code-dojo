"""
SEE
https://leetcode.com/problems/sum-of-two-integers/discuss/84290/Java-simple-easy-understand-solution-with-explanation


01010
10011

xor
11001

and
00010

<< 1
00100

xor
11101 > return

and
00000  > exi


a , b

c = a ^ b
and_ab = a & b
if and_ab == 0:
  return c
and_ab <<= 1
a = c
b = and_ab


11
10
01

110  6
101  5
010

001 ~(a&b)&b = d
011 a = c | d
010 b




"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        return getSum(a^b, (a&b)<<1) if b != 0 else a
        return b==0? a:getSum(a^b, (a&b)<<1)
        if a == 0 or b == 0:
            return a or b
        if a*b > 0:
            assert (a < 0 and b < 0) or (a > 0 and b > 0)
            isnegative = a < 0
            if isnegative:
                a *= -1
                b *= -1
            while True:
                c = a ^ b
                if a & b == 0:
                    break
                b = (a & b) << 1
                a = c
            return -c if isnegative else c
        else:  # different
            a, b = (a, b) if a < b else (b, a)
            isnegative = a == -max(abs(a), abs(b))
            a *= -1
            a = abs(a)
            b = abs(b)
            a, b = (b, a) if a < b else (a, b)
            print(bin(a), bin(b))
            # now: 0 < b < a
            while True:
                c = b & (~(a & b))  # 1-1 = 0
                extra = (~a & b)
                if extra == 0:  # has no 0-1
                    break
                # substruct: 10-01=01
                c |= extra  # 10 | 01 = 11
                b = (extra << 1)
                a = c
                print(bin(a), bin(b), bin(c))
            return -c if isnegative else c


if __name__ == '__main__':
    print(Solution().getSum(int(input().strip()), int(input().strip())))
