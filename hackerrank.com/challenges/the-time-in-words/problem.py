#!python3

h = int(input().strip())
m = int(input().strip())
num2words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'quarter', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', \
            20:'twenty'}

if m == 0:
    print(num2words[h], "o' clock")
else:
    if m == 30:
        print('half past', num2words[h])
    else:
        m2 = m if m < 30 else 60 - m
        minutes = num2words[m2] if m2 <= 20 else num2words[20] + " " + num2words[m-20]
        if m2 != 15:
            minutes += ' minute' if m2 == 1 else ' minutes'
        print(minutes, 'past ' + num2words[h] if m <= 30 else 'to ' + num2words[(h+1)%12])







