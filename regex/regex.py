# import re
# ip='hello world'
# regex=r'hello'
# op=re.match(regex,ip)
# print(op)

# # search --> returns the matched object if it is found anywhere in the given string
# # if not foune return none
# # onec it found the maatch then stops searching
# ip='hello world'
# regex=r'world'
# op=re.search(regex,ip)
# print(op)


# ip='hello world world world world'
# regex=r'world'
# op=re.findall(regex,ip)
# print(op)

# ip='c.t'
# op=re.search(ip,'culrcatculet')
# print(op)

# ip='c.t'
# op=re.match(ip,'culrcatculet')
# print(op)


# ip='p.t'
# op=re.search(ip,'okdpotivalidplt')
# if(op):
#     print('valid')
# else:
#     print('not valid')
# #with the help of this dot only check 3 letters only not more than 3 letters



# # example1 for icic ifsc code
# regex1=r'^icic'
# op=re.match(regex1,'icic012324')
# if(op):
#     print('valid ifsc code')
# else:
#     print('invalid ifsc code')

# #example2 for sbi ifsc code--sbi
# regex1=r'^sbi'
# op=re.match(regex1,'sbi012324')
# if(op):
#     print('valid ifsc code')
# else:
#     print('invalid ifsc code')

# #example for $
# regex1=r'gmail.com$'
# op=re.search(regex1,'shanmukha@gmail.com')
# if(op):
#     print('valid email')
# else:
#     print('invalid email ')

# #example for \d
# regex1=r'\d'
# op=re.match(regex1,'012324')
# if(op):
#     print('valid input')
# else:
#     print('invalid input')

# regex1=r'\d'
# op=re.search(regex1,'kjnkk012324')
# if(op):
#     print('valid input')
# else:
#     print('invalid input')


# regex1=r'\w'
# op=re.search(regex1,'@$%$%')
# if(op):
#     print('valid input')
# else:
#     print('invalid input')

# regex1=r'\s'
# op=re.search(regex1,'012324 uh')
# if(op):
#     print('valid input')
# else:
#     print('invalid input')


# regex='[abc]'
# op=re.search(regex,'012324abc')
# if(op):
#     print('valid input')
# else:
#     print('invalid input')


# regex1=r'[aeiou]'
# op=re.match(regex1,'shanmukha')
# if(op):
#     print('vowels are present')
# else:
#     print('vowels are not present')


# regex1=r'[e-i]'
# regex1=r'[A-Z]'
# regex1=r'[^shanmukha]' #this will not allow a string with pure vowels
# op=re.search(regex1,'alove')
# if(op):
#     print('valid')
# else:
#     print('invalid')
# regex = r'^[A-Z]{5}[0-9]{4}[A-Z]$'

# import re
# #accept a input when it have lenght more than 5
# # regex1='\w{5,}'
# regex1=r"^\w{5,10}$"
# op=re.search(regex1,"jasvasnkhj")
# if(op):
#     print('valid')
# else:
#     print('invalid')


# regex1=r"^[A-Z]{5}[0-9]{4}[A-z]$"
# pan=input("Enter your pancard number : ").upper()
# op=re.search(regex1,pan)
# if(op):
#     print('valid Pan')
# else:
#     print('invalid Pan')


# regex1=r'^[hdfc]{4}[\d]$'
# op=re.match(regex1,'hdfc012324')
# if(op):
#     print('valid input')
# else:
#     print('invalid input')
import re




#it checks the valid sequences
# regex1=r'(a-f)'
# op=re.search(regex1,'hbhja-fjhjh')
# if(op):
#     print('valid input')
# else:
#     print('invalid input')


# {5} -->should have exactly length
# {5,}-->min length is 5
# {5,10}-->min:5 and max is 10

# regex=r"^(\+91)\s[6-9]{1}[0-9]{9}$"
# mobile=input("Enter your mobile number : ")
# op=re.search(regex,mobile)
# if(op):
#     print('valid mobile')
# else:
#     print('invalid mobile')

# regex=r"^[1-9]{1}[0-9]{5}$"
# pincode=input("Enter pincode : ")
# op=re.search(regex,pincode)
# if(op):
#     print('valid pincode')
# else:
#     print('invalid code')


regex=r"^[1-9]{1}[0-9]{3}-(0[1-9]|1[0-2]){2}-(0[1-9]|1[1-{2}$"
date=input("Enter data : ")
op=re.search(regex,date)
if(op):
    print('valid date')
else:
    print('invalid date')


