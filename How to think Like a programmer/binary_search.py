import random as r

my_list=[]

for i in range(10):
	c=r.randint(1,10)
	my_list.append(c)

my_list.sort()

print(my_list)
key=4

loc=-1

u=len(my_list)-1
l=0

m=int((l+u)/2)

while(l<=u and my_list[m]!=key):
	if key<my_list[m]:
		u=m-1
	else:
		l=m+1
	m=int((l+u)/2)

if my_list[m]==key:
	loc=m
	print(key,"found in list at index ",loc)
else:
	print("Sorry, nothing was found.")

