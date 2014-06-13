# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 15:47:01 2014

@author: Milad
"""

import itertools

def l_to_n(l):
    n = 0
    length = len(l)
    for i in range(length):
        n += l[i]*10**(length-i-1)
    return n

l = [list(a) for a in itertools.permutations([1,2,3,4,5,6,7,8,9])]

pand = []
for perm in l:
    for m in range(4):
        for e in range(m+1,5):
            if l_to_n(perm[0:(m+1)]) * l_to_n(perm[(m+1):(e+1)]) == l_to_n(perm[(e+1):9]):
                pand.append(l_to_n(perm[(e+1):9]))

t = 0
for i in set(pand):
    t += i

print t