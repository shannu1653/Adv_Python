#Encapsulation
class Sample:
    def __init__(self):
        self.__name='shannu'
obj=Sample()
print(obj.__dict__)
# print(obj.__name) # it gives AttributeEroor
print(obj._Sample__name)

# public    --> name -->we can access without restriction
# protected --> _name --> we are not suppose to access but we can access.
# private   --> __name --> we can't access out of the class but we
# can hack it using name mangling approach.which is not recommended.

# but we can access private varibles using getter and setter methos which will define in the  same class.

# whenever we use only single class...we are not suppose to use protected variable outside of the class.

# whenever if we do inheritance then protected variables are allowed to use in both child and parent.

class Parent:
    def __init__(self):
        self._user="shannu"
class Child(Parent):
    def __init__(self):
        super().__init__()
        print(self._user)   #it is allowed
obji=Child()

class Parent:
    def __init__(self):
        self.__user='shannu'
class Child(Parent):
    def __init__(self):
        super().__init__()
        print(self.__user)  #it is restricted to Parent class only
# obj2=Child()

class Sample:
    def __init__(self):
        self.__name='shannu'
    
    def Details(self):
        # print(self.__name)
        return self.__name
obj3=Sample()
print(obj3.Details())

class Demo:
    def __init__(self):
        self.name='shannu'
obj=Demo()
print(obj.__dict__)
obj.name='kiran'
print(obj.__dict__)


class Demo:
    def __init__(self):
        self._name='harish'

obj=Demo()
print(obj.__dict__)
obj._name='kiran'
print(obj.__dict__)

class Demo:
    def __init__(self):
        self.__name='shannu'
obj=Demo()
print(obj.__dict__)
obj.__name='naveen'
print(obj.__dict__)

class Demo:
    def __init__(self):
        self.__name="shannu"
    def setDetails(self):
        self.__name="kiran"

obj=Demo()
print(obj.__dict__)
print(obj._Demo__name)
obj.setDetails.vv()
print(obj.__dict__)
print(obj._Demo__name)

