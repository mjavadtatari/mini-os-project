from logs_file import *
from account import *
from management import *
from command import *


while True:
    user = Account()
    user.loginPage()

    if user.relogin:
        user = Account()
        user.loginPage()

    if user.logged_in:
        while True:
            cm = Command(user.username)
            quit = cm.read_input_command()
            if quit:
                break


# add_record('javad', 'add', '3, 4', '7')
