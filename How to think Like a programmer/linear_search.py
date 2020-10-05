import random as r

my_list=[]

for i in range(10):
	c=r.randint(1,10)
	my_list.append(c)

print(my_list)
key=4

index=0
flg=False
while(flg==False):
	if index>9:
		break
	if my_list[index]==key:
		print(key," found in the list at index ",index)
		flg=True
		continue
	index+=1


if flg==False:
	print(key," not found in list.")