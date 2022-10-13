import functions
import sys
import menu
import introduction


def menu_numbers():
    print("\nNumber menu:")
    menu.menu_generate(5, ["Calculator", "Factorial", "Quadratic equation", "Main menu", "Quit"])
    res = introduction.key_check()
    menu_number_key(res)


def menu_number_key(key):
    match key:
        case "'1'":
            calculator_menu()
            sign = input()
            calculator(sign)
            main_menu()
        case "'2'":
            factorial()
            main_menu()
        case "'3'":
            quadratic_equations()
            main_menu()
        case "'4'":
            main_menu()
        case "'5'":
            sys.exit()


def menu_strings():
    print("\nString menu:")
    menu.menu_generate(3, ["Palindrome", "Main menu", "Quit"])
    res = introduction.key_check()
    menu_string_key(res)


def menu_string_key(key):
    match key:
        case "'1'":
            is_palindrome()
            main_menu()
        case "'2'":
            main_menu()
        case "'3'":
            sys.exit()


def menu_list():
    print("\nList menu:")
    menu.menu_generate(3, ["List of random numbers", "Main menu", "Quit"])
    res = introduction.key_check()
    menu_list_key(res)


def menu_list_key(key):
    match key:
        case "'1'":
            functions.list_of_random_numbers()
            main_menu()
        case "'2'":
            main_menu()
        case "'3'":
            sys.exit()


def menu_help():
    print(" You can make a choice by using numbers 1/2/3..etc..")
    print(" Press '1' to return to main menu.\n3. Press '2' to exit the program")
    menu.menu_generate(2, ["Main menu", "Quit"])
    res = introduction.key_check()
    menu_number_key(res)


def menu_help_key(key):
    match key:
        case "'1'":
            main_menu()
        case "'2'":
            sys.exit()


def is_palindrome():
    string = input("Input smth: ")
    print(functions.is_palindrome(string))


def factorial():
    num = input("Input your number: \n")
    print(functions.factorial_recursive(int(num)))


def quadratic_equations():
    print("ax^2 + bx + c = 0:")
    print("Enter the coefficients for the equation\n")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print(functions.quadratic_equation(a, b, c))


def calculator_menu():
    print("Choose the operator (+, -, *, /, //, %): ")


def main_menu():
    print("\nMain menu: ")
    menu.menu_generate(7, ["Number", "String", "List", "Queue", "Tree", "Help", "Quit"])
    res = introduction.key_check()
    main_menu_key(res)



def main_menu_key(key):
    match key:
        case "'1'":
            menu_numbers()
        case "'2'":
            menu_strings()
        case "'3'":
            menu_list()
        case "'4'":
            print("Soon...")
            main_menu()
        case "'5'":
            print("Soon...")
            main_menu()
        case "'6'":
            menu_help()
        case "'7'":
            sys.exit()


def calculator(sign):
    if sign not in ("+", "-", "*", "%", "/", "//"):
        print("Invalid character")
    else:
        first_number = input("First number: ")
        second_number = input("Second number: ")
        print(functions.calculator(first_number, second_number, sign))
