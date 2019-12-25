#!python3


def sort(A):
    gap = 1
    while gap < len(A):
        gap = gap*3 + 1  # 1 4 13 40 121 ...
    while gap >= 1:
        for i in range(gap, len(A), gap):
            j = i
            while j > 0 and A[j-gap] > A[j]:
                A[j-gap], A[j] = A[j], A[j-gap]
                j -= gap
        gap = gap // 3
    return A


if __name__ == '__main__':
    assert sort([3,2,1]) == [1,2,3], 'out: %s' % sort([3,2,1])
    assert sort([1]) == [1], 'out: %s' % sort([1])
    assert sort([9,1,8,2,7,3,6,4,5]) == [1,2,3,4,5,6,7,8,9]
    print('tests pass')


