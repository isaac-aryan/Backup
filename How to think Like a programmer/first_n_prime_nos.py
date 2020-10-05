
num=int(input("Enter the number..."))

limit=num/2

i=2
ctr=0

while i<=num:
	isPrime=True
	for j in range(2,int(i**0.5)+1):
		if i%j==0:
			isPrime=False
			break
	if isPrime==True:	
		print(i," is a prime number.")
		ctr+=1	
	i+=1
print("The total count of prime numbers is ",ctr)
#Code for finding first n prime numbers

"""ctr=2
i=0
while i<num:
	if isPrime(ctr)==True:
		print(ctr,i)
		i+=1
	ctr+=1"""