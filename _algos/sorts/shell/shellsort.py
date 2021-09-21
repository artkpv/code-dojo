
def shellsort(a):
    n = len(a)
    if n == 0:
        return a
    gap = 1
    while gap * 3 + 1 < n:  # 1 4 13 40 121 ...
        gap = gap * 3 + 1
    while gap > 0:
        i = gap
        while i < n:
            j = i
            while j - gap >= 0 and a[j-gap] > a[j]:
                a[j-gap], a[j] = a[j], a[j-gap]
                j -= gap
            i += gap
        gap //= 3
    return a

def myassert(a):
    print(f'TEST {a}')
    b = shellsort(a.copy())
    assert sorted(a) == b, f' res: {b}'
    print('PASS')

myassert([])
myassert([1])
myassert([9,2,2,48,3])
myassert([1,2,4,9,7,6,5,4])
myassert(list(range(100, 0, -1)))


    
