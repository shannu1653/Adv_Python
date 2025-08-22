#Banking_appication
import random
class Bank:
    total_user=[]   
    def creat_new_bankaccount(self):
        user_details={}
        data=random.randint(100000000000,999999999999)
        user_details['name']=input("Enter your name : ")
        user_details['Mobile']=input('Enter your mobile number : ')
        user_details['Aadhar_no']=input('Enter your aadhar no. :')
        user_details['ifsc code ']='ANDB056535'
        user_details['account_no']=data
        n1=input('Select type od account saving/zero :').lower()
        while True:
            if n1=='saving':
                n2=int(input('Deposite 1000 rupees....'))
                if n2==1000:
                    user_details['Balance']=n2
                    break
                else:
                    print("Deposite 1000 rupees.....")
            elif n1=='zero':
                n3=int(input('Deposite 500 rupees...'))
                if n3==500:
                    user_details['Balance']=n3
                    break
                else:
                    print("Deposite 500 rupees.....")
        
        Bank.total_user.append(user_details)
        print(Bank.total_user)
        print('Your BankAccount Successfully Created')    
        
    def deposite(self):
        print('============Deposite Form =============')
        name1=input('Enter your name :').lower()
        account_num=int(input('Enter your Account number : '))
        for user in Bank.total_user:
            if name1==user['name'] and account_num==user['account_no']:
                deposite_money=int(input("Enter Deposite money : "))
                user['Balance']=user['Balance']+deposite_money
                print("Deposit successful!")
                print("Updated Balance:", user['Balance'])
                break
            else:
                print('Deposite cancelld please check your name and password')
    def withdrawl(self):
        print('========== withdrawl Form =========')
        name1=input('Enter your name :').lower()
        account_num=int(input('Enter your Account number : '))
        for user in Bank.total_user:
            if name1==user['name'] and account_num==user['account_no']:
                withdrawl_money=int(input("Enter Withrawl money : "))
                user['Balance']=user['Balance']-withdrawl_money
                print("Withrawl successful!")
                print("Updated Balance:", user['Balance'])
                break
            else:
                print('withdrawl cancelld please check your name and password')

obj=Bank()
obj.creat_new_bankaccount()
obj.deposite()
obj.withdrawl()

    

