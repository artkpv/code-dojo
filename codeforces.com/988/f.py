#!python3

# http://codeforces.com/contest/988/problem/F

from bisect import bisect_left as bl

a, n, m = [int(i) for i in input().strip().split(' ')]
R = []
for i in range(n):
    l, r = [int(j) for j in input().strip().split(' ')]
    inx = bl(R, l)
    R.insert(inx, l)
    R.insert(inx+1, r)
A = []
for i in range(m):
    A += [tuple(int(j) for j in input().strip().split(' '))]
A = sorted(A)


class S:  # Solution
    def __init__(self, a, t):
        self.t = t  # tiredness
        self.a = a  # umbrella

    def __repr__(self):
        return "({} {})".format(self.a, self.t)


O = [S(0,0)]  # no umbrellas, not tired
x = 0  # starts at 0
x_prev = 0
is_rain = False
optimal = None
while x <= a:
    # check if rain:
    rain_inx = bl(R, x)
    if rain_inx < len(R):
        rain_coord = R[rain_inx]
        if x == rain_coord:
            is_rain = not is_rain

    # update tiredness in solutions:
    distance = x - x_prev
    optimal = 9*999
    for o in O:
        umb = o.a
        if umb > 0:
            p = A[umb-1][1]
            o.t += p*distance
        if o.t < optimal:
            optimal = o.t

    # pick up new umbrellas:
    k = bl(A, (x, 0))  # inx of next umbrellas or one at x
    if k < len(A):  # have some here or next
        while k < len(A) and A[k][0] == x:  # every umbrella at x
            umb = k + 1
            O += [S(umb, optimal)]
            k += 1
    assert k >= len(A) or A[k][0] != x, "k should be next umb or none"

    # drop solution without umbrella if rains:
    index_list = [i for i, el in enumerate(O) if el.a == 0]
    s_inx = index_list[0] if len(index_list) > 0 else None
    if is_rain and s_inx is not None:  # can not go without umbrella
        assert O[s_inx].a == 0
        del O[s_inx]
    elif not is_rain and s_inx is None:  # can go without one
        O.append(S(0, optimal))

    if not any(O) and x != a:
        optimal = -1
        break

    # get next x:
    next_x = a
    if rain_inx < len(R):
        if x < R[rain_inx]:
            next_x = R[rain_inx]
        elif rain_inx + 1 < len(R):
            next_x = R[rain_inx+1]
    if k < len(A) and A[k][0] < next_x:
        next_x = A[k][0]
    if x == next_x:
        break
    x_prev = x
    x = next_x

print(optimal)
