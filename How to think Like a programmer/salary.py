salary=float(input("Please enter your salary.."))
grade=float(input("Please enter your grade..."))

if grade>=15:
	salary=salary+50/100*salary
	print("Your new salary is ",salary)
else:
	salary=salary+25/100*salary
	print("Your new salary is ",salary)