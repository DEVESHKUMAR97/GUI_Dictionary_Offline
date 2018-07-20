from cx_Freeze import setup, Executable
import os
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
base = None

executables = [Executable("GUI_Dictionary.py", base=base)]

packages = ["idna","difflib","tkinter","tkinter.messagebox","os","sys"]
options = {
    'build_exe': {
        'packages':packages,
        'includes':["idna","difflib","tkinter","tkinter.messagebox","os","sys"],
        'include_files':[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
         ],
    },
}

setup(
    name = "GUI_OFFLINE_DICTIONARY",
    options = options,
    version = "1.0",
    description = 'This is a Gui Offline Dictionary which is intelligent in gussing the correct match of user input.',
    executables = executables
)
