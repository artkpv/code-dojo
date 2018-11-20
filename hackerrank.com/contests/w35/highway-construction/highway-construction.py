#!python3

"""

n n-1 n-2 n-3 .. 3 2 1

n-n+2
n-n+3
..
n-3
n-2
n-1

"""
import sys, math

mod_sum_saved = {}
def get_mod_sum(k, mod):
    global mod_sum
    if k not in mod_sum_saved:
        mod_sum = 0
        for i in range(0, mod):
            mod_sum = (mod_sum + pow(i, k, mod)) % mod
        mod_sum_saved[k] = mod_sum
    return mod_sum_saved[k]

def highwayConstruction(n, k):
    mod = 1000000009
    q, r = divmod(n-2, mod)
    mod_sum = None
    if q > 0:
        mod_sum = get_mod_sum(k, mod)

    sum_ = 0
    for i in range(2, n):
        # add mod sums :
        if i % mod == 0:
            mod_sums_to_add = (n-i)//mod
            sum_ += mod_sum * mod_sums_to_add
            i += mod * mod_sums_to_add
        else:
            sum_ += pow(i, k, mod)
    return sum_


#if sys.argv[1] == 'test':
#    for i in range(200):
#        r = highwayConstruction(10**3, 10)
#        sys.stdout.write('\rhighwayConstruction(10**3, 10): ' + str(i))
#    sys.stdout.write('\n')
#
#    # largest  TODO: optimize
#    for i in range(1):
#        r = highwayConstruction(10**18, 1000)
#        sys.stdout.write('\rhighwayConstruction(10**18, 1000): ' + str(i))

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, k = input().strip().split(' ')
        n, k = [int(n), int(k)]
        result = highwayConstruction(n, k)
        print('{:.0f}'.format(result))


