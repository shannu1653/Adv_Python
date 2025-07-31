class Emp():
    def __init__(self, id, name, Add):
        self.id = id
        self.name = name
        self.Add = Add

# Class freelancer inherits EMP
class Freelance(Emp):
    def __init__(self, id, name, Add, Emails):
        self.Emails = Emails
        super().__init__(id, name, Add)

Emp_1 = Freelance(103, "Suraj kr gupta", "Noida" , "abc@gmails")
print('The ID is:', Emp_1.id)
print('The Name is:', Emp_1.name)
print('The Address is:', Emp_1.Add)
print('The Emails is:', Emp_1.Emails)


# A Python program to demonstrate inheritance
class Person:
    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)
    

class Emp(Person):
    
    def __init__(self, name, id):
        self.name_=name
        super().__init__(name, id)

    def Print(self):
        print("Emp class called")

Emp_details = Emp("Mayank", 103)

# calling parent class function
print(Emp_details.name_, Emp_details.name)


class A:
    def method(self):
        print("Method in A")

class B(A):
    def method(self):
        print("Method in B")
        super().method()

class C(A):
    def method(self):
        print("Method in C")
        super().method()

class D(B, C):
    def method(self):
        print("Method in D")
        super().method()

obj = D()
obj.method()
