#!python3

def is_valid(p, n, dobstacles):
    if p in dobstacles:
        return False
    if p[0] < 1 or p[0] > n:
        return False
    if p[1] < 1 or p[1] > n:
        return False
    return True

def queensAttack(n, k, r_q, c_q, obstacles):
    dobstacles = set((o[0], o[1]) for o in obstacles)
    directions = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
    count = 0
    for d in directions:
        p = (r_q, c_q)
        while True:
            p = (p[0]+d[0], p[1]+d[1])
            if is_valid(p, n, dobstacles):
                count += 1
            else:
                break
    return count


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    r_qC_q = input().split()
    r_q = int(r_qC_q[0])
    c_q = int(r_qC_q[1])
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    result = queensAttack(n, k, r_q, c_q, obstacles)
    print(result)
