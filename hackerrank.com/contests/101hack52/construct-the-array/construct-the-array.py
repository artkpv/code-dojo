#!python3

"""

< n k x
  3 2 2  >  0   1 ? 2


< 4 3 2
  1 2 1 2


< 5 4 2

  1 2 1 3 2
  1 2 3 1 2
  1 2 3 4 2
  1 2 4 1 2
  1 2 4 3 2



2nd:   k-1
3rd:   k-1
...
n-2th:   k-1
n-1th?
 a . x
 if a == x -> (k-1)
 else       > (k-2)



"""

import sys
sys.setrecursionlimit(20000)

MOD = 10**9+7

D = {}

def combinations(a, i, k):
    global MOD, D
    if (a[i-1],i) not in D:
        count = 0
        islast = i == len(a) - 2
        for j in range(1, k+1):
            if a[i-1] == j:
                continue
            if islast:
                if a[i+1] == j:
                    continue
                count += 1
            else:
                a[i] = j
                count += combinations(a, i+1, k)
                count = count % MOD
        D[(a[i-1],i)] = count
    return D[(a[i-1],i)]

def countArray(n, k, x):
    global MOD
    # Return the number of ways to fill in the array.
    count = 0

    # if n <= 10**3 and k <= 10**2:
    a = [1] + ([None] * (n-2)) + [x]
    count = combinations(a, 1, k)
    return count % MOD


def countArrayIter(n, k, x):
    """
    Counts all variants begining with the least ones.
    Example 5 4 3:
        1 2 1 2 3
        1 2 1 4 3
        1 2 3 1 3
        1 2 3 2 3
        1 2 3 4 3
        1 2 4 1 3
        1 2 4 2 3 | vars for 3rd position. 1:2, 3:3, 4:2
        1 3 1 2 3
        1 3 1 4 3
        1 3 2 1 3
        1 3 2 4 3 | from 3rd pos.: 1:2, 2:2, 3:3, 4:2 ;
        ...

        Кол-во вариантов на 2-й поз. * на кол-во вар. на 3-й ...
    """
    global MOD
    # Return the number of ways to fill in the array.
    count = 0
    prev_count = 0
    D = {}
    a = [1] + [1] * (n-2) + [x]
    i = 1  # 0 based
    # iterate over variants from the least to the most
    # TODO:
    #  этот код это обход дерева. Postorder. Сначала берет листья. Нужно перед обходом листа проверять были ли мы в таком дереве (i, a[i]) и брать сохраненный обход. Сохранять обход после того как все листья обошли. Но не понятно где эта точка здесь. Посмотри итеративный алгоритм обхода деревьев.
    while True:
        # increase a[i]:
        if a[i] >= k:
            a[i] = 1
        while a[i-1] == a[i] or (i == n - 2 and a[i] == a[i+1])
            a[i] += 1

        print(' '.join(str(i) if i != None else '-' for i in a) + " : " + str(count))
        print(D)

        if a[i] <= k:
            if i + 2 < n: # go to i+1
                if (i, a[i]) in D:  # already counted this tree
                    count += D[(i, a[i])]
                else:
                    i += 1
            else:  # can't i+1 so stay at i
                count = (count+1) % MOD
        else: # tree at i is counted
            if i > 1:  # can go back
                # go back:
                a[i] = 1
                i -= 1
            else:  # can not go back and no variants
                break  # END

    return count % MOD

if __name__ == "__main__":
    n, k, x = input().strip().split(' ')
    n, k, x = [int(n), int(k), int(x)]
    answer = countArrayIter(n, k, x)
    #expected= countArray(n, k, x)
    #assert answer == expected, "Res:{} Exp:{}".format(answer, expected)
    print(answer)
