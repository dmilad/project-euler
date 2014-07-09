# -*- coding: utf-8 -*-
"""
Created on Tue Jul 08 17:21:27 2014

@author: Milad
"""

def sort(x):
    s = str(x)
    l = [c for c in s]
    return sorted(l)

x = 100
found = False

while not found:
    x += 1
    if len(str(x)) == len(str(6*x)):
        found = True
        for i in range(2,7):    
            if sort(x) != sort(i*x):
                found = False
                break

print x
