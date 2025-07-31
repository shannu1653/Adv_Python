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