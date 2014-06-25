# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 15:25:31 2014

@author: Milad
"""

import re

def is_triangle(x):
    t = (((1 + 8 * x)**0.5) - 1) / 2 
    if int(t) - t == 0:
        return True
    else:
        return False

def word_num(word):
    n = 0
    for c in word:
        n += ord(c) - 64
    return n

wfile = open("words.txt", "r")
wstring = wfile.read()

t = 0
words = re.findall(r"\"([A-Z]*?)\"", wstring)
for word in words:
    if is_triangle(word_num(word)):
        t += 1

print t