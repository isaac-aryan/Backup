def choice_func():
	print("1.] Add a student.\n2.] Delete a student\n3.] Search for a student\n4.]Display Students\n5.]Update a Student\n6.] Exit/Quit.\n")

	choice=int(input("Enter your choice: "))
	return choice

choice=choice_func()


students=[]
while choice !=6:
	if choice==1:
		name=input("Enter the name of the student you want to add...")
		students.append(name)
		print("Student added successfully!\n")

	elif choice==2:
		name=input("Enter the student you want to delete...")
		if name in sudents:
			students.remove(name)
			print("Student deleted successfully!\n")
		else:
			print("Student not found.")

	elif choice==3:
		print("Search for a student...\n")
		name=input()
		if name in students:
			print("Student found.")
		else:
			print("Student not found.")

	elif choice==4:
		print(students)

	elif choice==5:
		name=input("Enter the student you want to update...")
		index=students.index[name]
		update=input("Enter the updated name...")
		students[index]=update
	else:
		print("Invalid option.")

	choice=choice_func()