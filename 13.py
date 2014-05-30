file_13 = open("13.txt","r")

x = 0
for i in range(100):
    x += int(file_13.readline())

print x / 10**(len(str(x))-10)
