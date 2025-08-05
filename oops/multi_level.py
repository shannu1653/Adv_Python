# Base class
class Grandfather:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        # Call the constructor of Grandfather
        Grandfather.__init__(self, grandfathername) #or super().__init__(grandfathername)

# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        # Call the constructor of Father
        Father.__init__(self, fathername, grandfathername) #or super().__init__(fathername,grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)

# Driver code
s1 = Son('shannu', 'Ram', 'ramsetty')
print(s1.grandfathername)
s1.print_name()

#example2
class Human:
    can_breath='yes'
    def __init__(self,num_heart):
        print('calling init from human class')
        self.eyes=2
        self.heart=num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can  work")
class Male(Human):
    def __init__(self, name,num_heart):
        print('calling inti from male class ')
        self.name=name
        self.heart=num_heart
    def sleep(self):
        print("I can sleep whole day")
class Boy(Male):
    def __init__(self,heart,name ,can_dance):
        Human.__init__(self,heart)
        Male.__init__(self,name,num_heart=10)
        self.know_dancing=can_dance
    def work(self):
        print('I can code')
boy_1=Boy(1,'rahul',True)
print(boy_1.name)
print(boy_1.heart)
print(boy_1.know_dancing)
print(boy_1.can_breath)
print(Boy.mro())