from My_module import add_2
num1=int(input("Enter num 1: "))
num2=int(input("Enter num 2: "))
print("The sum of the two numbers is: ",num1+num2)

#Taking multiple inputs on the same line using split function

data=input("Enter your name,age,standard: ")
print(data.split(","))

data2=input("5 space separated numbers")
Split=data2.split()
print("The biggest number is: ",max(Split))