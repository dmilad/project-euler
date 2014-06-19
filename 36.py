# -*- coding: utf-8 -*-
"""
Created on Thu Jun 19 14:40:05 2014

@author: Milad
"""

def palin(x):
    rev = ""
    for c in x:
        rev = c + rev
    if rev == x:
        return True
    else:
        return False
    
s = 0
for i in range(1000000):
    if palin(str(i)) and palin(bin(i)[2:]):
        s += i

print s