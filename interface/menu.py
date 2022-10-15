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
    list_of_titles = ["Calculator", "Factorial", "Quadratic equation", "Main menu", "Quit"]
    menu_generate(len(list_of_titles), list_of_titles)
    ui.menu_number_key()


def menu_strings():
    print("\nString menu:")
    list_of_titles = ["Palindrome", "Main menu", "Quit"]
    menu_generate(len(list_of_titles), list_of_titles)
    ui.menu_string_key()


def menu_stack():
    print("\nStack menu:")
    list_of_titles = ["List of random numbers", "Main menu", "Quit"]
    menu_generate(len(list_of_titles), list_of_titles)
    ui.menu_list_key()


def menu_help():
    print(" \nYou can make a choice by using numbers 1/2/3..etc..")
    print(" Press '1' to return to main menu.\n3. Press '2' to exit the program")
    list_of_titles =["Main menu", "Quit"]
    menu_generate(len(list_of_titles), list_of_titles)
    ui.menu_number_key()


def quadratic_equations():
    print("\nax^2 + bx + c = 0:")
    print("Enter the coefficients for the equation\n")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print(functions.quadratic_equation(a, b, c))
    introduction.repeat_input()


def menu_calculator():
    first_number = input("\nFirst number: ")
    second_number = input("Second number: ")
    print("Choose the operator (+, -, *, /, //, %): ")
    sign = input()
    print(functions.calculator(first_number, second_number, sign))
    introduction.repeat_input()


def menu_list():
    print("\nList menu:")
    list = ["List of random numbers", "Flexible list", "Main menu", "Quit"]
    menu_generate(len(list), list)
    ui.menu_list_key()

def menu_flexible_list():
    print("\nFlexible list menu:")
    list = ["Add", "Edit", "Remove", "Print *", "Back", "Quit"]
    menu_generate(len(list), list)
    key = ui.menu_flexible_list_key()
    functions.flexible_list(key)