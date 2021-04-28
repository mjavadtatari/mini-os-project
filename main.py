from logs_file import *
from account import *
from management import *
from command import *


user = Account()
user.loginPage()

if user.relogin:
    user = Account()
    user.loginPage()

if user.logged_in:
    while True:
        pass
# add_record('javad', 'add', '3, 4', '7')
