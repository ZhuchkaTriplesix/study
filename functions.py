import math
import random
import sys
import time

import introduction
from interface import menu


def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


def list_of_random_numbers():
    time_before = time.perf_counter()
    [random.randint(0, 2000000) for i in range(2000000)]
    time_after = time.perf_counter()
    print("\nTime spend:", round(time_after - time_before, 2), "sec")
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


def factorial_recursive(num):
    if num == 1:
        return num
    elif num < 0:
        print("Incorrect value")
    else:
        return num * factorial_recursive(num - 1)


def calculator(first_number, second_number, sign):
    first_number_check = introduction.input_check_number(first_number)
    second_number_check = introduction.input_check_number(second_number)
    if first_number_check or second_number_check:
        match sign:
            case "+":
                return float(first_number) + float(second_number)
            case "-":
                return float(first_number) - float(second_number)
            case "/":
                return float(first_number) / float(second_number)
            case "//":
                return float(first_number) // float(second_number)
            case "%":
                return float(first_number) % float(second_number)
            case "*":
                return float(first_number) * float(second_number)
            case _:
                print("Invalid input")
                introduction.repeat_input()


items = []


def flexible_list(key):
    match key:
        case "1":
            add_items()
        case "2":
            edit_items()
        case "3":
            remove_items()
        case "4":
            print_items()
        case "5":
            menu.menu_list()
        case "6":
            sys.exit()


def delay_and_back():
    time.sleep(0.5)
    menu.menu_flexible_list()


def add_items():
    print("\nEnter the content which you want to add:")
    element = str(input())
    items.append(element)
    print("\nElement was added successfully!")
    delay_and_back()


def edit_items():
    length = len(items)
    if length != 0:
        print(f"\nEnter the index of element which you want to edit (from 0 to {length - 1}): \n")
        element_index = str(input())
        if element_index.isdigit() and (length > int(element_index) >= 0):
            print("\nEnter the content of element")
            element_content = str(input())
            items[int(element_index)] = element_content
            print("\nElement was edited successfully!")
            delay_and_back()
        else:
            print("\nInvalid input")
            delay_and_back()
    else:
        print("\nNo items to edit")
        delay_and_back()


def remove_items():
    length = len(items)
    if length != 0:
        print(f"\nEnter the index of element which you want to remove (from 0 to {length - 1}): \n")
        element_index = str(input())
        if element_index.isdigit() and (length > int(element_index) >= 0):
            items.pop(int(element_index))
            print("\nElement was removed successfully!")
            delay_and_back()
        else:
            print("\nInvalid input")
            delay_and_back()
    else:
        print("\nNo items to remove")
        delay_and_back()


def print_items():
    print(f"\n{items}")
    delay_and_back()
