import sys
import keyboard
import time
import main


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
