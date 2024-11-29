# def add (x,y):
#     return x + y
# def subtract (x,y):
#     return x - y
# def multiply (x,y):
#     return x * y
# def divide (x,y):
#     return x / y

# choice = input("chose option ('+' , '-' , '*' , '/') :" )
# first_number = int(input("Enter First Number: "))
# second_number = int(input("Enter Second Number: "))

# if choice == "+":
#     print(add(first_number, second_number))
# elif choice == "-":
#     print(subtract(first_number, second_number))
# elif choice == "*":
#     print(multiply(first_number, second_number))
# else:
#     print(divide(first_number, second_number))


# def add(x, y):
#     """This function adds two numbers."""
#     return x + y

# def subtract(x, y):
#     """This function subtracts two numbers."""
#     return x - y

# def multiply(x, y):
#     """This function multiplies two numbers."""
#     return x * y

# def divide(x, y):
#     """This function divides two numbers and handles division by zero."""
#     return x /   y

# def mod(x, y):
#     """This function calculates the modulus of two numbers."""
#     return x % y

# def exponent(x, y):
#     """This function raises x to the power of y."""
#     return x ** y


# first_value = int(input( "write your first number : "))
# second_value = int(input( "write your second number : "))
# choice = input("choice what do you want to do : ( '+ , - , * , / , % , **'  ) : ")
# if choice == "+":
#     print(add(first_value,second_value))
# elif choice == "*":
#     print(multiply(first_value , second_value))
# elif choice == "-":
#     print(subtract(first_value, second_value))
# elif choice == "/":
#     print(divide(first_value, second_value))
# elif choice == "%":
#     print(mod(first_value, second_value))
# elif choice == "**":
#     print(exponent(first_value, second_value))
# else :
#     print("invalid choice")

# # print("ishaq")







# def add(x,y):
#     # add two numbeers
#     return x + y
# def subtract (x,y):
#     # subtract two numbers
#     return x - y
# def multiply (x,y):
#     # multiply two numbers
#     return x * y
# def divide (x,y):
#     # divide two numbers
#     return x / y
# choice = input("action : ('+ , '-' , '*' , '/') : ")
# first_number = int(input("Enter Number: "))
# second_number = int(input("Enter Number: "))
# # choice = input("action : ( '+ , - , * , /'  ) : ")

# if choice == "+":
#     print(add(first_number, second_number))
# elif choice == "-":
#     print(subtract(first_number, second_number))
# elif choice == "*":
#     print(multiply(first_number, second_number))
# else:
#     print(divide(first_number, second_number))

















# def add (x , y):
# # adding tow numberss
#     return x + y

# def subtract (x , y):
# # subtracting two nubers
#     return x - y

# def multiply (x , y):
# # multiplying two numbers
#     return x * y

# def divide (x , y):
# # dividing two numbers
#     return x / y

# choice = input("chose '+' , '-' , '*' , '/'")
# number_1 = int(input("Enter First Number: "))
# number_2 = int(input("Enter Second Number: "))

# if choice == "+":
#     print(add(number_1, number_2))
# elif choice == "-":
#     print(subtract(number_1, number_2))
# elif choice == "*":
#     print(multiply(number_1, number_2))
# else:
#     print(divide(number_1, number_2))

# except ValueError:
#     print("Invalid input. Please enter valid numbers.")
# except ZeroDivisionError:
#     print("Cannot divide by zero.")


def add(x , y):
    return x + y
def subtract (x , y):
    return x - y
def multiply(x , y):
    return x * y
def divide(x , y):
    return x / y
choice = input("Choose action '+' , '-' , '*' , '/':  ")
try:

    first_number = int(input("Enter Firstnumber: "))
    second_number = int(input("Enter Second Number: "))


    if choice == "+":
        print(add(first_number, second_number))
    elif choice == "-":
        print(subtract(first_number, second_number))
    elif choice == "*":
        print(multiply(first_number, second_number))
    elif choice == "/":
        print(divide(first_number, second_number))
    else:
        print("invalid choice")
except ValueError:
    print("invalid choice. Plese enter choice again")
except ZeroDivisionError:
    print("can't divide by zero")