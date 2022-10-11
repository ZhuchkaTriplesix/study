import math
import random


def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


def list_of_random_numbers():
    items = [random.randint(0, 2000000) for i in range(2000000)]
    print(items)


def quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("x1 = ", x1)
        print("x2 = ", x2)
    elif discriminant == 0:
        x = -b / (2 * a)
        print("x = ", x)
    else:
        print("No roots")


def float_check(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def factorial_recursive(num):
    if num == 1:
        return num
    elif num < 0:
        print("Incorrect value")
    else:
        return num * factorial_recursive(num - 1)


def calculator(num1, num2, sign):
    num_check1 = float_check(num1)
    num_check2 = num1.isdigit()
    if num_check1 or num_check2:
        num_check1 = float_check(num2)
        num_check2 = num2.isdigit()
        if num_check1 or num_check2:
            if sign == "+":
                result = float(num1) + float(num2)
                return result
            elif sign == "-":
                result = float(num1) - float(num2)
                return result
            elif sign == "*":
                result = float(num1) * float(num2)
                return result
            elif sign == "/":
                result = float(num1) / float(num2)
                return result
            elif sign == "//":
                result = float(num1) // float(num2)
                return result
            elif sign == "%":
                result = float(num1) % float(num2)
                return result
        else:
            print("Invalid second input")
    else:
        print("Invalid first input")
