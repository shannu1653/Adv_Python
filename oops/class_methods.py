# class Instructor:
#     followers=0 #CLASS OBJECT VARIBLE
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#     def display(self,subject_name):
#         print(f"hi {self.name} , youre from {self.address} a in am teaching {subject_name}")
#     def updated_followers(self,follower_name):
#         self.followers +=1
# instructor_1=Instructor('shannu','nemalam')
# print(instructor_1.name,instructor_1.followers)
# instructor_1.display('python')
# instructor_1.updated_followers('hello')
# print(instructor_1.followers)
# instructor_2=Instructor('shannu','ram')
# instructor_2.updated_followers('rama')
# print(instructor_2.followers)

# #area and circumeference of a circle
# class Circle:
#     pi=3.14
#     def __init__(self,radius=4):
#        self.radius=radius
#        self.area=Circle.pi * radius*radius
#     # def area(self):
#     #     return (f"{self.pi*self.radius**2}")
#     def cicumference(self):
#         return (f"{2*Circle.pi*self.radius}")
# # area_1=Circle(5)
# cicumeference_1=Circle(4)
# # print(area_1.area())
# print(cicumeference_1.cicumference())
# area_1=Circle()
# print(area_1.area)

# for i in range(1,4):
#     for j in range(1 ,i+1):
#         if (i+j)%2==0:
#             print("*",end=" ")
#             print()
        
#         else:
#             print("#",end=" ")
#             print()
        

class BankAccount:
    def __init__(self,name,email,ph,balance):
        self.name=name
        self.email=email
        self.ph=ph
        self.balance=balance
    def deposite(self,d_mat):
        self.balance+=d_mat
    def withdrawl(self,w_mat):
        self.balance-=w_mat
    def checkbalance(self):
        print(self.balance)
harish=BankAccount("Harish",'harish@gmail.com',453245234,10000)
harish.checkbalance()
harish.deposite(2000)
harish.checkbalance()
harish.withdrawl(10000)
harish.checkbalance()

       