
stack=[]

def choice_func():
	print("1.] Insert an element.\n2.] Delete an element\n3.]Display the stack\n4.] Exit/Quit.\n")

	choice=int(input("Enter your choice: "))
	return choice

choice=choice_func()

while(choice!=4):
	if choice==1:
		if len(stack)==5:
			print("Stack is already full.")
		else:
			element=input("Enter the element you want to insert...")
			stack.append(element)

	elif choice==2:
		if len(stack)<1:
			print("Stack is empty")
		else:
			stack.pop()

	elif choice==3:
		print(stack)

	else:
		print("Invalid option.")

	choice=choice_func()
