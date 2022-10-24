import math
import random
import sys
import time
import constants
import introduction
from interface import menu
from numba import njit


def menu_help_output():
    print("\nYou can make a choice by using numbers 1, 2, 3..."
          "\nPress '1' to return to main menu.\nPress '2' to exit the program.")


def is_palindrome(string) -> bool:
    reversed_string = string[::-1]
    return string == reversed_string


@njit
def list_create():
    [random.randint(0, 2000000) for i in range(2000000)]


def list_of_random_numbers():
    time_before = time.perf_counter()
    list_create()
    time_after = time.perf_counter()
    res = time_after - time_before
    print(f"\nTime spent: {res:.2f} sec")
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
        print(f"\nResult: x = {x}")
    else:
        print("\nResult: No roots")


def factorial_recursive(num: int) -> int:
    return num if num == 1 else "Incorrect value" if num < 0 else (num * factorial_recursive(num - 1))


def calculator(first_number, second_number, key):
    for i in (first_number, second_number):
        introduction.input_check_number(i)
    first_number, second_number = map(float, [first_number, second_number])
    match key:
        case "1":
            return first_number + second_number
        case "2":
            return first_number - second_number
        case "3":
            return first_number * second_number
        case "4":
            try:
                return first_number / second_number
            except ZeroDivisionError:
                return "Division by zero is not allowed"
        case "5":
            try:
                return first_number // second_number
            except ZeroDivisionError:
                return "Division by zero is not allowed"
        case "6":
            try:
                return first_number % second_number
            except ZeroDivisionError:
                return "Division by zero is not allowed"
        case "7":
            menu.menu_numbers()
        case "8":
            sys.exit()
        case _:
            print("\nInvalid input")
    menu.menu_numbers()


items = []
queue = []

for i in range(10):
    items.append("Element" + str(i))
    queue.append("Element" + str(i))


def flexible_list(key):
    is_list = True
    match key:
        case "1":
            add_items_to_list()
        case "2":
            edit_items_in_list()
        case "3":
            remove_items_from_list()
        case "4":
            print_items(is_list)
        case "5":
            menu.menu_list()
        case "6":
            sys.exit()
        case _:
            print("\nInvalid input")


def add_or_remove_check(len_before, len_after, is_add):
    if is_add:
        print("Element was added successfully!") if len_after != len_before else print("Something went wrong :c")
    else:
        print("Element was removed successfully!") if len_after != len_before else print("Something went wrong :c")


def delay_and_back(is_list):
    time.sleep(constants.delay)
    menu.menu_flexible_list() if is_list else menu.menu_flexible_queue()


def add_items_to_list():
    is_list = True
    is_add = True
    len_before = len(items)
    print("\nEnter the content which you want to add:")
    element = str(input())
    items.append(element)
    len_after = len(items)
    add_or_remove_check(len_before, len_after, is_add)
    delay_and_back(is_list)


def edit_items_in_list():
    is_list = True
    length = len(items)
    if length != 0:
        print(f"\nEnter the index of element which you want to edit (from 0 to {length - 1}): \n")
        element_index = str(input())
        if element_index.isdigit():
            if length > int(element_index) >= 0:
                print("\nEnter the content of element")
                element_content = str(input())
                items[int(element_index)] = element_content
                print("\nElement was edited successfully!")
                delay_and_back(is_list)
            else:
                print("\nInvalid index")
        else:
            print("\nInvalid input")
            delay_and_back(is_list)
    else:
        print("\nNo items to edit")
        delay_and_back(is_list)


def remove_items_from_list():
    is_list = True
    is_add = False
    len_before = len(items)
    if len_before != 0:
        print(f"\nEnter the index of element which you want to remove (from 0 to {len_before - 1}): \n")
        element_index = str(input())
        if element_index.isdigit():
            if len_before > int(element_index) >= 0:
                items.pop(int(element_index))
                len_after = len(items)
                add_or_remove_check(len_before, len_after, is_add)
                delay_and_back(is_list)
            else:
                print("\nInvalid index")
        else:
            print("\nInvalid input")
            delay_and_back(is_list)
    else:
        print("\nNo items to remove")
        delay_and_back(is_list)


def print_items(is_list):
    print(f"\n{items}") if is_list else print(f"\n{queue}")
    delay_and_back(is_list)


def flexible_queue(key):
    is_list = False
    match key:
        case "1":
            menu.menu_add_items_queue()
        case "2":
            edit_items_in_queue()
        case "3":
            remove_items_from_queue()
        case "4":
            print_items(is_list)
        case "5":
            menu.menu_list()
        case "6":
            sys.exit()


def add_queue(key):
    is_start = True
    match key:
        case "1":
            add_items_to_queue(is_start)
        case "2":
            is_start = False
            add_items_to_queue(is_start)
        case _:
            print("Invalid input")


def add_items_to_queue(is_start):
    is_list = False
    is_add = True
    len_before = len(queue)
    print("\nEnter the content which you want to add:")
    element = str(input())
    queue.appendleft(element) if is_start else queue.append(element)
    len_after = len(queue)
    add_or_remove_check(len_before, len_after, is_add)
    delay_and_back(is_list)


def edit_items_in_queue():
    is_list = False


def remove_items_from_queue():
    is_list = False
    is_add = False
    len_before = len(queue)
    if len_before != 0:
        print(f"\nEnter the index of element which you want to remove (from 0 to {len_before - 1}): \n")
        element_index = str(input())
        if element_index.isdigit() and (len_before > int(element_index)):
            if int(element_index) == (len_before - 1):  # If equal last index
                queue.pop()
                len_after = len(queue)
                add_or_remove_check(len_before, len_after, is_add)
                delay_and_back(is_list)
            elif int(element_index) == 0:
                queue.popleft()
                len_after = len(queue)
                add_or_remove_check(len_before, len_after, is_add)
                delay_and_back(is_list)
            else:
                "туц туц туц, а бебра тутутутуц"

        else:
            print("\nInvalid input")
            delay_and_back(is_list)
    else:
        print("\nNo items to remove")
        delay_and_back(is_list)
