m1=[[1]*3 for i in range(3)]


m2=[[j]*3 for j in range(3)]

print(m1,m2)

m3=[[0]*3 for d in range(3)]

for i in range(3):
	for j in range(3):
		m3[i][j]=m1[i][j]+m2[i][j]
print(m3)