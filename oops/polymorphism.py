class Dog:
    def speak(self):
        return 'woof!!'
class Cat:
    def speak(self):
        return "Meow!"
class Tiger:
    def speak(self):
        return "Roar"
def animated_sound(animals):
    print(animals.speak())
dog=Dog()
cat=Cat()
tiger=Tiger()
animated_sound(dog)
animated_sound(cat)