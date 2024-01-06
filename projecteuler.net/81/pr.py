"""
https://projecteuler.net/problem=81
"""

from matrix import matrix

from heapq import heappush, heappop

n = len(matrix)
m = len(matrix[0])

dist = [[float('inf')] * m for _ in range(n)]
dist[0][0] = matrix[0][0]
q = [(matrix[0][0], 0, 0)]

while q:
    _, i, j = heappop(q)
    if i == n-1 and j == m-1:
        break
    for ii, jj in ((i,j+1), (i+1,j)):
        if ii < n and jj < m:
            d = dist[i][j] + matrix[ii][jj]
            if dist[ii][jj] > d:
                k = next((qi for (qi, (_, vi, vj)) in enumerate(q) if (vi, vj) == (ii, jj)), -1)
                if k != -1:
                    del q[k]
                    heapify(q)
                heappush(q, (d, ii, jj))
                dist[ii][jj] = d
print(dist[-1][-1])





