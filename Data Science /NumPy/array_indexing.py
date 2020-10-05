#ARRAY INDEXING WITH NUMPY

import numpy as np

arr=np.arange(0,11)

print(arr[8]) #returns value at index 8

print(arr[1:5]) #returns array of values from index 1 to index 5

print(arr[:6]) #returns all the values upto index 6

print(arr[0:]) #returns all the values beyond index 0

arr[0:5]=100 # sets the values of all numbers from index 0 to 4 to 100
print(arr)

arr=np.arange(0,11)

arr_2d=np.array([[5,10,15],[20,25,30],[35,40,45]])

print(arr_2d[0]) #prints the first row of the 2d matrice

print(arr_2d[1][1]) #prints the value at the poition 1,1 of the matrix

#As of now, your 2D matrix looks like this
# [5,10,15]
# [20,25,30]
# [35,40,45]
# If you want to grab a sub list of lets say just the top corner, you can do this with slice notation

subarr_2d=arr_2d[:2,1:]
print(subarr_2d)

#>,< 

bool_arr=arr>5 #returns an array of data type boolean. It checks the value of each index number to be > 5 and returns True or False
print(bool_arr)

arr=subarr_2d[bool_arr] #returns all the values that were True



