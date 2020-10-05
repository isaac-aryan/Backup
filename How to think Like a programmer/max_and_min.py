list1=[100,10,23,48,7,54]

maxi=list1[0]

for i in list1:
	
	if maxi>=i:
		continue
	else:
		maxi=i


		
print(maxi," is the largest value.")

mini=list1[0]
for j in list1:
	if j<=mini:
		mini=j
print(mini," is the minimum value.")
