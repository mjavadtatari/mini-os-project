from management import *
from logs_file import *
from calculator import *
from cm_list import *

q_list = ['q', 'quit', 'exit', 'stop', 'logout']


class Command():

    def __init__(self, username, *args, **kwargs):
        self.username = username

    def username_title(self):
        return '\n{} >> '.format(self.username)

    def read_input_command(self):
        while True:
            temp_cm = input(self.username_title())
            temp_cm = temp_cm.split(' ')

            if temp_cm[0].lower() in q_list:
                add_record(self.username, 'logout', temp_cm[0], 'Success')
                print('\n\n\n')
                return temp_cm[0]

            try:
                print(all_cm[temp_cm[0].lower()]['func']
                      (self.username, temp_cm[1:]))
            except KeyError:
                print(colored('Enter a Valid Command Key!\n', 'yellow'))

                add_record(self.username, 'Not Valid', temp_cm[0],
                           'Fail')
