import time
from utility.clearConsole import clearConsole


def loadAnimation():
    i = 1
    j = 10
    empty_unicode = "⣀"
    filled_unicode = "⣿"
    while i < 11:
        time.sleep(0.1)
        clearConsole()
        j -= 1
        print(f"{i * filled_unicode}{j * empty_unicode}")
        i += 1
