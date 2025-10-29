#decoraotr:
#are also higher order function
# def check_meg(func):
#     def wrapper():
#         print("before original function")
#         func()
#         print('after the original function')
#     return wrapper


# @check_meg  #using decorator on a function
# def say_hello():
#     print('hello world')
# # say_hello()



# @check_meg
# def good_evng():
#     print("good evening")
# good_evng()


# def check_int(fun):
#     def wrapper(a,b):
#         print(type(a),type(b))
#         # if type(a)!=int or type(b)!=int:

#         if  not isinstance(a,int) or not isinstance(b,int):
#             return "invalid inputs"
#         res=fun(a,b)  #only when there is a return stattement in the original function
#         return res
#     return wrapper


# @check_int
# def sum(a,b):
#     return a+b
# print(sum(77,2))

# print(isinstance("1",str)) #it gives true or false
# print(isinstance(False,bool)) #it gives 

# def check_str(func):
#     def wrapper(n):
#         if not isinstance(n,str):
#             return "invalid name"
#         res=func(n)
#         return res
#     return wrapper

# @check_str
# def str1(name):
#     return 'hello '+ name
# print(str1(1233))



# def has_zero(org):
#     def wrapper(*args):
#         if 0 in args:
#             res=org('zero includes not print')
#             return res
#         else:
#             res=org(*args)
#             return res
#     return wrapper

# @has_zero
# def params(*args):
#     return args
# print(params(1,2,3,4,34,44,4334,0))



def hate_names(org):
    def wrapper(*args):
        if 'babar' in args:
            res=org('please remove babar i hate them')
            return res
        else:
            res=org(*args)
            return res
    return wrapper

@hate_names
def crick_names(*args):
    return args
print(crick_names('virat','shannu','dhoni','shannu','babar'))