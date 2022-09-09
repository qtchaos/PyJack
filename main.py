import time

from utility.initialize import initialize
from utility.clearConsole import clearConsole
from utility.fileHandler import fileHandler
from utility.inputHandler import inputHandler
from utility.dataBridge import *


def gameLoop():
    while True:
        clearConsole()
        if len(fileHandler(fileName="name", Read=True)) == 0:
            initialize()
            time.sleep(TIMEOUT)
            clearConsole()
        inputHandler()


if __name__ == "__main__":
    gameLoop()
