file_18 = open("triangle.txt","r")

l = []
for i in range(100):
    l.append(file_18.readline().split(" "))

for i in range (98,-1,-1):
    for j in range(i+1):
        l[i][j] = int(l[i][j]) + max(int(l[i+1][j]),int(l[i+1][j+1]))
        
print l[0][0]