#Tuples are similar to lists but they are immutable
#Immutable means they cannot be changed i.e a single element of the list cannot be removed or updated
tup1=('physics', 'chemistry', 1997, 2000)
tup2=(1,2,3,4,5)
tup3=("a","b","c","d",)

#Accesing values in tuples is similar to the way we do it in lists
print(tup1[1])
print(tup2[1:3+1])

#We cannot update a tuple as it is but we can always create a new tuple and add elements to it

tup4=tup3+('e',)
print(tup4)

#To delete tuple elements we cannot do so as tuple is immutable but we can delete an entire tuple

del tup4
tup4=tup3+('f',)
print(tup4)

#BASIC EXPRESSIONS ON TUPLES
#1) Length

print(len(tup3))

#2) Addition

print(tup2+tup3)

#3)Repetition or Multiplication

print(('Hi!',)*4)

#4)For going over each element in the tuple(iteration)

for x in (tup2):
	print (x)

#INDEXING AND SLICING

print(tup1[0])

print(tup1[-1])

print(tup1[1:])

#The same function used for lists are used for tuples. Some functions are

#1) cmp(tup1,tup2)
#2) max(tup1), min(tup1)
#3)To convert a sequence into a tuple, tuple(seq)

