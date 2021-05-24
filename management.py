from os import system, name
from time import sleep
from logs_file import *
# from termcolor import colored
from account import *


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
