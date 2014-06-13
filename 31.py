# -*- coding: utf-8 -*-
"""
Created on Thu Jun 12 21:39:19 2014

@author: Milad
"""

p = 200
i = 0

for a in range(p,-1,-200):
    for b in range(a,-1,-100):
        for c in range(b,-1,-50):
            for d in range(c,-1,-20):
                for e in range(d,-1,-10):
                    for f in range(e,-1,-5):
                        for g in range(f,-1,-2):
                            i += 1

print i