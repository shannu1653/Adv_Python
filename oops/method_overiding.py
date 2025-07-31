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

car=Car()
cycle=Cycle()
car.speed()
cycle.speed()

