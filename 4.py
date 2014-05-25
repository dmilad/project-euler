def is_palin(x):
    if str(x)[::-1]==str(x):
        return True
    else:
        return False

max_pal = 1

for i in range(999,100,-1):
    for j in range(999,100,-1):
        if is_palin(i*j):
            max_pal = max(max_pal, i*j)
            
print max_pal