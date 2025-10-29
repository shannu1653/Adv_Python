login = False

def check_user(login):
    user_input = input("Enter True or False: ").lower()
    if user_input == "true":
        login = True
    else:
        login = False
    return login

print(check_user(login))
