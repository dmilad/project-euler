# -*- coding: utf-8 -*-
"""
Created on Sun Jun 22 12:29:32 2014

@author: Milad
"""

def sols(x,a):
    xf = float(x)
    af = float(a)
    bf = ((xf**2)-2*af*xf)/(2*(xf-af))
    if bf - int(bf) == 0:
        return True, int(bf)
    else:
        return False, 0

maxl = 1
for x in range(12,1001):
    l = []
    for a in range(1,x/2):
        s = sols(x, a)
        if s[0]:
            t = sorted([a, s[1]])
            if t not in l:
                l.append(t)
    if len(l)>maxl:
        maxl = len(l)
        print "%d\t%s" % (x, l)