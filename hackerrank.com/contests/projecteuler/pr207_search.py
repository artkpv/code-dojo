import matplotlib.pyplot as plt
import math
import sys


y = 2**(1/100)
print(' '.join("{}:{}".format(i, y**(i-1)-i) for i in range(2,100)))
n = range(2,1300)
plt.plot(n, [y**(i-1)-i for i in n])
plt.show()

#a = 1
#b = 2
#x = []
#y = []
#range_ = range(2,100001)
#for k in range_:
#    f_ = f(k, a, b)
#    if f_ > 0:
#        x += [k]
#        y += [f_]
#        sys.stdout.write("({} {}) ".format(x, y))
#
#plt.plot(x, y, 'r,')
#plt.ylabel("f")
#plt.show()
#
#
