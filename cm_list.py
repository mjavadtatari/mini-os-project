from calculator import *


def help_command(user, temp_x):
    help_file = open("help_commands.txt", "r")
    temp_text = help_file.readlines()
    text = ''

    for i in temp_text:
        text += i.replace("+t", "\t\t")

    help_file.close()

    add_record(user, 'HELP', 'help',
               'Success')

    return text


all_cm = {
    'help': {'func': help_command, },
    'add': {'func': add_command, },
    'mul': {'func': mul_command, },
    'div': {'func': div_command, },
    'pow': {'func': '', },
    'root': {'func': root_command, },
    'mod': {'func': '', },
    'lcm': {'func': '', },
    'gcd': {'func': '', },
    'base': {'func': '', },
    'home': {'func': '', },
    'chd': {'func': '', },
    'mkd': {'func': '', },
    'ded': {'func': '', },
    'cpd': {'func': '', },
    'mvd': {'func': '', },
    'rnd': {'func': '', },
    'exd': {'func': '', },
    'mkf': {'func': '', },
    'opf': {'func': '', },
    'def': {'func': '', },
    'cpf': {'func': '', },
    'mvf': {'func': '', },
    'rnf': {'func': '', },
    'stf': {'func': '', },
    'sef': {'func': '', },
    '': {'func': '', },
}
