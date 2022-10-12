import functions
import sys


def menu_numbers():
    print("Numbers menu:\n")
    user_choice = input("1. Calculator.\n2. Factorial.\n3. Quadratic equation.\n9. Main menu.\n10. Quit.\n")
    if user_choice not in ("1", "2", "3", "9", "10"):
        print("Invalid choice")
        menu_numbers()
    elif user_choice == "1":
        calculator_menu()
        sign = input()
        calculator(sign)
    elif user_choice == "2":
        factorial()
    elif user_choice == "3":
        quadratic_equations()
    elif user_choice == "9":
        main_menu()
    elif user_choice == "10":
        sys.exit()


def menu_strings():
    print("Strings menu")
    user_choice = input("1. Palindrome.\n9. Main menu.\n10. Quit.\n")
    if user_choice not in ("1", "9", "10"):
        print("Invalid choice")
        menu_strings()
    elif user_choice == "1":
        is_palindrome()
    elif user_choice == "9":
        return_to_main_menu()
    elif user_choice == "10":
        sys.exit()


def menu_list():
    print("List menu:")
    user_choice = input("1. List of random numbers.\n9. Main menu.\n10. Quit.\n")
    if user_choice not in ("1", "9", "10"):
        print("Invalid choice")
        menu_list()
    elif user_choice == "1":
        functions.list_of_random_numbers()
    elif user_choice == "9":
        return_to_main_menu()
    elif user_choice == "10":
        sys.exit()


def return_to_main_menu():
    flag = input("9. Return to main menu\n10. Quit\n")
    if flag not in ("9", "10"):
        print("Please choose '9' or '10'")
        return_to_main_menu()
    elif flag == "9":
        main_menu()
    elif flag == "10":
        sys.exit()


def menu_help():
    print("1. You can make a choice by using numbers 1/2/3..etc..")
    print("2. Press '9' to return to main menu.\n3. Press '10' to exit the program")
    user_choice = input()
    if user_choice not in ("9", "10"):
        print("Invalid choice")
        menu_help()
    elif user_choice == "9":
        return_to_main_menu()
    elif user_choice == "10":
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
    print("Main menu:\n ")
    print("1. Numbers.\n2. Strings.\n3. List.\n4. Queue.\n5. Branch.\n9. Help.\n10. Exit\n")
    user_choice = input()
    if user_choice not in ("1", "2", "3", "4", "5", "9", "10"):
        print("Invalid choice")
        main_menu()
    elif user_choice == "1":
        menu_numbers()
    elif user_choice == "2":
        menu_strings()
    elif user_choice == "3":
        menu_list()
    elif user_choice == "4":
        print("In future. Please wait")
        main_menu()
    elif user_choice == "5":
        print("In future. Please wait")
        main_menu()
    elif user_choice == "9":
        menu_help()
    elif user_choice == "10":
        sys.exit()


def calculator(sign):
    if sign not in ("+", "-", "*", "%", "/", "//"):
        print("Invalid character")
    else:
        first_number = input("First number: ")
        second_number = input("Second number: ")
        print(functions.calculator(first_number, second_number, sign))
