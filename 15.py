def factorial(x):
    t = 1
    for i in range(1,x+1):
        t *= i
    return t

print factorial(40)/(factorial(20)**2)