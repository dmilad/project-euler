# -*- coding: utf-8 -*-
"""
Created on Thu Jul 03 09:31:09 2014

@author: Milad
"""

import sieve

n = 1000000
l = sieve.sieve(n)

suml=[2]

for i in range(1,len(l)):
    suml.append(suml[i-1]+l[i])     

count = 0
m = 0
for i in range(len(l)):
    for j in range(i-count+1,-1,-1):
        if suml[i] - suml[j] > n:
            break
        if suml[i] - suml[j] in l:
            count = i - j
            m = suml[i] - suml[j]

print count, m



"""
n = 1000
l = sieve.sieve(n)

m = [0, 0, len(sieve.sieve(n/2-1))]

for i in range(len(l)-1,-1,-1):
    t = l[i]
    tl = len(sieve.sieve(t/2-1))
    for j in range(m[2]):
        s = sum(l[j:j+m[1]])
        count = m[1]
        if s < t:
            for h in range(j+m[1],tl):
                s += l[h]
                count += 1
                if s > t:
                    break
                elif s == t and count > m[1]:
                    m = [t, count, j]
                    print m
                    break

print m
    """    