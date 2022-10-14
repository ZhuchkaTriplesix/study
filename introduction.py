import sys
import keyboard
import time
import main


def float_check(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def input_check_number(num):
    float_check_input = float_check(num)
    int_check_input = num.isdigit()
    if float_check_input or int_check_input:
        return num
    else:
        print("Input error")
        repeat_input()


def key_check():
    time.sleep(1)
    key = keyboard.read_key()
    time.sleep(0.5)
    return key


def repeat_input():
    flag = input('One more time? [y/n]: ')
    if flag == 'y':
        main.convert()
    else:
        sys.exit()
