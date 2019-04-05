#!python3
"""

swap
reverse

"""


def is_order(arr):
    return all(i == 0 or arr[i-1] < e for i, e in enumerate(arr))



def getanswer_orderway(array):
    # TODO BUG
    order = sorted(array)
    left = None
    right = None
    i = 0
    cansort = True
    isswap = False
    n = len(array)
    while cansort and i < n:
        if array[i] == order[i]:
            i += 1
        else:  # array[i] != order[i]:
            if left is None:
                left = i
                right = left + 1
                while right < n and array[right] != order[right]:
                    right += 1
                right -= 1
                i = right + 1
            else:  # left is not None
                if right == left:
                    right = i
                    i = right + 1
                    isswap = True
                else:
                    cansort = False
    if right - left == 1:
        isswap == True
    result = 'yes' if cansort else 'no'
    if cansort and left is not None:
        result += '\n%s %d %d' % (
            'swap' if isswap else 'reverse',
            left+1, right+1
        )
    return result


def is_ascend(a, i, j):
    if not (0 <= i < len(a)) or not (0 <= j < len(a)):
        return True
    return a[i] < a[j]


def getreverse(a, i):
    j = i + 1
    n = len(a)
    while j < n and not is_ascend(a, j-1, j):
        j += 1
    j -= 1
    if j - i == 1:  # it is swap
        return None
    return (i, j)


def getswap(a, i):
    if not is_ascend(a, i, i+1):  # reverse that is swap
        return (i, i+1)
    for j, e in enumerate(a):
        if not is_ascend(a, j-1, j):
            return (i, j)
    return None


def cansort(a, n):
    reverse = None
    swap = None
    for i, e in enumerate(a):
        if not is_ascend(a, i-1, i):
            if reverse or swap:
                return (False, None, None)
            reverse = getreverse(a, i)
            if not reverse:
                swap = getswap(a, i)
    return (True, reverse, swap)


def getresult(a, n):
    can, reverse, swap = cansort(a, n)
    result = 'yes' if can else 'no'
    if can:
        result += '\n'
        result += '%d %d' % (reverse or swap)
    return result



n = int(input('').strip())
array = [int(i) for i in input('').strip().split(' ')]
print(getresult(array, n))
exit()


left = None
right = None
cansort = True
swap_right = None
i = 1
while i < n and cansort:
    if array[i-1] < array[i]:
        i += 1
    else:  # a[i-1] > a[i] as all distinct
        if left is None:  # all elements before -- sorted
            left = i-1
            j = left + 1
            while j < n and array[j-1] > array[j]:
                j += 1
            right = j - 1
            # now: a[left] > .. > a[right], left < right

            # if right end is good:
            if left > 0 and not (array[left-1] < array[right]):
                cansort = False
                break
            # if left end is good:
            elif right < n - 1 and not (array[left] < array[right+1]):
                # possible swap of a[left]:
                if right - left == 1:
                    i = left + 2
                else:
                    cansort = False
                    break
            else:  # reversable interval
                i = right + 2
        else:
            # Exist: left < right < i-1
            # a[i-1] > a[i]
            if (swap_right is not None  # second swap
                    or right - left > 1):  # can not swap
                cansort = False
                break
            else:  # possible swap
                array[left], array[i-1] = array[i-1], array[left]
                if is_order(array[left-1:left+2] + array[i-2:i+1]):
                    swap_right = i-1
                    i += 1
                else:
                    cansort = False
                    break

print('yes' if cansort else 'no')
if cansort and left is not None:
    if right - left == 1 or swap_right:
        print('swap', left+1, (swap_right or right) + 1)
    else:
        print('reverse', left+1, right+1)
