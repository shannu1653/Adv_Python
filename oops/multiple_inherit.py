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

class ParentActor:
    def __init__(self,name,PWorth):
        self.pname=name
        self.Pworth=PWorth
        print(f"{self.pname} is the parent")
    def ParentAssets1(self,):
        print(f"{self.name} assets are {self.Pworth} cr")
class ChildActor(ParentActor):
    def __init__(self, Pname,Cname, PWorth):
        super().__init__(Pname,PWorth)
        self.Cname=Cname
        print(f"{self.Cname} is came by the reference of {self.pname}")
    def Childassets(self,worth):
        self.Cworth=worth
        print(f"{self.Cname} is having worth of {self.Cworth} cr")
    def TotalAssets(self):
        print(f"total assets of {self.Cname} is {self.Pworth+self.Cworth}")

ramcharan=ChildActor("chiranjivi","ramcharan",100)
ramcharan.Childassets(75)
ramcharan.TotalAssets()