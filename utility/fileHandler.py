import os
import time

from utility.dataBridge import *


def fileHandler(fileName: str, Text="", Read=False, Delete=False):
    try:
        if Read:
            try:
                f = open(fileName + ".txt", "r")
                return f.read()
            except FileNotFoundError:
                return ""
        else:
            if Delete:
                os.remove(fileName + ".txt")
            f = open(fileName + ".txt", "w+")
            f.write(str(Text))
            f.close()

        return True
    except (OSError, FileExistsError) as err:
        print(f"ERROR: {err}")
        time.sleep(TIMEOUT)
        return err
