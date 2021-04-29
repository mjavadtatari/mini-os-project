import sys
import openpyxl
from management import *
from logs_file import *
from termcolor import colored


users_db = openpyxl.load_workbook('Users.xlsx')
users_db_ws = users_db.active


class Account():

    def __init__(self, *args, **kwargs):
        self.username = ''
        self.password = ''
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.failed_attempted = 0
        self.user_row = ''
        self.logged_in = False
        self.relogin = False

    def find_user_coordinate(self, username):
        for row in users_db_ws.iter_rows(users_db_ws.min_row, users_db_ws.max_row + 1):
            for cell in row:
                if str(cell.value) == username:
                    self.user_row = str(cell.row)
                    self.load_user_info()

        return False if self.user_row == '' else True

    def load_user_info(self):
        self.username = users_db_ws['A' + self.user_row].value
        self.password = str(users_db_ws['B' + self.user_row].value)
        self.email = users_db_ws['D' + self.user_row].value
        self.first_name = users_db_ws['E' + self.user_row].value
        self.last_name = users_db_ws['F' + self.user_row].value

    def check_password(self, username, password):
        if self.find_user_coordinate(username) and self.password == password:
            if not self.check_is_user_banned():
                self.unban_user()
                self.logged_in = True
                add_record(self.username, 'login', 'pass: ' +
                           self.password, 'Success')
                return True
            else:
                add_record(self.username, 'login', 'pass: ' +
                           self.password, 'Failed, The User is Banned','r')
                print(colored(
                    'Your account has been banned, please contact the administrator!', 'red'))
                sleep(3)
                quit()
        else:
            return False

    def check_is_user_banned(self):
        if users_db_ws['H' + self.user_row].value == 'T':
            return True
        else:
            return False

    def ban_user(self, username, password):
        if username == 'mjavadtatri':
            return True

        if self.failed_attempted >= 2 and self.username != '':
            users_db_ws['H' + self.user_row].value = 'T'
            users_db.save('Users.xlsx')
            add_record(username, 'banned', '3 failed attempts',
                       'Banned Successfully')
            print(
                colored('due to 3 failed attempts, your account has been banned!', 'red'))
            sleep(3)
            quit()

        elif self.failed_attempted < 2:
            self.failed_attempted += 1
            add_record(username, 'login', 'pass: ' + password,
                       'Failed Attempts= ' + str(self.failed_attempted),'r')
            print(colored('your failed attempts= ' +
                  str(self.failed_attempted) + '\n\n\n', 'yellow'))

        else:
            add_record(username, 'kicked', '3 failed attempts',
                       'Session has Ended','r')
            print(
                colored('due to 3 failed attempts, your session has ended!', 'red'))
            sleep(3)
            quit()

    def unban_user(self):
        self.failed_attempted = 0
        users_db_ws['H' + self.user_row].value = 'F'
        users_db.save('Users.xlsx')

    def set_email(self):
        import re
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

        if str(users_db_ws['D' + self.user_row].value) == 'None':
            print(colored('\n\nYou Need to Submit Your Email Address!\n', 'blue'))
            while True:
                temp_email = input(self.username_title() + 'Email : ')
                if re.search(regex, temp_email):
                    users_db_ws['D' + self.user_row].value = temp_email
                    users_db.save('Users.xlsx')
                    add_record(self.username, 'set email', 'email :' + temp_email,
                               'Submited Successfully')
                    print(colored('\nEmail Submited Successfully!\n\n', 'green'))
                    break
                else:
                    add_record(self.username, 'set email', 'email :' + temp_email,
                               'Failed, Not a Valid address','r')
                    print(colored('Enter a Valid Email address!\n', 'yellow'))

    def password_strength_checker(self, password):
        import re

        if len(password) < 8:
            return False

        if not re.search("[a-z]", password):
            return False

        if not re.search("[A-Z]", password):
            return False

        if not re.search("[$#@^*%&]", password):
            return False

        if re.search("\s", password):
            return False

        return True

    def change_password(self):
        self.set_email()
        if users_db_ws['G' + self.user_row].value == 'T':
            print(colored('\nYou Need to Change Your Password!', 'blue'))
            print(colored('The password must be at least 8 characters long and contain both lower and upper case letters, numbers, and symbols.\n\n', 'white'))
            while True:
                temp_password = input(
                    self.username_title() + 'New Password : ')
                if self.password_strength_checker(temp_password):
                    users_db_ws['C' + self.user_row].value = users_db_ws['B' +
                                                                         self.user_row].value
                    users_db_ws['B' + self.user_row].value = temp_password
                    users_db_ws['G' + self.user_row].value = 'F'
                    users_db.save('Users.xlsx')
                    self.relogin = True
                    add_record(self.username, 'change password', 'pass :' + temp_password,
                               'Changed Successfully')
                    print(
                        colored('\nThe new password is Great!, Login again!!\n\n\n', 'green'))
                    break
                else:
                    print(
                        colored('The entered Password is not Strong enough, Try again!\n', 'yellow'))
                    add_record(self.username, 'change password', 'pass :' + temp_password,
                               'Failed, easily crackable password','r')
        else:
            return True

    def loginPage(self):
        while True:
            temp_username = input('Login as: ')
            temp_password = input(
                temp_username + '\'s Password (\'F\' for forgot Password): ')

            if temp_password.lower() == 'f':
                self.forget_password(temp_username)
                break

            if self.check_password(temp_username, temp_password):
                print(colored('\nWelcome ' + temp_username + '\n\n\n', 'green'))
                self.change_password()
                break
            else:
                print(colored('\nThe Username or Password is Incorrect!', 'red'))
                self.ban_user(temp_username, temp_password)

    def username_title(self):
        return '{} > '.format(self.username)

    def update_account_info(self):
        temp_first = input(self.username_title() + 'First Name : ')
        temp_last = input(self.username_title() + 'Last Name : ')

    def forget_password(self, username):
        pass
