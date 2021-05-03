from management import *



def add_command(user, temp_list=None):
    user=user.username
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
    user=user.username
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
    user=user.username
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


def pow_command(user, temp_list=None):
    user=user.username
    if len(temp_list) > 1:
        try:
            temp_x, temp_p = float(temp_list[0]), float(temp_list[1])
        except ValueError:
            add_record(user, 'POW', 'nums: ' +
                       temp_list[0] + ' , ' + temp_list[1], 'Fail')
            return 'Enter Valid Numbers!'

    else:
        while True:
            temp_x = input('Enter the Number (OR Q for Quit) : ')

            if temp_x.lower() == 'q':
                add_record(user, 'POW', 'nums: ' +
                           temp_x + ' , ' + 'None', 'Canceled')
                return 'Canceled!'

            temp_p = input('Enter the Power : ')

            try:
                temp_x, temp_p = float(temp_x), float(temp_p)
                break
            except ValueError:
                print(colored('Enter a Valid Number!', 'yellow'))

    try:
        add_record(user, 'POW', 'nums: ' + str(temp_x) + ' , ' + str(temp_p),
                   'Resualt= ' + str(temp_x ** temp_p))
        return 'Answer = {}'.format(temp_x ** temp_p)

    except OverflowError:
        add_record(user, 'POW', 'nums: ' + str(temp_x) + ' , ' + str(temp_p),
                   'Resualt= ' + 'Fail: Number too large!')
        return 'Number too large!'


def root_command(user, temp_list=None):
    user=user.username
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


def mod_command(user, temp_list=None):
    user=user.username
    if len(temp_list) > 1:
        try:
            temp_x, temp_r = float(temp_list[0]), float(temp_list[1])
        except ValueError:
            add_record(user, 'MOD', 'nums: ' +
                       temp_list[0] + ' , ' + temp_list[1], 'Fail')
            return 'Enter Valid Numbers!'

    else:
        while True:
            temp_x = input('Enter First Number (OR Q for Quit) : ')

            if temp_x.lower() == 'q':
                add_record(user, 'MOD', 'nums: ' +
                           temp_x + ' , ' + 'None', 'Canceled')
                return 'Canceled!'

            temp_r = input('Enter Second Number : ')

            try:
                temp_x, temp_r = float(temp_x), float(temp_r)
                break
            except ValueError:
                print(colored('Enter a Valid Number!', 'yellow'))

    add_record(user, 'MOD', 'nums: ' + str(temp_x) + ' , ' + str(temp_r),
               'Resualt= ' + str(temp_x % temp_r))

    return 'Answer = {}'.format(temp_x % temp_r)


def gcd_command(user, temp_list=None):
    user=user.username
    if len(temp_list) > 1:
        try:
            temp_x, temp_y = float(temp_list[0]), float(temp_list[1])
        except ValueError:
            add_record(user, 'GCD', 'nums: ' +
                       temp_list[0] + ' , ' + temp_list[1], 'Fail')
            return 'Enter Valid Numbers!'

    else:
        while True:
            temp_x = input('Enter First Number (OR Q for Quit) : ')

            if temp_x.lower() == 'q':
                add_record(user, 'GCD', 'nums: ' +
                           temp_x + ' , ' + 'None', 'Canceled')
                return 'Canceled!'

            temp_y = input('Enter Second Number : ')

            try:
                temp_x, temp_y = float(temp_x), float(temp_y)
                break
            except ValueError:
                print(colored('Enter a Valid Number!', 'yellow'))

    temp_y2 = temp_y

    while(temp_y):
        temp_x, temp_y = temp_y, temp_x % temp_y

    try:
        if temp_list[2] == '*':
            return temp_x

    except IndexError:
        add_record(user, 'GCD', 'nums: ' + str(temp_x) + ' , ' + str(temp_y2),
                   'Resualt= ' + str(temp_x))

        return 'Answer = {}'.format(temp_x)


def lcm_command(user, temp_list=None):
    user=user.username
    if len(temp_list) > 1:
        try:
            temp_x, temp_y = float(temp_list[0]), float(temp_list[1])
        except ValueError:
            add_record(user, 'LCM', 'nums: ' +
                       temp_list[0] + ' , ' + temp_list[1], 'Fail')
            return 'Enter Valid Numbers!'

    else:
        while True:
            temp_x = input('Enter First Number (OR Q for Quit) : ')

            if temp_x.lower() == 'q':
                add_record(user, 'LCM', 'nums: ' +
                           temp_x + ' , ' + 'None', 'Canceled')
                return 'Canceled!'

            temp_y = input('Enter Second Number : ')

            try:
                temp_x, temp_y = float(temp_x), float(temp_y)
                break
            except ValueError:
                print(colored('Enter a Valid Number!', 'yellow'))

    lcm = (temp_x * temp_y) // float(gcd_command(user, [temp_x, temp_y, '*']))
    add_record(user, 'LCM', 'nums: ' + str(temp_x) + ' , ' + str(temp_y),
               'Resualt= ' + str(lcm))

    return 'Answer = {}'.format(lcm)


def base_command(user, temp_list=None):
    user=user.username
    if len(temp_list) > 1:
        try:
            temp_x, temp_y = temp_list[0], int(temp_list[1])
        except ValueError:
            add_record(user, 'BASE', 'nums: ' +
                       temp_list[0] + ' , ' + temp_list[1], 'Fail')
            return 'Enter Valid Numbers!'

    else:
        while True:
            temp_x = input('Enter the Decimal Number (OR Q for Quit) : ')

            if temp_x.lower() == 'q':
                add_record(user, 'BASE', 'nums: ' +
                           temp_x + ' , ' + 'None', 'Canceled')
                return 'Canceled!'

            temp_y = input('Enter the Base : ')

            try:
                temp_x, temp_y = temp_x, int(temp_y)
                break
            except ValueError:
                print(colored('Enter a Valid Number!', 'yellow'))

    temp_b = int(temp_x, temp_y)
    add_record(user, 'BASE', 'nums: ' + str(temp_x) + ' , ' + str(temp_y),
               'Resualt= ' + str(temp_b))

    return 'Answer = {}'.format(temp_b)
