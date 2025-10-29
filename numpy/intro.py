#numpy ==>it is a python library which is used to perfoem numerical operations/computations on array of numbers
#we can use numpy on ndarray(n dimensional array)
# []-->1d array
#[[],[],[],[]]--> 2d array --each row should contain equal number of columns
#[[[]]]-->3d array

import numpy as np

#1.creating arrays
# #1d array
# arr1=np.array([1,3,5])
# print(type(arr1))
# print(arr1)

# #2d array
# arr2=np.array([[1,2,3],[5,5,6]])
# print(type(arr2))
# print(np.ndim(arr2))
# print(arr2)


# #3d array
# arr3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(np.ndim(arr3)) #to know dimension of the array

# #2.Array Attributes
# arr = np.array([[1,2,3],[4,5,6]])
# arr=np.array([23.30,33,343])
# arr1=np.array(['a','b'])
# print("shape",arr.shape)
# print("shape",np.shape(arr))
# print("dimension",arr.ndim)
# print("total number of values",arr.size)
# print("datatype",arr.dtype)
# print("datatype",arr1.dtype)
# print(arr.dtype)
# print("bytes per element",arr.itemsize)

# #4.Array Indexinf=g & slicing

# #1d aray
# arr=np.array([10,20,30,40,50])
# print(arr[0]) 
# print(arr[-1])
# print(arr[1:5])

# #2d array
# arr=np.array([[10,20,30],[30,32,34],[35,34,34]])
# print(arr[0,2])
# # print(arr[0:2,2:3])
# # print(arr[0:3,0:3])
# # print(arr[:,0:3])


#5.Array Operations
