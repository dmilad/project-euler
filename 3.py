
x = 600851475143

factor = 2
bigfactor = 1
while x>1:
    if x%factor == 0:
        bigfactor = factor
        x /= factor
    while x%factor == 0:
        x /= factor
    factor += 1
        
print bigfactor