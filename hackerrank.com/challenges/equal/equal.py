"""
Hackerrank Equal problem
https://www.hackerrank.com/challenges/equal/problem

Min num of operations to get equal number of chocos.
Operations: give 1/2/5 except some one.

A1 = 8 8 8  / 24

op1 col1 - 22 sum
    col2
    col3
op2 col1 - 20 sum
    col2
    col3

Example. In:
"1
4
2 2 3 7"
Out:
2
--
2 2 3 7 | 0 0
3 3 3 8 | 3 1
8 8 8 8 | 4 6 (6 // 5 = 1, 6%


1    1000 1000 A1 0   0
1000 1999 1000 A2 3th 201 (999//5= 199, 999%5//2 = 2, 999%5%2 = 0)
1999 1999 1999 A3 2th 402 (999//5= 199, 999%5//2 = 2, 999%5%2 = 0)

Оптимальное решение - сама последовательность, элемент не изменненый с предыдущего опт. решения, кол-во операций ?


----------------

Opt. sol.: набор чисел и кол-во шагов минимальное до этих цифр от исходныого набора цифр. - А
А - 1, 2, 5 * кол-во элементов (30000) -  оптималь. наборы, от исходного до этих ... Как двигаться до исходноо набора? Как увеличивать до равного?

2 2 3 7  | 0 0 1 5 (разница между мин и макс
1 2 3 4 5 6 | 0 1 2 3 4 5
1 50 100 150 200 250 | 0 49 99 149 199 249

1 50
5 50 | 2 * 2
50 50 | 5 * 5

1 50 100
5 50 104 | 2 * 2
50 50 149 | 5 * 5
54 54 149 | 2 * 2
149 149 149 | 5 * 19  | всего: 28 шагов


100 50 1
100 100 50 | 5 * 10
???




Брут форс?

1. Нашел минимум и максимум.
2. Вычислил для каждого расстояние до минимума. Высоту.
3. ...

sort(a) # asc
steps = 0
for i in range(1, n):
    d = a[i] - a[i-1]
    if d > 0:
        steps += get_steps(d)


А если 0 1 1 1 2 ?



"""
import sys

sys.setrecursionlimit(10000)

def increase(x, A, k):  # increase all with x except k-th
    assert k > 0, "won't increase the smallest element"
    B = [A[i] + x if i != k else A[i] for i in range(len(A))]
    # insert k-th element to maintain order:
    i, j = k - 1, k
    while i > 0 and B[i] > B[j]:
        t = B[i]
        B[i] = B[j]
        B[j] = t
        j = i
        i -= 1
    return tuple(B)


MAX = sys.maxsize
D = {}  # min distance from an item (array) to the equal
def EqualTD(A):
    # assert A sorted
    global D, MAX
    if all(A[i] == A[0] for i in range(len(A))):
        return 0
    if A not in D:
        _min = MAX
        for i in range(1, len(A)):
            # TODO: unclear here how to increase. It gets error (stackoverflow?) then as unlimitted number of such arrays
            Ai5 = increase(5, A, i)
            Ai2 = increase(2, A, i)
            Ai1 = increase(1, A, i)
            _min = 1 + min(EqualTD(Ai1), EqualTD(Ai2), EqualTD(Ai5))
        D[A] = _min
    return D[A]

T = int(input().strip())
N = int(input().strip())
A = tuple(sorted(int(i) for i in input().strip().split(' ')))
print(EqualTD(A))
