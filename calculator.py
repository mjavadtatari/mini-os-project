from management import *


def add_command(user, temp_list=None):
    def many_add():
        addition, temp_nums = 0, ''
        while True:
            temp_x = input('Enter a Number (OR S for Submit) : ')
            if temp_x.lower() == 's':
                break
            else:
                try:
                    temp_nums += temp_x + ' + '
                    addition += float(temp_x)
                except ValueError:
                    temp_nums = temp_x[:-3]
                    print(colored('Enter a Valid Number!', 'yellow'))

        add_record(user, 'ADD (many)', 'nums: ' + temp_nums[:-3],
                   'Resualt= ' + str(addition))

        return 'Answer = {}'.format(addition)

    addition, temp_nums = 0, ''

    if temp_list:

        if temp_list[0].lower() == 'many':
            return many_add()

        else:
            temp_flag = False
            for i in temp_list:
                try:
                    temp_nums += i + ' + '
                    addition += float(i)
                except ValueError:
                    temp_flag = True
                    addition = 'Fail'

            add_record(user, 'ADD', 'nums: ' + temp_nums[:-3],
                       'Resualt= ' + str(addition))

            return 'Enter Valid Numbers!' if temp_flag else 'Answer = {}'.format(addition)

    else:
        return many_add()


def mul_command(user, temp_list=None):
    multiplication, temp_nums = 1, ''

    def many_mul():
        multiplication, temp_nums = 1, ''
        while True:
            temp_x = input('Enter a Number (OR S for Submit) : ')
            if temp_x.lower() == 's':
                break
            else:
                try:
                    temp_nums += temp_x + ' x '
                    multiplication *= float(temp_x)
                except ValueError:
                    print(colored('Enter a Valid Number!', 'yellow'))

        add_record(user, 'MUL (many)', 'nums: ' + temp_nums[:-3],
                   'Resualt= ' + str(multiplication))

        return 'Answer = {}'.format(multiplication)

    if temp_list:

        if temp_list[0].lower() == 'many':
            return many_mul()

        else:
            temp_flag = False
            for i in temp_list:
                try:
                    temp_nums += i + ' x '
                    multiplication *= float(i)
                except ValueError:
                    temp_nums = temp_nums[:-3]
                    temp_flag = True

            add_record(user, 'MUL', 'nums: ' + temp_nums[:-3],
                       'Resualt= ' + str(multiplication))

            return 'Enter Valid Numbers!' if temp_flag else 'Answer = {}'.format(multiplication)

    else:
        return many_mul()


def div_command(user, temp_list=None):
    division, temp_nums = 0, ''

    def many_div():
        division, temp_nums = 0, ''
        while True:
            temp_x = input('Enter a Number (OR S for Submit) : ')
            if temp_x.lower() == 's':
                break
            else:
                try:
                    temp_nums += temp_x + ' / '
                    if division != 0:
                        division /= float(temp_x)
                    else:
                        division = float(temp_x)
                except ValueError:
                    print(colored('Enter a Valid Number!', 'yellow'))

        add_record(user, 'DIV (many)', 'nums: ' + temp_nums[:-3],
                   'Resualt= ' + str(division))

        return 'Answer = {}'.format(division)

    if temp_list:

        if temp_list[0].lower() == 'many':
            return many_div()

        else:
            temp_flag = False
            for i in temp_list:
                try:
                    temp_nums += i + ' / '
                    if division != 0:
                        division /= float(i)
                    else:
                        division = float(i)
                except ValueError:
                    temp_nums = temp_nums[:-3]
                    temp_flag = True

            add_record(user, 'DIV', 'nums: ' + temp_nums[:-3],
                       'Resualt= ' + str(division))

            return 'Enter Valid Numbers!' if temp_flag else 'Answer = {}'.format(division)

    else:
        return many_div()


def root_command(user, temp_list=None):
    if len(temp_list) > 1:
        try:
            temp_x, temp_r = float(temp_list[0]), float(temp_list[1])
        except ValueError:
            add_record(user, 'ROOT', 'nums: ' +
                       temp_list[0] + ' , ' + temp_list[1], 'Fail')
            return 'Enter Valid Numbers!'

    else:
        while True:
            temp_x = input('Enter the Number (OR Q for Quit) : ')

            if temp_x.lower() == 'q':
                add_record(user, 'ROOT', 'nums: ' +
                           temp_x + ' , ' + 'None', 'Canceled')
                return 'Canceled!'

            temp_r = input('Enter the Root : ')

            try:
                temp_x, temp_r = float(temp_x), float(temp_r)
                break
            except ValueError:
                print(colored('Enter a Valid Number!', 'yellow'))

    add_record(user, 'ROOT', 'nums: ' + str(temp_x) + ' , ' + str(temp_r),
               'Resualt= ' + str(temp_x**(1 / temp_r)))

    return 'Answer = {}'.format(temp_x**(1 / temp_r))
