''' 
Implement a function that outputs the Look and Say sequence:
1
11
21
1211
111221
312211
13112221
1113213211
31131211131221
13211311123113112211

Time:
How does the output length scale?
O(2**n)
max length of new string is 2*n: each char gives 2 new.

What is the max single digit that can exist in the output?
3?

What is the only starting sequence that never grows in length?
22
22


'''

def look_and_say(count):
    if count <= 0:
        raise Exception('invalid count')
    a = '1'
    for _ in range(1, count):
        k = 1
        i = 1
        b = []
        while i < len(a):
            if a[i] == a[i-1]:
                k += 1
            else:
                b += [k, a[i-1]]
                k = 1
            i += 1
        b += [k, a[i-1]]
        a = ''.join(str(e) for e in b)
    return a


'''
E1 
4 > 1211

a 
21
  i
k 1
b
1 2 1 1
'''


assert look_and_say(1) == '1'
assert look_and_say(2) == '11'
assert look_and_say(3) == '21'
assert look_and_say(4) == '1211', look_and_say(4)
assert look_and_say(10) == '13211311123113112211', look_and_say(10) 


print('pass')





