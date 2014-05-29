#number of divisors of x is the product of every (exponent+1) of the prime factors of x

def prime_fac(n):
    i = 2
    d = 1
    while i**2 < n:
        l = 0
        while n%i == 0:
            n /= i
            l += 1
        d *= (l+1)
        i += 1
    if n > 1:
        d *= 2
    return d

n = 2
while True:
    p = (n*(n+1))/2
    if prime_fac(p) > 500:
        print p
        break
    n += 1
              