My_list=[2,4,6,8,10,12,14,16,18,20]

#To acess an element in a list we use the same method as used for strings
print(My_list[5])

#To acess multiple elements in the list, we can give a range
print(My_list[1:9])

#To iterate over all elements in a list we can use a for loop
for t in My_list:
	print(t)

#Multi data type lists are supported in python
My_list2=['Aryan',13,87.6,'A']
print(""+My_list2[0]+" age "+str(My_list2[1])+", secured a percentage of "+str(My_list2[2])+" and a grade of "+My_list2[3]+".")

#Adding more data to a list we use the append method
My_list2.append('Bhobe')
print(My_list2) 

#To change an element in the list, we can simply assign a new value by its index
My_list2[2]=88
print(My_list2)

#We can even delete an element from the list using the del funtion
del(My_list2[3])
print(My_list2)

#Basic list Operations
#1) To get length of a list
print(len(My_list2))

#2) To add multiple elements to the list or to join two lists we use the + operator
print(My_list+My_list2)

#3)To repeat elements in a list we use the * operator
My_list3=['Hi']
print(My_list3*4)

#4)To check if an element is present in a list we use the in operator
if('Aryan' in My_list2):
	print("The list contains Aryan.")

#REVERSING A LIST
#We can reverse a list in the following manner:
reversed_list=My_list[::-1]
print(reversed_list)

#We can also adress a list in python using negative numbers which start from the last element in the list
Last_element=My_list2[-1]
print(Last_element)

#We can also cut a list using splice
spliced_list=My_list[4:]
print(spliced_list)

spliced_list2=My_list[:4]
print(spliced_list2)

#INBUILT FUNCTIONS FOR LISTS
#1) Sum of a list(can only be used for integers and floats)
print(sum(My_list))

#Reversing a list
My_list2.reverse()
print(My_list2)

#Sorting a list
My_list4=[3,52,74,11,7]
My_list4.sort()
print(My_list4)

#Finding the index of an element in the list
print(My_list.index(20))

#Getting the minimum and maximum of a list
print(min(My_list4))
print(max(My_list4))

#List Comprehensions


New_list=[]
for i in range(1,11,2):
		New_list.append(i)
print(New_list)

#This process of creating a dynamic list can be shortened to one line using list comprehensions.
New_list2=[i for i in range(1,11)]
print(New_list2)

def is_consonant(c):
	vowels=['a','e','i','o','u','A','E',"I",'O','U']
	if c in vowels:
		return False
	else:
		return True


New_list3=[i for i in 'Aryan' if is_consonant(i)]
print(New_list3)


