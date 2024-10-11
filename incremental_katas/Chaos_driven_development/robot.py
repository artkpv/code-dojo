

class Robot():
    def __init__(self, size=2):
        self._x = size - 1
        self._y = size - 1
        self._face = 'N'
        self._size = size

    def draw(self):
        return '\n'.join(
            ''.join(
                f'[{self._face if self._x == x and self._y == y else " "}]'
                for y in range(self._size)
            )
            for x in range(self._size)
        )

    def move(self, command, steps=1):
        POLES = 'NESW'
        POLES_M = ((-1, 0), (0, 1), (1, 0), (0, -1))
        if command[0] == 'T':
            d = -1 if command[1] == 'L' else 1
            self._face = POLES[(POLES.index(self._face) + d) % len(POLES)]
        elif command[0] == 'D':
            p_inx = POLES.index(self._face)
            move_x, move_y = POLES_M[p_inx]
            if command[1] == 'B':
                move_x *= -1
                move_y *= -1
            else:
                assert command[1] == 'F'

            move_x *= steps
            move_y *= steps

            nx = self._x + move_x
            ny = self._y + move_y
            if 0 <= nx < self._size and 0 <= ny < self._size:
                self._x = nx
                self._y = ny
