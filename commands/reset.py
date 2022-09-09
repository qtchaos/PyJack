import time
from utility.dataBridge import *
from utility.fileHandler import fileHandler


def reset():
    if (input("Are you sure? >").lower())[0] == "y":
        fileHandler(fileName="name", Text="", Delete=True)
        print("Successfully reset.")
    else:
        print("Cancelled reset.")
    time.sleep(TIMEOUT)
