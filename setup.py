from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna", "os", "time", "shutil", "pathlib", "datetime",
            "openpyxl", "account", "calculator", "cm_list", "command",
            "directory", "file", "logs_file", "reset_password",
            "management"]
options = {
    'build_exe': {
        'packages': packages,
    },
}

setup(
    name="miniOS",
    options=options,
    version="1.0",
    description='The Smallest OS in the World!',
    executables=executables
)
