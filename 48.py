# -*- coding: utf-8 -*-
"""
Created on Tue Jul 01 17:11:07 2014

@author: Milad
"""

s = 0
for i in range(1,1001):
    s += i**i
    
print str(s)[len(str(s))-10:]