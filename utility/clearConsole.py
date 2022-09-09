import os
import platform


def clearConsole():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
