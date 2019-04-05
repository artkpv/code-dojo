#!python
s = input('').strip()
indecies = list(range(len(s)))
while True:
    for i,e in enumerate(indecies):
        if i > 0 and s[indecies[i-1]] == s[e]:
            del indecies[i]
            del indecies[i-1]
            break
    else:
        break
print(''.join(s[i] for i in indecies) if indecies else 'Empty String')

