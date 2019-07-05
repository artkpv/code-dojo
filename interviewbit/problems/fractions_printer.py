"""
d n

d = q*n + r
d1 = q2

"""

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, n, d):
        if d == 0:
            raise Exception('division by zero')
        if n == 0:
            return '0'
        negative = (n < 0 and d > 0) or (n > 0 and d < 0)
        if negative:
            n, d = abs(n), abs(d)
        q, r = divmod(n, d)
        result = [('-' if negative else '') + str(q)]
        if r == 0:
            return ''.join(result)
        memo = {}
        q, r = divmod(r*10, d)
        result += ['.', str(q)]
        memo[(q,r)] = len(result) - 1
        while r != 0:
            q2, r2 = divmod(r*10, d)
            if (q2, r2) in memo:
                result.insert(memo[(q2, r2)], '(')
                result += [')']
                break
            result += [str(q2)]
            memo[(q2,r2)] = len(result) - 1
            q = q2
            r = r2
        return ''.join(result)
"""
20  / 6
res
3.

"""

print(Solution().fractionToDecimal(87, 22))
print(Solution().fractionToDecimal(1, 3))
print(Solution().fractionToDecimal(2, 6))
print(Solution().fractionToDecimal(1, 2))
