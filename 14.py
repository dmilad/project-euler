m = 0
mi = 999999

def collatz(x, count=0):
    count += 1
    if x == 1:
        return count
    elif x%2 == 0:
        return collatz(x/2,count)
    else:
        return collatz(3*x + 1,count)

for i in range(999999,1,-1):
    s = collatz(i)
    if s > m:
        m = s
        mi = i

print mi, m
