import random as r

my_list=[]

for i in range(10):
	c=r.randint(1,100)
	my_list.append(c)


n=len(my_list)

print("List before sorting: ",my_list)


for k in range(1,n):
	flg=False
	for i in range(n-k):
		if my_list[i]>my_list[i+1]:
			temp=my_list[i]
			my_list[i]=my_list[i+1]
			my_list[i+1]=temp
			flg=True

	if flg==False:
		break

print("The sorted list is: ",my_list)