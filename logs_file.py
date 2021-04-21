import openpyxl
import os

logs_file_dir = 'administrator'
logs_file = None
logs_file_worksheet = None


def open_logs_file():
    # Try to open or create logs_file.xlsx
    global logs_file

    if not os.path.exists(logs_file_dir):
        # Try to open or create directory.
        os.makedirs(logs_file_dir)

    if os.path.isfile(logs_file_dir + '\\logs_file.xlsx'):
        # Try to find the xlsx file or create a new one.
        # Opens and returns the worksheet.
        logs_file = openpyxl.load_workbook(logs_file_dir + '\\logs_file.xlsx')
        logs_file_worksheet = logs_file['system logs']
    else:
        logs_file = openpyxl.Workbook()
        logs_file_worksheet = logs_file.active
        logs_file_worksheet.title = 'system logs'

    return logs_file_worksheet


def save_logs_file():
    # Saving the xlsx as logs_file.
    global logs_file

    logs_file.save(logs_file_dir + '\\logs_file.xlsx')

    return True


def last_line():
    return logs_file_worksheet.max_row
