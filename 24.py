# -*- coding: utf-8 -*-
"""
Created on Fri Jun 06 18:52:08 2014

@author: Milad
"""

e = 10
p = 999999

def factorial(x):
    f = 1    
    for i in range(x):
        f *= i+1
    return f

l = [x for x in range(e)]
o = []

n = factorial(e)
for i in range(e,0,-1):
    n /= i
    o.append(p/n)
    p %= n
    
s = ""
for i in range(e):
    s += str(l.pop(o[i]))

print s