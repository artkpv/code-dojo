#!python3

"""
https://www.pramp.com/challenge/8noLWxLP6JUZJ2bA2rnx
decrypt s
encrypt:
 s_i += s[i-1] % 26
 s[0] += 1

0<= s <= unlimited


1)
range = 0..25
s -> s in digits in range
s[0] = 26 - (s[0] - 1) % 26

a % b = r  =>  b*c + r = a
-1 % 26; 26*c + r = -1; 0 -1, -1 25,

s[i] = ord_a + range[(s[i] - s[i-1] - ord_a) % 26]


ii2 = o_a + (i2 + ii1 - o_a) % 26
(ii2 - o_a) + 26*x = i2 + ii1 - o_a
26*x + ii2 - ii1 = i2

o_a + (ii2 - ii1 - o_a)%26 = i2

"""

s = [ord(i) for i in input().strip()]
R = ord('z') - ord('a') + 1

for i in range(len(s)-1, 0, -1):
    s[i] = ord('a') + (s[i] - s[i-1] - ord('a'))%R

s[0] = ord('a') + (s[0] - 1 - ord('a'))%R

print(''.join(chr(i) for i in s))
