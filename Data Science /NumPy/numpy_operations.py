#NUMPY OPERATIONS

import numpy as np

arr=np.arange(1,11)
print(arr+arr) #prints the sum of the array with itself on an element per element basis

print(arr-arr) #prints the subraction of the array with itself on an element per element basis

print(arr*arr) #prints the product of the array with itself on an element per element basis

print(arr-100) #prints the subtraction of the array with 100 for each element

#Dividing by 0 in numpy does not throw an error, but it issues a warning but still gives an output of null or infinity

print(arr**2) #prints each elemnt of the array to the power of 2

print(np.sin(arr)) #returns an array of the sine value of every element in arr

print(np.log(arr)) #returns logarithm of every element in arr

