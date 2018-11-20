#!/bin/python3

import sys

def sumOfGroup(k):
    # Return the sum of the elements of the k'th group.
    k_i = k*(k-1)//2
    s_0 = (2*k_i)+1
    s_n = s_0+2*(k-1)
    return (s_0 + s_n)*k/2

if __name__ == "__main__":
    k = int(input().strip())
    answer = sumOfGroup(k)
    print(answer)
