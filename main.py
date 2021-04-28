from logs_file import *
from login import *
from management import *
from command import *


user = LoggedInUser()
user.loginPage()

if user.relogin:
    user = LoggedInUser()
    user.loginPage()

if user.logged_in:
    while True:
        pass
# add_record('javad', 'add', '3, 4', '7')
