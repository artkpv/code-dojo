
from matrix import matrix

from heapq import heappush, heappop

n = len(matrix)
m = len(matrix[0])

best_path_sum = float('inf')

for left in range(n):
    dist = [[float('inf')] * m for _ in range(n)]
    dist[left][0] = matrix[left][0]
    q = [(matrix[left][0], left, 0)]

    while q:
        _, i, j = heappop(q)
        for ii, jj in ((i,j+1), (i+1,j), (i-1, j)):
            if 0 <= ii < n and 0 <= jj < m:
                d = dist[i][j] + matrix[ii][jj]
                if d < dist[ii][jj]:
                    k = next((qi for (qi, (_, vi, vj)) in enumerate(q) if (vi, vj) == (ii, jj)), -1)
                    if k != -1:
                        del q[k]
                        heapify(q)
                    heappush(q, (d, ii, jj))
                    dist[ii][jj] = d
    min_d = min(dist[i][-1] for i in range(n))
    if min_d < best_path_sum:
        best_path_sum = min_d
        print(left, best_path_sum)
print(best_path_sum)





