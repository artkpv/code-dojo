#!python3

import sys
sys.setrecursionlimit(10000)


def merge(A, l, m, r, aux):
    for i in range(l, m+1):
        aux[i] = A[i]
    for i in range(m+1, r+1):
        aux[i] = A[i]
    i, j = l, m+1
    i_last = m
    j_last = r
    inversions = 0
    for k in range(l, r+1):
        if i > i_last:
            A[k] = aux[j]
            j += 1
        elif j > j_last:
            A[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            A[k] = aux[i]
            i += 1
        else:
            A[k] = aux[j]
            j += 1
            inversions += i_last - i + 1  # number of elements greater than R[j] in L
    return inversions


def merge_sort_inversions(a, l, r, aux):
    if l < r:
        mid = l + (r - l) // 2
        inversions = merge_sort_inversions(a, l, mid, aux)
        inversions += merge_sort_inversions(a, mid+1, r, aux)
        inversions += merge(a, l, mid, r, aux)
        return inversions
    return 0


d = int(input().strip())
for t in range(d):
    n = int(input().strip())
    a = [int(i) for i in input().strip().split(' ')]
    aux = [None] * n
    print(merge_sort_inversions(a, 0, len(a) - 1, aux))




