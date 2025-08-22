# # Base class
# class Parent:
#     def func1(self):
#         print("This function is in parent class.")

# # Derived class 1
# class Child1(Parent):
#     def func2(self):
#         print("This function is in child 1.")

# # Derived class 2
# class Child2(Parent):
#     def func3(self):
#         print("This function is in child 2.")

# # Driver code
# object1 = Child1()
# object2 = Child2()

# object1.func1()
# object1.func2()
# object2.func1()
# object2.func3()

class Human():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def showDetails(self):
        print(f'name : {self.name}, age : {self.age}')
    def eat(self):
        print('i can eat')
class Male(Human):
    def __init__(self, name, age,location):
        super().__init__(name, age)
        self.location=location
    def sleep(self):
        print('I can sleep whole day')
class Female(Human):
    def __init__(self, name, age, can_dance):
        print('Calling inti from Female class')
        super().__init__(name, age)
        self.know_dancing=can_dance
    def showDetails_F(self):
        super().showDetails()
        print(f"knowo_dancing:{self.know_dancing}")
    def work(self):
        print('I can code')
female_1=Female('suppu',23,'yes')
female_1.work()
female_1.showDetails()
female_1.showDetails_F()
print(female_1.name)
# male_1=Male('shannu',22,'hyd')
# male_1.showDetails()
# male_1.sleep()