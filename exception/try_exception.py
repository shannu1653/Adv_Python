#ModulNOtFounEroor
try:
    import srebd
except ModuleNotFoundError as a:
    print("module not found :",a)

#we use only run time errors only in python
#avoid stuck in our programm,avoid crash our websites
#use in real time projects in our code


try: 
    for i in range(10):
        print(i)
except SyntaxError:
    print("give valid suntax") #Syntax error can't handle beacuse it occurs before runtime
#so finnaly exception handling works only runtime errors

try:
    # Code that may cause an error
    num = int(input("Enter a number: "))
    print(10 / num)

except ZeroDivisionError as error:
    print("You cannot divide by zero!",error)

except ValueError:
    print("Invalid input! Please enter a number.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("Execution finished.")


try:
    x=int(input('enter x value :'))
    y=int(input('enter y value :'))
    print(x+y+z)
except TypeError as error:
    print('division can be done only b/w numbers',error)
except ZeroDivisionError as error:
    print('we cant divide any number with 0',error)
except ValueError as error:
    print('input should be a number',error)
except NameError as error:
    print('variable is not defined',error)
except IndentationError:
    print('indentation is not proper')
except:
     print('something went wrong')
finally:
    print('code execution is completed ')

# 7️⃣ Raising Your Own Exception

# You can create your own exceptions using raise:
age = int(input("Enter your age: "))
if age < 18:
    raise Exception("Age must be 18 or above.")
else:
    print("You are eligible.")
print('hello')
