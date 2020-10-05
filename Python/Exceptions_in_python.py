#In Python, handling exceptions is more important than handling exceptions in C
#This is because in C, errors come or can be noticed when we are compiling the code
#But, in Python the errors can come at anytime during the execution of the code, causing many bugs.
#Therefore, in Python, we try to predict when an error might occur and write some code to handle the error without causing the programme to crash.

#Error Handling using try and except
#Similar to if else where if=try and elif=except and else=else

try:
	my_file=open("XYZ",'r')
	my_file.write("This is my file.")
except Exception as e:
	print(e)
	print("error occured")
else:
	print("File written succesfully")
	my_file.close()