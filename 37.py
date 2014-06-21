# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 17:18:51 2014

@author: Milad
"""

def prime(x):
    if x > 1:    
        for i in range(2,int(x**0.5)+1):
            if x%i == 0:
    		return False
    		break
        else:
            return True
    else:
        return False

def trunc(x):
    s = str(x)
    l = [x]
    for i in range(len(s)):
        t1 = int(s[i:])
        t2 = int(s[:len(s)-i])
        if not (prime(t1) and prime(t2)):
            l = []
            break
    return l

i = 11
l = []
while len(l) < 11:
    l += trunc(i)
    i += 2

print (l)
print sum(l)