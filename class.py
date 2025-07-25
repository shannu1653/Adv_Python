# #class SamplePersion:
#       ---
#       ---

#same object

class Person:
    name='shannu'
    age=24
    gender='male'
obj1=Person()
obj2=Person()
print(obj1)
print(obj2)
print(obj1.name)
print(obj2.name)

#updating value in obj1
obj1.name="shannu penta"
print(obj1.name)#reflecting only in obj1
print(obj2.name)#does not refecting to ojject2
print(Person().name)#does not  reflcet to persion class also

# class Person:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender

# obj_rakesh=Person("Rakesh",24,"male")
# Obj_kiran=Person("kiran",24,"male")

# print(obj_rakesh.name)
# print(Obj_kiran.age)


# class SocialMedia:
#     def __init__(self,name,pltform):
#         self.name=name
#         self.pltform=pltform
# instagram=SocialMedia("istagram","online")
# print(instagram.name)


# #dynamic applications 
# class Application:
#     def __init__(app,name,purpose,logocolor):
#         app.name=name
#         app.purpose=purpose
#         app.logocolor=logocolor
# insta=Application("instagram","social Media","pink")
# youtube=Application("youtube","reels","blue")
# print(insta.name,insta.purpose,insta.logocolor)
# print(youtube.name,youtube.purpose,youtube.logocolor)
        

# #static        
# class Application:
#     def __init__(app,name,purpose,logocolor):
#         app.name=name
#         app.purpose=purpose
#         app.logocolor=logocolor
#     def purpose(self):
#         print("socail media purpose")
# insta=Application("instagram","social Media","pink")
# insta.purpose


# #dynamic
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
# youtube=Application("Facebook","entertainment","blue")
# youtube.purpose("youtube","reels")
# print(youtube.name,youtube.purpose1,youtube.logocolor)

