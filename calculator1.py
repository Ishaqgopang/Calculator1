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