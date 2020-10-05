print ("Hello World")

a=10
b=20
c=a+b
d=a-b
e=a*b
f=float(a)/b

print (c,d,e,f)

#name=(input("Enter your name: "))
#print ("Hello, "+name)

"""num=int(input("Enter a number: "))
print(num**2,num**0.5)

num2=int(input("Enter a number: "))
if(num2%2==0):
	print("Your number is an even number")
else:
	print("You rnumber is an odd number")

num3=int(input("Enter a number: "))
while(num3>=0):
	print(num3)
	num3-=1"""

def num_taker(x,y,z):
	greatest=0
	if(x>y and x>z):
		greatest=x
		lowest=0
		if(y>z):
			lowest=z
			print(greatest,y,lowest)
		else:
			lowest=y
			print(greatest,z,lowest)
	elif(y>x and y>z):
		greatest=y
		lowest=0
		if(x>z):
			lowest=z
			print(greatest,x,lowest)
		else:
			lowest=x
			print(greatest,z,lowest)
	else:
		greatest=z
		lowest=0
		if(x>y):
			lowest=y
			print(greatest,x,lowest)
		else:
			lowest=x
			print(greatest,y,lowest)

no1=int(input("Enter first number: "))
no2=int(input("Enter second number: "))
no3=int(input("Enter third number: "))

#num_taker(no1,no2,no3)

def disp_descend(m,n,o):
	List1=[m,n,o]
	List1.sort(reverse=True)
	print(List1[0],List1[1],List1[2])

disp_descend(no1,no2,no3)

                                                                                                                                                                                                                                                                                                                                                                                         
