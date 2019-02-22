#!python3
"""

arr, n length 
swap k
1 <= n,k <= 10^6
Out: YES / NO


I1. BF, O(n^2)
for i in k-1..n-1:  // ~n
    for j in i..k-1:  // O(n)
        if < 
            break
        swap
check ordered  // ~n

I2. Modif. quicksort with k-th place swap
Can put in any order on k-th places.
x1 .. x_m   1  5 9 
y_1 .. y_p  2 4  10
inx(x_i) < inx(y_i) and max(x_i) > max(y_i) - and otherwise


I3 
Run Quicksort on k-th groups. n/k times. O(k*n/k*log(n/k)) = O(n*log(n/k))
Run check. ~n



E0
3 2
2 1 3

E1 
5 3
1 5 3 4 1

E2
6 2
1 2 5 4 9 10

"""
import sys
fr = open('input.txt' if len(sys.argv) < 2 else sys.argv[1])
fw = open('output.txt', 'w')

n, k = [int(i) for i in fr.readline().strip().split(' ')]
a = [int(i) for i in fr.readline().strip().split(' ')]

def sort_by_k(a, k, left, right):
    """
    Sorts elements at k-th position beginning from left and ending on right
    """
    if left >= right: 
        return
    """ 
    Mid point:
     a=0 1 2 3 4 5 6 
     k=2, left=0, right=6 => m=2

     a[2..11]= { 2 3 4 5 6 7 8 9 10 11 }, 2 5 8 11
     k=3 (from 2), left=2, right=11 => m = 5
    """
    elements_num = right-left + 1
    k_th_elements_num = elements_num // k + 1
    middle_el_num = k_th_elements_num // 2
    middle_inx = left + (middle_el_num - 1)*k
    pivot = a[middle_inx]
    i = left
    j = right
    while i <= j:
        while a[i] < pivot:
            i += k
        while a[j] > pivot:
            j -= k
        if i <= j:
            a[i], a[j] = a[j], a[i]
            i += k
            j -= k
    return sort_by_k(a, k, left, i-k) and sort_by_k(a, k, i+k, right)

if k == 1:
    fw.write("YES")
    exit()

"""
Examples:
1) n=5, k=3, s=0, r=3, s=1 r=4, s=2 r=2, 
0 1 2 3 4
2) n=6, k=2, s=0 r=4, s=1 r=5
"""
for left in range(k-1):
    right = left + k*(n//k)
    while right >= n:
        right -= k
    sort_by_k(a, k, left, right)

# print(a)

i = 1
while i < len(a):
    if a[i-1] > a[i]:
        fw.write("NO")
        break
    i += 1
else:
    fw.write("YES")
