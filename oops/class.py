# #creating a class
class Instructior:
    def __init__(self,name,age):
        self.Fname=name
        self.Fage=age
        self.followers=0
        print(f"my name is {self.Fname}")
Obj_varaible=Instructior("shannu",27)
print(Obj_varaible)
# print (Obj_varaible.followers)




# #exercise Creating class and object -CarDesign
# class CarDesign:
#     name="toyato"
#     number=22324
# car1=CarDesign()
# car2=CarDesign()
# print(car1.name)
# print(car2.number)

# #how to add attribite to object
# car1.age=23
# car1.name1="bulero"
# print(car1.age)
# print(car1.name1)






# # class Sample:
# #     name="shannu"
# #     age=27
# #     gender='male'
# # obj1=Sample()
# # obj2=Sample()
# # print(obj1)
# # print(obj2)
# # print(obj1.name)
# # print(obj2.gender)
# # print(Sample.age)

# # #updating a obj1 value
# # obj1.name="prashanth"
# # print(obj1.name)#reflecting only in obj1
# # print(obj2.name)#does not reflecting only in obj2
# # print(Sample().name)#does not  reflcet to persion class also
# # print(Sample.name)#does not  reflcet to persion class also

# # #dynamic objects
# # class Person:
# #     def __init__(self,name,age,gender):
# #         self.name=name
# #         self.gender=gender
# #         self.age=age
# # obj_shannu=Person("shanmukha",23,'Male')
# # obj_naveen=Person('naveen',23,'male')
# # print(obj_naveen.name,obj_naveen.age,obj_naveen.gender)
# # print(obj_shannu.name,obj_shannu.age,obj_shannu.gender)


# # #static        
# class Application:
#     def __init__(app,name,purpose1,logocolor):
#         app.name=name
#         app.purpose1=purpose1
#         app.logocolor=logocolor
#     def purpose(self):
#         print("socail media is nice")
# insta=Application("instagram","social Media","pink")
# print(insta.name,insta.purpose1,insta.logocolor)
# insta.purpose()


# # #dynamic
# class Application:
#     def __init__(app,name,purpose1,logocolor):
#         app.name=name
#         app.purpose1=purpose1
#         app.logocolor=logocolor
#     def purpose(self,app_name,purpose):
#         print(f"{app_name} is used for {purpose}")
# insta=Application("instagram","social Media","pink")
# print(insta.name,insta.purpose1,insta.logocolor)
# insta.purpose("instagram","social Media")
# #for youtube
# facebook=Application("Facebook","entertainment","red")
# facebook.purpose("facebook","reels")
# print(facebook.name,facebook.purpose1,facebook.logocolor)
