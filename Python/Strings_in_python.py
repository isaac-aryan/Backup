
My_string='Aryan'
My_string2='Bhobe'

#strings in python are treated as an array of characters
#Therefore each character in the string can be adressed individualy by its position

print(My_string2[0])

#We can also get sub strings from the main string
print(My_string2[1:3+1])

#We can add two strings or can add characters to the string using the + operator.
My_string3=My_string+' Isaac '+My_string2
print(My_string3)

#String Operations
#1) String Repetition using * operator
print(My_string*4)

#2)Check if a character is present in the string
print('B' in My_string2)
print('B' in My_string)


#built in string functions
My_string4='my name is aryan '
print(My_string4.capitalize())#Capitalizes the first word of the sentence


print(My_string4.count('a'))#Counts the number of occurences of a sub string in a given string

print(len(My_string4))#prints the number of characters in a string

print(My_string4.find('aryan'))#find returns the starting index of the sub string else it returns -1 if it cannot find the substring

print(My_string3.lower())

print(max(My_string3))
print(min(My_string))

print(My_string4.split()[3])

print(My_string4.title())

print(My_string3.upper(++++))
