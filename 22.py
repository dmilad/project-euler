# -*- coding: utf-8 -*-
"""
Created on Thu Jun 05 19:09:53 2014

@author: Milad
"""
names_f = open("names.txt","r")

names = names_f.readline().split(",")

names.sort()

s = 0

for i in range(len(names)):
    t = 0    
    for c in range(1,len(names[i])-1):
        t += ord(names[i].lower()[c])-96
    s += t*(i+1)

print s

