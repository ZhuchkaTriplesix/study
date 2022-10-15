import sys
import time

import keyboard
from interface import menu
import constants


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
    time.sleep(constants.delay)
    key = keyboard.read_key()
    time.sleep(constants.delay)
    return key


def repeat_input():
    flag = input('One more time? [y/n]: ')
    if flag == 'y':
        menu.main_menu()
    else:
        sys.exit()
