import time

import constants
import functions
import introduction
from interface import ui


def menu_generate(strings_numbers, list_of_titles):
    for i in range(1, strings_numbers + 1):
        print(str(i) + ".", list_of_titles[i - 1])
        i += 1


def main_menu():
    print("\nMain menu: ")
    list_of_titles = ["Number", "String", "Stack", "Queue", "Tree", "Help", "Quit"]
    menu_generate(len(list_of_titles), list_of_titles)
    ui.main_menu_key()


def menu_numbers():
    print("\nNumber menu:")
    list_of_titles = ["Calculator", "Factorial", "Quadratic equation", "Back", "Quit"]
    menu_generate(len(list_of_titles), list_of_titles)
    ui.menu_number_key()


def menu_strings():
    print("\nString menu:")
    list_of_titles = ["Palindrome", "Back", "Quit"]
    menu_generate(len(list_of_titles), list_of_titles)
    ui.menu_string_key()


def menu_help():
    print("\nYou can make a choice by using numbers: 1,2,3..."
          "\nPress '1' to return to main menu.\nPress '2' to quit from program.")
    list_of_titles = ["Back", "Quit"]
    menu_generate(len(list_of_titles), list_of_titles)
    ui.menu_help_key()


def quadratic_equations():
    print("\nax^2 + bx + c = 0:")
    print("Enter the coefficients for the equation by spaces:\n")
    a, b, c = input().strip().split()
    for i in (a, b, c):
        introduction.input_check_number(i)
    a, b, c = map(float, (a, b, c))
    functions.quadratic_equation(a, b, c)
    menu_numbers()


def menu_calculator():
    time.sleep(constants.delay)
    first_number = input("\nFirst number: ")
    second_number = input("Second number: ")
    list = ["+", "-", "*", "/", "//", "%", "Back", "Quit"]
    menu_generate(len(list), list)
    key = introduction.key_check()
    time.sleep(constants.delay)
    print("\nResult:", functions.calculator(first_number, second_number, key))
    menu_numbers()


def menu_list():
    print("\nList menu:")
    list = ["List of random numbers", "Flexible list", "Back", "Quit"]
    menu_generate(len(list), list)
    ui.menu_list_key()


def menu_flexible_list():
    print("\nFlexible list menu:")
    list = ["Add", "Edit", "Remove", "Print *", "Back", "Quit"]
    menu_generate(len(list), list)
    key = ui.menu_flexible_list_and_queue_key()
    functions.flexible_list(key)


def menu_queue():
    print("\nQueue menu:")
    list = ["Flexible queue", "Back", "Quit"]
    menu_generate(len(list), list)
    ui.menu_queue_key()


def menu_flexible_queue():
    print("\nFlexible queue menu:")
    list = ["Add", "Edit", "Remove", "Print *", "Back", "Quit"]
    menu_generate(len(list), list)
    key = ui.menu_flexible_list_and_queue_key()
    functions.flexible_queue(key)


def menu_add_items_queue():
    print("\nAdd items menu:")
    list = ["Add in start", "Add in end"]
    menu_generate(len(list), list)
    key = ui.menu_flexible_list_and_queue_key()
    functions.add_queue(key)
