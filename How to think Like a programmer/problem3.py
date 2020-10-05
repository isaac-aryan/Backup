num1=float(input("Enter the first number...\n"))
num2=float(input("Enter the second number...\n"))
oper=raw_input("Enter the operator...\n")

if oper=='+':
	print(num1+num2)
elif oper=='-':
	print(num1-num2)
elif oper=='x':
	print(num1*num2)
elif oper=='/':
	if num2==0:
		print("Division by 0 is infinite")
	else:
		print(num1/num2)
else:
	print("Invalid input")
