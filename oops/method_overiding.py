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