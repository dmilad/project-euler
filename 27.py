# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 21:11:41 2014

@author: Milad
"""

def is_prime(x):
    if x>2:    
        for i in range(2,int(round(x**0.5))+1):
            if x%i == 0:
                return False
                break
        else:
            return True
    else:
        return False
        
def len_primes(a, b):
    n = 0
    while True:
        p = n**2 + (a*n) + b        
        if is_prime(p):
            n += 1
        else:
            break
    return n

max_ab = [0, 0]
for a in range(-999,1000):
    for b in range(-999,1000):
        l = len_primes(a, b)        
        if l > max_ab[1]:
            max_ab = [a*b, l]

print max_ab