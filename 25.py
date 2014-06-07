# -*- coding: utf-8 -*-
"""
Created on Sat Jun 07 08:59:42 2014

@author: Milad
"""
n = 10**999

i = j = 1
k = 2
count = 3

while True:
    i = j
    j = k
    k = i+j
    count += 1
    if k >= n:
        break

print count
        