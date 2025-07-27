class Instructor:
    followers=0 #CLASS OBJECT VARIBLE
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self,subject_name):
        print(f"hi {self.name} , youre from {self.address} a in am teaching {subject_name}")
    def updated_followers(self,follower_name):
        self.followers +=1
instructor_1=Instructor('shannu','nemalam')
print(instructor_1.name,instructor_1.followers)
instructor_1.display('python')
instructor_1.updated_followers('hello')
print(instructor_1.followers)
instructor_2=Instructor('shannu','ram')
instructor_2.updated_followers('rama')
print(instructor_2.followers)