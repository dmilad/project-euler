# -*- coding: utf-8 -*-
"""
Created on Tue Jun 24 16:51:25 2014

@author: Milad
"""

import itertools

def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
            break
    else:
        return True

l = [list(x) for x in itertools.permutations([7,6,5,4,3,2,1])]
n = []
for item in l:
    p = 0
    for i in item:
        p = p * 10 + i
    n.append(p)

for i in n:
    if is_prime(i):
        print i
        break