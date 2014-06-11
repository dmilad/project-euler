# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 18:12:52 2014

@author: Milad
"""

l = []

for a in range(2,101):
    for b in range(2,101):
        l.append(a**b)

print len(set(l))