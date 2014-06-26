# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 16:21:43 2014

@author: Milad
"""

from sieve import sieve
import itertools

l = sieve(17)
n = [list(a) for a in itertools.permutations([0,1,2,3,4,5,6,7,8,9])]

pan = []
for i in n:
    p = 0
    for j in i:
        p = p * 10 + j
    if len(str(p)) == 10:
        pan.append(str(p))

s = 0
for p in pan:
    for i in range(1,8):
        if int(p[i:i+3]) % l[i-1] != 0:
            break
    else:
        s+= int(p)

print s