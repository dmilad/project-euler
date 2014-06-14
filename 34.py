# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 10:31:02 2014

@author: Milad
"""

def factorial(x):
    f = 1    
    for i in range(2,x+1):
        f *= i
    return f

l = []
for i in range(3,1000000):
    n = 0    
    for c in str(i):
        n += factorial(int(c))
    if i == n:
        l.append(i)

print l
for i in range(1,len(l)):
    l[0] += l[i]

print l[0]