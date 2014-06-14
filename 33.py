# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 21:21:53 2014

@author: Milad
"""
f = 1.0
l = 1.0
for n in range(11,100):
    for d in range(n+1,100):
        f = float(n)/float(d)
        for c in str(n):
            if c in str(d) and c!="0":
                nn = [i for i in str(n)]
                nn.remove(c)
                dd = [i for i in str(d)]
                dd.remove(c)
                if int(dd[0])!=0:
                    if f == float(nn[0])/float(dd[0]):
                        l *= (float(nn[0])/float(dd[0]))
                        
print l