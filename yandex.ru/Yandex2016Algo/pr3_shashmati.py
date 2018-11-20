"""
https://contest.yandex.com/algorithm2016/contest/2497/problems/C/


Строить дерево ходов. Для текущего хода кого-нибудь, найти такой ход при котором будет выигрыш,


knight (w), shashka (black)

  a b c d
1
2
3 w
4   b
             0 a3, b4, b
         (a3)               1 a3, c3, w
               2 c4, c3, b (черные выигрывают)   3 b1  4 c2  5 b5

Tree (b - black moves, w - white moves, W - white wins, B - black wins):
       b           b
    w    w   w w     w w w w
   b b  b B

Knight moves:
 1 2 3 4 5
1
2
3    k
4
5

"""

FIELD_SIZE = 8  # field size

class Position:
    def __init__(self, knight, shashka, turn, winner=None):
        self.k = knight
        self.s = shashka
        self.t = turn
        self.w = winner

    def is_s(self):
        return self.t

    def is_shashka_at_home(self):
        return self.s[1] == 1  # shasha.hor

    def _get_notation(self, v):
        return chr(ord('a') + v[0] - 1) + str(v[1])

    def __eq__(self, other):
        return self.k == other.k and self.s == other.k and  self.t == other.t

    def __hash__(self):
        return hash((self.k, self.s, self.t))

    def __str__(self):
        return '({} {} {} "{}")'.format( \
                self._get_notation(self.k), \
                self._get_notation(self.s), \
                'shashka' if self.is_s() else 'knight', \
                self.w + ' wins' if self.w else '')


class Game:
    def __init__(self, root):
        if root.is_shashka_at_home():
            root.w = 'shashka'

        self.root = root
        self.G = {root: []}
        self._add_moves([root])

    def _add_moves(self, queue):  # BFS
        """
        Строит дерево всех ходов
        """
        while len(queue) > 0:
            v = queue.pop()
            if v not in self.G:
                self.G[v] = []
            if v.w is None:  # not game end
                for w in self._next_moves(v):
                    self.G[v] += [w]
                    if w not in self.G:
                        queue.insert(0, w)
        # end of while, all moves in G

    def _next_moves(self, v):
        global FIELD_SIZE
        assert v.w is None, 'not game end'

        sver = v.s[0]
        shor = v.s[1]
        kver = v.k[0]
        khor = v.k[1]

        if v.is_s():  # shashka
            assert shor != 1, "shashka didn't reach last line"
            # left move:
            if sver > 1: # can move to left
                if sver - 1 == kver and shor - 1 == khor:  # knight there
                    if sver > 2 and shor > 2:  # there is space to jump
                        yield Position(v.k, (sver - 2, shor - 2), False, 'shashka')
                    # else there is no space to jump over
                else:  # knight not there
                    yield Position(v.k, (sver - 1, shor - 1), False, 'shashka' if shor == 2 else None)

            # right move:
            if sver < FIELD_SIZE: # can move
                if sver + 1 == kver and shor - 1 == khor:  # knight there
                    if sver < FIELD_SIZE - 1 and shor > 2:  # there is space to jump
                        yield Position(v.k, (sver + 2, shor - 2), False, 'shashka')
                    # else there is no space to jump over
                else:  # knight not there
                    yield Position(v.k, (sver + 1, shor - 1), False, 'shashka' if shor == 2 else None)

        else:  # knight moves
            get_move = lambda k: Position(k, v.s, True, 'knight' if k == v.s else None)
            # left 4 moves:
            if kver - 2 > 0 and khor - 1 > 0:
                yield get_move((kver - 2, khor - 1))
            if kver - 1 > 0 and khor - 2 > 0:
                yield get_move((kver - 1, khor - 2))
            if kver - 2 > 0 and khor + 1 <= FIELD_SIZE:
                yield get_move((kver - 2, khor + 1))
            if kver - 1 > 0 and khor + 2 <= FIELD_SIZE:
                yield get_move((kver - 1, khor + 2))

            # right 4 moves:
            if kver + 2 <= FIELD_SIZE and khor - 1 > 0:
                yield get_move((kver + 2, khor - 1))
            if kver + 1 <= FIELD_SIZE and khor - 2 > 0:
                yield get_move((kver + 1, khor - 2))
            if kver + 2 <= FIELD_SIZE and khor + 1 <= FIELD_SIZE:
                yield get_move((kver + 2, khor + 1))
            if kver + 1 <= FIELD_SIZE and khor + 2 <= FIELD_SIZE:
                yield get_move((kver + 1, khor + 2))


    def winner(self):
        return self._winner(self.root)

    def _winner(self, v):
        # выигрышь в текущей позиции определяется тем,
        # может ли игрок, делающий ход сейчас выбрать выигрышный
        # вариант. Если вариант не определен, то спускаемя ниже по дереву.
        if not v.w:
            moves = self.G[v]
            if v.is_s():  # shashka
                v.w = 'shashka' \
                        if any(self._winner(w) == 'shashka' for w in moves) \
                        else 'knight'
            else:
                v.w = 'knight' \
                        if any(self._winner(w) == 'knight' for w in moves) \
                        else 'shashka'
        return v.w

    def __str__(self):
        return self.s(self.root, 0)

    def s(self, v, level):
        s = (' ' * level) + str(v) + '\n'
        for w in self.G[v]:
            s += self.s(w, level + 1)
        return s




turn = (input().strip() == 'black')  # otherwise it is white
parse = lambda s: ((ord(s[0]) - ord('a') + 1), int(s[1]))  # (ver, hor)
knight = parse(input().strip())  # white knight
shashka = parse(input().strip())  # black shashka

first = Position(knight, shashka, turn)
game = Game(first)  # (white position, black position, who moves next, who won)
w = game.winner()
print('white' if w == 'knight' else 'black')
