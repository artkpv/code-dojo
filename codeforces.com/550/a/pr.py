#!python3
s = input().strip()
n = len(s)

def has():
    for i in range(n-1):
        if s[i:i+2] == 'AB':
            for j in range(i+2, n-1):
                if s[j:j+2] == 'BA':
                    return True
            break
        
    for i in range(n-1):
        if s[i:i+2] == 'BA':
            for j in range(i+2, n-1):
                if s[j:j+2] == 'AB':
                    return True
            break
    return False


print('YES' if has() else 'NO')



