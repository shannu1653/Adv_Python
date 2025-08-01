# #multiple inheritance
# class Parent1:
#     def P1method(self):
#         print("i am a method from parent1")
# class Parent2:
#     def P2method(self):
#         print("i am a method from parent2")
# class Child(Parent2,Parent1):
#     def Cmethod(self):
#         super().P1method()
#         super().P2method()
#         print("i am method from child")
# obj1=Child()
# obj1.Cmethod()

# class A:
#     def display(self):
#         print("A class")
# class B:
#     def display(self):
#         print("B class")        
# class C(A,B):
#     def display(self):
#         super().display()
#         print("C class")
#         B().display()
# obj=C()
# obj.display()

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
# Male.work(boy_1)#approach 2
# Human.work(boy_1)
print(Boy.mro())