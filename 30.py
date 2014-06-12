# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 21:50:14 2014

@author: Milad
"""

def fifth_powers(x):
    t = 0
    for c in str(x):
        t += int(c)**5
    return t

limit = 6 * (9**5)

t = 0
for i in range(2,limit+1):
    if fifth_powers(i) == i:
        t += i

print t        