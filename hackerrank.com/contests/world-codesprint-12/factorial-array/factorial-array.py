#!python3

import sys, math
sys.setrecursionlimit(10000)

MOD = 10**9
D = [1,1,2,6,24,120,720,5040,40320,362880,3628800,39916800,479001600,227020800,178291200,674368000,789888000,428096000,705728000,408832000,176640000,709440000,607680000,976640000,439360000,984000000,584000000,768000000,504000000,616000000,480000000,880000000,160000000,280000000,520000000,200000000,200000000,400000000,200000000,800000000,0]

def fact_mem(n):
    global D, MOD
    if n < len(D):
        return D[n]
    return 0  # it wraps up to zero!
    #i = len(D) - 1
    #while i <= n:
    #    i += 1
    #    D += [(D[i-1]*i)%MOD]
    #return D[n]

class Node:
    def __init__(self, lo, hi, val):
        assert lo <= hi
        self.lo = lo
        self.hi = hi
        self.val = val
        self.fact = fact_mem(val)
        self.left = None
        self.right = None
        self.p = None

    def __lt__(self, other):
        assert not self.has(other.lo, other.hi)
        return self.lo < other.lo

    def has(self, lo, hi):
        return self.lo <= hi and lo <= self.hi

    def __str__(self):
        return '{}..{} {}'.format(self.lo, self.hi, self.val)

class Intervals:
    def __init__(self, a):
        self.root = None
        assert len(a) > 0
        last = Node(0, 0, a[0])
        for i in range(1, len(a)):
            if last.val == a[i]:
                last.hi = i
            else:
                self.add(last)
                last = Node(i, i, a[i])
        self.add(last)

    def _transplant(self, u, v):
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != None:
            v.p = u.p

    def _min(self, x):
        while x.left != None:
            x = x.left
        return x

    def delete(self, z):
        if z.left == None:
            self._transplant(z, z.right)
        elif z.right == None:
            self._transplant(z, z.left)
        else:
            y = self._min(z.right)
            if y.p != z:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.p = y
            self._transplant(z, y)
            y.left = z.left
            y.left.p = y

    def add(self, z):
        y = None
        x = self.root
        while x != None:
            y = x
            if z < x:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None:
            self.root = z
        elif z < y:
            y.left = z
        else:
            y.right = z

    def inorder_intercect(self, a, v, l, r):
        if v != None:
            if l < v.lo:
                self.inorder_intercect(a, v.left, l, r)
            if v.has(l, r):
                a.append(v)
            if v.hi < r:
                self.inorder_intercect(a, v.right, l, r)

    def print_preorder(self, v=None, level=0):
        if v == None:
            v = self.root
        sys.stdout.write(' ' * level)
        sys.stdout.write(str(v))
        sys.stdout.write('\n')
        if v.left:
            self.print_preorder(v.left, level+1)
        if v.right:
            self.print_preorder(v.right, level+1)

    def change(self, l, r, val=None):
        I = []
        self.inorder_intercect(I, self.root, l, r)
        while len(I) > 0:
            v = I.pop()
            v_r = v.hi
            v_l = v.lo
            new_val = v.val + 1 if val == None else val
            assert v.has(l, r)
            if v.val != new_val:
                if l <= v_l and v_r <= r:
                    #   ---   --    --   --
                    #  -----  ---  ---   --
                    v.val = new_val
                    v.fact = fact_mem(v.val)   # TODO CAREFULL. Incapsulation broken
                elif v_l < l and r < v_r: # div by 3
                    #  ------
                    #   ---
                    self.delete(v)
                    self.add(Node(v_l, l-1, v.val))
                    self.add(Node(l, r, new_val))
                    self.add(Node(r+1, v_r, v.val))
                else:  # div by 2
                    #  ---   ---
                    #  --   ---
                    self.delete(v)
                    if l <= v_l:
                        assert r < v_r
                        self.add(Node(v_l, r, new_val))
                        self.add(Node(r+1, v_r, v.val))
                    else: # v_l < l
                        assert v_r <= r
                        self.add(Node(v_l, l-1, v.val))
                        self.add(Node(l, v_r, new_val))

        # once again to merge intervals with the same val:
        self.merge(l, r)

    def merge(self, l, r):
        I = []
        self.inorder_intercect(I, self.root, l, r)
        right = I.pop() if len(I) > 0 else None
        while right != None and len(I) > 0:
            left = I.pop()
            if left.fact == right.fact:
                self.delete(left)
                self.delete(right)
                new_node = Node(left.lo, right.hi, left.val)
                self.add(new_node)
                right = new_node
            else:
                right = left

    def sum(self, l, r):
        global MOD
        I = []
        self.inorder_intercect(I, self.root, l, r)
        sum_ = 0
        for v in I:
            assert v.has(l, r)
            size = min(r, v.hi) - max(l, v.lo) + 1
            f = (v.fact*size)%MOD
            sum_ = (sum_+f)%MOD
        return sum_

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    A = list(map(int, input().strip().split(' ')))
    intervals = Intervals(A)
    #intervals.print_preorder()
    for a0 in range(m):
        op = [int(i) for i in input().strip().split(' ')]
        if op[0] == 1:
            l, r = op[1]-1, op[2]-1
            intervals.change(l, r)
        elif op[0] == 2:
            l, r = op[1]-1, op[2]-1
            sum_ = 0
            print(intervals.sum(l, r))
        elif op[0] == 3:
            inx = op[1]-1
            val = op[2]
            intervals.change(inx, inx, val)
        #intervals.print_preorder()


