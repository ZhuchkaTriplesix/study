import functions
import sys
import menu
import introduction
import time


def menu_numbers():
    print("\nNumber menu:")
    menu.menu_generate(5, ["Calculator", "Factorial", "Quadratic equation", "Main menu", "Quit"])
    menu_number_key()


def menu_number_key():
    number_of_menu = introduction.key_check()
    match number_of_menu:
        case "1":
            calculator_menu()
            sign = input()
            calculator(sign)
            time.sleep(0.5)
        case "2":
            factorial()
            time.sleep(0.5)
        case "3":
            quadratic_equations()
            time.sleep(0.5)
        case "4":
            main_menu()
        case "5":
            sys.exit()
        case _:
            print("\nInvalid input")
            introduction.repeat_input()


def menu_strings():
    print("\nString menu:")
    menu.menu_generate(3, ["Palindrome", "Main menu", "Quit"])
    menu_string_key()


def menu_string_key():
    number_of_string = introduction.key_check()
    match number_of_string:
        case "1":
            is_palindrome()
            time.sleep(0.5)
        case "2":
            main_menu()
        case "3":
            sys.exit()
        case _:
            print("\nInvalid input")
            introduction.repeat_input()


def menu_list():
    print("\nList menu:")
    menu.menu_generate(3, ["List of random numbers", "Main menu", "Quit"])
    menu_list_key()


def menu_list_key():
    number_of_list = introduction.key_check()
    match number_of_list:
        case "1":
            functions.list_of_random_numbers()
            time.sleep(0.5)
        case "2":
            main_menu()
        case "3":
            sys.exit()
        case _:
            print("\nInvalid input")
            introduction.repeat_input()


def menu_help():
    print(" \nYou can make a choice by using numbers 1/2/3..etc..")
    print(" Press '1' to return to main menu.\n3. Press '2' to exit the program")
    menu.menu_generate(2, ["Main menu", "Quit"])
    menu_number_key()


def menu_help_key():
    key = introduction.key_check()
    match key:
        case "1":
            main_menu()
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


def quadratic_equations():
    print("\nax^2 + bx + c = 0:")
    print("Enter the coefficients for the equation\n")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print(functions.quadratic_equation(a, b, c))
    introduction.repeat_input()


def calculator_menu():
    print("\nChoose the operator (+, -, *, /, //, %): ")


def main_menu():
    print("\nMain menu: ")
    menu.menu_generate(7, ["Number", "String", "List", "Queue", "Tree", "Help", "Quit"])
    main_menu_key()


def main_menu_key():
    key = introduction.key_check()
    match key:
        case "1":
            menu_numbers()
        case "2":
            menu_strings()
        case "3":
            menu_list()
        case "4":
            print("Soon...")
            main_menu()
        case "5":
            print("Soon...")
            main_menu()
        case "6":
            menu_help()
        case "7":
            sys.exit()
        case _:
            print("\nInvalid input")
            introduction.repeat_input()


def calculator(sign):
    if sign not in ("+", "-", "*", "%", "/", "//"):
        print("Invalid character")
    else:
        first_number = input("First number: ")
        second_number = input("Second number: ")
        print(functions.calculator(first_number, second_number, sign))
        introduction.repeat_input()
