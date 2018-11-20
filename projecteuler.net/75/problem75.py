"""
https://projecteuler.net/problem=75

Singular integer right triangles
Problem 75
It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
3/12 = 1/4
4/12 = 1/3


24 cm: (6,8,10)
6/24 = 1/4
8/24 = 1/3

30 cm: (5,12,13)
5/30 = 1/6
12/30 =

36 cm: (9,12,15)
9/36 =

40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?

----

Кол-во треугольников, для длины a: ~a^3
> sum(i**3 for i in range(1_500_000))
1265623312500562500000000
> s = sum(i**3 for i in range(1_500_000))
> s / 10**9
1265623312500562.5
> s / 10**9 / 60
21093721875009.375
> s / 10**9 / 60 / 60
351562031250.15625  hours?!
>

Results ( l, a, l/a, b, l/b, l - a - b ):
12: 3(4) 4(3) 5
24: 6(4) 8(3) 10
30: 5(6) 12(2.5) 13
36: 9(4) 12(3) 15
40: 8(5) 15(2.6666666666666665) 17
48: 12(4) 16(3) 20
56: 7(8) 24(2.3333333333333335) 25
60: 10(6) 24(2.5) 26
70: 20(3.5) 21(3.3333333333333335) 29
72: 18(4) 24(3) 30
80: 16(5) 30(2.6666666666666665) 34
84: 12(7) 35(2.4) 37
90: 9(10) 40(2.25) 41
96: 24(4) 32(3) 40
108: 27(4) 36(3) 45
112: 14(8) 48(2.3333333333333335) 50
120: 20(6) 48(2.5) 52
126: 28(4.5) 45(2.8) 53
132: 11(12) 60(2.2) 61
140: 40(3.5) 42(3.3333333333333335) 58
144: 16(9) 63(2.2857142857142856) 65
150: 25(6) 60(2.5) 65
154: 33(4.666666666666667) 56(2.75) 65
156: 39(4) 52(3) 65
160: 32(5) 60(2.6666666666666665) 68
168: 21(8) 72(2.3333333333333335) 75
176: 48(3.6666666666666665) 55(3.2) 73
180: 18(10) 80(2.25) 82
182: 13(14) 84(2.1666666666666665) 85
192: 48(4) 64(3) 80
198: 36(5.5) 77(2.5714285714285716) 85
200: 40(5) 75(2.6666666666666665) 85
204: 51(4) 68(3) 85
208: 39(5.333333333333333) 80(2.6) 89
210: 35(6) 84(2.5) 91
216: 54(4) 72(3) 90

----
Progress:

1. Brute force. O(L^3): 300 in 20 sec. 3750 hours

2. With some math: O(L^2). w=58498 in 602s. 4.3hrs

3. Through this:
        https://ru.wikipedia.org/wiki/Целочисленный_треугольник
        https://ru.wikipedia.org/wiki/Целочисленный_треугольник#.D0.A2.D1.80.D0.B5.D1.83.D0.B3.D0.BE.D0.BB.D1.8C.D0.BD.D0.B8.D0.BA.D0.B8_.D0.93.D0.B5.D1.80.D0.BE.D0.BD.D0.B0
        https://ru.wikipedia.org/wiki/Пифагорова_тройка

-----

Next:
      - why 157730 is not answer?


"""

L = 1_500_000
m, n, k = 2, 1, 1

triangles = [[] for i in range(L)]

def gcd(k, v):
    if v == 0:
        return k
    return gcd(v, k % v)

# to print progress:
import timeit, sys, threading
start = timeit.default_timer()
def print_progress():
    global m, n, k
    time = int(timeit.default_timer() - start)
    speed = m // time if time > 0 else 0
    sys.stdout.write("\r m={}, n={}, k={} in {}s ({} m/s)".format(m, n, k, time, speed ))
    threading.Timer(1, print_progress).start()
print_progress()

# TODO. TOO LONG. ~2 hrs more.  m=19102, n=2133, k=1 in 386s (49 m/s)
for m in range(2, L // 4 + 1):
    for n in range(1, m):
        # взаимнопростые:
        if gcd(m, n) != 1:
            continue
        # не оба нечетны
        if m % 2 == 1 and n % 2 == 1:
            continue

        k = 1
        while True:
            a = k*(m**2 - n**2)
            b = k*2*m*n
            c = k*(m**2 + n**2)
            p = a + b + c
            if p > L:
                break
            if sorted((a, b, c)) not in triangles[p - 1]:
                triangles[p - 1] += [sorted((a, b, c))]

            k += 1

count = sum(1 if len(i) == 1 else 0 for i in triangles)
print(count)
for i in range(L):
    t = triangles[i]
    if len(t) > 0:
        print('{}: {}'.format(i + 1, str(t)))

exit()



# BRUTE FORCE BELOW:
# ====================================================================


def has_only_one_rat(l):
    found = 0
    for a in range(1, l//2 + 1):
        r = (l**2 - 2*l*a) % (2*l-2*a)
        if r == 0:
            found += 1
            if found > 1:
                return False
    return found == 1


count = 0
w = 0

# to print progress:
import timeit, sys, threading
start = timeit.default_timer()
def print_progress():
    global w, count, start
    time = int( timeit.default_timer() - start)
    speed = w // time if time > 0 else 0
    sys.stdout.write("\r w={}, count={} in {}s ({} l/s)".format(w, count, time, speed ))
    threading.Timer(1, print_progress).start()
print_progress()

# run calculation:
while w <= L:
    if has_only_one_rat(w):
        count += 1
    w += 1

