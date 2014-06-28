# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 20:31:18 2014

@author: Milad
"""

def is_pen(p):
    x = ((24*p + 1)**0.5 + 1)/6
    return int(x) == x

def pen(x):
    return x*(3*x-1)/2

i = 1
l = []
while l == []:
    pi = pen(i)
    for j in range(i-1,0,-1):
        pj = pen(j)
        if is_pen(pi+pj) and is_pen(pi-pj):
            l.append([i,j,pi-pj])
            break
    i += 1
   
print l