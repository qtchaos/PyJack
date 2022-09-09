import os
import time

from utility.dataBridge import *


def fileHandler(fileName: str, Text="", Read=False, Delete=False):
    try:
        if Read:
            try:
                with open(fileName + ".txt", "r") as f:
                    return f.read()
            except FileNotFoundError:
                return ""
        else:
            if Delete:
                os.remove(fileName + ".txt")
            with open(fileName + ".txt", "w+") as f:
                f.write(str(Text))

        return True
    except OSError as err:
        print(f"ERROR: {err}")
        time.sleep(TIMEOUT)
        return err
