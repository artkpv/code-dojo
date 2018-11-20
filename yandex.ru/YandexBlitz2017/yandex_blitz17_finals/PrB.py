"""
https://contest.yandex.ru/hiring/contest/5187/problems/B

YEAH!

NEXT: test won't pass there
6 1
...00-
3 4
2 3
1 5
1 2
1 6

"6 1`n...00-`n3 4`n2 3`n1 5`n1 2`n1 6" | py PrB.py

"8 1`n..-0..-+`n1 2`n2 3`n2 4`n1 5`n5 6`n6 7`n6 8" | py PrB.py


NEXT:
- find out why uninterrupted loop


"""
import sys
sys.setrecursionlimit(10000)

class GTree():
    def __init__(self, n):
        self._root = 1
        self._adj = {}
        self._results = {}
        self._vertexes = n

    def add_edge(self, u, v):
        if u not in self._adj:
            self._adj[u] = []
        if v not in self._adj[u]:
            self._adj[u] += [v]

    def add_result(self, v, result):
        self._results[v] = result

    def add_reverse_edges(self, k):
        self._add_reverse_edges(k, 0, self._root)

    def _add_reverse_edges(self, k, level, v):
        if k < level:
            return
        if v in self._adj:
            if k == level:
                to_copy = list(self._adj[v])
                for w in to_copy:
                    self._copy_tree_and_reverse(w, v)
                return
            else:
                for w in self._adj[v]:  # with new edges now
                    self._add_reverse_edges(k, level+1, w)

    def _copy_tree_and_reverse(self, original, parent):
        # add new reversed vertex and edge:
        self._vertexes += 1
        new_v = self._vertexes
        self.add_edge(parent, new_v)
        r = self._results[original]
        if r == '-':
            r = '+'
        elif r == '+':
            r = '-'
        self._results[new_v] = r

        if original in self._adj:
            for w in self._adj[original]:
                self._copy_tree_and_reverse(w, new_v)

    def winner(self):
        return self._winner(self._root, True)

    def _winner(self, v, is_first):
        if self._results[v] == '.':
            assert v in self._adj
            winName = 'First' if is_first else 'Second'
            is_there_draw = False
            is_there_win = False

            for w in self._adj[v]:
                r = self._winner(w, not is_first)
                if r == winName or r == '+':  # there is win variation
                    self._results[v] = winName
                    is_there_win = True
                    break
                if r == 'Draw' or r == '0':
                    is_there_draw = True
            if not is_there_win:
                if is_there_draw:
                    self._results[v] = 'Draw'
                else:  # lose then
                    loseName = 'Second' if is_first else 'First'
                    self._results[v] = loseName

        return self._results[v]


n, k = (int(i) for i in input().strip().split(' '))
tree = GTree(n)
leafs = input().strip()
for i in range(n - 1):
    u, v = (int(i) for i in input().strip().split(' '))
    tree.add_edge(u, v)

for i in range(len(leafs)):
    tree.add_result(i + 1, leafs[i])

tree.add_reverse_edges(k)

print(tree.winner())
