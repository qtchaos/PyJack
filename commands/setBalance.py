import time
from utility.fileHandler import fileHandler
from utility.dataBridge import *


def setBalance(Internal=False, Amount=None):
    if Internal and Amount != None:
        x = Amount
        fileHandler(fileName="balance", Text=x)
    else:
        x = input("Specify amount. >")
        fileHandler(fileName="balance", Text=x)
        print(f"Set balance to {x}.")
        time.sleep(TIMEOUT)
