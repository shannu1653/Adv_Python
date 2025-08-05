#method overriding -->replacing or changing the logic of method from superclsaa in subclass is called method overiding
#method ovveriding can be applicable only when inheritance happens otherwiese it won't applicable

class Vehicle:
    def speed(self):
        print("vahicle speedis normal")
class Car(Vehicle):
    def speed(self):
        print("car speed is 120kmph")
class Cycle(Vehicle):
    def speed(self):
        print("cycle speed is 20kmph")

# car=Car()
# cycle=Cycle()
# car.speed()
# cycle.speed()


#method overiding
# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class that overrides speak()
class Dog(Animal):
    def speak(self):
        print("Dog barks")

# Creating objects
a = Animal()
d = Dog()

# Calling methods
a.speak()  # Output: Animal makes a sound
d.speak()  # Output: Dog barks

#solution for overriding
class Bird:
    def fly(self):
        print("Bird can fly")

class Parrot(Bird):
    def fly(self):
        print("Parrot can fly faster")
        super().fly()  # Call the parent class method

p = Parrot()
p.fly()

# Output:
# Parrot can fly faster
# Bird can fly


class Oreder:
    def __init__(self,customer,order_id):
        self.customer=customer
        self.order_id=order_id
    def deliver(self):
        print(f"{self.customer} will get his order num {self.order_id} with standard delivery")
class ExpressOreder(Oreder):
    def __init__(self, customer, order_id):
        super().__init__(customer, order_id)
    def deliver(self):
        print(f"{self.customer} will get his oreder num {self.order_id} with express delivery")

obj1=Oreder("shannu",123)
obj1.deliver()
obj2=Oreder('harish',1223)

obj3=ExpressOreder('naresh','nar24')

print(obj1.__dict__)
print(obj2.__dict__)
print(ExpressOreder.mro())#method of resotion oreder --> to check flow of inheritance happeing b/w the classes.

# Python Program to depict multiple inheritance
# when method is overridden in one of the classes

class Class1:
    def m(self):
        print("In Class1") 
      
class Class2(Class1):
    pass

class Class3(Class1):
    def m(self):
        print("In Class3")    
     
class Class4(Class2, Class3):
    pass       

obj = Class4()
obj.m()


# Python Program to depict multiple inheritance
# when every class defines the same method

class Class1:
    def m(self):
        print("In Class1") 
      
class Class2(Class1):
    def m(self):
        print("In Class2")

class Class3(Class1):
    def m(self):
         print("In Class3")     
    
class Class4(Class2, Class3):
    def m(self):
        print("In Class4")   

obj = Class4()
obj.m()

Class2.m(obj)
Class3.m(obj)
Class1.m(obj)


# Python Program to depict multiple inheritance
# when we try to call m of Class1 from both m of
# Class2 and m of Class3

class Class1:
    def m(self):
        print("In Class1")   
    
class Class2(Class1):
    def m(self):
        print("In Class2")
        Class1.m(self)

class Class3(Class1):
    def m(self):
        print("In Class3")
        Class1.m(self)   
     
class Class4(Class2, Class3):
    def m(self):
        print("In Class4")   
        Class2.m(self)
        Class3.m(self)
     
obj = Class4()
obj.m()


# Python program to demonstrate
# super()

class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()

class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()

class Class4(Class2, Class3):
    def m(self):
        print("In Class4")   
        super().m()
     
print(Class4.mro())         #This will print list
print(Class4.__mro__)        #This will print tuple


# ✅ Method Overloading with Multiple Dispatch in Python

# Python doesn’t support traditional method overloading directly, but we can simulate it more cleanly using a library called multipledispatch.

# 🔹 What is multipledispatch?

# It’s a third-party library that allows multiple versions of a function (same name, different argument types) — similar to method overloading in statically typed languages like Java or C++.

# 🔧 Installation:

# pip install multipledispatch

# 🔍 Example:

from multipledispatch import dispatch

class Greet:

 @dispatch()
 def hello(self):
    print("Hello!")

 @dispatch(str)
 def hello(self, name):
     print(f"Hello, {name}!")

 @dispatch(str, int)
 def hello(self, name, age):
    print(f"Hello, {name}! You are {age} years old.")

g = Greet()
g.hello() # Output: Hello!
g.hello("shannu") # Output: Hello, shannu!
g.hello("shannu", 22) # Output: Hello, shannu! You are 22 years old



# ✅ How to achieve method overloading in Python?

# Python uses default arguments, *args, and **kwargs to simulate method overloading.
# 🔹 Using Default Arguments:

class Demo:
 def show(self, a=None, b=None):
    if a is not None and b is not None:
        print("Two arguments:", a, b)
    elif a is not None:
        print("One argument:", a)
    else:
        print("No arguments")

d = Demo()
d.show() # No arguments
d.show(10) # One argument: 10
d.show(10, 20) # Two arguments: 10 20

#🔹 Using *args:

class Add:
 def result(self, *args):
    print("Sum:", sum(args))

a = Add()
a.result(1, 2) # Sum: 3
a.result(10, 20, 30) # Sum: 60