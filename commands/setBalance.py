import time
from utility.fileHandler import fileHandler
from utility.dataBridge import *


def setBalance(Internal=False, Amount=None):
    if Internal and Amount != None:
        fileHandler(fileName="balance", Text=Amount)
    if Internal == False and Amount != None:
        fileHandler(fileName="balance", Text=Amount)
        print(f"Set balance to {Amount}.")
    else:
        x = int(input("Specify amount. >"))
        fileHandler(fileName="balance", Text=x)
        print(f"Set balance to {x}.")

    time.sleep(TIMEOUT)
