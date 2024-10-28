import math


def num_hills(arr):
    ans = 0
    n = len(arr)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and arr[j] < arr[j + 1]:
            j += 1
        if j == i:
            i += 1
        else:
            # potential hill
            k = j
            while k + 1 < n and arr[k] > arr[k + 1]:
                k += 1
            if j < k:
                # hill
                ans += (j - i) * (k - j)
            i = k
    return ans


def solve():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = [int(i) for i in input().strip().split(" ")]
        ans = num_hills(arr)
        if ans is not None:
            print(ans)


if __name__ == "__main__":
    solve()
