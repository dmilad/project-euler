ones = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
ten_19 = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
tens = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
hundred = 7
a_nd = 3

t = 0

def count_letters(i):
    total = 0
    if len(str(i)) == 3:
        e = int(round(i/100))
        total += ones[int(e)]
        total += hundred
        i = i%100
        if i is not 0:
            total += a_nd
    if len(str(i)) == 2:
        e = round(i/10)
        total += tens[int(e)]
        if e == 1:
            total += ten_19[i-10]
        else:
            i = i%10
    if len(str(i)) == 1:
        total += ones[i]
    return total  

for i in range(1,1000):
    t += count_letters(i)

# add one thousand
t += 11

print t