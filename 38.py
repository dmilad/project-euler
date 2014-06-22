# -*- coding: utf-8 -*-
"""
Created on Sat Jun 21 18:32:50 2014

@author: Milad
"""
def is_pan(s):
    s = sorted(s)
    for i in range(1,10):
        if str(i)!=s[i-1]:
            return False
            break
    else:
        return True

maxp = 0

for t in range(9,6,-1):
    for x in range(9999):
        p = ""
        y = 1
        while len(str(p))<9:
            p += str(x*y)
            y += 1
        if len(p) == 9 and is_pan(p):
            maxp = max(maxp,int(p))

print maxp