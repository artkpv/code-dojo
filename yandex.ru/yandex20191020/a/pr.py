#!python3


class PQ(object):
    def __init__(self, num):
        self.arr = [float('inf')] * (num+1)
        self.i_to_v = [-1] + list(range(num))
        self.v_to_i = list(range(1, num+1))
        self.size = 0

    def __str__(self):
        return 'PQ {} {} {} {}'.format(
            self.size,
            repr(self.arr),
            repr(self.i_to_v),
            repr(self.v_to_i)
        )

    def contains(self, v):
        i = self.v_to_i[v]
        return i <= self.size

    def insert(self, v, priority):
        i = self.v_to_i[v]
        self.size += 1
        n = self.size
        self.exch(i, n)
        self.arr[n] = priority
        self.sink_up(n)

    def decrease(self, v, priority):
        i = self.v_to_i[v]
        assert i <= self.size
        self.arr[i] = priority
        self.sink_up(i)

    def sink_up(self, i):
        p = i // 2
        if 0 < p and self.arr[p] > self.arr[i]:
            self.exch(p, i)
            self.sink_up(p)

    def sink_down(self, i):
        n = self.size
        while 0 < i and i*2 <= n:
            k = i*2
            if k + 1 <= n and self.arr[k+1] < self.arr[k]:
                k += 1
            if self.arr[k] >= self.arr[i]:
                break
            exch(i, k)

    def exch(self, i, j):
        if i == j:
            return
        def _exch(a, k, p):
            a[k], a[p] = a[p], a[k]
        _exch(self.arr, i, j)
        _exch(self.i_to_v, i, j)
        _exch(self.v_to_i, self.i_to_v[i], self.i_to_v[j])
        assert self.v_to_i[self.i_to_v[i]] == i
        assert self.v_to_i[self.i_to_v[j]] == j

    def pop(self):
        if self.size == 0:
            return None
        v = self.i_to_v[1]
        priority = self.arr[1]
        n = self.size
        a = self.arr
        self.exch(1, n)
        self.size -= 1
        if 1 < self.size:
            self.sink_down(1)
        return v


pnum, dnum, P, K = [int(i) for i in input().strip().split(' ')]
adj = [[] for _ in range(pnum+dnum)]
e_dist = {}
d_to_p_num = int(input().strip())
for i in range(d_to_p_num):
    d, p, dist = [int(i) for i in input().strip().split(' ')]
    p = dnum + p
    adj[d] += [p]
    e_dist[(d, p)] = dist

p_to_p_num = int(input().strip())
for i in range(p_to_p_num):
    p1, p2, dist = [int(i) for i in input().strip().split(' ')]
    p1 = dnum + p1
    p2 = dnum + p2
    adj[p1] += [p2]
    e_dist[(p1, p2)] = dist

p_cost = [K] * pnum
for d in range(dnum):
    distto = [float('inf')] * (pnum + dnum)
    distto[d] = 0
    pq = PQ(dnum + pnum)
    pq.insert(d, 0)
    # print('insert', str(pq))
    while pq.size > 0:
        v = pq.pop()
        # print('pop', str(pq))
        # Skip if dist is greater than P.
        if distto[v] >= P:
            continue
        for w in adj[v]:
            roaddist = e_dist[(v, w)] if (v, w) in e_dist else float('inf')
            if distto[w] > distto[v] + roaddist:
                distto[w] = distto[v] + roaddist
                if pq.contains(w):
                    pq.decrease(w, distto[w])
                    # print('decrease', str(pq))
                else:
                    pq.insert(w, distto[w])
                    # print('insert', str(pq))
    # Update cost for passengers.
    for p in range(pnum):
        I = distto[dnum + p]
        if I < P:
            p_cost[p] = max(1, p_cost[p] - (P - I))
    # print('SP', d, p_cost)

print(min(p_cost) if p_cost else ' ')
