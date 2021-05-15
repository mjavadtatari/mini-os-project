import os
import shutil
from management import *
from pathlib import Path


def user_root_dir(user):
    os_root_dir = 'root'
    user_root = os_root_dir + '\\' + user.username

    return user_root


def mkf_command(user, temp_list=None):
    if not temp_list or len(temp_list) > 1:
        temp_f = ''
        for i in temp_list:
            temp_f += i + ', '

        add_record(user.username, 'MKF', temp_f,
                   'Failed. Invalid Parameters!')
        return 'Invalid Parameters For MKF. Type HELP MKF for more Information.'

    temp_a = temp_list[0].split('\\')

    if len(temp_a) > 1:
        temp_address = 'root'

        for i in temp_a[:-1]:
            temp_address += '\\' + i

    else:
        temp_address = user.real_current_dir

    if Path(temp_address + '\\' + temp_a[-1]).is_file():
        add_record(user.username, 'MKF', temp_address + '\\' + temp_a[-1],
                   'Failed. File Already Exists!')
        return 'File Already Exists!'

    temp_file = open(os.path.join(temp_address, temp_a[-1]), 'w')
    temp_file.close()

    add_record(user.username, 'MKF', temp_address + '\\' + temp_a[-1],
               'Success. File Created!')
    return 'File Created Successfully!'


def opf_command(user, temp_list=None):
    if not temp_list or len(temp_list) > 1:
        temp_f = ''
        for i in temp_list:
            temp_f += i + ', '

        add_record(user.username, 'OPF', temp_f,
                   'Failed. Invalid Parameters!')
        return 'Invalid Parameters For OPF. Type HELP OPF for more Information.'

    temp_a = temp_list[0].split('\\')

    if len(temp_a) > 1:
        temp_address = 'root'

        for i in temp_a[:-1]:
            temp_address += '\\' + i

    else:
        temp_address = user.real_current_dir

    if not Path(temp_address + '\\' + temp_a[-1]).is_file():
        add_record(user.username, 'OPF', temp_address + '\\' + temp_a[-1],
                   'Failed. File Dose NOT Exists!')
        return 'File Dose NOT Exists!'

    if temp_a[-1][-3:].lower() != 'txt':
        add_record(user.username, 'OPF', temp_address + '\\' + temp_a[-1],
                   'Failed. File Format NOT Supported!')
        return 'File Format NOT Supported! Only .txt'

    temp_file = open(os.path.join(temp_address, temp_a[-1]), 'r+')
    temp_lines = temp_file.readlines()
    temp_file.close()
    for i in range(len(temp_lines)):
        print(str(i + 1) + ': ' + temp_lines[i], end='')

    while True:
        print('\n\nEnter Line Number as (&Line) to Edit OR type anything to append.')
        print('type (&Save) to save and close file')
        temp_input = input('>> ')

        if temp_input.lower() == '&save':
            print('\n')
            break

        elif temp_input[:5].lower() == '&line':
            t_line_num = temp_input[5:]
            try:
                t_line_num = int(t_line_num) - 1
            except:
                print('Please Enter a Valid Line Number!')
                continue

            if t_line_num + 1 > len(temp_lines) or t_line_num < 0:
                print('Please Enter a Valid Line Number!')
            else:
                temp_input_line = input(temp_lines[t_line_num][:-1] + ' >>> ')
                temp_lines[t_line_num] = temp_input_line + '\n'
        else:
            temp_lines.append('\n' + temp_input)

    temp_file = open(os.path.join(temp_address, temp_a[-1]), 'w')
    temp_file.writelines(temp_lines)
    temp_file.close()

    add_record(user.username, 'OPF', temp_address + '\\' + temp_a[-1],
               'Success. File Saved!')
    return 'File Saved Successfully!'


def def_command(user, temp_list=None):
    pass


def cpf_command(user, temp_list=None):
    pass


def mvf_command(user, temp_list=None):
    pass


def stf_command(user, temp_list=None):
    pass


def sef_command(user, temp_list=None):
    pass
