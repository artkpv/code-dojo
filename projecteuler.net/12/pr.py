'''
...

5770 16649335 15
5771 16655106 63
5772 16660878 63
5773 16666651 7
'''
def factor(n):
    res = 0
    for i in range(1, n//2 + 1):
        if n % i == 0:
            res += 1
    return res

def solve():
    n = 5772
    tn = 16666651
    while True:
        n += 1
        tn += n
        divs = factor(tn)
        print(n, tn, divs)
        if divs > 500:
            break

solve()

