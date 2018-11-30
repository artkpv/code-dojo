#!python3

"""
Дан массив чисел длинны N. Нужно найти любые два числа не превосходящие значение t и не отстоящие друг от друга на k.


Ex.1
a k t
0 100 , 1 100



"""

def find_nn(a, t, k):
    j = -1
    for i in range(len(a)):
        if j > -1 and j < i - k:
            j = -1
        if a[i] <= t:
            if j != -1:
                return [a[j], a[i]]
            j = i
    return []



if __name__ == '__main__':
    assert(find_nn([1,2], 10, 1) == [1,2])
    assert(find_nn([1,11], 10, 1) == [])
    assert(find_nn([1,11,2], 10, 2) == [1,2])
    assert(find_nn([1,11,2], 10, 1) == [])
