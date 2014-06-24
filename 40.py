# -*- coding: utf-8 -*-
"""
Created on Mon Jun 23 17:12:11 2014

@author: Milad
"""

l=[]
for i in range(190000):
    for c in str(i):
        l.append(c)

p = 1
for i in range(7):
    p *= int(l[10**i])

print p