#!python3

"""
2D digits
t<=5
1<=|G|,|P|<= 1e6
1<=r,c<= 1e3
Find if P in G

1) BF
Time O(N**2),  S 1

2) Regex
Via groups. Count num of chars between groups.
Time: O(N**2) ???

3)
Somehow determine if P is included?
Modulo on numbers?
Take into account that it is digits.


"""
import re

def find(pattern, graph, diff):
    """
    Example:
    graph:   012345678
             0110#0110
    pattern: (11)\d*(#)\d*(11)
    cols:    4
    """
    for mo in re.finditer(pattern, graph):
        passed = True
        for g in range(2, len(mo.groups())+1):
            s_left = mo.span(g-1)
            s = mo.span(g)
            if '#' not in graph[s_left[1]: s[0]]:
                passed = False
        if passed:
            return True
    return False


tests = int(input().strip())
while tests > 0:
    tests -= 1
    graphR,graphC = [int(i) for i in input().strip().split(' ')]
    graphRows = []
    for i in range(graphR):
        graphRows += [input().strip()]
    graph = '#'.join(graphRows)
    pR, pC = [int(i) for i in input().strip().split(' ')]
    diff = graphC - pC
    patternRows = []
    for i in range(pR):
        patternRows += [input().strip()]
    pattern = (r'[\d#]{' + str(diff+1) + '}').join('(' + i + ')' for i in patternRows)
    print('YES' if find(pattern, graph, diff) else 'NO')











