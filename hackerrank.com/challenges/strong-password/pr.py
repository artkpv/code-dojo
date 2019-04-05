#!python3
numbers = "0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
n = input('').strip()
s = input('').strip()
n = len(s)
toadd = 0
if not any(set(numbers).intersection(set(s))):
    toadd += 1
if not any(set(lower_case).intersection(set(s))):
    toadd += 1
if not any(set(upper_case).intersection(set(s))):
    toadd += 1
if not any(set(special_characters).intersection(set(s))):
    toadd += 1

print(max(6-n, toadd))
