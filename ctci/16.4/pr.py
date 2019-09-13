#!python3


class Solution(object):
    def solve(self, field, player):
        dimension = len(field)

        def otherp(p):
            if p == "X":
                return "O"
            else:
                return "X"

        def printfield():
            print("\n".join(''.join(c for c in row) for row in field))
            print("\n")

        def getwinner():
            def rows():
                for r in range(dimension):
                    yield field[r]
            def cols():
                for c in range(dimension):
                    yield [row[c] for row in field]
            def diagonals():
                yield [field[i][i] for i in range(dimension)]
                yield [field[i][-i-1] for i in range(dimension)]

            xlines = 0
            olines = 0
            for gen in (rows(), cols(), diagonals()):
                for line in gen:
                    xnum = 0
                    onum = 0
                    for c in line:
                        if c == "X":
                            xnum += 1
                        elif c == "O":
                            onum += 1
                    if xnum == dimension:
                        xlines += 1
                    elif onum == dimension:
                        olines += 1
            if xlines > olines:
                return "X"
            elif olines > xlines:
                return "O"
            return None

        def getfreecells():
            yield from (
                (r, c)
                for r in range(dimension)
                for c in range(dimension)
                if field[r][c] == '.'
            )

        def playgame(player):
            winner = getwinner()
            if winner:
                return winner
            hasdraw = False
            hasmoves = False
            for r, c in getfreecells():
                hasmoves = True
                assert field[r][c] == '.'
                field[r][c] = player
                res = playgame(otherp(player))
                field[r][c] = "."
                if res == player:
                    return res
                if res == "DRAW":
                    hasdraw = True
            if not hasmoves or hasdraw:
                return "DRAW"
            else:  # All lead to lose.
                return otherp(player)

        winner = playgame(player)
        return winner


n = int(input().strip())
player = input().strip()
field = [[c for c in input().strip()] for _ in range(n)]
winner = Solution().solve(field, player)
print(winner)
