# -*- coding: utf-8 -*-
"""
Created on Sun Jun 08 14:52:52 2014

@author: Milad
"""
"""
Let n < d, and you're trying to figure out the repeating part of n/d. 
Let p be the number of digits in the repeating part: then 
n/d = R * 10^(-p) + R * 10^(-2p) + ... = R * ((10^-p)^1 + (10^-p)^2 + ...) 
The bracketed part is a geometric series, equal to 1/(10^p - 1).

So n / d = R / (10^p - 1). Rearrange to get R = n * (10^p - 1) / d. 
To find R, loop p from 1 to infinity, 
and stop as soon as d evenly divides n * (10^p - 1).

Note, n/d will only have a finite decimal representation 
if all the prime factors of d that aren't 2 or 5 are also present in n.
"""

def rep_len(d):
    while d%2 == 0:
        d /= 2
    while d%5 == 0:
        d /= 5

    if d == 1:
        return 0
    else:
        p = 0
        while True:
            p += 1
            if (10**p - 1)%d == 0:
                break
        return p    


max_len = 0
max_i = 1
for i in range(1,1000):
    m = rep_len(i)
    if m > max_len:
        max_len = m
        max_i = i

print max_i, max_len
