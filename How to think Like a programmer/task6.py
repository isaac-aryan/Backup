n=int(input("Enter a number greater than 1..."))
ctr=2

while ctr<=int(n/2):
	if n%ctr==0:
		print("",n," is not a prime number")
		break
	elif ctr==int(n/2):
		print("It is a prime number..")
		break
	else:
		ctr+=1

