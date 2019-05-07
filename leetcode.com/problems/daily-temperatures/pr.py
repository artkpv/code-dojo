#!python3
"""
1
T: N*N
S: 1

2
Array: 30..100 - closest points.
Find min ID in that array

T: n*70
S: 70

"""


class Solution:
    def dailyTemperatures(self, T):
        MAX = 100
        MIN = 30
        INF = 9e9
        last = [INF] * (MAX-MIN+1)
        wait_days = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            last[T[i]-MIN] = i
            next_temp_offset = T[i]-MIN+1
            if next_temp_offset < len(last):
                greater = (e for e in last[T[i]-MIN+1:] if e is not None)
                min_id = min(greater)
                if min_id != INF:
                    wait_days[i] = min_id - i
        return wait_days

if __name__ == '__main__':
    s = Solution()
    out = s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    assert out == [1,1,4,2,1,1,0,0], out

"""
E1
73, 74, 75, 71, 69, 72, 76, 73

i
7 6 5 4 3 2 1 0
last
39 4
41 3
42 5
43 0
44 1
45 2
46 6
wait_days
1 1 4 2 1 1 0 0
"""
