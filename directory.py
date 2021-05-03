import os
from management import *


def user_root_dir(user):
    os_root_dir = 'root'
    user_root = os_root_dir + '\\' + user.username

    if not os.path.exists(user_root):
        os.makedirs(user_root)
        add_record(user.username, 'Directory', user.username,
                   'Directory Created Successfully')

    return user_root


def home_command(user, temp_list=None):
    temp_dir = user_root_dir(user)
    if not os.path.exists(temp_dir + '\\home'):
        os.makedirs(temp_dir + '\\home')
        add_record(user.username, 'Home-Directory', user.username +
                   '\home', 'Directory Created Successfully')

    if temp_list != 'No_dir_change':
        user.current_dir = 'home'
        user.real_current_dir = temp_dir + '\\home'

        add_record(user.username, 'HOME', user.real_current_dir + '\\',
                   'Directory Changed Successfully')

    return 'Directory Changed!'


def chd_command(user, temp_list=None):
    home_command(user, 'No_dir_change')

    temp_address = 'root\\' + user.username + '\\'

    if temp_list[0].lower() == 'f':
        temp_address += temp_list[1].replace("\\", "\\")

    elif temp_list[0] == '..':
        temp_x = user.real_current_dir.split('\\')
        temp_address = ''
        for i in temp_x[:-1]:
            temp_address += i + '\\'
        temp_address = temp_address[:-1]

    elif not '.' in temp_list[0]:
        temp_address = user.real_current_dir + '\\' + \
            temp_list[0].replace("\\", "\\")

    else:
        add_record(user.username, 'CHD',
                   user.real_current_dir + '\\' + temp_list[0], 'Failed. the Directory does not exist')
        return 'the Directory does not exist'

    if not os.path.exists(temp_address):
        add_record(user.username, 'CHD',
                   user.real_current_dir + '\\' + temp_list[0], 'Failed. the Directory does not exist')
        return 'the Directory does not exist'

    elif temp_address == 'root':
        add_record(user.username, 'CHD',
                   user.real_current_dir + '\\' + temp_list[0], 'Failed. Try Reaching the Root!')
        return 'the Directory does not exist, You are at Root'

    else:
        temp_x = temp_address.split('\\')
        user.current_dir = ''

        for i in temp_x[2:]:
            user.current_dir += i + '\\'
        user.real_current_dir = temp_address

        add_record(user.username, 'CHD', user.real_current_dir + '\\',
                   'Success. Directory Changed!')

        return 'Directory Changed!'


def mkd_command(user, temp_list=None):
    if temp_list:
        temp_a = temp_list[0].split('\\')
        if len(temp_a) > 1:
            if temp_a[0] == user.username:
                temp_address = 'root\\' + temp_list[0]
                print(temp_address)

                if not os.path.exists(temp_address):
                    os.makedirs(temp_address)

                    temp_x = temp_address.split('\\')
                    user.current_dir = ''

                    for i in temp_x[2:]:
                        user.current_dir += i + '\\'
                    user.real_current_dir = temp_address

                    add_record(user.username, 'MKD', temp_address + '\\',
                               'Success. Directory Created!')
                    return 'Directory Created Successfully!'

                else:
                    add_record(user.username, 'MKD', temp_address + '\\',
                               'Fail. Directory already exist!')
                    return 'Directory already exist!'

            else:
                add_record(user.username, 'MKD', temp_list[0] + '\\',
                           'Fail. Not Valid!')
                return 'Enter a Valid Name or Address!'

        else:
            temp_address = user.real_current_dir + '\\' + temp_list[0]

            if not os.path.exists(temp_address):
                os.makedirs(temp_address)

                temp_x = temp_address.split('\\')
                user.current_dir = ''

                for i in temp_x[2:]:
                    user.current_dir += i + '\\'
                user.real_current_dir = temp_address

                add_record(user.username, 'MKD', temp_address + '\\',
                           'Success. Directory Created!')
                return 'Directory Created Successfully!'

            else:
                add_record(user.username, 'MKD', temp_address + '\\',
                           'Fail. Directory already exist!')
                return 'Directory already exist!'
