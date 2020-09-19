#!/bin/python3

from random import Random

r = Random()
alpha = 'abcdefghijklmnopqrstuvwxyz'
for i in range(100000):
    print(r.choice(alpha), end='')


