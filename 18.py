file_18 = open("18.txt","r")

l = []
for i in range(15):
    l.append(file_18.readline().split(" "))

for i in range (13,-1,-1):
    for j in range(i+1):
        l[i][j] = int(l[i][j]) + max(int(l[i+1][j]),int(l[i+1][j+1]))
        
print l[0][0]
