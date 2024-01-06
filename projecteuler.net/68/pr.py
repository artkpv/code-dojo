"""

I1 BF
O(n! * 10)

I2 
Recurssion, tree traverse. 

visit(gon, left):
if
for each left

gon - five equations, each sharing variables. Arrays of array

"""

def gon_iter(gon):
    for i in range(4):
        yield gon[i:i+1] + gon[i+5:i+7]
    yield gon[4:5] + gon[9:10] + gon[5:6]

def visit(pos, gon, left):
    if pos == len(gon):
        gon_arr = list(gon_iter(gon))
        start_i = gon_arr.index(min(gon_arr))
        gon_s = ''.join(str(e) for arr in gon_arr[start_i:] + gon_arr[:start_i] for e in arr)
        return gon_s
    max_gon_s = None
    for l in left.copy():
        gon[pos] = l
        is_good = True
        gon_sum = None
        for g_eq in gon_iter(gon):
            if not is_good:
                break
            if None in g_eq:
                continue
            eq_sum = sum(g_eq)
            if gon_sum == None:
                gon_sum = eq_sum
            if eq_sum != gon_sum:
                is_good = False
        if is_good:
            left.remove(l)
            sub_max_gon_s = visit(pos+1, gon, left)
            if sub_max_gon_s and (not max_gon_s or sub_max_gon_s > max_gon_s):
                max_gon_s = sub_max_gon_s
            left.add(l)
        gon[pos] = None
    return max_gon_s

res = visit(0, [None] * 10, set(range(1, 11)))
print(res)



    




