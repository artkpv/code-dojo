#!python3

s = input().strip().lower()
r = []
vowels = 'aeiouy'
for i in range(len(s)):
    is_vowel = s[i] in vowels
    if not is_vowel:
        r += '.' + s[i]
print(''.join(r))

