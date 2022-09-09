import time
from utility.dataBridge import *
from utility.fileHandler import fileHandler


def viewBalance(Internal=False):
    x = fileHandler(fileName="balance", Read=True)
    if Internal:
        return int(x)
    else:
        print(f"You currently have {x}{currency}")
        time.sleep(TIMEOUT)
