#!python3
"""
arr, n=10^5
min swaps for beautiful
beautiful: min sum of |a[i] - a[i-1]|, i=0..n

Idea 1
asc sort
desc sort

swaps to sort 1
swaps to sort 2

Time: n*log(n)*4
Space: ~n


Ex 1
7 15 12 3
desc 15 12 7 3
     7 15 12 3
     12 15 7 3
     15 12 7 3  2
asc 7 15 12 3
    15 7 12 3
    3 7 12 15

3 7 12 15

Example 2
2 5 3 1

desc
3 5 2 1
5 3 2 1  2

Example 3


4 3 2 1


"""


def getswaps(order, array):
    swaps = 0
    num_to_inx = {e: i for i, e in enumerate(order)}
    for i in range(len(array)):
        while array[i] != order[i]:
            j = num_to_inx[array[i]]
            array[i], array[j] = array[j], array[i]
            swaps += 1
    return swaps


n = int(input('').strip())
array = [int(i) for i in input('').strip().split(' ')]

sarray = list(sorted(array))
swaps = getswaps(sarray, array.copy())
desc_swaps = getswaps(list(reversed(sarray)), array)
print(min(swaps, desc_swaps))
