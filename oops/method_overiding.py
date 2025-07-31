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



