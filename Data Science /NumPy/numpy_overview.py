#NUMPY OVERVIEW AND BASIC FUNCTIONS

import numpy as np

#CREATING A NUMPY ARRAY
#One dimensional array

my_list=[1,2,3]
arr=np.array(my_list)

#Two dimensional array

my_matrice=[[1,2,3],[1,2,4]]
mat=np.array(my_matrice)

#List using a loop type thingy
#arrange(starting value, ending value, step size)

np.arange(1,11,2)

#List of only zeros

np.zeros(4)
np.zeros((2,3))

#List only of ones

np.ones(4)
np.ones((2,3))

#The linspaace function takes three parameters: Start point, End point and a third point parameter. 
#Lets assume the value of the 3rd para is 5. It then returns an array of 5 evenly spaced numbers from he start point to the end point.

np.linspace(0,10,5)

#The eye function returns an identity matrix. An identity matrix is a 2 dimensional matrix composed of zeros with a diagonal of ones.

np.eye(4)

#rand functions returns an array or matrix of random numbers between 0 and 1 with the length of the array passed as a parameter

np.random.rand(5)
np.random.rand(5,5)

#randint function return an array of random numbers from a low value to a high value and the array size as the third parameter

np.random.randint(1,100,6)

#reshape function returns a matrix reshaped to the dimensions you want.
#If the matrix does not contain enough elements to reshape it, it will give you an error.

arr=np.arange(25)
print(arr.reshape(5,5))

#max and min functions return the highest and lowest values in the array

print(arr.max())
print(arr.min())

#argmax and argmin return the index value of the highest and lowest values in the array

arr.argmax()
arr.argmin()

#shape function returns the length and shape of an array/matrix

arr.shape() #will return (25,) because its a 1d array of size 25

#dtype function returns the data type of the values in the array

arr.dtype()
