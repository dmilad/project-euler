# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 15:13:46 2014

@author: Milad
"""

def is_pen(p):
    x = ((24*p + 1)**0.5 + 1)/6
    return int(x) == x
    
def is_hex(h):
    x = ((8*h + 1)**0.5 + 1)/4
    return int(x) == x

def tri(t):
    return t*(2*t - 1)

t = 285
while True:
    t += 1
    if is_pen(tri(t)) and is_hex(tri(t)):
        break

print tri(t)
    
    