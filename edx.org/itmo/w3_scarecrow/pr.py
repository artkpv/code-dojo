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
fr = open('input.txt')
fw = open('output.txt', 'w')

n, k = [int(i) for i in fr.readline().strip().split(' ')]
a = [int(i) for i in fr.readline().strip().split(' ')]

def quicksortx(a, k, l, r):
    """
    Sorts elements at k-th position beginning from l and ending on r

    Mid point:
     Example: k = 2, l=1, r=13
     1 3 5 7 9 11 13  -> m = 7
     0 1 2 3 4 5  6 -> offset=3, offset*k+1 = m
     Ex2: k=2 l=1, r=11
     1 3 5 7 9 11 -> m=5 (not 6)
     0 1 2 3 4 5 -> offset=2, 3th from left
     Ex3: k=1 l=0 r=9

    """
    if l >= r: 
        return
    offset = (r-l)//k//2
    m = offset * k + 1
    # choose median to improve:
    m = m if a[m] > a[l] and a[m] < a[r] else l if a[l] < a[r] else r
    p = a[m]
    i = l
    j = r
    while i <= j:
        while i < j and a[i] < p:
            i += k
        while i < j and a[j] > p:
            j -= k
        if i >= j:
            break
        a[i], a[j] = a[j], a[i]
        i += k
        j -= k
    return quicksortx(a, k, l, i-k) and quicksortx(a, k, i, r)

"""
Examples:
1) n=5, k=3, s=0, r=3, s=1 r=4, s=2 r=2, 
0 1 2 3 4
2) n=6, k=2, s=0 r=4, s=1 r=5

"""
if k == 1:
    fw.write("YES")
    exit()

for s in range(k-1):
    quicksortx(a, k, s, s+k*((n-s-1)//k))

print(a)

for i in range(1, len(a)):
    if a[i-1] > a[i]:
        fw.write("NO")
        break
else:
    fw.write("YES")
