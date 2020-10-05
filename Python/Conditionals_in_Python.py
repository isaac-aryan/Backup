a=10
b=20

c,d=20,10

if(a>b):
	if(c>d):
		print("a and c are greater than b and d")
	else:
		print("a is greater than b but c is not greater than d")
elif(c>d):
	print("c is greater than d but a is not greater than b")
else:
	print("a and c are less than b and d")