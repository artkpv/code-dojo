"""
6 4 4 6
2

6 4 4 6
6 8 6  8
14 6   22
20     42

10 4 6  10
10 10   20
20      40
"""

INF = 9e9


class Solution:
    def mergeStones(self, stones, k: int) -> int:
        self.D = {}
        stones = tuple(stones)
        min_ = self._merge(stones, k)
        return min_ if min_ < INF else -1

    def _merge(self, stones, k):
        if len(stones) == 1:
            return 0
        if len(stones) < k:
            return INF
        if stones not in self.D:
            minmoves = INF
            for i in range(len(stones) - k + 1):
                sum_ = sum(stones[i:i+k])
                moves = sum_
                new = tuple(stones[:i]) + tuple([sum_]) + tuple(stones[i+k:])
                moves += self._merge(new, k)
                if moves < minmoves:
                    minmoves = moves
            self.D[stones] = minmoves
        return self.D[stones]
