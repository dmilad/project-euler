def is_prime(x):
    lim = int(round(x**0.5))+1
    for i in range(2,lim):
        if x%i == 0:
            return False
            break
    return True

count = 1
n = 3

while count<10001:
    if is_prime(n):
        count += 1
    n += 1

print n-1