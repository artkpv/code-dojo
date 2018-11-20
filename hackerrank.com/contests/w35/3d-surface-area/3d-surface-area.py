#! python3

"""
3 3
1 3 4
2 2 3
1 2 4
60

top - 9
bottom - 9
left - 4*3 = 12; -3 = 8
right


BruteForce
price = 0
for i in 1..H  # from left to right
    for j in 1..W  # from near to far
       x_i_j - cube
       price += price for this cube alone
       price -= intercections with cube i-1,j * 2
       price -= intercections with cube i,j-1 * 2

10000 times max. ~H*W
"""

height, width = [int(i) for i in input().strip().split(' ')]
A = [None] * height
price = 0
for i in range(height):
    A[i] = [int(v) for v in input().strip().split(' ')]
    assert len(A[i]) == width
    for j in range(width):
        if A[i][j] > 0:
            price += 2 + (A[i][j] * 4)
            if i > 0 and A[i-1][j] > 0:
                price -= min(A[i-1][j], A[i][j]) * 2
            if j > 0 and A[i][j-1] > 0:
                price -= min(A[i][j-1], A[i][j]) * 2
print(price)



