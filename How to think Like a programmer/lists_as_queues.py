from collections import deque

queue=deque([])
def choice_func():
	print("1.] Insert an element.\n2.] Delete an element\n3.]Display the stack\n4.] Exit/Quit.\n")

	choice=int(input("Enter your choice: "))
	return choice

choice=choice_func()

while(choice!=4):
	if choice==1:
		if len(queue)==5:
			print("Queue is already full.")
		else:
			element=input("Enter the element you want to insert...")
			queue.append(element)
			print(element, "added to the queue.")

	elif choice==2:
		if len(queue)<1:
			print("Stack is empty")
		else:
			element=queue.popleft()
			print(element,"deleted successfully")

	elif choice==3:
		for i in queue:
			print(i)

	else:
		print("Invalid option.")

	choice=choice_func()
