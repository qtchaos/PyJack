import time
from utility.clearConsole import clearConsole


def loadAnimation():
    i = 0
    j = 0
    chars = ["/", "-", "\\"]
    while i < 10:
        i += 1
        print(f"{chars[j]}\n")
        j += 1
        if j == 3:
            j = 0
        time.sleep(0.1)
        clearConsole()
