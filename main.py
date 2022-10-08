import math


# add a new function sqrteq

def floatCheck(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def convert():
    start = input("Choose one: \n1. Calc\n2. Factorial \n")
    if start not in ("1", "2", "3"):
        print("Invalid argument")
    else:
        if start == "1":
            what = input("Choose the operator (+, -, *, /, //, %): ")
            if what not in ("+", "-", "*", "%", "/", "//"):
                print("Invalid character")
            else:
                a = input("First number: ")
                b = input("Second number: ")
                bool = floatCheck(a)
                bool1 = a.isdigit()
                if bool or bool1:
                    bool = floatCheck(b)
                    bool1 = b.isdigit()
                    if bool or bool1:
                        if what == "+":
                            res = float(a) + float(b)
                            print("Result: " + str(res))
                        elif what == "-":
                            res = float(a) - float(b)
                            print("Result: " + str(res))
                        elif what == "*":
                            res = float(a) * float(b)
                            print("Result: " + str(res))
                        elif what == "/":
                            res = float(a) / float(b)
                            print("Result: " + str(res))
                        elif what == "//":
                            res = float(a) // float(b)
                            print("Result: " + str(res))
                        elif what == "%":
                            res = float(a) % float(b)
                            print("Result: " + str(res))
                    else:
                        print("Invalid second input")
                else:
                    print("Invalid first input")

        elif start == "2":
            method = input("Choose the method: (loop)")
            if method not in ("\n1. Loop \n2. Recursion"):
                print("Invalid character")
            else:
                if method == "1":
                    number = input("Input your number: ")
                    bool = number.isdigit()
                    if bool:
                        factorial = 1
                        for i in range(2, int(number) + 1):
                            factorial *= i
                        print(factorial)
                    else:
                        print("Invalid input")


convert()
while True:
    flag = input("One more time? [y/n]: ")

    if flag == 'y':
        convert()
    else:
        break
