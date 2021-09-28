'''
Given array of operations:
INSERT item price
VIEW - -

where item - lowercase english chars
price - 1..10**5 

INSERT is to insert into a DB item with price.
VIEW is to print k-th item in asc order by (price, item). k is the number of VIEW command.

Example:
INSERT orange 1
INSERT apple 1
VIEW - - 
> apple
VIEW - - 
> orange
INSERT table 10 
INSERT chair 5
VIEW - -
> chair

Return array of output of this commands.

I1 BF
Maintain sorted (insertion sort). Get at index.
T: n*n + 1
S: n

I2 Two heaps.
T: n*log(n) + log(n)
S: n
'''

from heapq import heappop, heappush

class contra_string(str):
    def __init__(self, s):
       self.original = s

    def __lt__(self, s):
        return self.original.__gt__(s)

    def __le__(self, s):
        return self.original.__ge__(s)

    def __eq__(self, s):
        return self.original.__eq__(s)

    def __ne__(self, s):
        return self.original.__ne__(s)

    def __gt__(self, s):
        return self.original.__lt__(s)

    def __ge__(self, s):
        return self.original.__le__(s)

    def normal(self):
        return self.original

def insert_view_db(commands):
    if not commands:
        return []
    assert commands[0][0] == 'INSERT'
    left = [(-int(commands[0][2]), contra_string(commands[0][1]))]
    right = []
    res = []
    queries = 0
    for op, p1, p2 in commands[1:]:
        if op == 'INSERT':
            p = int(p2)
            n = p1
            lp, ln = left[0]
            if (p, n) < (-lp, ln.original):
                heappush(left, (-p, contra_string(n)))
            else:
                heappush(right, (p, n))
            while len(left) < queries + 1:
                p, n = heappop(right)
                heappush(left, (-p, contra_string(n)))
            while queries + 1 < len(left):
                p, n = heappop(left)
                heappush(right, (-p, n.original))
        else:
            assert op == 'VIEW'
            assert len(left) == queries + 1
            p, n = left[0]
            res += [n.original]
            queries += 1
            if right:
                p, n = heappop(right)
                heappush(left, (-p, contra_string(n)))
    return res


def myassert(commands, expected):
    print('TEST:')
    print(commands)
    output = insert_view_db(commands)
    assert output == expected, f"FAILED. \Actual:\n{output}\nExpected:\n{expected}"
    print('PASS')


myassert([
    ('INSERT', 'orange', '1'),
    ('INSERT', 'apple', '1'),
    ('INSERT', 'applee', '1'),
    ('VIEW', '-', '-'),
    ('VIEW', '-', '-'),
    ('VIEW', '-', '-'),
    ('INSERT', 'table', '10'),
    ('INSERT', 'chair', '5'),
    ('VIEW', '-', '-'),
    ('VIEW', '-', '-')
], ['apple',
    'applee',
    'orange',
    'chair',
    'table' ]
)
