#multiple inheritance
class Parent1:
    def P1method(self):
        print("i am a method from parent1")
class Parent2:
    def P2method(self):
        print("i am a method from parent2")
class Child(Parent2,Parent1):
    def Cmethod(self):
        super().P1method()
        super().P2method()
        print("i am method from child")
obj1=Child()
obj1.Cmethod()

class A:
    def display(self):
        print("A class")
class B:
    def display(self):
        print("B class")        
class C(A,B):
    def display(self):
        super().display()
        print("C class")
        B().display()
obj=C()
obj.display()

class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male:
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code")


class Boy(Human,Male):  #(Male,Human)approach 1
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I can test")
boy_1=Boy()
# boy_1.flirt()
# boy_1.eat()
boy_1.work()
Male.work(boy_1)#approach 2
Human.work(boy_1)
print(Boy.mro())


class Human:
    def __init__(self,num_heart):
        print("cslling init from Human")
        self.eys=2
        self.nose=2
        self.num_heart=num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")

class Male:
    def __init__(self,name):
        print("calling init from Male")
        self.name=name
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code")


class Boy(Human,Male):  #(Male,Human)approach 1
    def __init__(self,name,languge,num_heart):
        Human.__init__(self,num_heart)
        Male.__init__(self,name)
        self.language=languge        
    def sleep(self):
        print("I can sleep")
    def work(self):
        print("I can test")
    def display(self):
        print(f"Hi i am {self.name} i am learning {self.language} and i have {self.num_heart} hearts")
boy_1=Boy("shannu","pyhton",3)
# boy_1.flirt()
# boy_1.eat()
print(boy_1.nose)
print(boy_1.num_heart)
print(boy_1.language)
boy_1.display()



#Example for diamond Problems 
#solve usind MRO
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
        super().show()
class C(A):
    def show(self):
        print("C")
        super().show()
class D(C,B):
    def show(self):
        print("D")
        super().show()
obj=D()
obj.show()


#i want to call both parents
#✅ Option 1: Explicitly call both parent methods inside Child
class Father:
    def skills(self):
        print("Father : knows gardening ")

class Mother:
    def skills(self):
        print("Mother : knows cooking")
class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
    def hobby(self):
        print("Child : Loves painting")
c=Child()
c.skills()

#✅ Option 2: Use super() carefully (only works in diamond inheritance / cooperative classes)
class Father:
    def skills(self):
        print("Father : knows gardening ")
        super().skills()
class Mother:
    def skills(self):
        print("Mother : knows cooking")
class Child(Father,Mother):
    pass
c=Child()
c.skills()