# -*- coding: utf-8 -*-
"""
Created on Wed Jul 02 11:22:19 2014

@author: Milad
"""

import sieve

m = sieve.sieve(9999)
n = sieve.sieve(1000)

l = [x for x in m if x not in n]

d = {}
for i in l:
    d[i] = "".join(sorted([x for x in str(i)]))

p={}
for k,v in d.iteritems():
    for l,w in d.iteritems():
        if v==w and k!=l:
            if v in p.keys():
                p[v].append(l)
                p[v] = list(set(p[v]))
            else:
                p[v] = [k,l]

for k, v in p.iteritems():
    v = sorted(v)
    for i in range(len(v)-2):
        for j in range(i+1,len(v)-1):
            diff = v[j] - v[i]
            third = v[j] + diff
            if third in v:
                print v[i], v[j], third, str(v[i])+str(v[j])+str(third)
