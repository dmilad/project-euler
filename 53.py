
def factorial(x):
    for i in range(1,x):
        x *= i
    return x

fdict = {}
for i in range(1,101):
    fdict[i] = factorial(i)

def com(n,r):
    return fdict[n] / (fdict[r] * fdict[n-r])

#facotrial(0)?
count = 0
for i in range(10,101):
    for j in range(1,i):
        if com(i,j) > 1000000:
            count += 1

print count
