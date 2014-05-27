file11 = open("11.txt","r")
x = []
for i in range(20):
    x.append(file11.readline().split(" "))
    for j in range(20):
        x[i][j] = int(x[i][j])

file11.close()

maxim = 0
#horizontal
for i in range(20):
    for j in range(17):
        maxim = max(maxim,x[i][j]*x[i][j+1]*x[i][j+2]*x[i][j+3])

#vertical
for i in range(17):
    for j in range(20):
        maxim = max(maxim,x[i][j]*x[i+1][j]*x[i+2][j]*x[i+3][j])

#descending diagonally
for i in range(17):
    for j in range(17):
        maxim = max(maxim,x[i][j]*x[i+1][j+1]*x[i+2][j+2]*x[i+3][j+3])

#ascending diagonally
for i in range(17):
    for j in range(3,20):
        maxim = max(maxim,x[i][j]*x[i+1][j-1]*x[i+2][j-2]*x[i+3][j-3])

print maxim

