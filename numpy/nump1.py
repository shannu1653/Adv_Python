# import numpy as np

# #1.creating single dimesional array
# a=np.array([1,2,4,4,4,23,2])
# print(a)

# #2.creating 2d array
# b=np.array([[5.3,3.2,44],[4.3,2.4,34]])
# print(b)

# #3.how to get dimensions-->ndim
# print(a.ndim)
# print(b.ndim)

# #shape
# print(a.shape) 
# print(b.shape)  #it gives info about rows and lenth of the single array

# #dtype
# print(a.dtype) #it gives datatype
# print(b.dtype)

# #size
# print(a.size) #it gives lenth of array
# print(b.size) 
# print(b.itemsize)

# #** Accesing/changing specific elements ,rows and  columns etc
# #1.get a specofic index(a[r,c]) r strats-0,c starts-0
# a=np.array([[1,2,3,4,5,9,9],[3,4,5,5,6,1,2]])
# print(a.shape)
# print(a[1,4])
# print(a[1,-1])

# #2.get specific row
# print(a[1 ,:])

# #3.get specific column
# print(a[:,0])

# #4.Getinng little more fancy slicing [startindex:endindex:stepsize]
# print(a[0,1:6:2])

# #5.replacing specific value
# a[0,5]=20
# print(a)
# print(a[0,1:6:2])

# #5.replacing all specic columns and all row values
# a[:,2]=100
# print(a)

# #6.replacing all specific columsn with diferent row values
# a[:,3]=[1,4]
# print(a)

import numpy as np
# #3d example
# b=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
# print(b)

# #get speifi element
# print(b[:,1,:])

# #replace
# b[:,1,:]=[[100,100],[99,99]]
# print(b)


# # Intialiazing differt types of arrays
# # all zeros()
# b=np.zeros((4,3))
# print(b)

# #all ones()
# c=np.ones((4,3,4) ,dtype=int)
# print(c)

# #any other number
# d=np.full((2,2),99,dtype=float)
# print(d)

# #any other numer(full_like)
# e=np.full_like(d,5)
# print(e)

# #random decimal numbers
# print(np.random.rand(4,4))
# print(np.random.random_sample(e.shape))

# #random integer values
# print(np.random.randint(15,19,size=(3,3))) #//import
# print(np.random.randint(-15,19,size=(3,3))) #//import
# print(np.random.randint(19,size=(3,3))) #//important

# #the identity matrix
# print(np.identity(5))

# #Repeat an array
# arr=np.array([[1,2,3]])
# r1=np.repeat(arr,4,axis=0)
# print(r1)
# r1=np.repeat(arr,4,axis=1)
# print(r1)

# #puzzle
# output=np.ones((5,5))
# a=np.zeros((3,3))
# a[1,1]=9
# output[1:4,1:4]=a
# output[1:-1,1:-1]=a
# print(output)

# #note--be carefull when copy an array
# a=np.array([1,2,3])
# b=a.copy()
# b[0]=100
# print(a)
# print(b)

# #MATHEMATICS

# a=np.array([1,2,3,4])
# print(a)
# print(a+2)
# print(a+3)
# b=a+2
# print(a+b)
# print(a**3)

# #trignometri
# print(np.sin(a))


# #linear algebra
# a=np.ones((2,3))
# print(a)
# b=np.full((3,2),2)
# print(b)
# print(np.matmul(a,b))

# #find the determinant
# c=np.identity(3)
# print(np.linalg.det(c)) #once search in chatgpt?

#*************statistics ***************

# stats=np.array([[2,3],[4,5]])
# print(stats)
# print(np.min(stats ,axis=1))
# print(np.max(stats,axis=1))
# print(np.sum(stats ,axis=0))
# print(np.sum(stats,axis=1))

# #*************Reorganizing arrays
# #reshping array
# before=np.array([[2,3,4,5],[3,4,3,3]])
# print(before)

# after=before.reshape(4,2)
# after=before.reshape(2,2,2)
# print(after.shape)
# print(after)

print('===================================================')
#vertically stacking vecotrs
v1=np.array([1,2,3,4,5])
v2=np.array([5,6,7,7,8])
print(np.vstack([v1,v2,v2,v1]))

#horizental stak
print(np.hstack([v1,v2,v1,v2]))

print("==================Miscelleneous=====================")
#load from data
field=(np.genfromtxt('data.txt',delimiter=","))
print(field.astype(int))

print("=========Boolean Maskig and advance indexing===========")
print(np.all(field>50,axis=0))
print(field[field>50])

a=np.array([2,3,4,5,6,4,3])
print(a[[1,3,1]])
print(np.all(field>50,axis=1))