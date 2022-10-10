import functions


def convert():
    start = input("Choose one: \n1. Calc\n2. Factorial \n3. Quadratic equation \n4. List of random numbers\n")
    if start not in ("1", "2", "3", "4"):
        print("Invalid argument")
    else:
        if start == "1":
            sign = input("Choose the operator (+, -, *, /, //, %): ")
            if sign not in ("+", "-", "*", "%", "/", "//"):
                print("Invalid character")
            else:
                num1 = input("First number: ")
                num2 = input("Second number: ")
                print(functions.calculator(num1, num2, sign))
        elif start == "2":
            num = input("Input your number: \n")
            print(functions.factorial_recursive(int(num)))
        elif start == "3":
            print("ax^2 + bx + c = 0:")
            print("Enter the coefficients for the equation\n")
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(functions.quadratic_equation(a, b, c))
        elif start == "4":
            functions.list_of_random_numbers()


convert()
while True:
    flag = input("One more time? [y/n]: ")

    if flag == 'y':
        convert()
    else:
        break
