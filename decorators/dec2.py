#  Decorators Practice 
# (Decorators are higher-order functions)

# 1️. Basic Decorator Example
def check_msg(func):
    def wrapper():
        print("Before the original function")
        func()
        print("After the original function")
    return wrapper
@check_msg
def say_hello():
    print("Hello, World!")
@check_msg
def good_evening():
    print("Good Evening!")

good_evening()


# 2️. Decorator to Check Integer Inputs
def check_int(func):
    def wrapper(a, b):
        print(type(a), type(b))
        if not isinstance(a, int) or not isinstance(b, int):
            return "Invalid inputs — please provide integers only."
        return func(a, b)
    return wrapper
@check_int
def add(a, b):
    return a + b
print(add(77, 2))


# 3. Decorator to Check String Input
def check_str(func):
    def wrapper(name):
        if not isinstance(name, str):
            return "Invalid name — must be a string."
        return func(name)
    return wrapper
@check_str
def greet(name):
    return f"Hello, {name}!"
print(greet(1233))


# 4️. Decorator to Block Function When Zero is in Arguments
def has_zero(func):
    def wrapper(*args):
        if 0 in args:
            return func("Zero found! Function skipped.")
        return func(*args)
    return wrapper
@has_zero
def numbers(*args):
    return args
print(numbers(1, 2, 3, 0, 4, 5))


# 5️. Decorator to Filter Specific Names
def hate_names(func):
    def wrapper(*args):
        if 'babar' in args:
            return func("Please remove 'babar' — I don't like them ")
        return func(*args)
    return wrapper
@hate_names
def cricket_players(*args):
    return args
print(cricket_players('virat', 'dhoni', 'babar', 'shannu'))
