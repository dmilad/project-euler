s = 0
fib1 = 1
fib2 = 1
fib3 = 0
while fib3 < 4000000:
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3
    if fib3%2 == 0:
        s += fib3

print s