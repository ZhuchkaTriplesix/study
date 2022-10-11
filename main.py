import functions
import ui


def convert():
    ui.main_menu()
    start = input()
    if start not in ("1", "2", "3", "4", "5"):
        print("Invalid argument")
    else:
        if start == "1":
            ui.calculator_menu()
            sign = input()
            ui.calculator(sign)
        elif start == "2":
            ui.factorial()
        elif start == "3":
            ui.quadratic_equations()
        elif start == "4":
            functions.list_of_random_numbers()
        elif start == "5":
            ui.is_palindrome()


convert()
while True:
    flag = input("One more time? [y/n]: ")
    if flag == 'y':
        convert()
    else:
        break
