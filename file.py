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
        temp_address = 'root\\' + user.username

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
        temp_address = 'root\\' + user.username

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
    if not temp_list or len(temp_list) > 1:
        temp_f = ''
        for i in temp_list:
            temp_f += i + ', '

        add_record(user.username, 'DEF', temp_f,
                   'Failed. Invalid Parameters!')
        return 'Invalid Parameters For DEF. Type HELP DEF for more Information.'

    temp_a = temp_list[0].split('\\')

    if len(temp_a) > 1:
        temp_address = 'root\\' + user.username

        for i in temp_a[:-1]:
            temp_address += '\\' + i

    else:
        temp_address = user.real_current_dir

    if Path(temp_address + '\\' + temp_a[-1]).is_file():
        os.remove(temp_address + '\\' + temp_a[-1])
        add_record(user.username, 'DEF', temp_address + '\\' + temp_a[-1],
                   'Success. File Removed!')
        return 'File Removed Successfully!'
    else:
        add_record(user.username, 'DEF', temp_address + '\\' + temp_a[-1],
                   'Failed. File Not Found!')
        return 'File Not Found!'


def cpf_command(user, temp_list=None):
    if not temp_list or len(temp_list) != 2:
        temp_f = ''
        for i in temp_list:
            temp_f += i + ', '

        add_record(user.username, 'CPF', temp_f,
                   'Failed. Invalid Parameters!')
        return 'Invalid Parameters For CPF. Type HELP CPF for more Information.'

    temp_a = temp_list[0].split('\\')
    temp_b = temp_list[1].split('\\')

    if len(temp_a) > 1 and len(temp_b) > 1:
        src = 'root\\' + user.username
        des = src

        for i in temp_a:
            src += '\\' + i
        for i in temp_b:
            des += '\\' + i

    if not Path(src).is_file():
        add_record(user.username, 'CPF', src + ' --> ' + des,
                   'Failed. File Not Found!')
        return 'File Not Found!'

    if Path(des).is_file():
        add_record(user.username, 'CPF', src + ' --> ' + des,
                   'Failed. File Already Exists!')
        return 'File Already Exists!'

    temp_c = shutil.copyfile(src, des)

    add_record(user.username, 'CPF', src + ' --> ' + des,
               'Success. File Copied!')
    return 'File Copied Successfully!'


def mvf_command(user, temp_list=None):
    if not temp_list or len(temp_list) != 2:
        temp_f = ''
        for i in temp_list:
            temp_f += i + ', '

        add_record(user.username, 'MVF', temp_f,
                   'Failed. Invalid Parameters!')
        return 'Invalid Parameters For MVF. Type HELP MVF for more Information.'

    temp_a = temp_list[0].split('\\')
    temp_b = temp_list[1].split('\\')

    if len(temp_a) > 1 and len(temp_b) > 1:
        src = 'root\\' + user.username
        des = src

        for i in temp_a:
            src += '\\' + i
        for i in temp_b:
            des += '\\' + i

    if not Path(src).is_file():
        add_record(user.username, 'MVF', src + ' --> ' + des,
                   'Failed. File Not Found!')
        return 'File Not Found!'

    if Path(des).is_file():
        add_record(user.username, 'MVF', src + ' --> ' + des,
                   'Failed. File Already Exists!')
        return 'File Already Exists!'

    temp_c = shutil.move(src, des)

    add_record(user.username, 'MVF', src + ' --> ' + des,
               'Success. File Moved!')
    return 'File Moved Successfully!'


def stf_command(user, temp_list=None):
    dest_file_name = None

    if not temp_list or len(temp_list) > 2:
        temp_f = ''
        for i in temp_list:
            temp_f += i + ', '

        add_record(user.username, 'STF', temp_f,
                   'Failed. Invalid Parameters!')
        return 'Invalid Parameters For STF. Type HELP STF for more Information.'

    if len(temp_list) > 1:
        temp_b = temp_list[1].split('\\')

        if len(temp_b) > 1:
            dest_file_name = 'root\\' + user.username

            for i in temp_b:
                dest_file_name += '\\' + i

        else:
            dest_file_name = temp_list[1]

    temp_a = temp_list[0].split('\\')

    if len(temp_a) > 1:
        temp_address = 'root\\' + user.username

        for i in temp_a[:-1]:
            temp_address += '\\' + i

    else:
        temp_address = user.real_current_dir

    if not Path(temp_address + '\\' + temp_a[-1]).is_file():
        add_record(user.username, 'STF', temp_address + '\\' + temp_a[-1],
                   'Failed. File Dose NOT Exists!')
        return 'File Dose NOT Exists!'

    if temp_a[-1][-3:].lower() != 'txt':
        add_record(user.username, 'STF', temp_address + '\\' + temp_a[-1],
                   'Failed. File Format NOT Supported!')
        return 'File Format NOT Supported! Only .txt'

    temp_file = open(os.path.join(temp_address, temp_a[-1]), 'r+')
    temp_lines = temp_file.readlines()
    temp_file.close()

    temp_lines.sort()

    if not dest_file_name:
        for i in range(len(temp_lines)):
            if temp_lines[i][-1:] != '\n':
                temp_lines[i] = temp_lines[i] + '\n'

            print(temp_lines[i], end='')
    else:
        for i in range(len(temp_lines)):
            if temp_lines[i][-1:] != '\n':
                temp_lines[i] = temp_lines[i] + '\n'

        if Path(dest_file_name).is_file():
            add_record(user.username, 'STF', dest_file_name,
                       'Failed. File Already Exists!')
            return 'File Already Exists!'

        temp_file = open(dest_file_name, 'w')
        temp_file.writelines(temp_lines)
        temp_file.close()

        add_record(user.username, 'STF', dest_file_name,
                   'Success. Sorted and File Created!')
        return 'Sorted and File Created Successfully!'
