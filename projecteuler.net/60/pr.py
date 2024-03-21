from tqdm import tqdm

def is_prime(p):
    for m in range(2, int(p**.5) + 1):
        if p % m == 0:
            return False
    return True

def test_set(s, p):
    for el in s:
        for a, b in ((el, p), (p, el)):
            new_p = int(str(a) + str(b))
            if not is_prime(new_p):
                return False
    return True

def main():
    inf_p = [3,7,109,673]

    p = 11 

    bar = tqdm()
    while True:
        if is_prime(p) and test_set(inf_p, p):
            print('Found', p)
            return p
        p += 2
        bar.desc = f'{p} '
        bar.update()

main()


