# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 21:47:03 2014

@author: Milad
"""

t = 1
d = 1
for l in range(3,1002,2):
    for c in range(4):
        d += (l-1)
        t += d

print t