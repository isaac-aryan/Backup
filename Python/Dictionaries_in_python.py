#Dictionaries are similar to tuples and lists but every element in a dictionary is a key:value pair
#For lists we use [] brackets for tuples () brackets and for dictionaries {} brackets.

dict1={'Name': 'Aryan', 'Age': 7, 'Class': 'Ninth'}
print(dict1)

#Accesing elements in a dictionary
#The advantage of dictionaries is we can access an element value without knowing its position but instead we use the key for the value

print(dict1['Class'])

#Updating a value
dict1['Name']='Aryan Bhobe'
print(dict1)

#Adding a new element(key:value)

dict1['School']='Sharada Mandir'
print(dict1)

#There are two ways to delete a list or an element in the list
#1) Deleting a single element
del dict1['School']
print(dict1)

#2)Clear the dictionary of all the elements
dict1.clear()
print(dict1)

#3)You can delete an entire dictionary from memory using the del keyword
#E.g del dict1

#PROPERTIES OF DICTIONARY KEYS
#1) In one dictionary, you cannot have duplicate keys
#2) Keys must be immutable(You can use strings or tuples as dictionary keys but you cannot use lists)

#We can use the functions learnt for lists and tuples for dictionaries as well
#E.g cmp, len, str, type

#Functions for Dictionary(dict methods)
#1) dict.copy() Returns a copy of the dictionary
#2) dict.fromkeys() Creates a new dictionary with keys from seq and values set to value
#3) dict.get(key, default=None)
dict1={'Name': 'Aryan Bhobe', 'Age': 7, 'Class': 'Ninth'}
print(dict1.get('Name','Aryan'))

#4) Get all the keys in a dictionary
print(dict1.keys()) 

#5) Get all key value pairs in a dictionary as the tuple
print (dict1.items())

#6) dict.setdefault(key,default=None)
#Similar to dict.get except if a key is missing it will add it to the dictionary with the default value

print(dict1.setdefault('School',None))
print(dict1)

#7)To get all the values in a dictionary

print(dict1.values())
