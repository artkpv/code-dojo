"""
MAX HEAP


Ex.6.1-5
Is an array that is in sorted order a min-heap?
Yes. Т.к. нигде элемент слева не может быть больше элемента справа, или никакой родитель не больше своих детей.

6.1-6
Is the array with values {23;17;14;6;13;10;1;5;7;12} a max-heap?
No:
    23 - 17 .. - 6 .. - 5 7 (FAILS MAX HEAP PROPERTY)


6.5-1
15 13 9 5 12 8 7 4 0 6 2 1
heap_extract_max:
    1 13 9 5 12 8 7 4 0 6 2 | 15
    13 1 9 5 12 8 7 4 0 6 2
    13 12 9 5 1 8 7 4 0 6 2
    13 12 9 5 4 8 7 1 0 6 2 done


"""

def parent(i):
    return (i-1)//2


def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def exch(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t


def float_down(a, i):
    l = left(i)
    r = right(i)
    largest = i
    if l < len(a) and a[l] > a[i]:
        largest = l
    if r < len(a) and a[r] > a[largest]:
        largest = r
    if largest != i:
        exch(a, largest, i)
        float_down(a, largest)


def float_up(a, i):
    p = parent(i)
    if p >= 0 and a[p] < a[i]:
        exch(a, p, i)
        float_up(a, p)


def heapify(a):
    """
    Makes from iterable a heap
    """
    for i in range(len(a)//2, -1, -1):
        float_down(a, i)
    return a

def heapadd(a, el):
    """
    Adds to a heap represented by a an el
    """
    pass


if __name__ == '__main__':
    print(heapify(list(range(10**4))))

