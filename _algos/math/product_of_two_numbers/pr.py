#!python3

def product(a, b):
    if not a or not b:
        return None
    if (len(a) == 1 and a[0] == 0) or (len(b) == 1 and b[0] == 0):
        return [0]
    sign = 1 if (a[0] > 0 and b[0] > 0) or (a[0] < 0 and b[0] < 0) else -1
    a[0] = abs(a[0])
    b[0] = abs(b[0])
    c = []
    for i in range(len(b)):
        for j in range(len(a)):
            x = b[-1-i] * a[-1-j]
            k = i + j
            while x > 0:
                while len(c) < k + 1:
                    c += [0]
                c[k] += x % 10
                x = x // 10 + c[k] // 10
                c[k] %= 10
                k += 1
    c = list(reversed(c))
    c[0] *= sign
    return c


def toint(arr):
    res = ''.join(str(e) for e in arr)
    return int(res)


assert toint(product([1,2,3,4], [5,6,7])) == 1234 * 567
assert toint(product([1,2,3,4,5,6,7,8,9,0,1,2,4,5], [5,6,7])) == 12345678901245 * 567
print('works')
