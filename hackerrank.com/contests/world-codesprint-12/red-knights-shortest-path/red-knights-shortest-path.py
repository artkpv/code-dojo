#!python3

import sys, math

def coord_to_inx(n, c):
    return c[0] * n + c[1]

def inx_to_coord(n, i):
    return (int(math.floor(i/n)), i%n)

def move_desc(from_, to_):
    #print(' move_descr' + str(from_) + ' ' + str(to_))
    row = from_[0] - to_[0]
    col = from_[1] - to_[1]
    if row == 2:
        if col == 1:
            return 'UL'
        if col == -1:
            return 'UR'
    if row == 0:
        if col == 2:
            return 'L'
        if col == -2:
            return 'R'
    if row == -2:
        if col == 1:
            return 'LL'
        if col == -1:
            return 'LR'
    raise 'invalid coords: ' + str(from_) + ' ' + str(to_)

def adj(n, v, quarter): # quarter: 1, 2, 3, 4
    row, col = v
    if row - 2 >= 0:
        if col - 1 >= 0:# and quarter == 2:
            yield (row-2, col-1)
        if col + 1 < n:# and quarter == 1:
            yield (row-2, col+1)
    if col + 2 < n: # and quarter in [1, 4]:
        yield (row, col+2)
    if row + 2 < n:
        if col + 1 < n:# and quarter == 4:
            yield (row+2, col+1)
        if col - 1 >= 0:# and quarter == 3:
            yield (row+2, col-1)
    if col - 2 >= 0:# and quarter in [2, 3]:
        yield (row, col-2)

def get_quarter(s, t):
    s_row, s_col = s
    t_row, t_col = t
    if t_row <= s_row:
        if t_col >= s_col:
            return 1
        else:
            return 2
    else:
        if t_col >= s_col:
            return 3
        else:
            return 4

def printShortestPath(n, i_start, j_start, i_end, j_end):
    #  Print the distance along with the sequence of moves.
    if (i_start%2) != (i_end%2):
        print("Impossible")
        exit()
    is_t_same_row_kind = (abs(i_start - i_end) // 2)%2 == 0
    if is_t_same_row_kind and j_start%2 != j_end%2:
        print("Impossible")
        exit()
    if not is_t_same_row_kind and j_start%2 == j_end%2:
        print("Impossible")
        exit()
    s = (i_start, j_start)
    t = (i_end, j_end)
    marked = set()
    q = []
    pathto = [-1] * (n*n)
    q.append(s)
    found = False
    quarter = get_quarter(s, t)
    while len(q) > 0:
        v = q.pop()
        v_inx = coord_to_inx(n, v)
        for w in adj(n, v, quarter):
            if w not in marked:
                marked.add(w)
                q.insert(0, w)
                #print(q)
                #for r_to_print in range(n):
                #    print(' '.join(str(c) for c in pathto[r_to_print * n:r_to_print*n + n]))
                pathto[coord_to_inx(n, w)] = v_inx
                if w == t:
                    found = True
                    break
        if found:
            break
    if not found:
        raise 'error'
    path = []
    v = t
    while True:
        w = inx_to_coord(n, pathto[coord_to_inx(n, v)])
        path += [move_desc(w, v)]
        v = w
        if v == s:
            break
    print(len(path))
    print(' '.join(reversed(path)))


if __name__ == "__main__":
    n = int(input().strip())
    i_start, j_start, i_end, j_end = input().strip().split(' ')
    i_start, j_start, i_end, j_end = [int(i_start), int(j_start), int(i_end), int(j_end)]
    printShortestPath(n, i_start, j_start, i_end, j_end)
