from management import *
from logs_file import *
from calculator import *


class Command():

    def __init__(self, username, *args, **kwargs):
        self.username = username

    def username_title(self):
        return '\n{} >> '.format(self.username)

    def read_input_command(self):
        while True:
            temp_cm = input(self.username_title())
            temp_cm = temp_cm.split(' ')

            if temp_cm[0] == 
