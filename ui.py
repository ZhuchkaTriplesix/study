import functions
import sys
import menu
import introduction
import time


def main_menu_key():
    menu_key = introduction.key_check()
    match menu_key:
        case "1":
            menu.menu_numbers()
        case "2":
            menu.menu_strings()
        case "3":
            menu.menu_list()
        case "4":
            print("Soon...")
            menu.main_menu()
        case "5":
            print("Soon...")
            menu.main_menu()
        case "6":
            menu.menu_help()
        case "7":
            sys.exit()
        case _:
            print("\nInvalid input")
            introduction.repeat_input()


def menu_number_key():
    number_of_menu = introduction.key_check()
    match number_of_menu:
        case "1":
            menu.menu_calculator()
            time.sleep(0.5)
        case "2":
            factorial()
            time.sleep(0.5)
        case "3":
            menu.quadratic_equations()
            time.sleep(0.5)
        case "4":
            menu.main_menu()
        case "5":
            sys.exit()
        case _:
            print("\nInvalid input")
            introduction.repeat_input()


def menu_string_key():
    number_of_string = introduction.key_check()
    match number_of_string:
        case "1":
            is_palindrome()
            time.sleep(0.5)
        case "2":
            menu.main_menu()
        case "3":
            sys.exit()
        case _:
            print("\nInvalid input")
            introduction.repeat_input()


def menu_list_key():
    number_of_list = introduction.key_check()
    match number_of_list:
        case "1":
            functions.list_of_random_numbers()
            time.sleep(0.5)
        case "2":
            menu.main_menu()
        case "3":
            sys.exit()
        case _:
            print("\nInvalid input")
            introduction.repeat_input()


def menu_help_key():
    key = introduction.key_check()
    match key:
        case "1":
            menu.main_menu()
        case "2":
            sys.exit()
        case _:
            print("\nInvalid input")
            introduction.repeat_input()


def is_palindrome():
    string = input("\nInput the string: ")
    print(functions.is_palindrome(string))
    introduction.repeat_input()


def factorial():
    num = input("\nInput your number: \n")
    print(functions.factorial_recursive(int(num)))
    introduction.repeat_input()
