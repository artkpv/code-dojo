#!python3

num1,num2 = [int(i) for i in input().strip().split(' ')]
A = [int(i) for i in input().strip().split(' ')]
B = [int(i) for i in input().strip().split(' ')]

def is_good(n):
    global A, B
    for i in A:
        if n%i != 0:
            return False
    for i in B:
        if i%n != 0:
            return False
    return True

count = 0
C = set()
for i in range(len(A)):
    for j in range(len(B)):
        q,r = divmod(B[j], A[i])
        if r != 0:
            print(0)
            exit()
        if is_good(q):
            C.add(q)

print(C)
print(len(C))
