import math


# add a new function factorial


def convert():
    Start = input("Choose one: (calc, factorial, sqrteq):")
    if Start not in ("calc", "factorial", "sqrteq"):
        print("invalid argument")
    else:
        if Start == "calc":
            what = input("Choose operator (+, -, *, /, //, %): ")

            if what not in ("+", "-", "*", "%", "/", "//"):
                print("invalid character")
            else:
                a = float(input("First number: "))
                b = float(input("Second number: "))
                if what == "+":
                    c = a + b
                    print("result: " + str(c))
                elif what == "-":
                    c = a - b
                    print("result: " + str(c))
                elif what == "*":
                    c = a * b
                    print("result: " + str(c))
                elif what == "/":
                    c = a / b
                    print("result: " + str(c))
                elif what == "//":
                    c = a // b
                    print("result: " + str(c))
                elif what == "%":
                    c = a % b
                    print("result: " + str(c))
        elif Start == "factorial":
            method = input("Choose the method: (loop or recursion)")
            if method not in ("loop", "recursion"):
                print("invalid character")
            else:
                if method == "loop":
                    number = int(input("Input your number: "))
                    factorial = 1
                    for i in range(2, number + 1):
                        factorial *= i
                    print(factorial)


convert()
while True:
    flag = input("One more time? [y/n]: ")

    if flag == 'y':
        convert()
    else:
        break
