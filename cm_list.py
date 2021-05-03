from calculator import *
from directory import *


def help_command(user, temp_x):
    user = user.username
    help_file = open("help_commands.txt", "r")
    temp_text = help_file.readlines()
    help_file.close()
    text = ''

    if len(temp_x) > 0:
        if temp_x[0].lower() in all_cm:
            for i in temp_text:
                if '*' + temp_x[0].upper() in i:
                    text = i.replace("+t", "\t\t")
                    text = text.replace("*", "")
                    break
            add_record(user, 'HELP', 'help ' + temp_x[0],
                       'Success')
        else:
            add_record(user, 'HELP', 'help ' + temp_x[0],
                       'Fail')
            return 'Enter Valid Command to Show Help!'

    elif len(temp_x) == 0:
        for i in temp_text:
            if i == 'dont include\n':
                break
            text += i.replace("+t", "\t\t")

        add_record(user, 'HELP', 'help',
                   'Success')

    return text


all_cm = {
    'help': {'func': help_command, },
    'add': {'func': add_command, },
    'mul': {'func': mul_command, },
    'div': {'func': div_command, },
    'pow': {'func': pow_command, },
    'root': {'func': root_command, },
    'mod': {'func': mod_command, },
    'lcm': {'func': lcm_command, },
    'gcd': {'func': gcd_command, },
    'base': {'func': base_command, },
    'home': {'func': home_command, },
    'chd': {'func': chd_command, },
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
