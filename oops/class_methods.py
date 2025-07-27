class Instructor:
    followers=0 #CLASS OBJECT VARIBLE
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self):
        print(f"hi {self.name} , youre from {self.address}")
instructor_1=Instructor('shannu','nemalam')
print(instructor_1.name,instructor_1.followers)
instructor_1.display()