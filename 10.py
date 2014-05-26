def is_prime(x):
    for i in range(2,int(round(x**0.5)+1)):
        if x%i == 0:
            return False
            break
    else: return True
    
total = 0
for i in range(2,2000000):
    total += is_prime(i)*i

print total
