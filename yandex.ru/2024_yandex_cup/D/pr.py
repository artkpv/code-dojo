"""

"""

import math


def main():
    print(1, flush=True)
    ans = input().strip()
    if ans == 'ok':
        print(f"! 1")
        return
    l = 1
    r = 10**18
    while r - l > 1:
        m = (l + r) // 2
        print(m, flush=True)
        ans = input().strip()
        if ans == "fail":
            r = m - 1
        elif ans == "ok":
            r = m
        elif ans == "wet":
            l = m
    print(f"! {r}")


def main2():
    for h in range(1, 10**18):
        print(h, flush=True)
        ans = input().strip()
        if ans == "fail":
            return
        elif ans == "ok":
            print(f"! {h}", flush=True)
            return
        elif ans == "wet":
            continue
        else:
            raise Exception(f"Invalid")


if __name__ == "__main__":
    main()
