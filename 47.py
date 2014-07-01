# -*- coding: utf-8 -*-
"""
Created on Mon Jun 30 19:50:15 2014

@author: Milad
"""

def factorlist(x):
    factor = 2
    factorl = []
    while x>1:
        while x%factor == 0:
            factorl.append(factor)
            x /= factor
        factor += 1
    return list(set(factorl))

a1 = 645
while True:
    if len(factorlist(a1)) == 4:
        if len(factorlist(a1+1)) == 4:
            if len(factorlist(a1+2)) == 4:
                print a1
                break
    a1 += 1

