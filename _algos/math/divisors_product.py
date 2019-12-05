#!python3

def dp(n):
    if n == 1:
        return 1
    count = 2
    d = 2
    while d * d <= n:
        if n % d == 0:
            count += 2
            if d * d == n:
                count -= 1
        d += 1
    return int(pow(n, count / 2))



assert dp(1) == 1
assert dp(2) == 2
assert dp(3) == 3
assert dp(4) == 8, 'Res= ' + str(dp(4))  # 4 ^1.5
assert dp(5) == 5
assert dp(6) == 36
assert dp(7) == 7
assert dp(8) == 64
assert dp(9) == 27
assert dp(10) == 100
assert dp(11) == 11
assert dp(12) == 1728

