#!python3

def csort(a, radix):
    count = [0] * (radix + 2)
    for i,e in enumerate(a):  # count frequencies
        count[e+1] += 1
    for i in range(1, radix+1):  # build index
        count[i] += count[i-1]   # count[i] - num of items before
    aux = [None] * len(a)
    for i,e in enumerate(a):  # copy;
        aux[count[e]] = e
        count[e] += 1
    for i,e in enumerate(aux):  # copy sorted
        a[i] = e


if __name__ == '__main__':
    a = [1,9,2,8,3,7,4,6,5,0]
    print('Sort: ', a)
    csort(a, 9)
    print( a)
