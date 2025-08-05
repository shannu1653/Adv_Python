import random
class Bank:
    def creat_new_bankaccount(self):
        user_details={}
        data=random.random(100000000000,999999999999)
        user_details['name']=input("Enter your name : ")
        user_details['Mobile']=input('Enter your mobile number : ')
        user_details['Aadhar_no']=input('Enter your aadhar no. :')
        user_details['ifsc code ']='ANDB056535'
        user_details['account_no']=data

        ni=input('Select type od account saving/zero :').lower()
        

