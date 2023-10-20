import math
import random
import introduction


def input_check_numbers(num):
    float_check_input = float_check(num)
    int_check_input = num.isdigit()
    if float_check_input or int_check_input:
        return num
    else:
        print("Input error")
        introduction.repeat_input()


def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


def list_of_random_numbers():
    items = [random.randint(0, 2000000) for i in range(2000000)]
    print(items)
    introduction.repeat_input()


def quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("x1 = ", x1)
        print("x2 = ", x2)
        introduction.repeat_input()
    elif discriminant == 0:
        x = -b / (2 * a)
        print("x = ", x)
        introduction.repeat_input()
    else:
        print("No roots")
        introduction.repeat_input()


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


def calculator(first_number, second_number, sign):
    first_number_check = input_check_numbers(first_number)
    second_number_check = input_check_numbers(second_number)
    if first_number_check or second_number_check:
        if sign == "+":
            result = float(first_number) + float(second_number)
            return result
        elif sign == "-":
            result = float(first_number) - float(second_number)
            return result
        elif sign == "*":
            result = float(first_number) * float(second_number)
            return result
        elif sign == "/":
            result = float(first_number) / float(second_number)
            return result
        elif sign == "//":
            result = float(first_number) // float(second_number)
            return result
        elif sign == "%":
            result = float(first_number) % float(second_number)
            return result
