# -*- coding: utf-8 -*-
"""
Eratosthenes Sieve for finding primes <= n

Created on Tue Jun 24 17:12:02 2014

@author: Milad
"""

def sieve(n):
    a = [False, False] + [True for x in range(2,n+1)]

    for i in range(2,int(n**0.5)+1):
        if a[i] == True:
            for j in range(i**2,n+1,i):
                a[j] = False

    b = []
    for i in range(len(a)):
        if a[i] == True:
            b.append(i)
    return b
    
