import numpy as np




# print(np.mode([1,2,3,4,4,5]))


# #1.reshape-->we can resape image our elements
# dim1=np.array([1,2,3,4,5,6,7,7,8,6])
# # print(np.reshape(dim1,(2,5)))
# print(np.reshape(np.arange(12),(2,2,3)))

# #2.flat-->convert multidimensionl array into 1d
# arr=[[1,2,34,5,6,7],[3,4,4,2,3,4]]
# print(np.array(arr).flatten())

#3.concatenate -->
# a=np.array([[1,2,3,4],[2,3,3,3]])
# b=np.array([[1,2,3,4],[3,2,3,3]])
# print(np.concatenate((a,b),axis=1))
# print(np.concatenate((a,b),axis=0))

# #4.indexing
# arr=[1,2,3,444,44,23,4342,23,43]
# np_arr=np.array(arr)
# print(np_arr)
# print(np.where(np_arr>50))

#vector
print([1,2,3]*2) #scalar vector
print(np.array([1,2,3])*2) #vector c