class Solution:
    def sum(self, a, b):
        """get a+b, a >= 0 and b >= 0

        Example:
        a
        0011 3
        b
        0101 5

        1.
        c
        0010
        a
        0110
        b = c

        2.
        c 0100
        a 0100
        b = c

        3.
        c 1000
        a 0000
        b = c

        4.
        c = 0
        a 1000
        b = c

        return a 2**3 = 8


        """
        while b > 0:
            c = (b&a) << 1
            a ^= b
            b = c
        return a

    def substruct(self, a, b):
        """get a-b, a > 0 and b > 0 and a > b

        a
        0101 5
        b
        0011 3

        1.
        c 0100
        a 0110
        b = c

        2.
        c 0000
        a 0010

        > 0010 2


        """
        while b > 0:
            c = (a^b)&b << 1
            a ^= b
            b = c
        return a

    def getSum(self, a: int, b: int) -> int:
        if a*b >= 0:
            negative = -1 if a < 0 else 1
            return negative*self.sum(a*negative, b*negative)
        else:
            a, b = (a, b) if a < b else (b, a)
            negative = -1 if -1*a > b else 1
            a, b = (-1*a, b) if -1*a > b else (b, -1*a)
            return negative*self.substruct(a, b)


if __name__ == '__main__':
    print(Solution().getSum(int(input().strip()), int(input().strip())))
