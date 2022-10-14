import functions
import introduction
import ui


def menu_generate(strings_numbers, list_of_names):
    for i in range(1, strings_numbers + 1):
        print(str(i) + ".", list_of_names[i - 1])
        i += 1


def main_menu():
    print("\nMain menu: ")
    menu_generate(7, ["Number", "String", "List", "Queue", "Tree", "Help", "Quit"])
    ui.main_menu_key()


def menu_numbers():
    print("\nNumber menu:")
    menu_generate(5, ["Calculator", "Factorial", "Quadratic equation", "Main menu", "Quit"])
    ui.menu_number_key()


def menu_strings():
    print("\nString menu:")
    menu_generate(3, ["Palindrome", "Main menu", "Quit"])
    ui.menu_string_key()


def menu_list():
    print("\nList menu:")
    menu_generate(3, ["List of random numbers", "Main menu", "Quit"])
    ui.menu_list_key()


def menu_help():
    print(" \nYou can make a choice by using numbers 1/2/3..etc..")
    print(" Press '1' to return to main menu.\n3. Press '2' to exit the program")
    menu_generate(2, ["Main menu", "Quit"])
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
