#!/bin/python3


def maximumPeople(p, x, y, r):
    # Return the maximum number of people that will be in a sunny town after removing exactly one cloud.
    towns = sorted((x[i], p[i]) for i in range(len(p)), key=lambda x: x[0])
    clounds = sorted((y[i], r[i], []) for i in range(len(y)), key=lambda x: x[0])

    now_clouds = []
    for i in range(1, 10**9 + 1):




if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    x = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    y = list(map(int, input().strip().split(' ')))
    r = list(map(int, input().strip().split(' ')))
    result = maximumPeople(p, x, y, r)
    print(result)
