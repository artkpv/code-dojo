#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    m_d = {}
    for w in magazine:
        m_d[w] = m_d[w] + 1 if w in m_d else 1

    for w in note:
        if w not in m_d or m_d[w] == 0:
            print('No')
            return
        m_d[w] -= 1
    print('Yes')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
