#!python3
"""
NEXT:
    fix this
    3 moves and 092282
    Need to substitude to max at first place
    and not waste moves on subst on less



0 < s <= 10^5
0 <= k <= 10^5
largest polindromic num ? or -1


Idea 1

u - unmatching = num of left != right pairs

1) k < u => -1
2) we can
    moves left = k
    if k - 2 >= u - 1:
        make both 9
    else:
        make one
3) if moves left:
    change to 9th from left

Time: ~(n + n + n)
Space: ~(n)


Ex1
1 3943 > 3993

Ex2
3 092282 > 992299

Ex3
1 0011 > -1

"""

def makeequal(array, moves, unmatch, changed, i):
    left = array[i]
    right = array[-i-1]

    if left != right
        if moves == 0:
            return False
        if right == '9':
            array[i] = '9'
            moves -= 1
            changed.add(i)
        else: 

    pass

def getpolyndrom(array, moves):
    unmatch = sum(1 if e != array[-i-1] else 0
                  for i, e in enumerate(array[:len(array)//2]))

    changed = set()

    for i, e in enumerate(array[:len(array)//2]):
        makeequal(array, moves, unmatch, changed, 0)

    # middle:
    if i == len(array)//2 and len(array) % 2 == 0:
        if array[i] != '9' and moves > 0:
            array[i] = '9'
            changed.add(i)
        return True



    # make polyndrom:
    for i, e in enumerate(array[:len(array)//2]):
        assert unmatch <= moves
        candoboth = unmatch - 1 < moves - 2
        if e != '9' and array[-i-1] != '9' and candoboth:
            # substitude both
            array[i] = '9'
            array[-i-1] = '9'
            moves -= 2
        else:  # substitude one
            x = array[i] if array[i] > array[-i-1] else array[-i-1]
            array[i] = x
            array[-i-1] = x
            moves -= 1
        unmatch -= 1
        print(array)

    assert unmatch == 0

    if moves == 0:
        return array

    # greater via left part
    for i, e in enumerate(array[:len(array)//2]):
        if moves == 0:
            break
        if e != '9':
            tosubstitude = 2 if array[-i-1] != '9' else 1
            if moves - tosubstitude < 0:
                continue
            moves -= tosubstitude
            array[i] = '9'
            array[-i-1] = '9'

    # greater via right part
    for i in range(len(array)//2-1, -1, -1):
        if moves == 0:
            break
        e = array[i]
        if array[-i-1] != '9':
            tosubstitude = 2 if e != '9' else 1
            if moves - tosubstitude < 0:
                continue
            moves -= tosubstitude
            array[i] = '9'
            array[-i-1] = '9'

    # middle
    if len(array) % 2 == 1 and moves > 0:
        array[len(array)//2] = '9'

    return array


n, k = [int(i) for i in input('').strip().split(' ')]
s = [c for c in input('').strip()]
poly = getpolyndrom(s, k)
print(''.join(poly) if poly else '-1')
