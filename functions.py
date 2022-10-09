def float_check(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def factorial_recursive(num):
    if num == 1:
        return num
    else:
        return num * factorial_recursive(num - 1)


def calculator(num1, num2, sign):
    num_check1 = float_check(num1)
    num_check2 = num1.isdigit()
    if num_check1 or num_check2:
        num_check1 = float_check(num2)
        num_check2 = num2.isdigit()
        if num_check1 or num_check2:
            if sign == "+":
                result = float(num1) + float(num2)
                return result
            elif sign == "-":
                result = float(num1) - float(num2)
                return result
            elif sign == "*":
                result = float(num1) * float(num2)
                return result
            elif sign == "/":
                result = float(num1) / float(num2)
                return result
            elif sign == "//":
                result = float(num1) // float(num2)
                return result
            elif sign == "%":
                result = float(num1) % float(num2)
                return result
        else:
            print("Invalid second input")
    else:
        print("Invalid first input")
