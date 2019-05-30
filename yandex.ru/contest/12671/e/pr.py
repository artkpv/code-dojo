#!python3

def todigit16(c):
    if ord('0') <= ord(c) <= ord('9'):
        return ord(c) - ord('0')
    if ord('a') <= ord(c.lower()) <= ord('f'):
        return 10 + ord(c.lower()) - ord('a')
    return None
     
a = [c for c in input().strip()]
b = [None] * len(a)
a_n = len(a)
b_n = len(b)

count = 0
while True:
    changes = 0
    # decode a into b
    a_i = 0
    b_i = 0
    while a_i < a_n:
        if (a_i + 3 < a_n and a[a_i] == '&' and a[a_i+3] == ';'):
            first = todigit16(a[a_i+1])
            second = todigit16(a[a_i+2])
            if first is not None and second is not None:
                ascii = 16*first + second
                # 32 <= ascii <= 126 or 128 <= ascii <= 255:
                if chr(ascii).isprintable():
                    b[b_i] = chr(ascii)
                    b_i += 1
                    b_n -= 3
                else:
                    b_n -= 4
                a_i += 4
                changes += 1
                continue
        b[b_i] = a[a_i]
        a_i += 1
        b_i += 1
    a = b
    a_n = b_n
    if changes > 0:
        count += 1
    else:
        break

print(count)

