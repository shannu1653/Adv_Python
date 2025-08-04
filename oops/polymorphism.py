#Polymorphsim:Functions with same name bahaving differently in different classes

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


#ex2
class SendMsg():
    def send(self, message):
        print(f"sms sent : {message}")
class SendEmail():
    def send(self, message):
        print(f"Email sent: {message}")
class Notifier():
    def send(self, message):
        print(f"Notifier send : {message}")

def sendMsg(sender, message):
    sender.send(message)

sendMsg(SendMsg(),'Hi your OTP is 2343')
sendMsg(SendEmail(),'congratulation your are hire')
sendMsg(Notifier(),'succefully created 10xxxxx your bankAccount')

