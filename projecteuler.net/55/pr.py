from tqdm import tqdm

def is_lychrel(n):  
    for t in range(50):
        # Calc length:
        l = 0
        m = n
        while m > 0:
            l += 1
            m //= 10
        # Get reversed and check for palindromic:
        nn = 0
        m = n
        i = 0
        while m > 0:
            nn *= 10
            nn += m % 10
            m //= 10
            i += 1
            if t > 0 and i == (l // 2):
                k = m if l%2 == 0 else m // 10
                if k == nn:
                    return False
        n = nn + n
    return True

l_count = 0
for n in tqdm(range(1, 10_000)):
    if is_lychrel(n):
        print(n)
        l_count += 1
print(l_count)

"""
n 121
t 1
l 3
m 121

i 1
m 12
nn 1
k 1
"""
