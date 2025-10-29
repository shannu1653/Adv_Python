#numpy-->series
# why numpy --> NumPy (Numerical Python) is used because it makes numerical computation:
# Faster
# More efficient
# Easier to code
# especially when working with large datasets or mathematical operations.
import numpy as np
import time

#creating array
# arr=np.array((1,2,3,4,))
# print(type(arr))


# start=time.time()
# num_arr=np.arange(100000)*2
# print('numpy time',start)
# print('numpy time',time.time())

# arr2=np.arange(10000)
# print(arr2)


# #zeroes
# print(np.zeros((3,3),dtype=int))
# print(np.zeros(6))
# print(np.zeros((7,8),dtype=int))

# #ones
# print(np.ones((5,4),dtype=int))

# print(np.linspace(2,101,100)) #start #stop #step(divided equally)
# print(np.linspace(1,1000,4))

# start=time.time()
# arr=[1,2,3,4,5,6,7,88,9]
# sum=0
# for i in arr:
#     sum+=i
# print(sum,time.time())



# start=time.time()
# print(np.sum([1,2,3,4,5,6,7,88,9]),time.time())

# #mean
# print(np.mean([1,2,3,4,5,6,7,88,9]))

# list2=[1,2,3,4,5,6,7,88,9,3]
# mid=len(list2)//2
# # print(list2[mid])
# print(list2[mid],list2[mid]-1)

# print(np.median([1,2,3,4,5,6,7,88,9]))
# print(np.median([1,2,3,4,5,6,7,88,9,3]))


# #******vartical calculation********y-axis
# print(np.mean([[1,2],[3,4]],axis=1)) 

# #******horixental calculation******** x-axis
# print(np.mean([[1,2],[3,4]],axis=0)) 






