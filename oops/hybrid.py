# # Base class
# class School:
#     def func1(self):
#         print("This function is in school.")

# # Derived class 1 (Single Inheritance)
# class Student1(School):
#     def func2(self):
#         print("This function is in student 1.")

# # Derived class 2 (Another Single Inheritance)
# class Student2(School):
#     def func3(self):
#         print("This function is in student 2.")

# # Derived class 3 (Multiple Inheritance)
# class Student3(Student1, School):
#     def func4(self):
#         print("This function is in student 3.")

# # Driver code
# obj = Student3()
# obj.func1()
# obj.func2()

# 0
# 1 3
# 1 5 13
# 2 8 21 34

# a=0
# b=1
# for i in range(0,3):
#     for j in range(0,i+1):
#         print(b)
#         a,b=b,a+b

# Number of rows
rows = 4

# Generate Fibonacci numbers
fib = [0, 1]
for i in range(2, 50):   # generate enough numbers
    fib.append(fib[-1] + fib[-2])

index = 0
for r in range(1, rows + 1):
    row = fib[index:index + r]
    print(" ".join(map(str, row)))
    index += r
    
