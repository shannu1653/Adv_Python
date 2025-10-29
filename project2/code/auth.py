import json
import random


def signup():
    with open("../data/data.json",'r') as f:
        username=input("Enter username : ")
        email=input("Enter Email : ")
        password=input("Enter Password : ")
        user_id=generateuserid(username)
        print(f"your userid is {user_id}\nyour password is {password}")
        user_info={
            "user_id" : user_id,
            "username" : username,
            "email" : email,
            "password" : password
        }
        users=json.load(f)
        users['users'].append(user_info)
    with open("../data/data.json",'w') as f:
        json.dump(users,f)
        print("signup successfully")

def generateuserid(username):
    user_id=username[0:3]+str(random.randint(9999,99999))
    return user_id

def login():
    user_id=input("Enter Userid :  ")
    password=input("Enter Password : ")
    with open("../data/data.json",'r') as f:
        data=json.load(f)
        users=data["users"]
        found=False  
    for user in users:
        if user["user_id"] == user_id:
            found = True
            if user["password"] == password:
                print("Login successful ")
            else:
                print("Password is incorrect ")
            break
    if not found:
        print("User ID is incorrect ")
    
    

def start():
    ip=int(input('Enter your choice : '))
    if ip==1:
        signup()
    elif ip==2:
        login()
    else:
        print('invalid input')