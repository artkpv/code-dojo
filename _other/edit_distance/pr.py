'''
 Write a function that returns whether two words are exactly "one edit" away using the following signature:
bool OneEditApart(string s1, string s2);
An edit is:

    Inserting one character anywhere in the word (including at the beginning and end)
    Removing one character
    Replacing one character

Examples:
OneEditApart("cat", "dog") = false
OneEditApart("cat", "cats") = true
OneEditApart("cat", "cut") = true
OneEditApart("cat", "cast") = true
OneEditApart("cat", "at") = true
OneEditApart("cat", "act") = false

cat
dog
i 

cat
og

at
dog

I 1. DP

C(i,j) = min {
    C(i+1, j+1) if s1[i] == s2[j]
    C(i, j+1) + 1 delete s2[j]
    C(i+1, j) + 1 delete s1[i]
    // C(i+1, j) + 1 insert at j
    // C(i, j+1) + 1 insert at i
    
'''

def oneeditapart(s1, s2):
    if not s1 and not s2:
        return True
    n = len(s1)
    m = len(s2)
    def dist(i, j, k):
        if k > 1:
            return False
        assert not (i > n or j > m)
        if i == n or j == m:
            return k + n - i + m - j <= 1
        if s1[i] == s2[j] and dist(i+1, j+1, k):
            return True
        if dist(i+1, j+1, k+1):  # replace
            return True
        if dist(i+1, j, k+1):  # delete in s1 or insert in s2
            return True
        if dist(i, j+1, k+1):  # delete in s2 or insert in s1
            return True
        return False
    return dist(0, 0, 0)

'''
cat
dog

dist 0 0 0 
 dist 1 0 1
  dist 2 0 2 > F
  dist 1 1 2 > F
  > F
 dist 0 1 1
  dist 1 1 2 > F 
  dist 0 2 2 > F
  > F
 > F

cat
cats

dist 0 0 0
 dist 1 1 0
  dist 2 2 0
   dist 3 3 0 > 0 + 0 + 1 = 1 > T
  > T
 > T
> T


0123
cat    3    
   i
cast   4    
    j

dist 0 0 0 
 dist 1 1 0
  dist 2 2 0
   dist 3 2 1 > 1 + 0 + 4 - 2 > F
   dist 2 3 1 
    dist 3 4 1 > 1 + 0 + 0 > T
   > T
> T


'''

assert oneeditapart("cat", "dog") == False
assert oneeditapart("cat", "cats") == True
assert oneeditapart("cat", "cut") == True
assert oneeditapart("cat", "cast") == True
assert oneeditapart("cat", "at") == True
assert oneeditapart("cat", "act") == False

print('pass')
