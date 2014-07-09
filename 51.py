# -*- coding: utf-8 -*-
"""
Created on Sun Jul 06 13:54:00 2014

@author: Milad
"""

from sieve import sieve

def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i == 0:
            return False
            break
    else:
        return True
            
def eight_fam(prime, rd):
    c = 0
    for digit in '0123456789':
        n = int(prime.replace(rd, digit))
        if (n>100000 and is_prime(n)):
            c += 1
    return c == 8

l = [str(x) for x in sieve(1000000)]

for s in l:
    if (int(s)>100000):
        last_digit = s[5:]
        if (s.count('0') == 3 and eight_fam(s,'0') \
         or s.count('1') == 3 and last_digit != '1' and eight_fam(s,'1') \
         or s.count('2') == 3 and eight_fam(s,'2')):
             print s
             break