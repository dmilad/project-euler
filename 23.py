# -*- coding: utf-8 -*-
"""
Created on Thu Jun 05 21:44:26 2014

@author: Milad
"""

def sum_prop(x):
    # sum of proper divisors
    t = 0
    l = 1
    h = x
    while l < h:
        if x%l == 0:
            h = x/l
            if l<h:
                t += l+h
            elif l==h:
                t += l
            else:
                break
        l += 1
    return t-x

# find abundant numbers
l1 = []
for i in range(1,28124):
    if sum_prop(i)>i:
        l1.append(i)
    
# find all sums of abundent numbers
l2 = []
for i in range(len(l1)):
    for j in range(i,len(l1)):
        l2.append(l1[i]+l1[j])

# remove duplicates using set
l2 = list(set(l2))

n = 0
# find sum of non-abundant numbers
for i in range(1,28124):
    if i not in l2:
        n += i

print n