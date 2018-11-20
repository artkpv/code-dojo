#!python3

import math
import os
import random
import re
import sys
import heapq


class V:
    def __init__(self, i, w, ll=None):
        # w - weight to get to this vertex
        self.i = i
        self.w = w
        self.ll = ll
        self.next = None
        self.prev = None

    def __lt__(self, other):
        if self.ll:
            if other.ll:
                return -self.ll.weight < -other.ll.weight
            else:
                return -self.ll.weight < -other.w
        else:
            if other.ll:
                return -self.w < -other.ll.weight
            else:
                return -self.w < -other.w

    def __repr__(self):
        if self.ll:
            return '({} {} {})'.format(self.i, self.w, self.ll.weight)
        else:
            return '({} {})'.format(self.i, self.w)


class LL:
    def __init__(self, cycle_v):
        self.last = None
        self.first = None
        self.weight = 0
        self.cycle_v = cycle_v

    def add_last(self, v):
        self.weight += v.w

        v.prev = self.last
        if self.last:
            self.last.next = v
        self.last = v
        if not self.first:
            self.first = v

    def delete_last(self, x):
        assert self.last == x
        assert x.next == None
        self.last = x.prev
        if self.last:
            assert self.last.next == x
            self.last.next = None

        assert self.weight >= x.w
        self.weight -= x.w
        if self.last == None:
            assert self.weight == 0

    def __repr__(self):
        s = str(self.weight)
        s += ':'
        y = self.first
        while y != None:
            s += repr(y)
            s += ' '
            y = y.next
        return s


class G:
    def __init__(self, w):
        n = len(w)
        self.count = n
        self.inx_to_v = {}
        self.adj = [None] * n
        self.rev = [None] * n
        for i in range(n):
            j = (i+1)%n
            v = V(j, w[i])
            self.adj[i] = [v]
            self.inx_to_v[j] = v

    def add_at_farthest(self, i, w):
        y, d = self.farthest(i)
        if y.ll:
            self.count += 1
            v = V(self.count - 1, w, y.ll)
            y.ll.add_last(v)
        else:
            self.add_at(y.i, w)

    def add_at(self, i, w):
        self.count += 1
        cycle_v = self.inx_to_v[i]
        ll = LL(cycle_v)
        u = V(self.count - 1, w, ll)
        ll.add_last(u)
        heapq.heappush(self.adj[i], u)

    def delete_farthest(self, i):
        y, d = self.farthest(i)
        if y.ll:
            y.ll.delete_last(y)
            if y.ll.weight == 0:
                self.adj[y.ll.cycle_v.i].remove(y.ll.first)
        else:
            raise 'can not delete in cycle'

    def farthest(self, i):
        """
        return farthest node and distance to it
        """
        max_dist = 0
        farthest = None
        dist = 0
        n = len(self.adj)
        for j in range(n):
            k = (i + j) % n
            u = self.adj[k][0]
            if not u.ll and u.i != i:
                if dist + u.w > max_dist:
                    max_dist = dist + u.w
                    farthest = u
            elif u.ll and u.ll.last:
                if dist + u.ll.weight > max_dist or \
                    (dist + u.ll.weight == max_dist and farthest.i < u.i):
                    max_dist = dist + u.ll.weight
                    farthest = u.ll.last

            next_ = self.inx_to_v[(j+1)%n]
            dist += next_.w

        assert farthest != None
        return (farthest, max_dist)

    def __repr__(self):
        s = ""
        for i in range(n):
            s += repr(self.inx_to_v[i]) + ": "
            for u in self.adj[i]:
                if u.ll:
                    s += repr(u) + " "
            s += "\n"
        return s


# Complete the cyclicalQueries function below.
def cyclicalQueries(w, m, prnt):
    # Return the list of answers to all queries of type 4. Take the query information from standard input.
    g = G(w)
    for i in range(m):
        q = [int(j) for j in input().strip().split(' ')]
        if q[0] == 1:
            g.add_at_farthest(q[1] - 1, q[2])
        elif q[0] == 2:
            g.add_at(q[1] - 1, q[2])
        elif q[0] == 3:
            g.delete_farthest(q[1] - 1)
        elif q[0] == 4:
            node, distance = g.farthest(q[1] - 1)
            prnt(distance)

if __name__ == '__main__':
    n = int(input())
    w = list(map(int, input().rstrip().split()))
    m = int(input())
    cyclicalQueries(w, m, lambda s: print(s))
