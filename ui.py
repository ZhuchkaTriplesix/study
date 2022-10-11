import functions


def is_palindrome():
    string = input("Input smth")
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
    print("Choose one:")
    print("1. Calc\n2. Factorial \n3. Quadratic equation \n4. Random numbers\n5. Is Palindrome\n")


def calculator(sign):
    if sign not in ("+", "-", "*", "%", "/", "//"):
        print("Invalid character")
    else:
        num1 = input("First number: ")
        num2 = input("Second number: ")
        print(functions.calculator(num1, num2, sign))
