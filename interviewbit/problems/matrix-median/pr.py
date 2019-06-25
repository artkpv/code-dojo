from bisect import bisect_left

INF = float('inf')
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def findMedian(self, A):
        if not A or not A[0]:
            return None
        n = len(A)
        m = len(A[0])
        median = A[0][m//2]
        while median not in (INF, -INF):
            lt_num = 0
            gt_num = 0
            ng = INF  # next greater
            nl = -INF  # next less
            for row in A:
                lt = bisect_left(row, median)  # less than
                gt = m - bisect_left(row, median+1)  # greater than
                lt_num += lt
                gt_num += gt
                ng = min(ng, row[m - gt - 1] if gt < m else INF)
                nl = max(nl, row[lt-1] if lt > 0 else -INF)
            if lt_num <= (m*n)//2 >= gt_num:
                return median
            median = nl if lt_num > gt_num else ng
        return -1

