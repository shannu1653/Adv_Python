#acquiring methods and attribute from already defined class into newly created -- inheritance
#creating new class from already created class

#types of inheritance
'''1.single inheritance #if u derive one child class from single parent class then it is a single inheritance
2.multiple   --> if u derive one child class from more than one parent class then it is a multiple inheritance inheritance
3.multilevel  "
4.hierarical   "
5.hybrid'''

# #single inheritance

class Parent:
    def Pmethod(self):
        print('i am a method from parent')
    def Pmethod2(self):
        print("i am a second method from parent")
    

class Child(Parent):
    def Cmethod(a):
        print('i am a method from child')
        super().Pmethod2() #calling method from super class using super()
obj1=Child()
obj1.Pmethod()
obj1.Cmethod()


class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
    def Method(self):
        print('All the Best u can do it please try it one\ce')
class Student(User):
    def __init__(self, name, email,enrolledcourses):
        super().__init__(name, email)
        self.enrolledcourses=enrolledcourses
    def getCourses(self):
        print(f"{self.name} is learning {self.enrolledcourses}")
    def removeCourses(self,coursename):
        self.enrolledcourses.remove(coursename)
        self.getCourses()
    def addCourses(self,course):
        self.enrolledcourses.append(course)
        self.getCourses()

class Trainer(User):
    def __init__(self,name,email,courses_training):
        super().__init__(name,email)
        self.courser_training=courses_training
    def Courses(self):
        print(f"{self.name} is trainer to {self.courser_training} ")
    def removecourse(self,coursename):
        self.courser_training.remove(coursename)
        self.Courses()
        super().Method()

student_object=Student("shanmukha","shanmukha@gmail.com",['html','python','js'])
student_object.getCourses()
student_object.removeCourses('html')
student_object.addCourses('sql')
Trainer_object=Trainer('shannu',"shannu@gmail.com",['python','html','frontend'])
Trainer_object.Courses()
Trainer_object.removecourse("python")

#ovveriding
class Human:
    def __init__(self,num_heart):
        self.num_eyse=2
        self.num_nose=1
        self.num_heart=num_heart
    def eat(self):
        print('I can eat')
    def work(self):
        print("I can work")
class male(Human):
    def __init__(self,name,heart):
        print('hi ra chinna')
        super().__init__(heart)
        self.name=name
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code")
        super().work()
    def display(self):
        print(f'hi, I am {self.name} and i have {self.num_heart} heart')
male_1=male("shannu",1)
#male_1.flirt()
#male_1.work()
print(male_1.num_nose)
male_1.display()

