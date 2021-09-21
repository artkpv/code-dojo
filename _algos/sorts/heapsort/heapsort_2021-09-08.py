
'''
IN:  5 4 2 9 1 0 
OUT: 0 1 2 4 5 9

Build max heap
Del max

'''

def heapsort(a):
    b = [None] + a.copy()
    n = len(a)
    def sift_down(i):
        while i*2 <= n:
            k = i * 2
            if k+1 <= n and b[k+1] > b[k]:
                k += 1
            if b[k] <= b[i]:
                break
            b[k], b[i] = b[i], b[k]
            i = k
    for i in range(n//2, 0, -1):
        sift_down(i)
    while n > 1:
        b[1], b[n] = b[n], b[1]
        n -= 1
        sift_down(1)
    return b[1:]


def myassert(a):
    print(f'TEST: {a}')
    r = heapsort(a.copy())
    assert r == sorted(a), f' res: {r}'
    print('PASS')

myassert([1])
myassert([1, 10, 9, 8, 7, 6, 5, 4, 3, 2])
myassert([])
myassert([1, 2, 3])
myassert([3, 2, 3])
        


        



