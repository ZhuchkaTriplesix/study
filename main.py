<<<<<<< HEAD
import math


def floatCheck(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def factorialRecursive(n):
    if n == 1:
        return n
    else:
        return n * factorialRecursive(n - 1)
=======
import functions
>>>>>>> develop


def convert():
    start = input("Choose one: \n1. Calc\n2. Factorial \n")
    if start not in ("1", "2"):
        print("Invalid argument")
    else:
        if start == "1":
            sign = input("Choose the operator (+, -, *, /, //, %): ")
            if sign not in ("+", "-", "*", "%", "/", "//"):
                print("Invalid character")
            else:
                num1 = input("First number: ")
                num2 = input("Second number: ")
                print(functions.calculator(num1, num2, sign))
        elif start == "2":
            num = input("Input your number: \n")
            print(functions.factorial_recursive(int(num)))

convert()
while True:
    flag = input("One more time? [y/n]: ")

    if flag == 'y':
        convert()
    else:
        break
