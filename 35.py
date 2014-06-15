# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 12:20:39 2014

@author: Milad
"""
def is_prime(x):
    for i in range(2,int((x**0.5))+1):
        if x%i == 0:
            return False
            break
    else:
        return True


def rotations(x):
    r = [x]    
    l = [e for e in str(x)]    
    for i in range(len(l)-1):
        l.insert(0,l.pop())        
        r.append(int("".join(l)))
    return r
        
l = [2]
for i in range(3,1000001,2):
    if is_prime(i):
        circular = 1
        r = rotations(i)        
        for j in range(1,len(r)):
            if not is_prime(r[j]) or r[j] > r[0]:
                circular = 0                
                break
        if circular == 1:
            for j in r:
                l.append(j)
       
print len(set(l))
