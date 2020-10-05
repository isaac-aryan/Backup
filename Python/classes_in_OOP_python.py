#Class is a user defined prototype for an object that defines a set of attributes that characterize any object of the class.

#Attributes of the class can be the variables, functions(also called methods) which can be accesed via the .(dot) operator

#class variable- It is a variable shared by all instances of a class. These are defined within the class but outside any class method.

#Data member- A class variable that holds data associated with a class and its objects.

#Function Overloading- The assignment of more than one behaviour to a particular function.

#Instance variable- A variable that is defined inside a method.

#Inheritance- The transfer of characteristics of a class to other classes that are derived from it.

#Instance- An individual object of a class.

#Instantiation- The creation of an instance of a class.

#method- A function that belongs to a class.

#object- A unique instance of a data structure defined by its class.

#Operator Overloading- The assignment of more than one function to a particular operator.

class Employee:
	'Common base class for all Employees' #Class documentation
	empCount=0 #Example of class variable. This can be accesed as Employee.empCount inside or outside the class.
	company_name="AryanCo"
	def __init__(self, name, salary):#Constructor of the class. Called when you create a new object.
		self.name=name
		self.salary=salary
		Employee.empCount+=1

	def displayCount(self):
		print("Total Employee Count ",Employee.empCount)

	def displayEmployee(self):	
		print("Name: ", self.name, ",Salary: ",self.salary)

	def __del__(self):
		Employee.empCount-=1

employee1=Employee("Aryan", 50000)
employee2=Employee("Tom", 45000)

print(employee1.displayEmployee())
print(employee2.displayEmployee())

print("Total Employees= ",employee1.displayCount())

print(Employee.__doc__)

print(Employee.__name__)

#To delete any instance of a class we use the del operator

del employee2

print(employee1.displayCount())

