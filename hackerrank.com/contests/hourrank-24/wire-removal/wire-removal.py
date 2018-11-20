#!python3

"""
https://www.hackerrank.com/contests/hourrank-24/challenges/wire-removal/problem

2 <= n <= 10^5
1 <= x,y <= n


Example 1
    6 edges.
    Pr(1-2) = Pr(1-3) = Pr1
    Pr(4-2) , 2-5 , 3-6, 3-7 = 2*Pr(1-2) = Pr2 = 2*Pr1
    Probability:
        Sum(Pr 1..6 edges) = 1
        2*Pr1 + 4*2*Pr1 = 1 => Pr1 = 1/10
    Expected:
        Sum for i wire in 1..n-1, Pr_i * remaining vertices
        1-2, 1-3: 4*Pr1
        2-4, 2-5, 3-6, 3-7: 5*2*Pr1
        = 2*4*Pr1 + 4*6*2*Pr1 = 56/10


"""

import sys

def cals_expected(vertices_num, graph):
    vertices_num = vertices_num
    adj = {}
    sizes = {}
    levels = {}

    root = 1
    levels[root] = 0
    adj[root] = []
    base_probability = 0

    # construct tree
    # top down: start from 1 and add all linked vertices:
    top_down = [root]
    bottom_up = [root]
    marked = set()
    marked.add(root)
    while len(top_down) > 0:
        v = top_down.pop()
        assert v in adj
        for w in graph[v]:
            if w not in marked:
                marked.add(w)
                bottom_up += [w]  # parents before children
                if w not in adj:
                    adj[w] = []
                    levels[w] = levels[v] + 1
                    base_probability += levels[w]
                    sizes[w] = 0  # to calc later

                adj[v] += [w]
                top_down.insert(0, w)

    # bottom up to calc expected
    expected = 0
    while len(bottom_up) > 0:
        v = bottom_up.pop()
        sizes[v] = 1  # self
        for w in adj[v]:
            sizes[v] += sizes[w]

        # v has correct size now
        remain = vertices_num - sizes[v]
        probability = levels[v] * (1/base_probability)
        expected += remain * probability
    return expected


if __name__ == "__main__":
    vertices_num = int(input().strip())
    graph = {}  # store in as bi-graph
    for a0 in range(vertices_num-1):
        x, y = input().strip().split(' ')
        x, y = [int(x), int(y)]
        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []
        graph[x] += [y]
        graph[y] += [x]

    print(cals_expected(vertices_num, graph))

