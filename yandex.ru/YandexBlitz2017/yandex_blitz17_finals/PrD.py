"""
https://contest.yandex.ru/hiring/contest/5187/problems/D/

TEST:
2 2
cc
a-
-b
4
ab
ac
cb
ba

"2 2`ncc`na-`n-b`n4`nab`nac`ncb`nba" | py .\PrD.py

TEST 2
3 2
ccc
ab-
-ab
5
abc
abb
aab
cbb
ccc

"3 2`nccc`nab-`n-ab`n5`nabc`nabb`naab`ncbb`nccc" | py .\PrD.py

TODO
FAILES$
	TEST 6	wrong-answer	61ms / 3.80Mb	-

"""
#class Tree:
#    class Node:
#        def __init__(self, c):
#            self.c = c
#            self.next = {}
#
#    def __init__(self, n):
#        self.root = Tree.Node(None)
#        self._at_level_nodes = [[]] * n
#        self._at_level_nodes[0] += [self.root]
#
#    def add_string(self, s, button_chars=[]):
#        current = [self.root]  # current level vertices
#        prev = []  # to keep track of previous level vertices
#        next_ = []  # to keep track of next level vertices to
#        for level in range(1, len(s) + 1):
#            char = s[level - 1]
#            for v in current:
#                if char == '-':
#                    pass
#                    # todo
#                    # use the button_chars some how to construct the tree
#                elif char in v.next:
#                    next_ += [v.next[char]]  # only this one
#                else:  #if c not in p.next:
#                    node = Tree.Node(char)
#                    v.next[char] = node
#                    next_ += [node]
#                    self._at_level_nodes[level - 1] += [node]
#
#            current = next_
#            level += 1
#
#    def test(self, s):
#        vertices = [self.root]
#        level = 0
#        while level < len(s):
#            c = s[level]
#            next_vertices = []
#            for v in vertices:
#                if c in v.next:
#                    next_vertices += [v.next[c]]  # only this one
#            if len(next_vertices) == 0:  # not found
#                return False
#            vertices = next_vertices
#            level += 1
#        return True  # all through


n, m = (int(i) for i in input().strip().split(' '))  # 1<= n,m <= 500
columns = []  # for each column store possible rows by a char:
for i in range(n + 1):
    columns.append(dict())
"""
ccc
abc
def 
-ab

columns:
[0] : {c:0, a:1, d:2, -:3}, [1] : {
"""
for i in range(m + 1):  # includes first state ('cccc..c')
    button = input().strip()
    for col_inx in range(n):
        char = button[col_inx]
        column = columns[col_inx]
        if char not in column:
            column[char] = set()
        column[char].add(i)


def test(s):
    global columns, m
    pressed_buttons = set(range(m + 1))  # variants of pressed buttons; could be all before the checking

    # move from left to right in the s and check if continuation possible
    for col_inx in range(len(s)):
        shown_char = s[col_inx]
        column = columns[col_inx]
        possible_buttons = set()
        if shown_char in column:
            possible_buttons = possible_buttons.union(column[shown_char])
        if '-' in column:
            possible_buttons = possible_buttons.union(column['-'])

        pressed_buttons = pressed_buttons.intersection(possible_buttons)
        if len(pressed_buttons) == 0:
            return False

    return len(pressed_buttons) != 0


k = int(input().strip())
for i in range(k):
    print('YES' if test(input().strip()) else 'NO')

