"""

is bounty:
 From left to right from the second and check if prev digit does not exceed the current
    For all? Return False
 From right to left
    For all? return False
 return True

"""
from tqdm import tqdm

def is_bouncy(n):
    is_desc = True
    is_asc = True
    m = n // 10
    k = n % 10
    while (is_desc or is_asc) and m > 0:
        is_asc = is_asc and m % 10 <= k
        is_desc = is_desc and m % 10 >= k
        k = m % 10
        m = m // 10
    return not is_desc and not is_asc

bouncy_count = 0
n = 100
bar = tqdm()
while bouncy_count * 100 != 99 * n:
    n += 1
    if is_bouncy(n):
        bouncy_count += 1
    if n == 1000 or n == 538 or n == 21780:
        print(f"\n{n}, bouncy {bouncy_count} ({bouncy_count * 100 //n}%)")
    bar.desc = f"{n}, bouncy {bouncy_count} ({bouncy_count * 100 //n}%)"
    bar.update()

print(f"\n {n}, bouncy {bouncy_count} ({bouncy_count * 100 //n}%)\n")


