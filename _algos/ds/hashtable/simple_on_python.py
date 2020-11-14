#!python3

size = 100
count = 0
ht = [None] * size

def ht_insert(x):
    global count
    hc = x % size
    i = 0
    while ht[(hc + i)%size] != None:
        i = inc_(i)
    ht[(hc+i)%size] = x
    count += 1

def ht_delete(x):
    global count
    hc = x % size
    i = 0 
    while True:
        ii = (hc + i)%size
        if ht[ii] == x:
            ht[ii] = None
            count -= 1
            break
        elif ht[ii] == None:
            return
        i = inc_(i)
    i = inc_(i)
    while ht[(hc + i)%size] != None:
        y = ht[(hc + i)%size]
        ht[(hc + i)%size] = None
        count -= 1
        ht_insert(y)
        i = inc_(i)

def has(x):
    hc = x % size
    i = 0
    while True:
        xx = ht[(hc + i)%size]
        if xx == x:
            return True
        elif xx == None:
            return False
        i = inc_(i)
    return False
    
def inc_(i):
    return i + 1

ht_insert(1)
assert(has(1))
print('has(1)')
ht_insert(101)
assert(has(101))
print('has(101)')
ht_insert(201)
assert(has(201))
print('has(201)')
ht_insert(2)
assert(has(2))
print('has(2)')
ht_insert(102)
assert(has(102))
print('has(102)')
ht_insert(202)
assert(has(202))
print('has(202)')
ht_delete(201)
assert(not has(201))
print('not has(201)')
ht_delete(101)
assert(not has(101))
print('not has(101)')
ht_delete(1)
assert(not has(1))
print('not has(1)')

