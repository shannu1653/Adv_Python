#acquiring methods and attribute from already defined class into newly created -- inheritance
#creating new class from already created class

#types of inheritance
'''1.single inheritance #if u derive one child class from single parent class then it is a single inheritance
2.multiple   --> if u derive one child class from more than one parent class then it is a multiple inheritance inheritance
3.multilevel  "
4.hierarical   "
5.hybrid'''

#single inheritance

class Parent:
    def Pmethod(self):
        print('i am a method from parent')

class Child(Parent):
    def Cmethod(self):
        print('i am a method from child')
obj1=Child()
obj1.Pmethod()
obj1.Cmethod()
