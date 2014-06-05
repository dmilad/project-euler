def factorial(x):
    f = 1
    for i in range(1,x+1):
        f *= i
    return f

s = factorial(100)

total = 0
for c in str(s):
    total += int(c)
    
print total