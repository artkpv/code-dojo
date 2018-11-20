
import math, time
primelist = [2, 3, 5, 7, 11, 13]

def isprime(num):
    for i in primelist:
        if i > math.sqrt(num):
            return True
        elif num % i == 0:
            return False

def buildprimelist(num):
    if isprime(num):
        primelist.append(num)

def numberofprimes(listsize):
    time0 = time.time()
    number = primelist[-1] + 2
    while len(primelist) < listsize:
        buildprimelist(number)
        number += 2
    print('Time of execution' + str(time.time() - time0))

numberofprimes(10001)
print(primelist)
