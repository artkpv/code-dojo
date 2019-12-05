

"""
0 1 2   (1-0+1)(3-1)
2 4 5   (4-2+1)(5-2+1-(4-2)) 6  2,4 2,5 3,4 3,5 4,4 4,5

"""
import sys
sys.setrecursionlimit(99999999)
MOD = 1e9 + 7
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        # print('solve', A, B)

        dpc = {}  # divisors product cache
        def dproduct(x):
            """
            4
            """
            if x not in dpc:
                d = 2
                res = x
                while d * d <= x:
                    if x % d == 0:
                        res = (res * d) % MOD
                        if d * d != x:
                            res = (res * (x // d)) % MOD
                    d += 1
                dpc[x] = int(res)
                # count = 2
                # while d * d <= x:
                    # if x % d == 0:
                        # count += 2
                        # if d * d == x:
                            # count -= 1
                    # d += 1
                # dpc[x] = int(pow(x, count / 2) % MOD)
            return dpc[x]

        dpf = []  # divisors product, frequency
        def add_max(lo, hi):
            if lo > hi:
                return
            inx = max((e, i) for i, e in enumerate(A[lo:hi+1]))[1] + lo
            freq = (inx - lo + 1) * (hi - inx + 1)
            dp = dproduct(A[inx])

            if dpf and dpf[-1][0] == dp:  # What if % MOD, gives us repeating dp but not dpf[-1][0]? TODO
                dpf[-1] = (dp, dpf[-1][1] + freq)
            else:
                dpf.append((dp, freq))

            add_max(lo, inx-1)
            add_max(inx+1, hi)

        n = len(A)
        add_max(0, n-1)
        dpf.sort()
        # print(dpf)
        dpf_index = [0]
        for i in range(len(dpf)-1):
            dpf_index.append(dpf_index[-1] + dpf[i][1])
        dpf_index.append(dpf_index[-1] + dpf[-1][1])  # Non existent dp index, last.
        # print(dpf_index)

        def query(inx):
            lo = 0
            hi = len(dpf_index) - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if dpf_index[mid] <= inx < dpf_index[mid+1]:
                    lo = mid
                    hi = mid
                elif inx < dpf_index[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # print('query', inx, dpf[lo][0])
            return dpf[lo][0]

        inum = n*(n+1) // 2
        ans = [query(inum - k) for k in B]
        return ans

if __name__ == '__main__':
    A = [int(e) for e in input().strip().split(' ')]
    B = [int(e) for e in input().strip().split(' ')]
    ans = Solution().solve(A, B)
    print(' '.join(str(e) for e in ans))


