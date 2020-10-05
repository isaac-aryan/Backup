
while(1):
	num=int(input("Enter the number..."))
	if num<=10:
		break
	else:
		print("The number cannot be more than 10.\nPlease re-enter.")


i=1
while i<=num:
	print(" ",i, end=' ')
	i+=1
print("\n","----"*num)

print()
print()

for j in range(1,num+1):
	print(j," | ",end='')
	for ctr in range(1,num+1):
		print(ctr*j, end=' ')
	print()





