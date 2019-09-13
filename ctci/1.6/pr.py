#!python3

"""
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""

def compress(s):
    if not s:
        return s
    cs = [s[0]]
    i = 0
    j = 1
    while j < len(s):
        if cs[-1] != s[j]:
            cs += [str(j-i)]
            cs += [s[j]]
            i = j
        j += 1
    if j > 1:
        cs += [str(j-i)]
    if len(cs) >= len(s):
        return s
    else:
        return ''.join(cs)


s = input().strip()
print(compress(s))

