
def spd(x):
    #sum of proper divisors
    total = 0
    for i in range(1,x):
        if x%i == 0:
            total += i
    return total

t = 0
for a in range(10000):
    b = spd(a)
    c = spd(b)
    if c == a and a != b:
        t += b+c

print t/2