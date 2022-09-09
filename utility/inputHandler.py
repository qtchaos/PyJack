import time

from utility.fileHandler import fileHandler
from utility.exitProgram import exitProgram
from utility.dataBridge import *

from commands.loadAnimation import loadAnimation
from commands.reset import reset
from commands.setBalance import setBalance
from commands.viewBalance import viewBalance
from commands.blackjack import blackjack


def inputHandler(Text="", Save=False, fileName=""):
    global dev
    try:
        if len(Text) == 0:
            inputText = input(">").lower()
        else:
            inputText = input(Text + " >").lower()
    except KeyboardInterrupt:
        exitProgram()

    if inputText == "":
        return

    if Save and fileName:
        fileHandler(Text=inputText, fileName=fileName)
        return

    if inputText == "blackjack":
        blackjack()
        return

    if inputText == "dev":
        dev = True
        print("Granted you developer permissions!")
        time.sleep(TIMEOUT)
        return

    if inputText == "loadanim":
        loadAnimation()
        return

    if inputText in ["money", "balance", "bal"]:
        viewBalance()
        return

    if inputText == "set_bal" and dev:
        setBalance()
        return

    if inputText == "reset":
        reset()
        return

    if inputText == "exit":
        exitProgram()

    print("Command not found.")
    time.sleep(TIMEOUT)
    return
