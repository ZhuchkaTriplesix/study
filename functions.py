import collections
import math
import random
import sys
import time
from collections import *

import constants
import introduction
from interface import menu


def menu_help_output():
    print(" \nYou can make a choice by using numbers 1/2/3..etc..")
    print(" Press '1' to return to main menu.\n3. Press '2' to exit the program")


def is_palindrome(string):
    reversed_string = string[::-1]
    return string == reversed_string


def list_of_random_numbers():
    time_before = time.perf_counter()
    [random.randint(0, 2000000) for i in range(2000000)]
    time_after = time.perf_counter()
    print("\nTime spent:", round(time_after - time_before, 2), "sec")
    time.sleep(constants.delay)
    menu.menu_list()


def quadratic_equation(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"\nResult:\nx1 ={x1}\nx2 ={x2}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print("\nResult: x = ", x)
    else:
        print("\nResult: No roots")


def factorial_recursive(num):
    return num if num == 1 else "Incorrect value" if num < 0 else (num * factorial_recursive(num - 1))


def calculator(first_number, second_number, key):
    first_number_check = introduction.input_check_number(first_number)
    second_number_check = introduction.input_check_number(second_number)
    if first_number_check or second_number_check:
        match key:
            case "1":
                return float(first_number) + float(second_number)
            case "2":
                return float(first_number) - float(second_number)
            case "3":
                return float(first_number) * float(second_number)
            case "4":
                try:
                    return float(first_number) / float(second_number)
                except ZeroDivisionError:
                    return "Division by zero is not allowed"
            case "5":
                try:
                    return float(first_number) // float(second_number)
                except ZeroDivisionError:
                    return "Division by zero is not allowed"
            case "6":
                try:
                    return float(first_number) % float(second_number)
                except ZeroDivisionError:
                    return "Division by zero is not allowed"
            case "7":
                menu.menu_numbers()
            case "8":
                sys.exit()
            case _:
                print("Invalid input")
        menu.menu_numbers()


items = []
queue = collections.deque(["First", "Second"])


def flexible_list(key):
    isList = True
    match key:
        case "1":
            add_items_to_list()
        case "2":
            edit_items_in_list()
        case "3":
            remove_items_from_list()
        case "4":
            print_items(isList)
        case "5":
            menu.menu_list()
        case "6":
            sys.exit()


def add_element_check(len_before, len_after):
    return "Element was added successfully!" if len_after != len_before else "Something went wrong :c"


def remove_element_check(len_before, len_after):
    return "Element was removed successfully!" if len_after != len_before else "Something went wrong :c"


def delay_and_back(isList):
    time.sleep(0.5)
    if isList:
        menu.menu_flexible_list()
    else:
        menu.menu_flexible_queue()


def add_items_to_list():
    isList = True
    print("\nEnter the content which you want to add:")
    element = str(input())
    items.append(element)
    print("\nElement was added successfully!")
    delay_and_back(isList)


def edit_items_in_list():
    isList = True
    length = len(items)
    if length != 0:
        print(f"\nEnter the index of element which you want to edit (from 0 to {length - 1}): \n")
        element_index = str(input())
        if element_index.isdigit() and (length > int(element_index) >= 0):
            print("\nEnter the content of element")
            element_content = str(input())
            items[int(element_index)] = element_content
            print("\nElement was edited successfully!")
            delay_and_back(isList)
        else:
            print("\nInvalid input")
            delay_and_back(isList)
    else:
        print("\nNo items to edit")
        delay_and_back(isList)


def remove_items_from_list():
    isList = True
    length = len(items)
    if length != 0:
        print(f"\nEnter the index of element which you want to remove (from 0 to {length - 1}): \n")
        element_index = str(input())
        if element_index.isdigit() and (length > int(element_index) >= 0):
            items.pop(int(element_index))
            print("\nElement was removed successfully!")
            delay_and_back(isList)
        else:
            print("\nInvalid input")
            delay_and_back(isList)
    else:
        print("\nNo items to remove")
        delay_and_back(isList)


def print_items(isList):
    if isList:
        print(f"\n{items}")
    else:
        print(f"\n{queue}")
    delay_and_back(isList)


def flexible_queue(key):
    isList = False
    match key:
        case "1":
            menu.menu_add_items_queue()
        case "2":
            edit_items_in_queue()
        case "3":
            remove_items_from_queue()
        case "4":
            print_items(isList)
        case "5":
            menu.menu_list()
        case "6":
            sys.exit()


def add_queue(key):
    isStart = True
    match key:
        case "1":
            add_items_to_queue(isStart)
        case "2":
            isStart = False
            add_items_to_queue(isStart)
        case _:
            print("Invalid input")


def add_items_to_queue(isStart):
    isList = False
    len_before = len(queue)
    print("\nEnter the content which you want to add:")
    element = str(input())
    if isStart:
        queue.appendleft(element)
        len_after = len(queue)
        add_element_check(len_before, len_after)
    else:
        queue.append(element)
        len_after = len(queue)
        add_element_check(len_before, len_after)
    delay_and_back(isList)


def edit_items_in_queue():
    isList = False


def remove_items_from_queue():
    isList = False
    len_before = len(queue)
    if len_before != 0:
        print(f"\nEnter the index of element which you want to remove (from 0 to {len_before - 1}): \n")
        element_index = str(input())
        if element_index.isdigit() and (len_before > int(element_index)):
            if int(element_index) == (len_before - 1):  # If equal last index
                queue.pop()
                len_after = len(queue)
                remove_element_check(len_before, len_after)
                delay_and_back(isList)
            elif int(element_index) == 0:
                queue.popleft()
                len_after = len(queue)
                remove_element_check(len_before, len_after)
                delay_and_back(isList)
            else:
                print("туц туц туц, а бебра тутутутуц")

        else:
            print("\nInvalid input")
            delay_and_back(isList)
    else:
        print("\nNo items to remove")
        delay_and_back(isList)
