# -*- coding: utf-8 -*-
"""
Created on Sun Jun 29 11:46:09 2014

@author: Milad
"""

from sieve import sieve

def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
            break
    else:
        return True

i = 3
found = False
while not found:
    i += 1
    if not is_prime(i):
        l = sieve(i)
        for j in l:
            if ((i-j)/2)**0.5 == int(((i-j)/2)**0.5):
                break
        else:
            found = True
            
print i
            