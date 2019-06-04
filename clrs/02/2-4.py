"""

c) Number of swaps = number of invertions

d) See X:\Yandex\_mine\Ref\И\ИнформатикаЗадачи\hackerrank.com\challenges\ctci-merge-sort

"""
def get_inversions_IS(a):
    inversions = 0
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j-1] > a[j]:
            t = a[j-1]
            a[j-1] = a[j]
            a[j] = t
            inversions += 1
            j -= 1
    return inversions

def get_inversions_MS(a):
    inversions = 0
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j-1] > a[j]:
            t = a[j-1]
            a[j-1] = a[j]
            a[j] = t
            inversions += 1
            j -= 1
    return inversions



print(get_inversions([2,3,8,6,1]))
print(get_inversions([5,4,3,2,1]))
