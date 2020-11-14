#!python3
'''
Problem :https://www.geeksforgeeks.org/minimum-edges-required-to-add-to-make-euler-circuit/
Given a undirected graph of n nodes and m edges. The task is to find minimum edges required to make Euler Circuit in the given graph.

n nodes
m edges
undirected
n <= 1000

Ex1
1    Ans 0 
Ex2
1 - 2   Ans 1
Ex3
1 = 2 - 3    Ans 1 
Ex4
1 = 2   3 = 4  Ans 2
Ex5
1 - 2   3 - 4  Ans 2
Ex6 
1 - 2   3   4   Ans 3 
Ex7
1 - 2 - 3   Ans 1
Ex8 
1-2=3-4  5=6  7-8
1=2=3=4=5=6=7=8  7
7-8
| |
1-2=3=4=5=6  5

-1-2=3-4-7-8-5-1-
            ||
             6
ans 4


Idea 
1) if cc = 1. Ans = oddedges / 2 
2) if cc > 1
Count CC. Count odd CCs, even CC.
odde = (oddedges - oddcc*2 )
ans = oddedges / 2


'''

def minedges(n, m, edges):
    cc, oddcc = 0, 0
    marked = set()
    def dfs(source):
        isoddcc = False
        s = [source]
        while s:
            v = s.pop()
            if len(edges[v]) % 2 == 1:
                isoddcc = True
            for u in edges[v]:
                if u in marked:
                    continue
                marked.add(u)
                s.append(u)
        return isoddcc
    for u in range(n):
        if u not in marked:
            cc += 1
            isoddcc = dfs(u)
            if isoddcc:
                oddcc += 1
    oddedges = sum(1 if len(edges[v]) % 2 == 1 else 0 for v in range(n))
    evencc = cc - oddcc
    print('cc',cc,'oddcc', oddcc,'evencc', evencc,'oddedges', oddedges)
    if cc > 1:
        return ((oddedges + (2 if evencc > 1 else 0)) -  (oddcc + (1 if evencc > 1 else 0)) * 2) // 2 + cc
    else:
        return oddedges // 2
        
def test(edges, answer):
    n = len(edges)
    m = sum(len(e) for e in edges)
    actual = minedges(n, m, edges)
    print('Actual:{} Expected:{} Graph:{}'.format(actual, answer, str(edges)))
    assert answer == actual

test([[]], 0)
test([[1, 1], [0, 0]], 0)
test([[1, 1], [0, 0], []], 2)
test([[1, 1], [0, 0], [3, 3], [2, 2]], 2)
test([[1, 1], [0, 0, 2], [3, 3, 1], [2, 2]], 1)
test([[1], [0], [3], [2]], 2)
test([[1], [0], [], []], 3)
test([[1], [0, 2], [1]], 1)
test([[1], [0, 2, 2], [1, 1, 3], [2], [5,5], [4,4], []], 4)
