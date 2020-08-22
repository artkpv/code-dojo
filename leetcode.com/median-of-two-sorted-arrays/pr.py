#!python3

from math import ceil, floor
import sys

def at(arr, i):
    if i < 0:
        return -float('inf')
    if len(arr) <= i:
        return float('inf')
    return arr[i]


def trace(*args):
    sys.stderr.write(str.join(' ', [str(e) for e in args]) + "\n")


class Solution:
    def findMedianSortedArrays(self, A, B):
        al = len(A)
        bl = len(B)
        if al == 0 and bl == 0:
            return None
        def a(inx):
            return at(A, inx)
        def b(inx):
            return at(B, inx)
        even = (al + bl) % 2 == 0
        alo = 0
        ahi = al
        while alo <= ahi:
            i = (alo + ahi) // 2
            j = (al + bl - 2 * i - (0 if even else 1)) // 2
            c = max(a(i-1), b(j-1))
            cc = min(a(i), b(j))
            trace(i, j, c, cc)
            if c <= cc:
                if even:
                    return (c + cc) * 1.0 / 2.0
                else:
                    if a(i) <= b(j):
                        return a(i) * 1.0
                    else:
                        return b(j) * 1.0
            elif c == a(i-1):
                ahi = i - 1
            else:
                alo = i + 1
                # if c == a(i-1):
                    # j = min(bl, j + i // 2)
                    # i = (al + bl - 2 * j - (0 if even else 1)) // 2
                # else:
                    # i = min(al, i + j // 2)
                    # j = (al + bl - 2 * i - (0 if even else 1)) // 2
        """
        1 2 5
        3 4 6 7 8

        i 1
        j 3
        c 6
        cc 2

        

        """

        # if (al + bl) % 2 == 0:
            # while True:
                # if a(i-1) <= b(j) and b(j-1) <= a(i):
                    # return (max(a(i-1), b(j-1)) + min(a(i), b(j))) / 2.0
                # elif a(i) < b(j-1):
                    # i = i + 1 if i + 1 == al else (i + al) // 2
                    # j = max(0, al + bl - 2 * i) // 2
                # elif b(j) < a(i-1):
                    # j = j + 1 if j + 1 == bl else (j + bl) // 2
                    # i = max(0, al + bl - 2 * j) // 2
                # else:
                    # raise Exception('bad even')
        # else:  # Odd
            # i = al // 2
            # j = (al + bl - 2 * i - 1) // 2
            # while True:
                # if a(i-1) <= b(j) <= a(i):
                    # return b(j) * 1.0
                # elif b(j-1) <= a(i) <= b(j):
                    # return a(i) * 1.0
                # elif b(j) < a(i-1):
                    # j = j + 1 if j + 1 == bl else (j + bl) // 2
                    # i = max(0, al + bl - 2 * j - 1) // 2
                # elif a(i) < b(j-1):
                    # i = i + 1 if i + 1 == al else (i + al) // 2
                    # j = max(0, al + bl - 2 * i - 1) // 2
                # else:
                    # raise Exception("bad odd")
        raise Exception("Should have found")


if __name__ == "__main__":
    tests = int(input().strip())
    for test in range(tests):
        A = [int(e) for e in input().strip().split(' ')]
        B = [int(e) for e in input().strip().split(' ')]
        median = Solution().findMedianSortedArrays(A, B)
        print("Test #{}: {}".format(test + 1, median))
    # assert Solution().findMedianSortedArrays([1,3], [2]) == 2.0, Solution().findMedianSortedArrays([1,3], [2])
    # print('test 1 pass')
    # assert Solution().findMedianSortedArrays([1,2], [3,4]) == 2.5, Solution().findMedianSortedArrays([1,2], [3,4])
    # print('test 2 pass')
    # assert Solution().findMedianSortedArrays([1,2,3,5,6], [4]) == 3.5, Solution().findMedianSortedArrays([1,2,3,5,6], [4])
    # print('test 3 pass')
    # """
    # al 5  bl 1
    # i 2
    # j 1
    # 1:
        # c = 4
        # cc = 3
        # > c != a(1) = 2
    # """
    # assert Solution().findMedianSortedArrays([1,2,3,4,6,7,8], [5]) == 4.5, Solution().findMedianSortedArrays([1,2,3,4,6,7,8], [5])
    # print('test 4 pass')
    # assert Solution().findMedianSortedArrays([1,2], [3,4,5,6,7,8]) == 4.5, Solution().findMedianSortedArrays([1,2], [3,4,5,6,7,8])
    # print('test 5 pass')

